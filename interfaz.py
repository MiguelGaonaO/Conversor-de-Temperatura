import conversor_de_escalas
import tkinter as tk
from tkinter import ttk

# Lista para el historial de conversiones
historial = []

def convertir():
    try:
        temperatura = float(entry_temperatura.get())
        escala_origen = combo_origen.get()
        escala_destino = combo_destino.get()

        if escala_origen == "Celsius":
            resultado = conversor_de_escalas.celsius(temperatura, escala_destino)
        elif escala_origen == "Kelvin":
            resultado = conversor_de_escalas.kelvin(temperatura, escala_destino)
        elif escala_origen == "Fahrenheit":
            resultado = conversor_de_escalas.fahrenheit(temperatura, escala_destino)
        else:
            resultado = "Escala no válida"

        label_resultado.config(text=f"Resultado: {resultado:.2f} {escala_destino}")
        
        # Agregar al historial
        conversion = f"{temperatura} {escala_origen} → {resultado:.2f} {escala_destino}"
        historial.insert(0, conversion)
        actualizar_historial()
    except ValueError:
        label_resultado.config(text="Por favor, ingrese un número válido.")

def limpiar():
    entry_temperatura.delete(0, tk.END)
    label_resultado.config(text="Resultado: ")

def actualizar_historial():
    historial_texto.config(state=tk.NORMAL)
    historial_texto.delete(1.0, tk.END)
    historial_texto.insert(tk.END, "\n".join(historial[:5]))
    historial_texto.config(state=tk.DISABLED)

# Crear ventana
root = tk.Tk()
root.title("Conversor de Temperatura")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Estilos
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 12))

# Entrada de temperatura
tk.Label(root, text="Temperatura:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
entry_temperatura = tk.Entry(root, font=("Arial", 12))
entry_temperatura.pack(pady=5)

# ComboBox para escala origen
tk.Label(root, text="De:", bg="#f0f0f0", font=("Arial", 12)).pack()
combo_origen = ttk.Combobox(root, values=["Celsius", "Kelvin", "Fahrenheit"], state="readonly")
combo_origen.pack(pady=5)
combo_origen.current(0)

# ComboBox para escala destino
tk.Label(root, text="A:", bg="#f0f0f0", font=("Arial", 12)).pack()
combo_destino = ttk.Combobox(root, values=["Celsius", "Kelvin", "Fahrenheit"], state="readonly")
combo_destino.pack(pady=5)
combo_destino.current(1)

# Botones
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

btn_convertir = ttk.Button(btn_frame, text="Convertir", command=convertir)
btn_convertir.pack(side=tk.LEFT, padx=10)

btn_limpiar = ttk.Button(btn_frame, text="Limpiar", command=limpiar)
btn_limpiar.pack(side=tk.LEFT)

# Etiqueta de resultado
label_resultado = tk.Label(root, text="Resultado: ", bg="#f0f0f0", font=("Arial", 14, "bold"))
label_resultado.pack(pady=10)

# Historial de conversiones
tk.Label(root, text="Historial:", bg="#f0f0f0", font=("Arial", 12, "bold")).pack()
historial_texto = tk.Text(root, height=5, width=40, state=tk.DISABLED, font=("Arial", 10))
historial_texto.pack(pady=5)

# Ejecutar ventana
root.mainloop()
