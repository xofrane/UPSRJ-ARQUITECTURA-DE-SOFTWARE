# 🧠 Intro to Software Architecture with Flask

## 📘 Project Overview

This project introduces key software architecture concepts using Python and Flask.  
It demonstrates a layered architecture with clear separation of concerns through components such as:

- **Repository** (data access logic)
- **Service** (business logic)
- **Controller** (HTTP interface)

Design patterns like **Repository** and **Dependency Injection** are applied to reinforce modularity and testability.

---

## 🚀 How to Run

1. **Install Flask** (if not already installed):

```bash
pip install flask
```

2. **Run the application** 

```bash
python app.py
```

3. **Access the endpoint**
- Open your browser and go to: `http://localhost:5000/users`
- You should see a JSON list of users.

## 🧩 Architecture Summary

[ Controller ] → [ Service ] → [ Repository ]

- **Controller:** Flask route that handles HTTP requests.
- **Service:** Contains business logic and delegates to repository.
- **Repository:** Provides user data (simulated with static list).

This structure reflects a **layered architecture**, promoting separation of concerns and maintainability.

## 🗺️ Patterns Used

| Pattern              | Purpose                                  |
|----------------------|------------------------------------------|
| Repository           | Abstracts data access logic              |
| Dependency Injection | Decouples components for flexibility     |



# 🧪 Class Activities: Software Architecture with Flask

## ✅ Objectives
- Practice modular design using Python packages
- Apply separation of concerns and low coupling
- Simulate a change request (CR) and adapt architecture accordingly

---

## 📌 Activities

1. **Modularize Components**
   - Refactor the current codebase by separating components into Python packages:
     - `repository/` → contains `user_repository.py`
     - `service/` → contains `user_service.py`
     - `controller/` → contains `routes.py`
   - Ensure each package has its own `__init__.py` for proper imports.

2. **Externalize Repository Data**
   - Create a `users.json` file with user data.
   - Modify `UserRepository` to read from this external JSON file instead of returning hardcoded data.

3. **Analyze Coupling**
   - Describe the current tight coupling between `UserService` and `UserRepository`.
   - Propose a solution to reduce coupling, such as:
     - Using an abstract interface or protocol
     - Injecting the repository via configuration or factory
     - Applying the Dependency Inversion Principle

4. **Simulate a Change Request (CR)**
   - Scenario: The client now requires a keyword to access **only** the data of the matching user.
   - Tasks:
     - Modify `UserRepository` to support keyword-based filtering.
     - Update `UserService` to accept and pass the keyword.
     - Adjust the controller to receive the keyword via query parameter or request body.
     - Ensure the response returns only the matching user or an error message if not found.

5. **Render HTML Templates**
   - Use Flask's template engine to render:
     - `search.html` → form for user input
     - `result.html` → displays user data
     - `error.html` → shows error messages
     - Replace JSON responses with HTML views for better user experience.

6. **Simulate a Change Request (CR #2)**
   - Scenario: The client now wants to allow searching by either ID or keyword.
   - Tasks:
     - Update UserRepository and UserService to support both search methods.
     - Modify the controller to handle both inputs.
     - Refactor the search.html template to allow switching between ID and keyword input dynamically.

---

## 🧠 Reflection Questions

- How does modularization improve maintainability?
- What are the risks of tight coupling in evolving systems?
- Which components are most sensitive to change, and how can we isolate them?
- How would the second CR (search by ID or keyword) have been more difficult if the service and repository were tightly coupled?
- What parts of the project are provided by the framework (Flask)?
- What parts are defined by our architecture?
- What parts implement design patterns?