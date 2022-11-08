from flask import Flask
from threading import Thread

from config import Config
from app.database import DynamoDB, MemoryDB
from app.jobs import update_local_config_job

app = Flask(__name__)
app.config.from_object(Config)

Thread(target=update_local_config_job).start()

from app import routes

