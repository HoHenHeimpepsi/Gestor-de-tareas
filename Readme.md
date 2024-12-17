Instruccion ejecucion proyecto "Gestor de Tareas"

paso 1: instalar dependencias descritas en el archivo "requeriments.txt", con pip install -r requirements.txt

paso 2: insertar las claves descritas en el archivo ".env.ejemplo" dentro del codigo "app.py"

paso 3: ejecutar en la consola dentro de la carpeta en la que este ubicado el proyecto el comando "python app.py"

paso 4: como se trabaja de forma local para revisar la interfaz grafica creada con flask, debera usar la url entregada por este en la terminal.


EJECUTAR SONARQUBE MODIFICAR TOKEN

sonar-scanner.bat -D"sonar.projectKey=Tareas" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_49630cc1428e5693945fc61ce8d1673631df73ba" -D"sonar.exclusions=**/venv/**"

Algunas imagenes del proyecto final:

-) Home con una tarea creada.
![image](https://github.com/user-attachments/assets/baaa470d-eabd-4081-a3fa-58d926fb4ad7)

-) Pagina en donde se crea una tarea con su titulo y descripcion. Iniciando el estado por defecto como pendiente.
![image](https://github.com/user-attachments/assets/63f01f7d-2b23-47c9-8f58-d0b8e6dd880d)

-)Pagina donde se puede actualizar el estado de la tarea, el titulo y la descripcion.
![image](https://github.com/user-attachments/assets/7271b97e-b82f-434e-801a-30c88ac04ab6)

Las tareas solo pueden eliminarse cuando una este en estado de completado.



