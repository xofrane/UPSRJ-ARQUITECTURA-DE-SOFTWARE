# 🧭 Instructions for Students – Week 1 Setup & Submission

Welcome to your first assignment in Software Architecture. This guide will help you copy the base code, work on your solution, and submit it for evaluation.

---

## 📥 Step 1: Fork the Repository

1. Go to the public repository:  
   👉 [https://github.com/chucholoport/UPSRJ-ARQUITECTURA-DE-SOFTWARE](https://github.com/chucholoport/UPSRJ-ARQUITECTURA-DE-SOFTWARE)
2. Click the **Fork** button in the top-right corner.
3. This will create a copy of the repository under your GitHub account.

---

## 💻 Step 2: Clone Your Fork Locally

```bash
git clone https://github.com/your-username/UPSRJ-ARQUITECTURA-DE-SOFTWARE.git
cd UPSRJ-ARQUITECTURA-DE-SOFTWARE
```


## 🛠️ Step 3: Implementa tu solución sobre la rama develop
- Trabaja directamente sobre la rama `develop` de tu fork.
- Sigue las instrucciones en `README.md` y `HOMEWORK.md`.

> 💡 **Nota:** Puedes usar herramientas de IA para ayudarte con el diseño de plantillas HTML, sugerencias de layout, estilos, etc.

## 📤 Step 4: Commit y Push
Guarda tus cambios y súbelos a tu fork:
```bash
git add .
git commit -m "Solución semana 1: implementación completa"
git push origin develop
```

## 📮 Step 5: Entrega tu trabajo
Para la entrega:
1. Ve a la pestaña **Actions** de tu repositorio en GitHub.
2. Haz clic en el workflow "Autograde" más reciente que se haya ejecutado sobre tu rama `develop`.
3. Copia el link de la ejecución (URL en tu navegador).
4. Comparte ese link en la plataforma classroom, según las instrucciones del profesor.

> 💡 **Nota:** Asegúrate de que tu rama develop tenga todos tus cambios antes de copiar el link de autograde.

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