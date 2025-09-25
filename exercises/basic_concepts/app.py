import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
from py_utils.logger import set_logging, plog

# Ajuste del path para importar py_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importamos la aplicación Flask desde el controller
from exercises.basic_concepts.controller.routes import app

# Configuración del logging
set_logging(log_file="app.log")

if __name__ == "__main__":
    plog("Iniciando aplicación Flask", INFO)
    app.run(debug=True)
