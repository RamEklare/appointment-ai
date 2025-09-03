# services/scheduler.py
import pandas as pd
from datetime import datetime, timedelta
from services.db import save_appointment


# business rule: new patient -> 60 min, returning -> 30 min


def calculate_duration(is_returning):
return 30 if is_returning else 60




def read_availability(excel_path='data/doctor_schedules.xlsx'):
xls = pd.ExcelFile(excel_path)
data = {}
for sheet in xls.sheet_names:
df = xls.parse(sheet)
data[sheet] = df[df['available'] == 1].copy()
return data




def find_next_available(doctor_sheet_df, desired_date=None, duration=30):
# Simple greedy find: return first slot >= now on desired_date
now = datetime.now()
if desired_date:
desired = pd.to_datetime(desired_date).date()
df = doctor_sheet_df[pd.to_datetime(doctor_sheet_df['date']).dt.date == desired]
else:
df = doctor_sheet_df
if df.empty:
return None
# choose first future slot
df['slot_dt'] = pd.to_datetime(df['slot'])
df = df[df['slot_dt'] >= now]
if df.empty:
return None
return df.iloc[0]['slot_dt'].isoformat()




def book_slot(mrn, doctor, slot_iso, is_returning):
duration = calculate_duration(is_returning)
save_appointment(mrn, doctor, slot_iso, duration)
return {'mrn': mrn, 'doctor': doctor, 'slot': slot_iso, 'duration': duration}