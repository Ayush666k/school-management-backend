# School Management Backend

A full-featured Django REST API for managing students, teachers, and courses.

## 🔧 Tech Stack
- Django 5.0
- Django REST Framework
- JWT Authentication
- PostgreSQL (Render Cloud)

## 🚀 Deployment
Live: https://school-backend.onrender.com/api/

## 🔑 Authentication
POST /api/token/
{
  "username": "admin",
  "password": "your_password"
}

## i will update you later right now AllowAny
Use access token:
Authorization: Bearer <access_token>

## 📚 Endpoints
| Endpoint | Method | Description |
|-----------|---------|-------------|
| /api/students/ | GET, POST | List or create students |
| /api/students/{id}/ | PUT, DELETE | Update/Delete student |
| /api/courses/ | GET, POST | List or create courses |

## 🧠 Author
Ayush — Django + React Full Stack Developer.
