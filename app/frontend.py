from nicegui import ui, app
from pathlib import Path

# ─────────────────────────────
# CONFIG
# ─────────────────────────────

BASE_DIR = Path(__file__).parent
PAPERS_DIR = BASE_DIR / "papers"

app.add_static_files('/papers', str(PAPERS_DIR))

BRANCHES = {
    "cse": "Computer Science",
    "da": "Data Science",
    "me": "Mechanical",
}

# ─────────────────────────────
# STATE
# ─────────────────────────────

class State:
    def __init__(self):
        self.branch = "cse"
        self.papers = []
        self.selected = None

    def load(self):
        path = PAPERS_DIR / self.branch

        if not path.exists():
            self.papers = []
            self.selected = None
            return

        self.papers = sorted([f.stem for f in path.glob("*.pdf")], reverse=True)
        self.selected = self.papers[0] if self.papers else None


state = State()
state.load()

# ─────────────────────────────
# HELPERS
# ─────────────────────────────

def format_name(name):
    if "-" in name:
        y, s = name.split("-")
        return f"{y} • Shift {s}"
    return name


def get_url():
    if state.selected:
        return f"/papers/{state.branch}/{state.selected}.pdf"
    return None


# ─────────────────────────────
# UI
# ─────────────────────────────

@ui.page("/")
def main():

    # 🔤 FONT + ICONS
    ui.add_head_html("""
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

    <style>
        * {
            font-family: 'Manrope', sans-serif;
        }
    </style>
    """)

    # ✅ Proper dark mode controller
    dark = ui.dark_mode()
    dark.enable()  # start in dark mode

    with ui.column().classes("w-full max-w-5xl mx-auto p-6 gap-6"):

        # HEADER
        with ui.row().classes("w-full justify-between items-center"):
            ui.label("📘 GATE Papers").classes("text-3xl font-bold")

            ui.switch(
                "🌙 Dark Mode",
                value=True,
                on_change=lambda e: toggle_theme(e.value)
            )

        ui.separator()

        # MAIN CARD
        @ui.refreshable
        def container():

            with ui.card().classes("w-full p-6 rounded-xl shadow-lg"):

                # Branch
                ui.label("Select Branch").classes("text-lg font-semibold")

                with ui.row().classes("gap-3"):
                    for key, name in BRANCHES.items():

                        def select(k=key):
                            state.branch = k
                            state.load()
                            container.refresh()

                        ui.button(name, on_click=select).props("color=primary")

                # Paper
                ui.label("Select Paper").classes("text-lg font-semibold mt-4")

                ui.select(
                    options={p: format_name(p) for p in state.papers},
                    value=state.selected,
                    on_change=lambda e: setattr(state, "selected", e.value)
                ).classes("w-full")

                # Buttons
                with ui.row().classes("gap-3 mt-4"):

                    if get_url():
                        ui.link(
                            "📖 View",
                            target=get_url(),
                            new_tab=True
                        ).classes("px-4 py-2 bg-blue-500 text-white rounded")

                    ui.button(
                        "⬇ Download",
                        on_click=download
                    ).props("outline")

        container()


# ─────────────────────────────
# ACTIONS
# ─────────────────────────────

def toggle_theme(value):
    if value:
        ui.dark_mode().enable()
    else:
        ui.dark_mode().disable()


def download():
    if state.selected:
        path = PAPERS_DIR / state.branch / f"{state.selected}.pdf"
        if path.exists():
            ui.download(path, f"{state.branch}_{state.selected}.pdf")


# ─────────────────────────────
# RUN
# ─────────────────────────────

ui.run(port=8080, reload=True)