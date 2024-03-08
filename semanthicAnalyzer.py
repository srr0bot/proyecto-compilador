from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class Analyzer:
    def semanticAnalyzer (self, code):
        self.code = code
        try:
            # Crear la instancia del cliente OpenAI con la clave de la API
            client = OpenAI(api_key=api_key)
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                                "content": f"Analiza cual  lenguaje de programacion es (Julia o Ruby)  y encuentra errores: {code}. Los errores muestralos como los mostraria el compilador nativo. si es correcto el codigo muestra la ejecucion",
                    }
                ],
            )
            response = completion.choices[0].message.content
            return response

        except OpenAIError as e:
            print(f"Error al inicializar la instancia de OpenAI: {e}")