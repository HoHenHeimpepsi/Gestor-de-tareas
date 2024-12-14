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
                        new_task = Tarea(Titulo=task_data['Titulo'], Descripcion=task_data['Descripcion'])
                        db.session.add(new_task)
                    db.session.commit()
                    flash("Tareas importadas correctamente desde el archivo JSON.")
                except json.JSONDecodeError:
                    flash("Error al procesar el archivo JSON.")
                    
        else:
            Titulo = request.form['title']
            Descripcion = request.form['description']
            new_task = Tarea(Titulo, Descripcion)
            db.session.add(new_task)
            db.session.commit()
            flash("Tarea creada correctamente")

        return redirect(url_for('tasks.tasks_list'))

    return render_template('create.html') 
    

@tasks.route('/tasks/delete/<id>', methods=['GET', 'POST'])
def tasks_delete(id):
    task = Tarea.query.get(id)
    db.session.delete(task)
    db.session.commit()

    flash("Tarea eliminada correctamente")
    return redirect(url_for('tasks.tasks_list'))


@tasks.route('/tasks/update/<id>', methods=['GET', 'POST'])
def tasks_update(id):
    if request.method == 'POST':
        task = Tarea.query.get(id)
        task.Titulo = request.form['title']
        task.Descripcion = request.form['description']
        db.session.commit()

        flash("Tarea actualizada correctamente")

        return redirect(url_for('tasks.tasks_list'))
    
    return render_template('update.html', task=Tarea.query.get(id))



 