# =============================
# archivo: eps_server.py  (NO modificar)
# Servidor HTTP (stdlib) para el Mini SI de EPS
# Depende del módulo: affiliates.py (desarrolado por estudiantes)
# - Afiliados/Encuestas 
# - Usuarios con roles/sesión 
# - Citas + Prescripciones (clinical.py)
# =============================

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import json
import sys

import affiliates         # funciones de afiliados + usuarios (roles/sesión)
import clinical              # citas + prescripciones (unificado)

HOST = "0.0.0.0"
PORT = 8080


def _json_response(handler, code, payload):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(code)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def _read_body(handler):
    length = int(handler.headers.get("Content-Length", 0) or 0)
    raw = handler.rfile.read(length) if length > 0 else b""
    ctype = (handler.headers.get("Content-Type") or "").lower()
    if "application/json" in ctype and raw:
        try:
            return json.loads(raw.decode("utf-8"))
        except Exception:
            return {}
    elif "application/x-www-form-urlencoded" in ctype and raw:
        return {k: v[0] for k, v in parse_qs(raw.decode("utf-8")).items()}
    return {}


class EPSHandler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stdout.write("%s - - [%s] " % (self.client_address[0], self.log_date_time_string()))
        sys.stdout.write((fmt % args) + "\n")

    # ------------------------------------------------------
    # GET
    # ------------------------------------------------------
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        q = {k: v[0] for k, v in parse_qs(parsed.query).items()}

        if path == "/health":
            return _json_response(self, 200, {"status": "ok"})

        # ---- AFILIADOS/ENCUESTAS (existentes) ----
        if path == "/list":
            try:
                data = affiliates.listAffiliates()
                return _json_response(self, 200, {"affiliates": data})
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        if path == "/search":
            try:
                _id = (q.get("id") or "").strip()
                found = affiliates.searchById(_id)
                if not found:
                    return _json_response(self, 404, {"error": "not found"})
                return _json_response(self, 200, found)
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        if path == "/stats":
            try:
                st = affiliates.stats()
                return _json_response(self, 200, st)
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        if path == "/survey_stats":
            try:
                seg = q.get("segment_by")
                s = affiliates.surveyStats(seg)
                return _json_response(self, 200, s)
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        # ---- CITAS ----
        if path == "/appointment/list":
            try:
                name = (q.get("name") or "").strip()
                pwd = (q.get("password") or "").strip()
                res = clinical.listAppointments(name, pwd)
                if isinstance(res, list):
                    return _json_response(self, 200, {"appointments": res})
                if res == "user not logged in":
                    return _json_response(self, 401, {"error": res})
                return _json_response(self, 400, {"error": res})
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        # ---- PRESCRIPCIONES ----
        if path == "/prescription/list":
            try:
                role = (q.get("role") or "").strip()
                name = (q.get("name") or "").strip()
                pwd = (q.get("password") or "").strip()
                res = clinical.listPrescriptions(role, name, pwd)
                if isinstance(res, list):
                    return _json_response(self, 200, {"prescriptions": res})
                if res == "unauthorized":
                    return _json_response(self, 401, {"error": res})
                return _json_response(self, 400, {"error": res})
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        return _json_response(self, 404, {"error": "unknown endpoint"})

    # ------------------------------------------------------
    # POST
    # ------------------------------------------------------
    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        b = _read_body(self)

        # ---- AFILIADOS/ENCUESTAS (existentes) ----
        if path == "/register":
            try:
                msg = affiliates.registerAffiliate(
                    str(b.get("id", "")).strip(),
                    str(b.get("names", "")).strip(),
                    str(b.get("surnames", "")).strip(),
                    str(b.get("birth", "")).strip(),
                    str(b.get("plan", "")).strip(),
                    str(b.get("gender", "")).strip(),
                    str(b.get("email", "")).strip(),
                )
                if msg == "ok":
                    return _json_response(self, 201, {"message": "registered"})
                return _json_response(self, 400, {"error": msg})
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        if path == "/export":
            try:
                affiliates.exportCsv()
                return _json_response(self, 200, {"message": "exported"})
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        if path == "/survey":
            try:
                msg = affiliates.recordSurvey(str(b.get("id", "")).strip(), int(b.get("rating", 0)))
                if msg == "ok":
                    return _json_response(self, 200, {"message": "recorded"})
                return _json_response(self, 400, {"error": msg})
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        # ---- USUARIOS (roles/sesión) ----
        if path == "/user/register":
            try:
                msg = affiliates.registerUser(
                    str(b.get("name", "")).strip(),
                    str(b.get("password", "")).strip(),
                    str(b.get("role", "")).strip()
                )
                if msg == "ok":
                    return _json_response(self, 201, {"message": "registered"})
                if msg == "user exists":
                    return _json_response(self, 409, {"error": msg})
                return _json_response(self, 400, {"error": msg})
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        if path == "/user/session":
            try:
                flag = bool(b.get("flag", False))
                msg = affiliates.openCloseSession(
                    str(b.get("name", "")).strip(),
                    str(b.get("password", "")).strip(),
                    flag
                )
                if msg == "ok":
                    return _json_response(self, 200, {"message": "session updated"})
                if msg == "wrong credentials":
                    return _json_response(self, 401, {"error": msg})
                return _json_response(self, 400, {"error": msg})
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        # ---- CITAS ----
        if path == "/appointment/schedule":
            try:
                msg = clinical.scheduleAppointment(
                    str(b.get("patient", "")).strip(),
                    str(b.get("password", "")).strip(),
                    str(b.get("doctor", "")).strip(),
                    str(b.get("date", "")).strip(),
                    str(b.get("time", "")).strip()
                )
                if msg == "ok":
                    return _json_response(self, 201, {"message": "scheduled"})
                if msg in ("doctor not found",):
                    return _json_response(self, 404, {"error": msg})
                if msg in ("user not logged in",):
                    return _json_response(self, 401, {"error": msg})
                if msg in ("out of range", "slot taken"):
                    return _json_response(self, 409, {"error": msg})
                return _json_response(self, 400, {"error": msg})
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        if path == "/appointment/cancel":
            try:
                msg = clinical.cancelAppointment(
                    str(b.get("patient", "")).strip(),
                    str(b.get("password", "")).strip(),
                    b.get("id", None)
                )
                if msg == "ok":
                    return _json_response(self, 200, {"message": "cancelled"})
                if msg == "user not logged in":
                    return _json_response(self, 401, {"error": msg})
                if msg == "not found":
                    return _json_response(self, 404, {"error": msg})
                return _json_response(self, 400, {"error": msg})
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        # ---- PRESCRIPCIONES ----
        if path == "/prescription/create":
            try:
                msg = clinical.createPrescription(
                    str(b.get("doctor", "")).strip(),
                    str(b.get("password", "")).strip(),
                    str(b.get("patient", "")).strip(),
                    b.get("appt_id", None),
                    str(b.get("text", "")).strip()
                )
                if msg == "ok":
                    return _json_response(self, 201, {"message": "created"})
                if msg == "unauthorized":
                    return _json_response(self, 401, {"error": msg})
                if msg == "not found":
                    return _json_response(self, 404, {"error": msg})
                return _json_response(self, 400, {"error": msg})
            except Exception as e:
                return _json_response(self, 500, {"error": str(e)})

        return _json_response(self, 404, {"error": "unknown endpoint"})


if __name__ == "__main__":
    httpd = HTTPServer((HOST, PORT), EPSHandler)
    print(f"EPS server running on http://{HOST}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        httpd.server_close()

