from apscheduler.schedulers.background import BackgroundScheduler
from ..scraper.ccmt import fetch_ccmt_updates
from ..scraper.gate_official import (
    fetch_gate_updates,
    save_updates_to_db
)


scheduler = BackgroundScheduler()


def scrape_and_store_updates():

    print("\nRunning scheduled scraper...\n")

    all_updates = []

    # GATE updates
    all_updates.extend(fetch_gate_updates())

    # CCMT updates
    all_updates.extend(fetch_ccmt_updates())

    save_updates_to_db(all_updates)

    print("\nScheduled scraping completed.\n")


# Run scraper once every 1 day
scheduler.add_job(
    scrape_and_store_updates,
    trigger="interval",
    days=1
)

