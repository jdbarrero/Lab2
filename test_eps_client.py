# =============================
# archivo: test_eps_client.py  (PUEDEN modificar libremente)
# Pruebas simples contra el servidor
# =============================

# =============================
# archivo: test_eps_client.py (REEMPLAZO, acorde a contrato)
# =============================
import requests
BASE = "http://localhost:8080"

# Registro
requests.post(BASE+"/register", json={
    "id":"2001","names":"Luis","surnames":"Pérez","birth":"05/11/1988",
    "plan":"B","gender":"M","email":"luis@example.com"
})

# Búsqueda + lista + stats
assert requests.get(BASE+"/search", params={"id":"2001"}).status_code==200
assert requests.get(BASE+"/list").status_code==200
assert requests.get(BASE+"/stats").status_code==200

# Encuestas
requests.post(BASE+"/survey", json={"id":"2001","rating":4})
requests.post(BASE+"/survey", json={"id":"2001","rating":5})
assert requests.get(BASE+"/survey_stats", params={"segment_by":"plan"}).status_code==200
print("OK")
