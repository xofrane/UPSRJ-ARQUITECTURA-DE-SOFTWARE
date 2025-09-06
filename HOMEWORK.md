# 📚 Homework – Class 2: Entity Relationships & Abstraction

## 🧩 Objective
Extend the architecture to support bidirectional relationships between users and groups, and refactor the abstraction layer to unify both entities under a common interface.

## 🛠️ Tasks
1. **Create `GroupRepository`**
- Implement a new repository class for groups.
- It must connect to `UserRepository` in both directions:
  - `get_users_for_group(group_id)` → returns all users in a group.
  - `get_groups_for_user(user_id)` → returns all groups a user belongs to.
2. Refactor Abstraction Layer
- Rename the interface `EntityRepository` to represent both users and groups.
- Ensure both `UserRepository` and `GroupRepository` implement this interface.
- Rename `EntityService` to reflect its generic role across entities.
- The service should accept any `EntityRepository` and expose:
  - `get_all()`
  - `get_by_id(id)`
  - `get_by_keyword(keyword)`
3. Update Controller
- Modify the `/search` route to:
  - Allow searching for users and groups.
  - When searching for a user, also return the groups they belong to.
  - When searching for a group, also return its members.
4. Update Templates
- `search.html`: allow switching between user and group search.
- `result.html`: show user details and their groups.
- `group.html`: show group details and its members.

## 🧠 Reflection Questions
- How does bidirectional linking between entities affect architectural complexity?
- How does abstraction via interfaces help unify logic across different entities?
- What would break if UserRepository and GroupRepository were tightly coupled?
- Which parts of the project are defined by the framework (Flask)?
- Which parts are defined by our architecture?
- Which parts implement design patterns?
