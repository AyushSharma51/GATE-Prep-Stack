import requests

from bs4 import BeautifulSoup

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.db_models import Update


BASE_URL = "https://gate2026.iitg.ac.in/"


def fetch_gate_updates():

    response = requests.get(BASE_URL)

    if response.status_code != 200:
        print("Failed to fetch website")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    updates = []

    news_section = soup.find("div", class_="news-text")

    if not news_section:
        print("News section not found")
        return []

    text = news_section.get_text(separator=" ", strip=True)

    notifications = text.split("|")

    for notification in notifications:

        cleaned_text = notification.strip()

        if cleaned_text:

            updates.append({
                "title": cleaned_text,
                "url": BASE_URL,
                "source": "GATE Official"
            })

    return updates


def save_updates_to_db(updates):

    db: Session = SessionLocal()

    try:

        print("Starting database insertion...")

        for item in updates:

            existing_update = db.query(Update).filter(
                Update.title == item["title"]
            ).first()

            if existing_update:
                print("Already exists:", item["title"])
                continue

            new_update = Update(
                title=item["title"],
                source=item["source"],
                source_url=item["url"]
            )

            print("Adding:", item["title"])

            db.add(new_update)

        print("Committing changes...")

        db.commit()

        print("Updates saved successfully")

    except Exception as e:

        db.rollback()

        print("Database error:", e)

    finally:

        db.close()


if __name__ == "__main__":

    updates = fetch_gate_updates()

    print("\n===== GATE NOTIFICATIONS =====\n")

    for item in updates:

        print(f"Title : {item['title']}")
        print(f"URL   : {item['url']}")
        print("-" * 50)

    # IMPORTANT
    save_updates_to_db(updates)