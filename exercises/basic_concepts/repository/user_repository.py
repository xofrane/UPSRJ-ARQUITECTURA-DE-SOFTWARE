from py_utils.logger import plog
from logging import DEBUG, INFO

class UserRepository:
    def get_users(self):
        plog("Fetching users from repository", DEBUG)
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

class UserRepository:
    """
    Repository component that handles user data access.

    Implements the Repository design pattern to abstract data retrieval.
    """

    def get_users(self):
        """
        Returns a static list of user dictionaries.

        In a real application, this would query a database.
        """
        plog("Fetching users from repository", DEBUG)
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
