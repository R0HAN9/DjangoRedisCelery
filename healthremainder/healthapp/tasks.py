from celery import shared_task
from datetime import datetime
from .models import Reminder

@shared_task
def send_reminders():
    now = datetime.now().time()
    reminders = Reminder.objects.filter(
        time__hour=now.hour, time__minute=now.minute, is_active=True
    )
    for r in reminders:
        print(f"[Reminder Log] {r.patient.name} - Take {r.medicine_name} at {r.time}")