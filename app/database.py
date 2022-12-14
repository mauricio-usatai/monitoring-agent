import requests
from datetime import datetime

import boto3
from boto3.dynamodb.conditions import Key

import app as App

class DynamoDB:
  def __init__(self):
    self.db_access_key_id = App.Config.ACCESS_KEY_ID
    self.db_secret_access_key = App.Config.SECRET_ACCESS_KEY
    self.machine_name = App.Config.MACHINE_NAME

  def connect(self):
    resource = boto3.resource(
      'dynamodb',
      aws_access_key_id = self.db_access_key_id,
      aws_secret_access_key = self.db_secret_access_key,
      region_name='sa-east-1',
    )
    return resource

  def get_config(self):
    return self.connect().Table('monitoring').query(
      KeyConditionExpression=Key('machine').eq(self.machine_name),
    )['Items']

class MemoryDB:
  def __init__(self):
    self.url = App.Config.MEMORY_DB_URL
    self.machine_name = App.Config.MACHINE_NAME

  def put_item(self, service_name):
    headers = { 'Content-Type': 'application/json' }
    reponse = requests.post(
      f'{self.url}/monitoring',
      json={
        'name': service_name,
        'date': str(datetime.now()),
        'machine': self.machine_name,
      },
      headers=headers,
    )
    return reponse.json()

  def get_item(self, item):
    response = requests.get(f'{self.url}/monitoring?name={item}')
    return response.json()
  
  def update_status(self, service_name, service_status):
    status = self.get_item('status')

    status[service_name] = {
      'status': service_status,
      'date': str(datetime.now()),
      'machine': self.machine_name,
    }
    new_status = {
      'status': status,
      'name': 'status',
    } 

    headers = { 'Content-Type': 'application/json' }
    reponse = requests.post(
      f'{self.url}/monitoring',
      json=new_status,
      headers=headers,
    )

  def clear_status(self):
    new_status = {
      'status': {},
      'name': 'status',
    } 

    headers = { 'Content-Type': 'application/json' }
    reponse = requests.post(
      f'{self.url}/monitoring',
      json=new_status,
      headers=headers,
    )