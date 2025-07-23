import tkinter as tk
from tkinter import ttk
from wise_api import obtener_cotizacion_wise

class WiseApp:
    def __init__(self, root):
        self.root = root
        root.title("Cotización Wise USD → CLP")
        root.geometry("420x280")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", font=("Helvetica", 11))
        style.configure("TButton", font=("Helvetica", 11, "bold"))
        style.configure("TEntry", font=("Helvetica", 11))

        ttk.Label(root, text="Monto en USD:").pack(pady=10)
        self.monto_entry = ttk.Entry(root, width=20)
        self.monto_entry.pack()

        ttk.Button(root, text="Cotizar", command=self.obtener_cotizacion).pack(pady=10)

        self.resultado_label = ttk.Label(root, text="", justify="left")
        self.resultado_label.pack(pady=10)

    def obtener_cotizacion(self):
        try:
            monto_usd = float(self.monto_entry.get())
            data = obtener_cotizacion_wise(monto_usd)

            opcion = data['paymentOptions'][0]  # tomamos la primera opción válida
            tasa = data['rate']
            recibido = opcion['targetAmount']
            comision_total = opcion['fee']['total']

            resultado = (
                f"Tasa Wise: {tasa:.2f}\n"
                f"Comisión total: {comision_total:.2f} USD\n"
                f"Recibirás: {recibido:,} CLP"
            )

            self.resultado_label.config(text=resultado)
        except Exception as e:
            self.resultado_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WiseApp(root)
    root.mainloop()
