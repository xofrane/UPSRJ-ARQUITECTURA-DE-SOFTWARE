import json
import sys
import os
from typing import List, Dict, Optional
from logging import DEBUG, INFO, WARNING, ERROR

# Ajuste del path para importar py_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

# Importamos la interfaz genérica
from exercises.basic_concepts.repository.interfaces import EntityRepository


class UserRepository(EntityRepository):
    """
    Implementación concreta de EntityRepository para Usuarios.
    Se conecta con un archivo JSON externo (users.json).
    """

    def __init__(self, json_path: str = None):
        """Permite configurar la ruta del archivo JSON (por defecto usa users.json)"""
        self.json_path = json_path or os.path.join(
            os.path.dirname(__file__), "users.json"
        )

    def _load_users(self) -> List[Dict]:
        """Carga los usuarios desde el archivo JSON"""
        plog(f"Cargando usuarios desde {self.json_path}", DEBUG)
        with open(self.json_path, "r") as file:
            users = json.load(file)
        return users

    def get_all(self) -> List[Dict]:
        """Devuelve todos los usuarios"""
        plog("Obteniendo todos los usuarios", INFO)
        return self._load_users()

    def get_by_id(self, entity_id: int) -> Optional[Dict]:
        """Busca un usuario por ID"""
        plog(f"Buscando usuario con ID={entity_id}", INFO)
        users = self._load_users()
        for user in users:
            if user.get("id") == entity_id:
                return user
        return None

    def get_by_keyword(self, keyword: str) -> List[Dict]:
        """Busca usuarios cuyo nombre contenga el keyword"""
        plog(f"Buscando usuarios con keyword='{keyword}'", INFO)
        users = self._load_users()
        return [user for user in users if keyword.lower() in user.get("name", "").lower()]
