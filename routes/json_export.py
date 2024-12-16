from flask import Blueprint, Response, request, flash, redirect, url_for
import json
from models.Tareas import Tarea

export = Blueprint('export', __name__)

@export.route('/tasks/export', methods=['GET'])
def export_tasks():
    tasks = Tarea.query.all()
    tasks_data = [{"id": task.id, "Titulo": task.Titulo, "Descripcion": task.Descripcion, "estado": task.estado} for task in tasks]

    json_data = json.dumps(tasks_data, indent=4)

    response = Response(
        json_data,
        mimetype='application/json',
        status=200
    )
    response.headers["Content-Disposition"] = "attachment; filename=tarea.json"
    
    return response


@export.route('/tasks/export_selected', methods=['POST'])
def export_selected_tasks():
    task_ids = request.form.getlist('task_ids')

    tasks = Tarea.query.filter(Tarea.id.in_(task_ids)).all()
    if not tasks:
       flash("No se encontraron tareas seleccionadas.", "error")
       return redirect(url_for('tasks.tasks_list'))
    tasks_data = [{"id": task.id, "Titulo": task.Titulo, "Descripcion": task.Descripcion, "estado": task.estado} for task in tasks]

    json_data = json.dumps(tasks_data, indent=4)

    response = Response(
        json_data,
        mimetype='application/json',
        status=200
    )
    response.headers["Content-Disposition"] = "attachment; filename=tareas_seleccionadas.json"
    
    return response