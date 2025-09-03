# services/comm.py
import os
from datetime import datetime


# Mock communicator. To enable actual sending, provide SMTP / Twilio creds via env vars.


USE_REAL_SMS = os.getenv('USE_REAL_SMS', 'false').lower() == 'true'
USE_REAL_EMAIL = os.getenv('USE_REAL_EMAIL', 'false').lower() == 'true'


# Mock functions (print to console) for now.


def send_email(to_email, subject, body, attachments=None):
# If configured, implement SMTP send here. For MVP we just print.
print(f"[EMAIL] To: {to_email} Subject: {subject}\n{body}\nAttachments: {attachments}")
return True




def send_sms(to_phone, message):
print(f"[SMS] To: {to_phone} Message: {message}")
return True




def schedule_reminders(appointment, patient, reminder_config=[1,3,7]):
# reminder_config are offsets (days) before appointment
# For MVP we simply log scheduled reminders
reminders = []
appt_dt = datetime.fromisoformat(appointment['slot'])
for offset in [7,3,1]:
send_on = appt_dt - timedelta(days=offset)
reminders.append({'send_on': send_on.isoformat(), 'method': 'email+sms'})
print('Scheduled reminders:', reminders)
return reminders