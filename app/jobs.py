import time
import schedule
import requests
import datetime

from app.database import MemoryDB, DynamoDB
from app.utils import get_time_delta

m_config = {}

def update_active_service_status(service):
  status = 'ok'
  try:
    response = requests.get(
      f"{service['active']['monitoring-endpoint']}",
      timeout=3,
    )
    if response.status_code != 200: 
      status = f'notok::{str(response.text)}'
  except Exception as e:
    status = f'notok::{str(e)}'
  finally:
    MemoryDB().update_status(service['name'], status)

def update_passive_service_status(service):
  last_service_status = MemoryDB().get_item(service['name'])
  if not last_service_status: return
  else:
    time_diff = get_time_delta(service['passive']['frequency'], last_service_status['date'])
    status = 'ok' if time_diff > 0 else 'notok'
    MemoryDB().update_status(service['name'], status)

def update_local_config():
  global m_config
  m_config = DynamoDB().get_config()

  for service in m_config:
    if service['_type'] == 'active': 
      update_active_service_status(service)

    elif service['_type'] == 'passive':
      update_passive_service_status(service)

def update_local_config_job():
  schedule.every().hour.at('00:00').do(update_local_config)
  while True:
    schedule.run_pending()
    time.sleep(1)