from flask import Flask, jsonify

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
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]


class UserService:
    """
    Service component that contains business logic.

    Uses dependency injection to receive a repository instance.
    """

    def __init__(self, repository: UserRepository):
        """Initializes the service with a given repository."""
        self.repository = repository

    def list_users(self):
        """Retrieves the list of users from the repository."""
        return self.repository.get_users()


app = Flask(__name__)
user_service = UserService(UserRepository())

@app.route("/users")
def get_users():
    """HTTP endpoint that returns a JSON list of users."""
    users = user_service.list_users()
    return jsonify(users)


if __name__ == "__main__":
    # Entry point: runs the Flask development server in debug mode.
    app.run(debug=True)