from flask import Flask, render_template, request
import json
import os
from datetime import datetime
from wise_api import obtener_cotizacion_wise

app = Flask(__name__)

def guardar_historico(tasa):
    archivo = "historico.json"
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
    else:
        datos = {"fechas": [], "tasas": []}

    datos["fechas"].append(fecha_actual)
    datos["tasas"].append(tasa)

    # Mantener solo los últimos 10 puntos
    if len(datos["fechas"]) > 10:
        datos["fechas"] = datos["fechas"][-10:]
        datos["tasas"] = datos["tasas"][-10:]

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

def obtener_historico():
    archivo = "historico.json"
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return datos["fechas"], datos["tasas"]
    return [], []

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            monto = float(request.form["monto"])
            respuesta = obtener_cotizacion_wise(monto)

            # Extraer desde paymentOptions[0]
            opciones = respuesta.get("paymentOptions", [])
            if not opciones:
                raise Exception("No se encontraron opciones de pago en la respuesta de Wise.")

            opcion = opciones[0]  # Usar la primera opción válida
            tasa = float(respuesta["rate"])
            comision = float(opcion["fee"]["total"])
            monto_clp = float(opcion["targetAmount"])

            guardar_historico(tasa)

            resultado = {
                "clp": monto_clp,
                "tasa": tasa,
                "comision": comision
            }

        except Exception as e:
            error = f"Error: {str(e)}"

    fechas, tasas = obtener_historico()

    return render_template("index.html", resultado=resultado, fechas=fechas, tasas=tasas, error=error)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
