# services/exporter.py
import pandas as pd
from services.db import list_appointments




def export_admin_report(path='data/admin_report.xlsx'):
appts = list_appointments()
with pd.ExcelWriter(path) as writer:
appts.to_excel(writer, sheet_name='appointments', index=False)
return path