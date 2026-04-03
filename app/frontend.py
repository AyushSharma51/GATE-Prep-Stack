import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="GATE Resources", layout="wide")

st.title("📚 GATE Preparation Hub")

# ===================== BRANCH MAPPING =====================
BRANCH_FULL_FORM = {
    "cse": "Computer Science and Engineering",
    "da": "Data Science and Artificial Intelligence",
    "me": "Mechanical Engineering",
    "ee": "Electrical Engineering",
    "ce": "Civil Engineering",
    "ec": "Electronics and Communication Engineering"
}

# ===================== PYQ SECTION =====================
st.header("📄 Previous Year Question Papers")

col1, col2 = st.columns(2)

with col1:
    branch = st.selectbox(
        "Select Branch",
        options=list(BRANCH_FULL_FORM.keys()),
        format_func=lambda x: BRANCH_FULL_FORM[x]
    )

with col2:
    year = st.text_input("Enter Year (e.g. 2023)")

if st.button("Get Paper"):
    st.session_state["paper_url"] = f"{BASE_URL}/papers/{branch}/{year}"
    st.session_state["paper_name"] = f"{branch}_{year}.pdf"
    st.session_state["view_mode"] = False


# ===================== OPTIONS =====================
if "paper_url" in st.session_state:
    st.subheader("Options")

    col1, col2 = st.columns(2)

    # 👉 VIEW PAPER
    with col1:
        if st.button("👁️ View Paper"):
            st.session_state["view_mode"] = True

    # 👉 DOWNLOAD PAPER
    with col2:
        response = requests.get(st.session_state["paper_url"])
        if response.status_code == 200:
            st.download_button(
                label="⬇️ Download Paper",
                data=response.content,
                file_name=st.session_state["paper_name"],
                mime="application/pdf"
            )
        else:
            st.error("Paper not found ❌")


# ===================== VIEW MODE =====================
if st.session_state.get("view_mode"):
    st.subheader("📖 Viewing Paper")

    pdf_url = st.session_state["paper_url"]

    st.markdown(
        f'<iframe src="{pdf_url}" width="100%" height="600"></iframe>',
        unsafe_allow_html=True
    )


# ===================== FREE RESOURCES =====================
st.header("🎯 Free Resources")

# STEP 1: LOAD BRANCHES
branches_res = requests.get(f"{BASE_URL}/resources/branches")

if branches_res.status_code == 200:
    branches = branches_res.json()

    branch_options = {b["name"]: b["id"] for b in branches}

    selected_branch = st.selectbox("Choose Branch", list(branch_options.keys()))

    branch_id = branch_options[selected_branch]

    # STEP 2: LOAD SUBJECTS
    subjects_res = requests.get(f"{BASE_URL}/resources/subjects/{branch_id}")

    if subjects_res.status_code == 200:
        subjects = subjects_res.json()

        subject_options = {s["name"]: s["id"] for s in subjects}

        selected_subject = st.selectbox("Choose Subject", list(subject_options.keys()))

        subject_id = subject_options[selected_subject]

        # STEP 3: LOAD VIDEOS
        videos_res = requests.get(f"{BASE_URL}/resources/videos/{subject_id}")

        if videos_res.status_code == 200:
            videos = videos_res.json()

            st.subheader("🎥 Videos")

            for v in videos:
                url = v["playlist_url"]

                st.markdown("---")

                col1, col2 = st.columns([1, 3])

                # 👉 LEFT: REAL THUMBNAIL
                with col1:
                    video_id = None

                    # 🎯 Normal video OR playlist with video
                    if "watch?v=" in url:
                        video_id = url.split("v=")[-1].split("&")[0]

                    # 🎯 Short link
                    elif "youtu.be" in url:
                        video_id = url.split("/")[-1]

                    if video_id:
                        thumbnail = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

                        st.markdown(
                            f"""
                            <a href="{url}" target="_blank">
                                <img src="{thumbnail}" width="260" style="border-radius:12px;">
                            </a>
                            """,
                            unsafe_allow_html=True
                        )
                    else:
                        # ❌ Playlist without video_id (no thumbnail possible)
                        st.markdown(
                            f"""
                            <a href="{url}" target="_blank">
                                <img src="https://img.icons8.com/color/240/youtube-play.png" width="120">
                            </a>
                            """,
                            unsafe_allow_html=True
                        )

                # 👉 RIGHT: TITLE + BUTTON
                with col2:
                    st.markdown(f"### {v['title']}")
                    st.link_button("▶️ Open Playlist", url)

        else:
            st.error("No videos found")

    else:
        st.error("No subjects found")

else:
    st.error("Failed to load branches")