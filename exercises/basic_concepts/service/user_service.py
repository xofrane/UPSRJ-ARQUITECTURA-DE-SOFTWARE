import sys
import os
from typing import List, Dict, Optional
from logging import DEBUG, INFO, WARNING, ERROR

# Ajuste del path para importar py_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

# Importamos la interfaz genérica
from exercises.basic_concepts.repository.interfaces import EntityRepository


class EntityService:
    def __init__(self, repository):
        self.repository = repository
        print("Inicializando EntityService con un repositorio")

    def get_entity_by_id(self, entity_id):
        return self.repository.get_by_id(entity_id)

    def get_entity_by_keyword(self, keyword):
        return self.repository.get_by_keyword(keyword)

    def get_all_entities(self):
        """Retorna todos los usuarios desde el repositorio"""
        return self.repository.get_all()
