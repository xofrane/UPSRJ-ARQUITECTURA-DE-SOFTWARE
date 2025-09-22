import json
import os
from exercises.basic_concepts.repository.interfaces import EntityRepository
from exercises.basic_concepts.repository.user_repository import UserRepository

class GroupRepository(EntityRepository):
    def __init__(self):
        json_path = os.path.join(os.path.dirname(__file__), "groups.json")
        with open(json_path, "r", encoding="utf-8") as f:
            self.groups = json.load(f)
        self.user_repo = UserRepository()

    def get_all(self):
        return self.groups

    def get_by_id(self, id: int):
        for g in self.groups:
            if g["id"] == id:
                return g
        return None

    def get_by_keyword(self, keyword: str):
        return [g for g in self.groups if keyword.lower() in g["name"].lower()]

    
    def get_users_for_group(self, group_id: int):
        group = self.get_by_id(group_id)
        if not group:
            return []
        members = group.get("members", [])
        return [self.user_repo.get_by_id(uid) for uid in members if self.user_repo.get_by_id(uid)]

    def get_groups_for_user(self, user_id: int):
        return [g for g in self.groups if user_id in g.get("members", [])]
