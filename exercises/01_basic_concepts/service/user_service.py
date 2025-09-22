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
    """
    Capa de servicio genérica que maneja la lógica de negocio.
    Funciona con cualquier repositorio que implemente EntityRepository.
    """

    def __init__(self, repository: EntityRepository):
        """Inyecta el repositorio en el servicio"""
        plog("Inicializando EntityService con un repositorio", DEBUG)
        self.repository = repository

    def list_entities(self) -> List[Dict]:
        """Devuelve todas las entidades"""
        plog("Listando entidades", INFO)
        return self.repository.get_all()

    def get_entity_by_id(self, entity_id: int) -> Optional[Dict]:
        """Obtiene una entidad por su ID"""
        plog(f"Buscando entidad con ID={entity_id}", INFO)
        return self.repository.get_by_id(entity_id)

    def get_entity_by_keyword(self, keyword: str) -> List[Dict]:
        """Obtiene entidades filtradas por palabra clave"""
        plog(f"Buscando entidades con keyword='{keyword}'", INFO)
        return self.repository.get_by_keyword(keyword)
