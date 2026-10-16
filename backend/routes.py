"""REST endpoints for the IBM Pictures starter data."""
from . import app
import json
from pathlib import Path
from flask import jsonify, request

data = json.loads((Path(__file__).parent / 'data/pictures.json').read_text())

def error(message, status):
    return jsonify(Message=message), status

def payload():
    obj = request.get_json(silent=True)
    fields = ('id', 'pic_url', 'event_country', 'event_state', 'event_city', 'event_date')
    if not isinstance(obj, dict) or any(k not in obj for k in fields):
        return None
    if not isinstance(obj['id'], int) or isinstance(obj['id'], bool) or obj['id'] < 1:
        return None
    if any(not isinstance(obj[k], str) or not obj[k].strip() for k in fields[1:]):
        return None
    return {k: obj[k] for k in fields}

@app.get('/health')
def health():
    return jsonify(status='OK'), 200

@app.get('/count')
def count():
    return jsonify(length=len(data)), 200

@app.get('/picture')
def get_pictures():
    return jsonify(data), 200

@app.get('/picture/<int:id>')
def get_picture_by_id(id):
    picture = next((p for p in data if p['id'] == id), None)
    return (jsonify(picture), 200) if picture else error('picture not found', 404)

@app.post('/picture')
def create_picture():
    picture = payload()
    if picture is None:
        return error('Invalid picture payload', 400)
    if any(p['id'] == picture['id'] for p in data):
        return error(f"picture with id {picture['id']} already present", 302)
    data.append(picture)
    return jsonify(picture), 201, {'Location': f"/picture/{picture['id']}"}

@app.put('/picture/<int:id>')
def update_picture(id):
    existing = next((p for p in data if p['id'] == id), None)
    if existing is None:
        return error('picture not found', 404)
    picture = payload()
    if picture is None or picture['id'] != id:
        return error('Invalid picture payload or mismatched id', 400)
    existing.update(picture)
    return jsonify(existing), 200

@app.delete('/picture/<int:id>')
def delete_picture(id):
    picture = next((p for p in data if p['id'] == id), None)
    if picture is None:
        return error('picture not found', 404)
    data.remove(picture)
    return '', 204
