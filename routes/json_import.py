from flask import request, redirect, url_for, Blueprint
import json
from models.Tareas import Tarea
from utils.mysql import db

tasks = Blueprint('tasks', __name__)

@tasks.route('/tasks/import', methods=['POST'])
def import_tasks():
    
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    
    
    if file.filename == '':
        return 'No selected file', 400

    
    try:
        tasks_data = json.load(file)
    except json.JSONDecodeError:
        return 'Invalid JSON file', 400

  
    for task_data in tasks_data:
        new_task = Tarea(Titulo=task_data['Titulo'], Descripcion=task_data['Descripcion'])
        db.session.add(new_task)

    
    db.session.commit()

    return redirect('/tasks')  
