# app.py
# Chatbot estilo WhatsApp mejorado - Eventos 💚

from app import Flask, render_template, request, jsonify
from datetime import datetime
import csv
import os

app = Flask(__name__)

# === Función principal de respuesta ===
def responder(mensaje):
    mensaje = mensaje.lower()

    if "hola" in mensaje or "buenas" in mensaje:
        return "¡Hola! 😊 Bienvenido a *Angelina Eventos*. ¿En qué puedo ayudarte hoy?"
    elif "evento" in mensaje or "servicios" in mensaje:
        return "Organizamos todo tipo de eventos 🎉: bodas, cumpleaños, aniversarios, fiestas infantiles y eventos corporativos."
    elif "cotización" in mensaje or "precio" in mensaje:
        return "Para cotizar, por favor indica el tipo de evento y cantidad de invitados 💰"
    elif "contacto" in mensaje or "número" in mensaje or "telefono" in mensaje:
        return "Puedes comunicarte con nosotros al 📞 +51 987 654 321 o al correo ✉️ contacto@eventosgalaxy.com"
    elif "horario" in mensaje or "atienden" in mensaje:
        return "Atendemos de lunes a sábado de 9:00 a.m. a 6:00 p.m. 🕕"
    elif "gracias" in mensaje or "ok" in mensaje:
        return "¡Gracias a ti! 💫 Si necesitas algo más, estaré aquí para ayudarte."
    elif "adios" in mensaje or "chau" in mensaje:
        return "¡Adiós! 👋 Que tengas un excelente día 💐"
    else:
        return "Lo siento 😅, aún estoy aprendiendo. ¿Podrías repetirlo de otra forma?"

# === Guardar historial en CSV ===
def guardar_historial(usuario, bot):
    archivo = "historial_chat.csv"
    existe = os.path.isfile(archivo)
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["Fecha", "Hora", "Usuario", "Bot"])
        hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([hora.split()[0], hora.split()[1], usuario, bot])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.get_json()
    user_msg = data.get("mensaje", "")
    respuesta = responder(user_msg)
    guardar_historial(user_msg, respuesta)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
