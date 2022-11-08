from flask import request, jsonify
from app import app

from app.database import MemoryDB

@app.route('/monitoring')
def monitoring():

  service_name = request.args.get('name')
  print(f'Passive check for {service_name}')
  MemoryDB().put_item(service_name)

  return jsonify({ 'status': 'ok' })
