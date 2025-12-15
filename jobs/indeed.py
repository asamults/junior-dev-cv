import requests
from bs4 import BeautifulSoup

def fetch_indeed():
    """
    Возвращает список вакансий с Indeed UK для Junior Python
    """
    url = "https://www.indeed.co.uk/jobs?q=junior+python&l=United+Kingdom&sort=date"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("a", class_="tapItem")
    
    jobs = []
    for job in job_cards[:10]:  # первые 10 вакансий
        title_tag = job.find("h2", class_="jobTitle")
        company_tag = job.find("span", class_="companyName")
        url_tag = job.get("href")
        if title_tag and company_tag and url_tag:
            jobs.append({
                "title": title_tag.text.strip(),
                "company": company_tag.text.strip(),
                "description": "",  # можно добавить, если парсить описание страницы
                "url": "https://www.indeed.co.uk" + url_tag
            })
    return jobs
