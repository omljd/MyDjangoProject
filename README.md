## Employee Presentation Project (Django MVT)

This is a simple, secure **Employee Presentation** web application built with Django using the **MVT (Model–View–Template)** pattern.

- **Model**: `employees.models.Employee`
- **Views**: class-based views in `employees.views`
- **Templates**: in `templates/employees/` with a shared `templates/base.html`

### 1. Setup (Windows PowerShell)

```powershell
cd C:\Users\omlun\OneDrive\Desktop\MyDjangoProject
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment variables (security)

In production you must set at least:

- **`DJANGO_SECRET_KEY`**: a long, random secret string
- **`DJANGO_DEBUG`**: `False`
- **`DJANGO_ALLOWED_HOSTS`**: e.g. `mydomain.com,www.mydomain.com`

Optional additional security flags:

- `DJANGO_SECURE_SSL_REDIRECT=1`
- `DJANGO_SESSION_COOKIE_SECURE=1`
- `DJANGO_CSRF_COOKIE_SECURE=1`
- `DJANGO_SECURE_HSTS_SECONDS=31536000`
- `DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=1`
- `DJANGO_SECURE_HSTS_PRELOAD=1`

For local development, defaults are more relaxed (`DEBUG=True`, local hosts allowed).

### 3. Database and superuser

```powershell
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run the development server

```powershell
python manage.py runserver
```

Then open:

- **Public employee list**: `http://127.0.0.1:8000/employees/`
- **Employee detail**: click an employee card
- **Admin-only list**: `http://127.0.0.1:8000/employees/admin-list/` (requires login)
- **Admin site**: `http://127.0.0.1:8000/admin/` (manage employees securely)

### 5. Security highlights

- Secret key and debug mode driven by **environment variables**.
- **SecurityMiddleware** enabled with HTTP security headers (`X_FRAME_OPTIONS=DENY`, content type sniffing protection, referrer policy).
- Hooks for **HSTS**, **secure cookies**, and **SSL redirect** configurable via env vars.
- Employee admin list protected with `LoginRequiredMixin` (requires authentication).

