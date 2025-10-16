import os
import google.generativeai as genai

# --- Configuración ---
# NOTA: DEBES CREAR TU PROPIA API KEY EN Google AI Studio.
# https://aistudio.google.com/app/apikey
# Luego, crea una variable de entorno llamada "GEMINI_API_KEY" con tu clave.

try:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("No se encontró la variable de entorno GEMINI_API_KEY")
    
    genai.configure(api_key=api_key)

    # --- Creación del Modelo ---
    # Usamos el modelo gemini-pro, que es un modelo de texto versátil.
    model = genai.GenerativeModel('gemini-pro')

    # --- Enviar un Prompt Simple ---
    prompt: str = "Explica qué es Python en una sola frase."
    print(f"Enviando prompt: '{prompt}'")

    # .generate_content() envía la petición a la API
    response = model.generate_content(prompt)

    # La respuesta de texto está en response.text
    print("\n--- Respuesta de Gemini ---")
    print(response.text)

except Exception as e:
    print(f"Ha ocurrido un error: {e}")
