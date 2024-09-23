@echo off

mkdir app\static
mkdir app\templates
mkdir migrations
mkdir venv

type NUL > app\__init__.py
type NUL > app\auth_routes.py
type NUL > app\forms.py
type NUL > app\models.py
type NUL > app\routes.py

type NUL > app\static\styles.css
type NUL > app\static\bootstrap.min.css
type NUL > app\static\bootstrap.bundle.min.js

type NUL > app\templates\base.html
type NUL > app\templates\index.html
type NUL > app\templates\login.html
type NUL > app\templates\new_task.html
type NUL > app\templates\register.html
type NUL > app\templates\tasks.html
type NUL > app\templates\edit_task.html
type NUL > app\templates\error.html

type NUL > .env
type NUL > .gitignore
type NUL > config.py
type NUL > run.py

echo Directory and file structure created.
pause
