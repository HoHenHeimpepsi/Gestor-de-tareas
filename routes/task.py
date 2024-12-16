from flask import Blueprint, redirect, render_template, request, url_for, flash, json
from models.Tareas import Tarea
from utils.mysql import db

tasks = Blueprint('tasks', __name__)

@tasks.route('/')
def tasks_list():
    Tareas = Tarea.query.all()
    return render_template('index.html', tasks=Tareas)

@tasks.route('/tasks/create', methods=['GET', 'POST'])
def tasks_create():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename.endswith('.json'):
                try:
                    tasks_data = json.load(file)
                    for task_data in tasks_data:
                        if not all(key in task_data for key in ('Titulo', 'Descripcion')):
                            flash("Estructura del JSON inválida. Cada tarea debe tener 'Titulo' y 'Descripcion'.")
                            return redirect(request.url)

                        new_task = Tarea(Titulo=task_data['Titulo'], Descripcion=task_data['Descripcion'])
                        db.session.add(new_task)
                    db.session.commit()
                    flash("Tareas importadas correctamente desde el archivo JSON.", "success")
                except json.JSONDecodeError:
                    flash("Error al procesar el archivo JSON.", "error")
                return redirect(url_for('tasks.tasks_list'))
            
        Titulo = request.form.get('title')
        Descripcion = request.form.get('description')
        estado = request.form.get('estado', 'Pendiente')  

        if not Titulo or not Descripcion:
            flash("Debe completar todos los campos para crear una tarea.", "error")
            return redirect(request.url)

        new_task = Tarea(Titulo=Titulo, Descripcion=Descripcion, estado=estado)
        db.session.add(new_task)
        db.session.commit()
        flash("Tarea creada correctamente", "success")

        return redirect(url_for('tasks.tasks_list'))

    return render_template('create.html')


@tasks.route('/tasks/delete/<int:id>', methods=['GET'])
def tasks_delete(id):
    task = Tarea.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()
    flash("Tarea eliminada correctamente.", "success")
    return redirect(url_for('tasks.tasks_list'))


@tasks.route('/tasks/update/<id>', methods=['GET', 'POST'])
def tasks_update(id):
    task = Tarea.query.get(id)
    if not task:
        flash("Tarea no encontrada.")
        return redirect(url_for('tasks.tasks_list'))

    if request.method == 'POST':
        try:
            task.Titulo = request.form['title']
            task.Descripcion = request.form['description']
            task.estado = request.form['estado'] 

            db.session.commit()
            flash("Tarea actualizada correctamente", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error al actualizar la tarea: {str(e)}", "error")

        return redirect(url_for('tasks.tasks_list'))
    
    return render_template('update.html', task=task)


@tasks.route('/tasks/update_status/<int:id>', methods=['POST'])
def update_status(id):
    task = Tarea.query.get_or_404(id)
    if task.estado == "Pendiente":  
        task.estado = "Finalizado"  
        db.session.commit()
        flash("Estado actualizado a 'Finalizado'", "success")
    else:
        flash("La tarea ya está finalizada o no puede ser modificada.", "error")
    
    return redirect(url_for('tasks.tasks_list'))




 