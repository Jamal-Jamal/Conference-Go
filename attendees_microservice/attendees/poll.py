import json
import requests

from .models import ConferenceVO


def get_conferences():
    url = "http://monolith:8000/api/conferences/"
    response = requests.get(url)
    content = json.loads(response.content)
    print(content)
    for conference in content["conferences"]:
        print(conference)
        ConferenceVO.objects.update_or_create(
            import_href=conference["href"],
            defaults={"name": conference["name"]},
        )
