Instruccion ejecucion proyecto "Gestor de Tareas"

paso 1: instalar dependencias descritas en el archivo "requeriments.txt"

paso 2: insertar las claves descritas en el archivo ".env.ejemplo" dentro del codigo "app.py"

paso 3: ejecutar en la consola dentro de la carpeta en la que este ubicado el proyecto el comando "python app.py"

paso 4: como se trabaja de forma local para revisar la interfaz grafica creada con flask, debera usar la url entregada por este en la terminal.


EJECUTAR SONARQUBE MODIFICAR TOKEN

sonar-scanner.bat -D"sonar.projectKey=Tareas" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_49630cc1428e5693945fc61ce8d1673631df73ba" -D"sonar.exclusions=**/venv/**"


