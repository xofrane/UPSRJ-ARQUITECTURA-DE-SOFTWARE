from py_utils.logger import plog  # tu logger personalizado
from logging import DEBUG, INFO   # niveles de log
from repository.user_repository import UserRepository  # importar la clase

class UserService:
    """
    Service component that contains business logic.

    Uses dependency injection to receive a repository instance.
    """

    def __init__(self, repository: UserRepository):
        """Initializes the service with a given repository."""
        plog("Initializing UserService with repository", DEBUG)
        self.repository = repository

    def list_users(self):
        """Retrieves the list of users from the repository."""
        plog("Listing users from service", INFO)
        return self.repository.get_users()