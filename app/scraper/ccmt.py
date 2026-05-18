import requests

from bs4 import BeautifulSoup


BASE_URL = "https://ccmt.admissions.nic.in/"


def fetch_ccmt_updates():

    response = requests.get(BASE_URL)

    if response.status_code != 200:
        print("Failed to fetch CCMT website")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    updates = []

    ticker_section = soup.find("div", class_="newsticker")

    if not ticker_section:
        print("CCMT ticker section not found")
        return []

    # Extract all list items from ticker
    items = ticker_section.find_all("li")

    for item in items:

        text = item.get_text(separator=" ", strip=True)

        if text:

            updates.append({
                "title": text,
                "url": BASE_URL,
                "source": "CCMT"
            })

    return updates


if __name__ == "__main__":

    updates = fetch_ccmt_updates()

    print("\n===== CCMT UPDATES =====\n")

    for item in updates:

        print(f"Title : {item['title']}")
        print(f"URL   : {item['url']}")
        print("-" * 50)