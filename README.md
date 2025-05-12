# 💊 Smart Health Reminder API – `healthremainder`

A backend system built using Django, PostgreSQL, Celery, and Redis to schedule and manage personalized health reminders for patients.

---

## 🚀 Project Goal

Millions of people miss their medications daily due to forgetfulness, especially the elderly and chronically ill. This API allows users to:

- Register patients
- Schedule reminders for medicine
- Automatically check reminders every minute
- Trigger a logging system (email/SMS to be added later)

---

## 🧠 Problem It Solves

- Helps patients take medications on time
- Supports hospitals, clinics, or caretakers to manage multiple patient schedules
- Provides a future-ready backend that can easily be integrated with mobile apps or web dashboards

---

## 🛠 Tech Stack

| Tool            | Usage                         |
|-----------------|-------------------------------|
| Django          | Web framework                 |
| DRF             | REST API                      |
| PostgreSQL      | Relational database           |
| Celery          | Task queue                    |
| Redis           | Celery broker                 |
| Django Celery Beat | Periodic task scheduler   |
| Python-Decouple | .env configuration            |
| Postman         | API testing                   |

---

## 🧩 Features

- Add & manage patients
- Create health reminders with time and medicine name
- Automatically checks and logs reminders every minute (can be extended to send email/SMS)
- Built with clean, scalable, and production-ready code

---

## 🏁 Getting Started


## 2. Set up Environment
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt


## 3. Configure .env
Create a .env file in the root directory:

SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=healthremainder
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
REDIS_URL=redis://localhost:6379/0


## 4. Run Migrations
python manage.py makemigrations
python manage.py migrate

## 5. Start Services
Django API:
  python manage.py runserver

Redis server (separately):
  redis-server

Celery worker:
  celery -A healthremainder worker --loglevel=info

Celery beat (scheduler):
  celery -A healthremainder beat --loglevel=info

## 🔌 API Endpoints
| Method | Endpoint             | Description        |
| ------ | -------------------- | ------------------ |
| POST   | /api/patients/       | Create patient     |
| GET    | /api/patients/       | List all patients  |
| POST   | /api/reminders/      | Create a reminder  |
| GET    | /api/reminders/      | List all reminders |
| PUT    | /api/reminders/{id}/ | Update a reminder  |
| DELETE | /api/reminders/{id}/ | Delete a reminder  |


 ## Postman Test Cases

1. Create Patient
POST http://localhost:8000/api/patients/
Body (JSON):

{
  "name": "xyz",
  "contact": "xyz@example.com"
}

2. Create Reminder
{
  "patient": 1,
  "medicine_name": "Vitamin D",
  "time": "14:30:00",
  "is_active": true
}


3. Get Patients
GET http://localhost:8000/api/patients/

5. Update Reminder
PUT http://localhost:8000/api/reminders/1/
Body (JSON):

{
  "patient": 1,
  "medicine_name": "Vitamin C",
  "time": "15:00:00",
  "is_active": true
}


6. Delete Reminder
DELETE http://localhost:8000/api/reminders/1/

7. Test Celery Logging
  Set a reminder to a time within the next minute.
  Wait for Celery Beat + Worker to print:

[Reminder Log] John Doe - Take Vitamin D at 14:30:00


## 👨‍💻 Author
Built with ❤️ by ROHAN
