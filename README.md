# Proyecto1-Aprendizaje-de-Maquina
## Recursos utilizados
El codigo de este proyecto esta escrito en Python y los paquetes requeridos para su correcto funcionamiento son los listados a continuacion:

``` 
pip install numpy
pip install pandas
pip install matplotlib
pip install scipy
```


## Trabajo asigando
El dataset corresponde a datos reales de velocidad de vehiculos de carga de empresas en distintos puntos de la ciudad considerando información de GPS. 

 
La descripcion de campos es: 

   <figure>
    <p align="center">
      <img src="https://github.com/Matii111/Proyecto1-Aprendizaje-de-Maquina/blob/master/pred-vel-desc-campo.png?raw=true" width="900">
    </p>
  </figure>

Los demás campos (20-68) corresponden a la velocidad promedio de vehículos en coordenadas en carretera de Santiago. El orden es importante dado que indica el orden de secuencia; es decir en carretera, el punto 68 viene después de 67, y este después de 66, y así. El primer punto es entonces el 20. 

 

*Hay algunos puntos que no aparecen; asumir que sigue el orden. Por ejemplo 64 viene después de 62. En total hay 44 puntos en secuencia.*

 

*Hay restriccion en horas debido a que horas fuera de ese intervalo hubo muy poca información.*

 

**La tarea a realizar corresponde a predecir la velocidad de todos los puntos en la hora siguiente, dada la información del pasado. Por ejemplo predecir la velocidad de los 44 puntos al mediodia del 1 de Febrero del 2015.**

 
