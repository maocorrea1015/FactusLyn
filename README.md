# Factuslyn - Rama de Desarrollo 🧪

Este documento está dirigido a los desarrolladores que trabajan en la rama de desarrollo de **Factuslyn**, el sistema de gestión de facturación web. Aquí encontrarás los pasos básicos para clonar el proyecto, configurar el entorno de desarrollo y trabajar correctamente con Git.

---

## 🔁 Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/tuusuario/factuslyn.git
```
```bash
cd factuslyn
```
```bash
git checkout desarrollo
```
---
## 🐍 Crear y activar entorno virtual
Asegúrate de tener Python 3.10+ instalado.

---
## En Linux/macOS:
```bash
python3 -m venv env
source env/bin/activate
```
---
## En Windows:
```bash
python -m venv env
env\Scripts\activate
```
---
## 📦 Instalar dependencias
Instala las librerías necesarias usando pip:

```bash
pip install -r requirements.txt
```
---

## ⚙️ Variables de entorno
Crea un archivo .env (si aplica) con las variables necesarias para desarrollo, como por ejemplo:

```bash 
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///database.db
```
## Nota: Consulta con el equipo si hay un .env.example disponible.
---
## 🧪 Ejecutar la app en modo desarrollo
```bash
flask run
```
---
## 🧬 Comandos útiles de Git
Crear nueva rama desde desarrollo:
```bash
git checkout desarrollo
git pull origin desarrollo
git checkout -b nombre-de-tu-rama
Subir tus cambios:
```
```bash
git add .
git commit -m "Descripción clara del cambio"
git push origin nombre-de-tu-rama
```
Hacer merge de tu rama a desarrollo (vía PR preferiblemente):
Abre un Pull Request desde tu rama hacia desarrollo.

Asegúrate de que pase la revisión de código.

Haz merge desde la interfaz de GitHub o GitLab.

---
## 📌 Recomendaciones
Mantén tu rama actualizada con desarrollo:

```bash
git checkout desarrollo
git pull origin desarrollo
git checkout tu-rama
git merge desarrollo
```
Escribe mensajes de commit claros y concisos.
Usa entornos virtuales para evitar conflictos de dependencias.
No subas archivos del entorno (env/, .env, etc.).

---
## 🧠 ¿Dudas?
Si tienes alguna pregunta, contacta con el responsable técnico del proyecto o abre una issue en el repositorio.

---
## 🚀 ¡Feliz desarrollo!