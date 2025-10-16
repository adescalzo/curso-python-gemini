import os
import google.generativeai as genai

# --- Configuración (igual que en la lección anterior) ---
try:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("No se encontró la variable de entorno GEMINI_API_KEY")
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    # --- Bucle de Chat ---
    print("¡Chatbot iniciado! Escribe 'salir' para terminar.")
    
    while True:
        # 1. Pedir la entrada del usuario
        prompt_usuario: str = input("Tú: ")

        # 2. Condición de salida
        if prompt_usuario.lower() == 'salir':
            print("Chatbot: ¡Hasta luego!")
            break

        # 3. Enviar el prompt al modelo y obtener respuesta
        response = model.generate_content(prompt_usuario)

        # 4. Mostrar la respuesta del chatbot
        print(f"Chatbot: {response.text}")

except Exception as e:
    print(f"Ha ocurrido un error: {e}")
