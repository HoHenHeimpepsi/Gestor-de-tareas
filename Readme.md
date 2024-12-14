EJECUTAR SONARQUBE MODIFICAR TOKEN

sonar-scanner.bat -D"sonar.projectKey=Tareas" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_49630cc1428e5693945fc61ce8d1673631df73ba" -D"sonar.exclusions=**/venv/**"
