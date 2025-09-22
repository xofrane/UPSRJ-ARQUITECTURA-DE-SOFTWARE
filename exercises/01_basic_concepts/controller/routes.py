from flask import Flask, request, render_template
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR

# Ajuste del path para importar py_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

# Importamos repositorio y servicio
from exercises.basic_concepts.repository.user_repository import UserRepository
from exercises.basic_concepts.service.user_service import EntityService

# Inicialización de Flask
app = Flask(__name__)

# Inyección de dependencias
user_repo = UserRepository()
entity_service = EntityService(user_repo)


@app.route("/")
def home():
    """Página principal con formulario de búsqueda"""
    plog("Cargando página principal /", INFO)
    return render_template("search.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Ruta para buscar entidades (usuarios).
    Permite búsqueda por ID o por keyword.
    """
    plog("Recibida petición en /search", INFO)

    if request.method == "POST":
        search_type = request.form.get("search_type")  # id o keyword
        query = request.form.get("query")

        if search_type == "id":
            try:
                user_id = int(query)
                user = entity_service.get_entity_by_id(user_id)
                if user:
                    return render_template("result.html", result=user)
                else:
                    return render_template("error.html", message=f"No se encontró usuario con ID {user_id}")
            except ValueError:
                return render_template("error.html", message="El ID debe ser un número válido.")

        elif search_type == "keyword":
            results = entity_service.get_entity_by_keyword(query)
            if results:
                return render_template("result.html", result=results)
            else:
                return render_template("error.html", message=f"No se encontraron usuarios con '{query}'.")

        else:
            return render_template("error.html", message="Tipo de búsqueda no válido.")

    # Si es GET → redirigimos al formulario
    return render_template("search.html")
