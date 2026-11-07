# Django Blog — Project Setup

## 1. Create the project directory and virtual environment

Create the root directory and move into it:

```bash
mkdir blog
cd blog
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**
```bash
source .venv/bin/activate
```

**Windows — PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows — Command Prompt**
```bat
.venv\Scripts\activate.bat
```

The `.venv` directory keeps this project's Python dependencies isolated from other projects and your system Python.

## 2. Install Django and create the project

Install Django inside the activated virtual environment:

```bash
python -m pip install django
```

Check the installed version:

```bash
python -m django --version
```

Create the Django project package from the root `blog/` directory:

```bash
django-admin startproject config .
```

The final `.` tells Django to create the project files in the current directory, rather than creating another nested directory.

The structure should look like this:

```text
blog/
├── .venv/
├── manage.py
└── config/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

Here, `config` contains project-wide settings and URL configuration. Naming it `config` is a convention, not a Django requirement.

## 3. Create and register the first app

From the root `blog/` directory, create an app for blog:

```bash
python manage.py startapp blog
```

Register the app in `config/settings.py` by adding `"blog"` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
]
```

Django does not register an app automatically when you create it, so this step is required.

The project structure now looks like this:

```text
blog/
├── .venv/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── manage.py
```

## Start the project

From inside the virtual environment run:

```bash
python manage.py runserver
```

On Windows, you can instead run `run.bat` from the project folder (or double-click it). It activates `.venv` and starts the Django development server.

### Naming conventions

- Root directory: `blog/`
- Virtual environment: `.venv/`
- Django project package: `config/`
- Django app: `blog/`
- Model classes: singular `PascalCase`, e.g. `Post`
- Python functions and variables: `snake_case`, e.g. `get_published_posts`
- Constants: `UPPER_SNAKE_CASE`
