# 🧭 Instructions for Students – Week 1 Setup & Submission

Welcome to your first assignment in Software Architecture. This guide will help you copy the base code, work on your solution, and submit it for evaluation.

---

## 📥 Step 1: Fork the Repository

1. Go to the public repository:  
   👉 [https://github.com/chucholoport/UPSRJ-ARQUITECTURA-DE-SOFTWARE-ALUMNOS](https://github.com/chucholoport/UPSRJ-ARQUITECTURA-DE-SOFTWARE-ALUMNOS)
2. Click the **Fork** button in the top-right corner.
3. This will create a copy of the repository under your GitHub account.

---

## 💻 Step 2: Clone Your Fork Locally

```bash
git clone https://github.com/your-username/UPSRJ-ARQUITECTURA-DE-SOFTWARE-ALUMNOS.git
cd UPSRJ-ARQUITECTURA-DE-SOFTWARE-ALUMNOS
```

## 🧪 Step 3: Create Your Working Branch
```bash
git checkout -b week-1-solution
```

Use a descriptive name like `week-1-solution` or `feature/yourname-week1`


## 🛠️ Step 4: Implement Your Solution
- Follow the instructions in `README.md` and `HOMEWORK.md`

> 💡 **Note:** You are encouraged to use AI tools freely to assist with HTML template design.
Whether it's layout suggestions, styling, or dynamic rendering ideas—leverage them to improve clarity and usability.


## 📤 Step 5: Commit Your Work
```bash
git add .
git commit -m "Week 1 solution: implemented user/group search and templates"
```

## 🚀 Step 6: Push Your Branch
```bash
git push origin week-1-solution
```

## 📮 Step 7: Submit via Pull Request
Once your branch is pushed to your forked repository:
1. Copy the URL of your solution branch, for example:
`https://github.com/your-username/UPSRJ-ARQUITECTURA-DE-SOFTWARE-ALUMNOS/tree/week-1-solution`
2. Send this link to the instructor via the designated channel (email, Teams, classroom platform, etc.)

> 💡 **Note:** Make sure the branch is visible and contains all your committed work before submitting.

## 🧠 Tips
- Commit often with meaningful messages.
- Ask questions early if you're stuck.
- You can update your PR until the deadline.
Good luck, and enjoy building!


## 📊 Evaluation Criteria
| Criterion                      | Description                                                                 | Max Points |
|--------------------------------|-----------------------------------------------------------------------------|------------|
| 🧩 Modular Architecture        | Clear separation of components (`repository/`, `service/`, `controller/`)  |     20     |
| 🧠 Abstraction & Interfaces    | Use of abstract classes or interfaces to reduce coupling and improve reuse |     20     |
| ⚙️ Framework Usage (Flask)     | Proper use of Flask routing, templates, and request handling               |     15     |
| 📋 Homework Compliance         | Implements all required features from `HOMEWORK.md`                        |     25     |
| 🌐 GitHub Workflow             | Uses branches, commits, and pull requests correctly                        |     10     |
| 🎯 Overall Clarity & Quality   | Code readability, naming, comments, and template usability                 |     10     |
|                                | **Total**                                                                  |   **100**  |