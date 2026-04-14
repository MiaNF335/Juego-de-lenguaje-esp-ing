from flask import Flask, render_template, request, jsonify
import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
from deep_translator import GoogleTranslator
import os

app = Flask(__name__)

# Configuración de tiempos de grabación por dificultad
DIFICULTADES = {
    "1": {"tiempo": 5},
    "2": {"tiempo": 4},
    "3": {"tiempo": 3}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    data = request.json
    palabra_es = data.get('palabra', '')
    nivel = data.get('nivel', '1')
    
    # Aseguramos que el nivel exista, si no, usamos el nivel 1 por defecto
    config = DIFICULTADES.get(str(nivel), DIFICULTADES["1"])
    tiempo = config['tiempo']

    # 1. Obtener la traducción correcta
    try:
        # Usamos translate() y nos aseguramos de limpiar el texto
        objetivo_en = GoogleTranslator(source='es', target='en').translate(palabra_es).lower().strip()
    except Exception as e:
        print(f"Error en traducción: {e}")
        objetivo_en = "error"

    # 2. Grabar audio del micrófono
    sample_rate = 44100
    try:
        # Grabamos según el tiempo de la dificultad elegida
        recording = sd.rec(int(tiempo * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
        sd.wait()
        wav.write("output.wav", sample_rate, recording)
    except Exception as e:
        print(f"Error al grabar: {e}")

    # 3. Reconocimiento de voz
    recognizer = sr.Recognizer()
    intento = ""
    
    if os.path.exists("output.wav"):
        try:
            with sr.AudioFile("output.wav") as source:
                # Ajuste para ruido ambiental (mejora la precisión)
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.record(source)
                intento = recognizer.recognize_google(audio, language="en-US").lower().strip()
        except sr.UnknownValueError:
            intento = None # No entendió la palabra
        except sr.RequestError:
            intento = "Error de conexión con Google"
        except Exception as e:
            intento = None
            print(f"Error inesperado: {e}")

    # 4. Comparación de resultados
    # Usamos una comparación flexible por si Google devuelve algo con un punto final
    es_correcto = False
    if intento:
        # Eliminamos puntos o comas que el dictado pueda agregar por error
        limpio_intento = intento.replace(".", "").replace(",", "").strip()
        es_correcto = (limpio_intento == objetivo_en)
    
    return jsonify({
        "intento": intento if intento else "No se detectó voz clara",
        "objetivo": objetivo_en,
        "resultado": "✅" if es_correcto else "❌"
    })

if __name__ == '__main__':
    # Usamos debug=True para que el servidor se reinicie solo si haces cambios
    app.run(debug=True)
