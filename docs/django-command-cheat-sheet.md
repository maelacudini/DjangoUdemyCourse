# Django Command Cheat Sheet

A practical reference for the most commonly used Django commands, from installing Django and starting a project to apps, migrations, testing, static files, and deployment checks.

> Run commands from your project’s working directory unless noted. Replace names such as `config`, `core`, and `posts` with your own project/app names. Commands below use `python`; on some systems you may need `python3` or `py`.

## 1. Check Python and pip

```bash
python --version
python -m pip --version
python -m pip list
python -m pip show Django
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

## 2. Create and activate a virtual environment

Create it:

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows — Command Prompt
.venv\Scripts\activate

# Windows — PowerShell
.venv\Scripts\Activate

# macOS / Linux
source .venv/bin/activate
```

Deactivate it when finished:

```bash
deactivate
```

## 3. Install Django and manage packages

Install Django:

```bash
python -m pip install Django
```

Install a package:

```bash
python -m pip install package-name
```

Uninstall a package:

```bash
python -m pip uninstall package-name
```

Save installed packages to a requirements file:

```bash
python -m pip freeze > requirements.txt
```

Install dependencies from that file:

```bash
python -m pip install -r requirements.txt
```

See installed packages:

```bash
python -m pip list
```

## 4. Start a project

Create a new project in the current directory:

```bash
django-admin startproject config .
```

Or create a project folder named `config`:

```bash
django-admin startproject config
```

The trailing `.` in the first command means “put the project files in the current directory.” A common layout is:

```text
myproject/
├── .venv/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

Check the Django version:

```bash
python -m django --version
```

Show general management help:

```bash
python manage.py help
```

List available commands:

```bash
python manage.py help --commands
```

Get help for one command:

```bash
python manage.py help migrate
```

## 5. Run the development server

Start the local development server:

```bash
python manage.py runserver
```

Use a different port:

```bash
python manage.py runserver 8080
```

Expose the development server on your local network (use only on a trusted network):

```bash
python manage.py runserver 0.0.0.0:8000
```

Stop the server with `Ctrl+C`.

> `runserver` is for development, not production hosting.

## 6. Create and manage apps

Create an app:

```bash
python manage.py startapp core
python manage.py startapp posts
```

Add each app to `INSTALLED_APPS` in `settings.py`, for example:

```python
INSTALLED_APPS = [
    # Django apps...
    "core",
    "posts",
]
```

A typical app contains `models.py`, `views.py`, `admin.py`, `apps.py`, `tests.py`, and `migrations/`. You can create a `urls.py` file yourself if the app needs its own URL routes.

## 7. Models and migrations

After creating or changing models in an app’s `models.py`, create migration files:

```bash
python manage.py makemigrations
```

Create migrations for a specific app:

```bash
python manage.py makemigrations posts
```

Apply pending migrations to the database:

```bash
python manage.py migrate
```

Show migration status:

```bash
python manage.py showmigrations
```

Show the SQL Django would run for a migration:

```bash
python manage.py sqlmigrate posts 0001
```

View the migration plan without applying it:

```bash
python manage.py migrate --plan
```

Check whether model changes need migrations:

```bash
python manage.py makemigrations --check
```

Check for project configuration problems:

```bash
python manage.py check
```

**Usual workflow:**

```bash
# 1. Edit models.py
python manage.py makemigrations
# 2. Apply the migrations
python manage.py migrate
```

> Commit migration files to version control. In a team, create migrations locally and apply them in each environment. Avoid deleting or editing migrations that have already been applied in shared or production databases unless you understand the consequences.

## 8. Admin user and database shell

Create an admin (superuser) account:

```bash
python manage.py createsuperuser
```

Open Django’s interactive Python shell with project settings loaded:

```bash
python manage.py shell
```

Open the configured database shell, if the relevant database client is installed:

```bash
python manage.py dbshell
```

The Django admin is usually available at `/admin/` after you register models in `admin.py` and run the server.

## 9. Users and permissions

Create a superuser:

```bash
python manage.py createsuperuser
```

Change a user's password from the command line:

```bash
python manage.py changepassword username
```

For custom user creation, permissions, groups, and authentication, use Django’s built-in auth system through the admin or application code.

## 10. URLs, templates, and static files

There is no management command required every time you edit a view, URL pattern, or template. Edit your code, then refresh the browser; the development server normally reloads automatically.

Collect static files into `STATIC_ROOT` (typically for deployment):

```bash
python manage.py collectstatic
```

Run deployment configuration checks:

```bash
python manage.py check --deploy
```

> Configure `STATIC_URL`, `STATIC_ROOT`, and production static-file serving before using `collectstatic` in a deployment. Do not treat `runserver` as your production static-file server.

## 11. Tests

Run all tests Django discovers:

```bash
python manage.py test
```

Run tests for one app:

```bash
python manage.py test posts
```

Run a specific test module or class:

```bash
python manage.py test posts.tests
python manage.py test posts.tests.PostModelTests
```

Django’s test runner discovers test cases in `tests.py` and test packages. Tests that touch the database normally use Django’s test database.

## 12. Useful troubleshooting commands

Confirm Django is installed in the active Python environment:

```bash
python -m django --version
python -m pip show Django
```

Check settings and URL configuration for common issues:

```bash
python manage.py check
```

See migration state:

```bash
python manage.py showmigrations
python manage.py migrate --plan
```

Recreate a requirements file after installing dependencies:

```bash
python -m pip freeze > requirements.txt
```

If `manage.py` cannot be found, change directory to the folder containing `manage.py` before running management commands. If a command reports that Django cannot be imported, activate the correct virtual environment and install the project requirements.

## 13. Typical project setup from scratch

These commands assume you are in the folder where you want the project created.

```bash
# Create and activate a virtual environment
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux instead:
# source .venv/bin/activate

# Install Django
python -m pip install Django

# Create project files in the current directory
django-admin startproject config .

# Create apps
python manage.py startapp core
python manage.py startapp posts

# Add "core" and "posts" to INSTALLED_APPS in config/settings.py
# Define models, then make and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create admin account
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

For a fresh project, Django’s initial migrations create the built-in tables for apps such as authentication and admin. Run `makemigrations` again after changing your own models.

## 14. Quick reference

| Task | Command |
|---|---|
| Django version | `python -m django --version` |
| Install Django | `python -m pip install Django` |
| Create project in current folder | `django-admin startproject config .` |
| Create app | `python manage.py startapp posts` |
| Start dev server | `python manage.py runserver` |
| Create migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Check migration status | `python manage.py showmigrations` |
| Create admin account | `python manage.py createsuperuser` |
| Open Django shell | `python manage.py shell` |
| Run tests | `python manage.py test` |
| Collect static files | `python manage.py collectstatic` |
| Check project | `python manage.py check` |
| Deployment checks | `python manage.py check --deploy` |
| Save dependencies | `python -m pip freeze > requirements.txt` |
| Install saved dependencies | `python -m pip install -r requirements.txt` |
