# Aplicación de Conversión de Divisas con Wise

Esta aplicación permite calcular la cantidad de pesos chilenos (CLP) que se reciben al enviar dólares estadounidenses (USD) usando la API de Wise. A continuación, se explica su funcionamiento.

---

## 📌 Funcionalidades principales

- Consulta automática del tipo de cambio USD → CLP mediante la API oficial de Wise.
- Cálculo del total recibido en CLP, considerando la comisión.
- Historial de las últimas 10 tasas consultadas.
- Visualización gráfica del historial.
- Interfaz visual moderna similar a Wise con banderas y botón interactivo.
- Actualización automática cada 60 segundos.
- Lectura de la clave API desde una variable de entorno para mayor seguridad.

---

## ⚙️ Requisitos

- Python 3.8+
- Flask
- `matplotlib`
- Conexión a internet
- Clave API de Wise (almacenada en una variable de entorno `WISE_APIKEY`)

---

## 🚀 Cómo usar

1. **Clonar el repositorio o descargar el código.**
2. **Crear un entorno virtual (opcional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # o .\venv\Scripts\activate en Windows
   ```

3. **Instalar dependencias:**

   ```bash
   pip install flask matplotlib requests
   ```

4. **Definir la variable de entorno con tu API Key de Wise:**

   - En Mac/Linux:
     ```bash
     export WISE_APIKEY=tu_clave_api
     ```
   - En Windows:
     ```cmd
     set WISE_APIKEY=tu_clave_api
     ```

5. **Ejecutar la app:**

   ```bash
   python app.py
   ```

6. **Abrir en navegador:**
   Visita `http://127.0.0.1:5000` para comenzar a utilizar la aplicación.

---

## 🧠 Estructura del proyecto

```
📁 app.py              # Aplicación principal Flask
📁 wise_api.py         # Módulo para interacción con Wise API
📁 historico.json      # Archivo generado con historial de tasas
📁 static/
    └── style.css      # Estilos personalizados
    └── refresh.js     # Script de actualización automática
📁 templates/
    └── index.html     # Interfaz principal
```

---

## 🔐 Seguridad

La clave de API **no se debe subir** a GitHub. Por eso, se usa la variable de entorno `WISE_APIKEY` para mantener la seguridad.

---

## 📈 Notas adicionales

- El historial gráfico muestra únicamente las últimas 10 tasas.
- Las banderas se ajustan automáticamente para mantener proporciones amigables.
- La aplicación detecta y muestra errores de conexión o formato incorrecto con mensajes claros.

---

## ✨ Autor Lorenzo Reyes

Desarrollado para monitorear el tipo de cambio USD → CLP en tiempo real usando Wise.