from flask import Flask, jsonify, request
from exercises.basic_concepts.service.entity_service import EntityService
from exercises.basic_concepts.repository.entity_repository import EntityRepository

app = Flask(__name__)

# Inicializamos repositorio y servicio
repository = EntityRepository()
service = EntityService(repository)

@app.route("/entities", methods=["GET"])
def get_all_entities():
    return jsonify(service.get_all())

@app.route("/entities/<int:entity_id>", methods=["GET"])
def get_entity_by_id(entity_id):
    entity = service.get_by_id(entity_id)
    return jsonify(entity) if entity else ("Not found", 404)

@app.route("/entities/search", methods=["GET"])
def search_entities():
    keyword = request.args.get("keyword", "")
    return jsonify(service.get_by_keyword(keyword))

if __name__ == "__main__":
    print("🚀 Servidor corriendo en http://127.0.0.1:5000/")
    app.run(debug=True)
