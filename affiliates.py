# =============================
# archivo: affiliates.py 
# uso de arcivos CSV: affiliates.csv, surveys.csv
# Gestiona:
#  A) Afiliados y encuestas en CSV 
#  B) Usuarios con roles/sesión en JSONL (users.txt)
# =============================
# =============================
# archivo: affiliates.py
# Estudiantes: COMPLETAR funciones indicadas con "ESTUDIANTES"
# Reglas:
# - Afiliados y encuestas en CSV (affiliates.csv, surveys.csv)
# - Usuarios (name, password, role, session) en JSON por línea (users.txt)
# - Formatos:
#     birth -> "dd/mm/yyyy"
#     plan  -> "A" | "B" | "C"
#     gender-> "M" | "F" | "X"
#     rating-> entero 1..5
# - Retornos de funciones: usar strings exactos indicados
# =============================

import os
import csv
import json
from datetime import datetime, date

# ---------- Archivos de datos ----------
AFF_FILE = "affiliates.csv"     # columnas: id,names,surnames,birth,plan,gender,email
SURV_FILE = "surveys.csv"       # columnas: id,rating
USERS_FILE = "users.txt"        # JSONL: {"name","password","role","session"}

# ---------- Utilidades sugeridas (opcionales para el estudiante) ----------
def _ensure_aff_files():
    """Crea los CSV si no existen (con sus cabeceras)."""
    # ESTUDIANTES: si no existe AFF_FILE, crearlo y escribir cabecera
    # ESTUDIANTES: si no existe SURV_FILE, crearlo y escribir cabecera
    pass

def _read_affiliates():
    """Lee ESTUDIANTESs los afiliados del CSV y retorna lista de dicts."""
    # ESTUDIANTES: abrir AFF_FILE y usar csv.DictReader
    pass

def _write_affiliates(rows):
    """Sobrescribe el CSV de afiliados con la lista 'rows'."""
    # ESTUDIANTES: abrir AFF_FILE y usar csv.DictWriter con cabeceras
    pass

def _read_surveys():
    """Lee todas las encuestas del CSV y retorna lista de dicts."""
    # ESTUDIANTES
    pass

def _write_surveys(rows):
    """Sobrescribe el CSV de encuestas con la lista 'rows'."""
    # ESTUDIANTES
    pass

def _ensure_users():
    """Crea users.txt si no existe."""
    # ESTUDIANTES
    pass

def _load_users():
    """Lee users.txt (JSON por línea) y retorna lista de dicts."""
    # ESTUDIANTES: por cada línea no vacía, json.loads y agregar a una lista
    pass

def _rewrite_users(rows):
    """Sobrescribe users.txt con una línea JSON por usuario."""
    # ESTUDIANTES: por cada dict en rows escribir json.dumps(...) + "\n"
    pass

def _find_user(rows, name):
    """Busca un usuario por name en la lista rows."""
    # ESTUDIANTES: recorrer y comparar u["name"] == name
    pass

def _parse_date_ddmmyyyy(s):
    """Convierte 'dd/mm/yyyy' a objeto date. Levanta excepción si no cumple formato."""
    return datetime.strptime(s, "%d/%m/%Y").date()

def _age(birth_date):
    """Calcula edad (entero) dada una fecha de nacimiento."""
    today = date.today()
    years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1
    return years

# ---------- Validaciones básicas ----------
def _valid_plan(p): return p in ("A", "B", "C")
def _valid_gender(g): return g in ("M", "F", "X")
def _valid_email(e):
    return isinstance(e, str) and ("@" in e) and ("." in e.split("@")[-1])

# ===============  API DE AFILIADOS  ===================


def registerAffiliate(_id, names, surnames, birth, plan, gender, email):
   
    # ESTUDIANTES:
    # 1) Validar que ningún campo esté vacío (strings con strip()).
    # 2) Intentar parsear birth con _parse_date_ddmmyyyy; si falla -> "invalid date format".
    # 3) Validar plan/gender/email; si falla -> "invalid data".
    # 4) Leer afiliados y verificar que el id NO exista -> si existe -> "id already exists".
    # 5) Agregar nuevo dict y escribir el CSV.
    pass

def listAffiliates():
   
    # ESTUDIANTES: leer CSV, ordenar por apellidos (minúsculas), retornar lista
    pass

def searchById(_id):
 
    # ESTUDIANTES: recorrer lectura y retornar el que coincida
    pass

def stats():
  
    # ESTUDIANTES:
    # - Recorrer afiliados, acumular por plan
    # - Calcular edades con _age(parse de birth)
    # - Promedio por gender (si no hay datos, 0.0)
    pass

def exportCsv():
    # ESTUDIANTES: llamar a _ensure_aff_files()
    pass

def recordSurvey(_id, rating):
 
    # ESTUDIANTES:
    # - Validar id
    # - Verificar afiliado existe
    # - Validar rating entero en 1..5
    # - Agregar fila al CSV de encuestas
    pass

def surveyStats(segment_by=None):

    # ESTUDIANTES:
    # - Leer afiliados y encuestas
    # - Ignorar ratings fuera de 1..5
    # - Si segment_by en {"plan","gender"} construir promedios por segmento
    pass


# ===============  API DE USUARIOS  ====================


def registerUser(name, password, role):

    # ESTUDIANTES:
    # - Validar no vacíos
    # - Validar role permitido
    # - Leer users.txt y verificar que no exista name
    # - Agregar {"name", "password", "role", "session": False}
    pass

def openCloseSession(name, password, flag):

    # ESTUDIANTES:
    # - Validar no vacíos
    # - Cargar usuarios, buscar por name y verificar password
    # - Actualizar campo "session" con bool(flag)
    pass

def findUser(name):

    # ESTUDIANTES: cargar lista y buscar por name
    pass
