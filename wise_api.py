import requests
import os

# Leer la API key desde variable de entorno
WISE_TOKEN = os.getenv("WISE_APIKEY")

if not WISE_TOKEN:
    raise Exception("La variable de entorno 'WISE_APIKEY' no está definida.")

HEADERS = {
    "Authorization": f"Bearer {WISE_TOKEN}",
    "Content-Type": "application/json"
}

# Obtener el ID de perfil personal
def obtener_profile_id():
    url = "https://api.transferwise.com/v1/profiles"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 200:
        perfiles = resp.json()
        perfil_personal = next((p for p in perfiles if p["type"] == "personal"), None)
        if perfil_personal:
            return perfil_personal["id"]
        else:
            raise Exception("No se encontró un perfil personal.")
    else:
        raise Exception(f"No se pudo obtener el profile ID de Wise: {resp.text}")

# Obtener cotización usando el endpoint v2
def obtener_cotizacion_wise(monto_usd):
    profile_id = obtener_profile_id()

    url = "https://api.transferwise.com/v2/quotes"
    datos = {
        "profile": profile_id,
        "sourceCurrency": "USD",
        "targetCurrency": "CLP",
        "rateType": "FIXED",
        "sourceAmount": monto_usd
    }

    resp = requests.post(url, headers=HEADERS, json=datos)
    if resp.status_code == 200:
        return resp.json()
    else:
        raise Exception(f"Error al obtener cotización de Wise: {resp.text}")
