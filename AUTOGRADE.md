# Configuración del ambiente de Autograde en GitHub Web IDE


Para que el sistema de autograde funcione correctamente en tu repositorio, debes:

1. Activar GitHub Actions en tu repositorio.
2. Agregar un secreto de autenticación (Personal Access Token) en la configuración de GitHub Actions.

Sigue estos pasos:

## 1. Accede a la configuración de secretos

1. Ingresa a tu repositorio en GitHub.
2. Haz clic en la pestaña **Settings** (Configuración).
3. En el menú lateral, selecciona **Secrets and variables** > **Actions**.
4. Haz clic en **New repository secret** (Nuevo secreto de repositorio).

## 2. Agrega el secreto requerido

- **Name**: `AUTOGRADE_PAT`
- **Secret**: `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`

> ⚠️ **Importante:** El valor del secret (`ghp_...`) es un ejemplo. Usa el token personal que corresponda a tu organización o cuenta.

## 3. Guarda el secreto

Haz clic en **Add secret** para guardar.

---

## 4. Activa GitHub Actions (si es necesario)

1. Ve a la pestaña **Actions** de tu repositorio en GitHub.
2. Si ves un mensaje indicando que las Actions están deshabilitadas, haz clic en **Enable Actions** o **Activar Actions**.
3. Confirma la activación si se solicita.

---

Una vez configurado y activadas las Actions, los workflows de autograde podrán autenticarse y ejecutarse correctamente en tu repositorio.

## 5. ¿Cómo leer el resultado de Autograde?

El pipeline de autograde se ejecuta automáticamente en los siguientes casos:
- Cuando haces push a las ramas `develop` o `feature/exercise**`.
- Cuando abres un pull request hacia esas ramas.

### Pasos del pipeline (autograde.yml)

1. **Checkout del repositorio:** Descarga el código de tu repositorio.
2. **Configura Python:** Prepara un entorno virtual con Python 3.11.
3. **Instala dependencias:** Ejecuta `pip install -r requirements.txt` para instalar los paquetes necesarios.
4. **Clona el repositorio de evaluación:** Descarga el repositorio `autograde-core` usando tu AUTOGRADE_PAT.
5. **Ejecuta las pruebas:** Corre los tests con `pytest` sobre tu código, usando los scripts de autograde-core.

### ¿Dónde ver los resultados?

1. Ve a la pestaña **Actions** de tu repositorio en GitHub.
2. Haz clic en el workflow "Autograde" más reciente.
3. Revisa los logs de cada paso para ver si hubo errores o si las pruebas pasaron.
4. El resultado final (aprobado o con errores) se muestra al final del pipeline.

---