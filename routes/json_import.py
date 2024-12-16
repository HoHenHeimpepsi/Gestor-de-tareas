from flask import request, redirect, url_for, Blueprint, flash
import json
from models.Tareas import Tarea
from utils.mysql import db
from json import JSONDecodeError  

imports = Blueprint('imports', __name__)

@imports.route('/tasks/import', methods=['POST'])
def import_tasks():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    print(f"Archivo cargado: {file.filename}")

    if file.filename == '':
        return 'No selected file', 400

    try:
        tasks_data = json.load(file)
        print(f"Datos del archivo JSON cargado: {tasks_data}")  
    except JSONDecodeError as e:
        return f'Archivo JSON inválido: {str(e)}', 400

    tasks_imported = 0

    for task_data in tasks_data:
        print(f"Tarea importada: {task_data}") 

        if not ('Titulo' in task_data and 'Descripcion' in task_data):
            missing_keys = [key for key in ('Titulo', 'Descripcion') if key not in task_data]
            print(f"Claves faltantes: {missing_keys}")  
            return f'Missing required keys: {", ".join(missing_keys)}', 400

        
        new_estado = task_data.get('estado', 'Pendiente')

        try:
            
            new_task = Tarea(Titulo=task_data['Titulo'], Descripcion=task_data['Descripcion'], estado=new_estado)
            db.session.add(new_task)
            db.session.commit()
            tasks_imported += 1
            flash(f'Tarea "{task_data["Titulo"]}" importada correctamente.', 'success')
        except Exception as e:
            return f'Error creating task: {str(e)}', 500

    flash(f'{tasks_imported} tareas importadas correctamente.', 'success')
    return redirect(url_for('tasks.tasks_list'))
