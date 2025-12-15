import requests

URL = "https://remoteok.com/api"

JUNIOR_KEYWORDS = [
    "junior", "entry", "intern", "graduate",
    "0-1", "0-2", "1 year", "early career"
]

ROLE_KEYWORDS = [
    "python",
    "data engineer",
    "data engineering"
]


def is_junior(text: str) -> bool:
    text = text.lower()
    return any(k in text for k in JUNIOR_KEYWORDS)


def is_target_role(text: str) -> bool:
    text = text.lower()
    return any(k in text for k in ROLE_KEYWORDS)


def fetch_remoteok():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    data = response.json()

    jobs = []

    for item in data[1:]:
        title = item.get("position", "")
        description = item.get("description", "")
        full_text = f"{title} {description}"

        if is_target_role(full_text) and is_junior(full_text):
            jobs.append({
                "title": title,
                "company": item.get("company", "Unknown"),
                "description": description,
                "url": item.get("url", "#")
            })

    print(f"RemoteOK: found {len(jobs)} junior jobs")
    return jobs[:5]
