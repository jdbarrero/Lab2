# =============================
# archivo: clinical.py
# Citas + Prescripciones (JSON-lines)
# Depende de affiliates.findUser (usuarios con role/session)
# =============================
# =============================
# archivo: clinical.py
# Estudiantes: COMPLETAR funciones indicadas con "ESTUDIANTES"
# Reglas/archivos:
# - Citas    en appointments.txt (JSON por línea)
#   { "id", "patient", "doctor", "date", "time", "status" }  # status: "scheduled" | "cancelled"
# - Recetas  en prescriptions.txt (JSON por línea)
#   { "id", "appt_id", "doctor", "patient", "text" }
# - Validaciones de horario:
#     Lunes a Viernes, 08:00 a 16:00, saltos de 30 min (minuto 0 o 30)
# - Autenticación:
#     Para agendar/listar/cancelar: el "patient" debe tener session=True
#     Para prescribir/listar como doctor: el "doctor" debe tener session=True y role="doctor"
# - Usar affiliates.findUser(name) para consultar usuarios y su session/role
# =============================

import os
import json
from datetime import datetime
from affiliates import findUser  # usar usuarios con rol/sesión implementados por ustedes

APPTS_FILE = "appointments.txt"
PRESC_FILE = "prescriptions.txt"

# ---------- Utilidades de archivo sugeridas ----------
def _ensure(path):
    """Crea el archivo si no existe."""
    # ESTUDIANTES: si no existe path, crearlo vacío
    pass

def _load_jsonl(path):
    """Lee JSON por línea y retorna lista de dicts."""
    # ESTUDIANTES
    pass

def _rewrite_jsonl(path, rows):
    """Sobrescribe el archivo JSONL con 'rows'."""
    # ESTUDIANTES
    pass

def _next_id(rows):
    """Retorna el siguiente id entero disponible (1,2,3,...) según 'id' en rows."""
    # ESTUDIANTES: recorrer y calcular máximo + 1
    pass

def _valid_slot(date_str, time_str):
    """
    Valida fecha/hora de la cita.
    Retorna ("ok", d, t) o ("out of range"/"invalid data", None, None)
    Reglas:
      - Formato: date "dd/mm/yyyy", time "HH:MM"
      - L-V (weekday 0..4), 08:00..16:00 (sin pasar de 16:00), minutos {0,30}
    """
    # ESTUDIANTES: intentar parsear; verificar día/hora; retornar tupla
    pass

# ===============  API DE CITAS  =======================


def scheduleAppointment(patient_name, patient_password, doctor_name, date_str, time_str):
    """
    Crea una cita "scheduled".
    Retorna:
      "ok" | "invalid data" | "doctor not found" | "user not logged in" | "out of range" | "slot taken"
    Pasos sugeridos:
      1) Validar no vacíos.
      2) findUser(doctor_name) -> role=="doctor".
      3) findUser(patient_name) -> password coincide y session==True.
      4) _valid_slot(date_str,time_str) -> "ok".
      5) Cargar citas; rechazar si (mismo doctor, misma fecha/hora, status=="scheduled").
      6) (opcional) Rechazar si el mismo paciente ya tiene una cita en ese slot.
      7) Calcular id, agregar registro y guardar.
    """
    # ESTUDIANTES
    pass

def listAppointments(patient_name, patient_password):
    """
    Lista las citas del paciente autenticado.
    Retorna:
      lista_de_citas | "invalid data" | "user not logged in"
    """
    # ESTUDIANTES:
    # - Validar credenciales y session del paciente
    # - Cargar citas y filtrar por patient == patient_name
    pass

def cancelAppointment(patient_name, patient_password, appointment_id):
    """
    Cancela una cita del paciente (si está en status "scheduled").
    Retorna:
      "ok" | "invalid data" | "user not logged in" | "not found"
    """
    # ESTUDIANTES:
    # - Validar credenciales y session del paciente
    # - Buscar por id (int) en sus citas "scheduled" y marcar "cancelled"
    pass

# ============  API DE PRESCRIPCIONES  =================


def createPrescription(doctor_name, doctor_password, patient_name, appt_id, text):
    """
    Crea una prescripción ligada a una cita existente (doctor, paciente).
    Retorna:
      "ok" | "invalid data" | "unauthorized" | "not found"
    Pasos sugeridos:
      1) Validar no vacíos. appt_id -> int.
      2) findUser(doctor_name): password coincide, role=="doctor", session==True.
      3) findUser(patient_name) existe.
      4) Cargar citas y verificar que exista appt_id con esa dupla (doctor/paciente).
         (Opcional: permitir solo si status=="scheduled" y fecha/hora ya ocurrió.)
      5) Crear id y guardar prescripción en JSONL.
    """
    # ESTUDIANTES
    pass

def listPrescriptions(role, name, password):
    """
    Lista prescripciones según el rol:
      - role=="patient": el usuario autenticado ve sus propias prescripciones
      - role=="doctor" : el usuario autenticado ve las que él emitió
    Retorna:
      lista_de_prescripciones | "invalid data" | "unauthorized"
    Pasos:
      1) Validar role en {"patient","doctor"} y credenciales (session==True).
      2) Cargar prescriptions.txt y filtrar por campo "patient" o "doctor" según el rol.
    """
    # ESTUDIANTES
    pass
