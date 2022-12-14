from flask import request, jsonify
from app import app
import app as App

from app.database import MemoryDB

@app.route('/monitoring')
def monitoring():

  service_name = request.args.get('name')
  MemoryDB().put_item(service_name)

  return jsonify({ 'status': 'ok' })

@app.route('/version')
def version():
  return jsonify({ 'version': App.Config.VERSION })