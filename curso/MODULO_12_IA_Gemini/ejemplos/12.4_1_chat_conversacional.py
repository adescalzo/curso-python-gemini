import os
import google.generativeai as genai

# --- Configuración ---
try:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("No se encontró la variable de entorno GEMINI_API_KEY")
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    # --- Iniciar un Chat Conversacional ---
    # .start_chat() crea una sesión de chat que mantiene el historial.
    chat = model.start_chat(history=[])

    print("¡Chatbot conversacional iniciado! Escribe 'salir' para terminar.")
    
    while True:
        prompt_usuario: str = input("Tú: ")

        if prompt_usuario.lower() == 'salir':
            print("Chatbot: ¡Hasta la próxima!")
            break

        # .send_message() envía el prompt y AÑADE automáticamente
        # tanto el prompt como la respuesta al historial del chat.
        response = chat.send_message(prompt_usuario)

        print(f"Chatbot: {response.text}")

except Exception as e:
    print(f"Ha ocurrido un error: {e}")
