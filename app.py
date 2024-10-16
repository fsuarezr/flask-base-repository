from src import init_app

from dotenv import load_dotenv
import os

load_dotenv()

app_secret_key = os.getenv('APP_SECRET_KEY')
app_port = os.getenv('APP_PORT')

class Config:
    SECRET_KEY = app_secret_key
    DEBUG = True

# Inicializamos la app con la configuración
app = init_app(Config)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=app_port)
