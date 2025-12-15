from jobs.remoteok import fetch_remoteok

def search_jobs():
    """
    Ищет вакансии Python на RemoteOK.
    Возвращает первые 5 вакансий в виде списка словарей:
    {
        'title': ...,
        'company': ...,
        'description': ...,
        'url': ...
    }
    """
    jobs = fetch_remoteok()
    
    if not jobs:
        print("No jobs found by search_jobs()")
        return []

    # Для теста возвращаем первые 5 вакансий
    return jobs[:5]
