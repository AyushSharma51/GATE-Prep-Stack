from apscheduler.schedulers.background import BackgroundScheduler

from app.scraper.gate_official import (
    fetch_gate_updates,
    save_updates_to_db
)


scheduler = BackgroundScheduler()


def scrape_and_store_updates():

    print("\nRunning scheduled scraper...\n")

    updates = fetch_gate_updates()

    save_updates_to_db(updates)

    print("\nScheduled scraping completed.\n")


# Run scraper once every 1 day
scheduler.add_job(
    scrape_and_store_updates,
    trigger="interval",
    days=1
)