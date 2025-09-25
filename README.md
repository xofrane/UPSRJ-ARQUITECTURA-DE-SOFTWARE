
# **Politécnica de Santa Rosa**

- **Carrera: ISW**
- **Materia: Arquitectura de Software**
- **Instructor:** Jesús Salvador López Ortega ([LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport))

---

## **Índice**
- [**Politécnica de Santa Rosa**](#politécnica-de-santa-rosa)
  - [**Índice**](#índice)
  - [**Introducción**](#introducción)
  - [**Configuración del entorno**](#configuración-del-entorno)
    - [🥚 Activar entorno virtual con setup\_venv.ps1](#-activar-entorno-virtual-con-setup_venvps1)
    - [🎨 Colores en la terminal](#-colores-en-la-terminal)
    - [🏁 Ejecución de scripts de actividad](#-ejecución-de-scripts-de-actividad)
    - [💬 Log generado](#-log-generado)
  - [**Configuración de Autograde**](#configuración-de-autograde)
    - [⚙️ Paso 1. Accede a la configuración de secretos](#️-paso-1-accede-a-la-configuración-de-secretos)
    - [🤫 2. Agrega el secreto requerido](#-2-agrega-el-secreto-requerido)
    - [💾 3. Guarda el secreto](#-3-guarda-el-secreto)
    - [✅ 4. Activa GitHub Actions (si es necesario)](#-4-activa-github-actions-si-es-necesario)
    - [👓 5. ¿Cómo leer el resultado de Autograde?](#-5-cómo-leer-el-resultado-de-autograde)
      - [👣 Pasos del pipeline (autograde.yml)](#-pasos-del-pipeline-autogradeyml)
      - [🔦 ¿Dónde ver los resultados?](#-dónde-ver-los-resultados)
  - [**Flujo de trabajo con GitHub**](#flujo-de-trabajo-con-github)
    - [📥 Paso 1: Haz Fork al Repositorio](#-paso-1-haz-fork-al-repositorio)
    - [💻 Paso 2: Clona tu Fork localmente](#-paso-2-clona-tu-fork-localmente)
    - [🛠️ Paso 3: Implementa tu solución sobre la rama develop](#️-paso-3-implementa-tu-solución-sobre-la-rama-develop)
    - [📤 Paso 4: Commit y Push](#-paso-4-commit-y-push)
    - [📮 Paso 5: Entrega tu trabajo](#-paso-5-entrega-tu-trabajo)
  - [**Criterios de evaluación**](#criterios-de-evaluación)
  - [**Contacto**](#contacto)

---

## **Introducción**
Este repositorio contiene los ejercicios y prácticas de la materia **Arquitectura de Software**. Aquí aprenderás a estructurar aplicaciones usando buenas prácticas, frameworks y herramientas modernas.

---

## **Configuración del entorno**

### 🥚 Activar entorno virtual con setup_venv.ps1
1. Abre PowerShell en la raíz del repositorio.
2. Ejecuta:
   ```powershell
   .\setup_venv.ps1
   ```
   Esto creará (si no existe) y activará el entorno virtual `venv`, instalará las dependencias de `requirements.txt` y mostrará los paquetes instalados.

### 🎨 Colores en la terminal
- <span style="color:gold;font-weight:bold">Amarillo</span>: El entorno virtual ya existe.
- <span style="color:royalblue;font-weight:bold">Azul</span>: Proceso en curso (creando entorno, instalando dependencias, etc.) / línea de debugging.
- <span style="color:green;font-weight:bold">Verde</span>: Proceso exitoso (entorno creado, dependencias instaladas, entorno listo).
- <span style="color:red;font-weight:bold">Rojo</span>: Error (por ejemplo, falta `requirements.txt`).

### 🏁 Ejecución de scripts de actividad
Para correr un ejercicio, navega a la carpeta correspondiente y ejecuta el script `.ps1` o el archivo Python, por ejemplo:
```powershell
cd exercises\01_basic_concepts
py app.py
```
O desde la raíz:
```powershell
py -m exercises.01_basic_concepts.app
```

**Para cada entrega el profesor te proveerá un script `.ps1` con el comando para ejecutar la actividad desde el directorio raíz, por ejemplo:**
```powershell
.\01_basic_concepts.ps1
```

### 💬 Log generado
Al ejecutar la aplicación, se genera un archivo `.log` (si tu app usa logging). Este archivo contiene los mensajes de log útiles para depuración y seguimiento de la ejecución.

---

## **Configuración de Autograde**

Para que el sistema de autograde funcione correctamente en tu repositorio, debes:

1. Activar GitHub Actions en tu repositorio.
2. Agregar un secreto de autenticación (Personal Access Token) en la configuración de GitHub Actions.

Sigue estos pasos:

### ⚙️ Paso 1. Accede a la configuración de secretos

1. Ingresa a tu repositorio en GitHub.
2. Haz clic en la pestaña **Settings** (Configuración).
3. En el menú lateral, selecciona **Secrets and variables** > **Actions**.
4. Haz clic en **New repository secret** (Nuevo secreto de repositorio).

### 🤫 2. Agrega el secreto requerido

- **Name**: `AUTOGRADE_PAT`
- **Secret**: `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`

> ⚠️ **Importante:** El valor del secret (`ghp_...`) es un ejemplo. Usa el token personal que corresponda a tu organización o cuenta.

### 💾 3. Guarda el secreto

Haz clic en **Add secret** para guardar.

### ✅ 4. Activa GitHub Actions (si es necesario)

1. Ve a la pestaña **Actions** de tu repositorio en GitHub.
2. Si ves un mensaje indicando que las Actions están deshabilitadas, haz clic en **Enable Actions** o **Activar Actions**.
3. Confirma la activación si se solicita.

Una vez configurado y activadas las Actions, los workflows de autograde podrán autenticarse y ejecutarse correctamente en tu repositorio.

### 👓 5. ¿Cómo leer el resultado de Autograde?

El pipeline de autograde se ejecuta automáticamente en los siguientes casos:
- Cuando haces push a las ramas `develop` o `feature/exercise**`.
- Cuando abres un pull request hacia esas ramas.

#### 👣 Pasos del pipeline (autograde.yml)

1. **Checkout del repositorio:** Descarga el código de tu repositorio.
2. **Configura Python:** Prepara un entorno virtual con Python 3.11.
3. **Instala dependencias:** Ejecuta `pip install -r requirements.txt` para instalar los paquetes necesarios.
4. **Clona el repositorio de evaluación:** Descarga el repositorio `autograde-core` usando tu AUTOGRADE_PAT.
5. **Ejecuta las pruebas:** Corre los tests con `pytest` sobre tu código, usando los scripts de autograde-core.

#### 🔦 ¿Dónde ver los resultados?

1. Ve a la pestaña **Actions** de tu repositorio en GitHub.
2. Haz clic en el workflow "Autograde" más reciente.
3. Revisa los logs de cada paso para ver si hubo errores o si las pruebas pasaron.
4. El resultado final (aprobado o con errores) se muestra al final del pipeline.

---

## **Flujo de trabajo con GitHub**

### 📥 Paso 1: Haz Fork al Repositorio

1. Ve al repositorio público:  
   👉 [https://github.com/chucholoport/UPSRJ-ARQUITECTURA-DE-SOFTWARE](https://github.com/chucholoport/UPSRJ-ARQUITECTURA-DE-SOFTWARE)
2. Da click en el botón **Fork** en la esquina superior derecha.
3. Esto creará una copia del repositorio en tu cuenta personal de GitHub.

### 💻 Paso 2: Clona tu Fork localmente
Clona tu Fork localmente para que puedas usar todas las herramientas embebidas de Visual Studio Code.
```bash
git clone https://github.com/your-username/UPSRJ-ARQUITECTURA-DE-SOFTWARE.git
cd UPSRJ-ARQUITECTURA-DE-SOFTWARE
```

### 🛠️ Paso 3: Implementa tu solución sobre la rama develop
- Trabaja directamente sobre la rama `develop` de tu fork.
- Sigue las instrucciones en `README.md`.

> 💡 **Nota:** Puedes usar herramientas de IA para ayudarte con el diseño de plantillas HTML, sugerencias de layout, estilos, etc.

### 📤 Paso 4: Commit y Push
Guarda tus cambios y súbelos a tu fork:
```bash
git add .
git commit -m "Solución semana 1: implementación completa"
git push origin develop
```

> 💡 **Nota:** Puedes poner el mensaje que gustes para el commit siempre que mantengas el respeto y profesionalidad.

### 📮 Paso 5: Entrega tu trabajo
Para la entrega:
1. Ve a la pestaña **Actions** de tu repositorio en GitHub.
2. Haz clic en el workflow "Autograde" más reciente que se haya ejecutado sobre tu rama `develop`.
3. Copia el link de la ejecución (URL en tu navegador).
4. Comparte ese link en la plataforma classroom, según las instrucciones del profesor.

> 💡 **Nota:** Asegúrate de que tu rama develop tenga todos tus cambios antes de copiar el link de autograde.

---

## **Criterios de evaluación**
| Criterio                      | Descripción                                                                 | Puntos |
|-------------------------------|-----------------------------------------------------------------------------|--------|
| 🧩 Modular Architecture        | Separación clara de componentes (`repository/`, `service/`, `controller/`)  |   20   |
| 🧠 Abstraction & Interfaces    | Uso de clases abstractas o interfaces para bajo acoplamiento y reutilización |   20   |
| ⚙️ Framework Usage (Flask)     | Uso correcto de Flask, rutas, templates, manejo de requests                 |   15   |
| 📋 Homework Compliance         | Cumple con todos los requerimientos de `HOMEWORK.md`                        |   25   |
| 🌐 GitHub Workflow             | Uso correcto de ramas, commits y entrega                                    |   10   |
| 🎯 Overall Clarity & Quality   | Legibilidad, nombres, comentarios, usabilidad de templates                  |   10   |
|                               | **Total**                                                                   | **100**|

---

## **Contacto**

¿Dudas? Consulta los archivos de ayuda o pregunta a tu instructor.

**Autor:** Jesús Salvador López Ortega  
[LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport)

Actualizado: septiembre 2025#   C a m b i o   p a r a   d i s p a r a r   A c t i o n s  
 #   R e - r u n   A c t i o n s   c o n   s e c r e t   A U T O G R A D E _ P A T  
 #   F o r z a r   w o r k f l o w   c o n   m i   u s u a r i o  
 # #   P r o b a r   a u t o g r a d e  
 