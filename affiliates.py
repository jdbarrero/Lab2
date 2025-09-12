# =============================
# archivo: affiliates.py  (PARA implementar por estudiantes)
# Interfaz (contrato) usada por eps_server.py
# Persistencia en CSV: affiliates.csv, surveys.csv
# =============================

import csv
import os
from datetime import datetime, date
from statistics import mean

AFF_FILE = "affiliates.csv"
SURV_FILE = "surveys.csv"

# ---------- utilidades de archivo ----------

def _ensure_files():
    if not os.path.exists(AFF_FILE):
        with open(AFF_FILE, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["id", "names", "surnames", "birth", "plan", "gender", "email"])  # dd/mm/yyyy
    if not os.path.exists(SURV_FILE):
        with open(SURV_FILE, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["id", "rating"])  # rating: 1..5


def _read_affiliates():
    _ensure_files()
    with open(AFF_FILE, "r", newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r)


def _write_affiliates(rows):
    with open(AFF_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "names", "surnames", "birth", "plan", "gender", "email"])
        w.writeheader()
        for row in rows:
            w.writerow(row)


def _read_surveys():
    _ensure_files()
    with open(SURV_FILE, "r", newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r)


def _write_surveys(rows):
    with open(SURV_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "rating"])
        w.writeheader()
        for row in rows:
            w.writerow(row)


def _parse_date_ddmmyyyy(s):
    return datetime.strptime(s, "%d/%m/%Y").date()


def _age(birth_date: date) -> int:
    today = date.today()
    years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1
    return years

# ---------- funciones del contrato ----------

# body: {id, names, surnames, birth(dd/mm/yyyy), plan(A|B|C), gender(M|F|X), email}
# retorna "ok" o mensaje de error (string)

def register_affiliate(body):
    # TODO: validar campos (no vacíos), unicidad de id, formato de fecha, plan/gender válidos, email con "@"
    # TODO: guardar en AFF_FILE
    # Reglas de error sugeridas: "invalid data", "id already exists", "invalid date format"
    return "TODO"


# retorna lista de dicts ordenada por apellidos ASC

def list_affiliates():
    # TODO: leer archivo y ordenar por "surnames" (casefold)
    return []


# retorna dict del afiliado o None

def search_by_id(_id):
    # TODO: buscar por id exacto
    return None


# retorna: {
#   "total_by_plan": {"A": n, "B": n, "C": n},
#   "avg_age_by_gender": {"M": x, "F": y, "X": z},
#   "min_age": a, "max_age": b
# }

def stats():
    # TODO: calcular a partir de archivo AFF_FILE
    return {
        "total_by_plan": {"A": 0, "B": 0, "C": 0},
        "avg_age_by_gender": {"M": 0, "F": 0, "X": 0},
        "min_age": 0,
        "max_age": 0,
    }


# exporta (reescribe) AFF_FILE tal cual; aquí sirve para respetar el endpoint /export

def export_csv():
    # TODO: si decides mantener el mismo archivo como fuente y destino, basta con verificar que exista
    _ensure_files()


# body: {id, rating(1..5)} -> "ok" o error

def record_survey(body):
    # TODO: validar: id existente, rating entre 1 y 5, guardar en SURV_FILE (append)
    return "TODO"


# segment_by: None | "plan" | "gender"
# retorna: {
#   "count": n,
#   "avg_rating": x,
#   "by_segment": {"A": {"count":.., "avg_rating":..}, ...}  # si aplica
# }

def survey_stats(segment_by=None):
    # TODO: combinar AFF_FILE y SURV_FILE por id
    return {"count": 0, "avg_rating": 0.0, "by_segment": {}}


