import os

class Config:
  ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID', None)
  SECRET_ACCESS_KEY = os.environ.get('SECRET_ACCESS_KEY', None)
  MEMORY_DB_URL = os.environ.get('MEMORY_DB_URL', None)
  MACHINE_NAME = os.environ.get('MACHINE_NAME', None)
  VERSION = os.environ.get('VERSION', None)