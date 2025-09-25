class EntityRepository:
    def __init__(self):
        # Datos de prueba en memoria
        self.entities = [
            {"id": 1, "name": "Entity One", "description": "First test entity"},
            {"id": 2, "name": "Entity Two", "description": "Second test entity"},
            {"id": 3, "name": "Entity Three", "description": "Third test entity"},
        ]

    def get_all(self):
        return self.entities

    def get_by_id(self, id):
        return next((e for e in self.entities if e["id"] == id), None)

    def get_by_keyword(self, keyword):
        return [e for e in self.entities if keyword.lower() in e["name"].lower()]
