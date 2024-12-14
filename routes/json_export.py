import json
from flask import Response, Blueprint
from models.Tareas import Tarea

tasks = Blueprint('tasks', __name__)

@tasks.route('/tasks/export', methods=['GET'])
def export_tasks():
    tasks = Tarea.query.all()

   
    tasks_data = [{"id": task.id, "Titulo": task.Titulo, "Descripcion": task.Descripcion} for task in tasks]

    
    json_data = json.dumps(tasks_data, indent=4)

    response = Response(
        json_data,
        mimetype='application/json',
        status=200
    )
    response.headers["Content-Disposition"] = "attachment; filename=tarea.json"
    
    return response
