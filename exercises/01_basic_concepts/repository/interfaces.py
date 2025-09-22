from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR

# Ajuste del path para importar py_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

# Interfaz genérica para repositorios de entidades (Usuarios, Grupos, etc.)
class EntityRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Dict]:
        """Devuelve todas las entidades"""
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[Dict]:
        """Busca una entidad por su ID"""
        pass

    @abstractmethod
    def get_by_keyword(self, keyword: str) -> List[Dict]:
        """Busca entidades que coincidan con una palabra clave"""
        pass
