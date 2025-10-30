from .settings import *

DEBUG = False
# CORS settings
CORS_ALLOW_ALL_ORIGINS = True  # For development only
ALLOWED_HOSTS = [
    'school-management-backend-mibm.onrender.com',
    '.onrender.com',
    'localhost',
    '127.0.0.1'
]

CSRF_TRUSTED_ORIGINS = [
    'https://school-management-backend-mibm.onrender.com',
    'https://*.onrender.com'
]

CORS_ALLOWED_ORIGINS = [
    "https://school-management-backend-mibm.onrender.com",
    "https://your-react-frontend.vercel.app",  # Your React app domain
    "http://localhost:3000",  # For local development
]

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'render_db',
        'USER': 'render_user',
        'PASSWORD': 'render_password',
        'HOST': 'db-host',
        'PORT': '5432',
    }
}

# Security headers
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True