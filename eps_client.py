# =============================
# archivo: eps_client.py  (NO modificar)
# Cliente de línea de comandos para probar el servidor EPS
# Requiere: pip install requests
# =============================

import requests
import json

BASE = "http://localhost:8080"

def pretty(x):
    print(json.dumps(x, ensure_ascii=False, indent=2))

def health():
    pretty(requests.get(BASE+"/health").json())

def register(sample):
    pretty(requests.post(BASE+"/register", json=sample).json())

def list_all():
    pretty(requests.get(BASE+"/list").json())

def search(_id):
    pretty(requests.get(BASE+"/search", params={"id": _id}).json())

def stats():
    pretty(requests.get(BASE+"/stats").json())

def export():
    pretty(requests.post(BASE+"/export").json())

def survey(_id, rating):
    pretty(requests.post(BASE+"/survey", json={"id": _id, "rating": rating}).json())

def survey_stats(segment_by=None):
    pretty(requests.get(BASE+"/survey_stats", params={"segment_by": segment_by} if segment_by else None).json())

if __name__ == "__main__":
    health()
    register({
        "id":"1010", "names":"Ana", "surnames":"García", "birth":"12/03/1999",
        "plan":"A", "gender":"F", "email":"ana@example.com"
    })
    list_all(); search("1010"); stats(); survey("1010",5); survey_stats("plan"); export()


