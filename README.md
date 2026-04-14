🎙️ Traductor-Bot:
Traductor-Bot es una aplicación interactiva desarrollada con Python (Flask) y JavaScript. El objetivo es ayudar a los usuarios a mejorar su pronunciación en inglés mediante un sistema de juego por niveles. La aplicación presenta una palabra en español y el usuario debe decir su traducción correcta en inglés en voz alta.


🚀 Características:
  -Tres niveles de dificultad: Principiante, Intermedio y Leyenda.
  -Sistema de puntuación: 10 puntos por cada acierto.
  -Feedback en tiempo real: Muestra qué interpretó la IA cuando fallás.
  -Lógica de progresión: Pantalla de resultados finales con sugerencia para subir de nivel.
  -Interfaz Moderna: Diseño oscuro (Dark Mode) con estética gamer.


🛠️ Tecnologías y Librerías

Para ejecutar este proyecto, necesitás tener instalado Python y las siguientes librerías:

-Flask: Para el servidor web.
-SoundDevice & SciPy: Para grabar el audio del micrófono.
-SpeechRecognition: Para convertir tu voz en texto.
-Deep-Translator: Para gestionar las traducciones automáticas.
-PyAudio: Requerido por la librería de reconocimiento de voz.
    Instalación>   pip install flask sounddevice scipy speechrecognition deep-translator pyaudio


📋 Estructura del Proyecto:
  /tu-proyecto
  │
  ├── app.py              # Lógica del servidor Python
  ├── output.wav          # Archivo temporal de audio (se genera solo)
  └── templates/
      └── index.html      # Interfaz de usuario y lógica JS


🎮 Paso a paso: Cómo funciona
  -Inicio: Al abrir la app, verás un menú con instrucciones claras. Seleccionás tu dificultad y hacés clic en "¡Empezar a Jugar!".
  -El Reto: Aparecerá una palabra (ej. "GATO"). Tenés que pensar la traducción ("CAT").
  -Grabación: Al presionar el botón de grabar, el servidor activará tu micrófono por unos segundos (según el nivel).
  -Procesamiento: La IA traduce la palabra, escucha tu voz, las compara y te da el resultado.
  -Puntuación: Si acertás, sumás 10 puntos. Si fallás, la app te muestra qué entendió la IA para que puedas corregirlo.
  -Fin del Juego: Al completar 5 rondas, verás tu puntaje final y podrás elegir subir de nivel si te fue bien.


🛠️ Solución a Errores Comunes (FAQ)
"No se detectó voz clara" > Asegurate de estar en un lugar silencioso y hablar cerca del micrófono. Revisá que el micrófono no esté silenciado en Windows.
Error con PyAudio > Si pip install pyaudio falla, puede que necesites instalar el compilador de C++ o descargar el .whl correspondiente a tu versión de Python.
"Error: ¿Corriste app.py?" > Este mensaje en el navegador significa que el servidor de Flask no está encendido o se cerró. Revisá la terminal de Python.


🖋️ Autora
Este es un proyecto desarrollado como parte de un curso de formación técnica.

¡Hola! Soy estudiante y siempre estoy en la búsqueda de mejorar mis habilidades. Si tenés alguna sugerencia, corrección o idea para optimizar este código, ¡tu ayuda es más que bienvenida! Podés abrir un Issue o enviarme un Pull Request para colaborar. 🚀
