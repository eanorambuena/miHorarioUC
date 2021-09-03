# miHorarioUC

Personalize su propia página web miHorario, con una foto de su horario y los links a las videollamadas de los ramos que desee

## Ventajas

- No necesita internet para acceder a miHorario

- Escrita en python

- 100% personalizable

- Fácil de usar

## Requisitos

- python 3

- pip (prefiera última versión)

- eggdriver 0.0.1a6 (o superior), puede instalarlo con: pip install eggdriver==0.0.1a6

## Inicio rápido

1. Clone este Repositorio con Git.

2. Añada sus ramos en main.py

3. Remplace miHorario.jpg por una foto de su horario de clases. Recuerde mantener el nombre "miHorario.jpg"

4. Abra index.html con su navegador de preferencia

5. (Sugerido) Añada a los Marcadores / Favoritos de su navegador el sitio web miHorario que le aparecerá, con el nombre que estime conveniente

## Comandos

### ramos

Es donde se almacenan lo ramos que desea mostrar en miHorario

#### ramos.añadir

Añade un ramo a **ramos**

### ramo

Crea un ramo entregándole como argumentos el nombre de el ramo y un link a lo que desees.
Se recomienda que sea el link a la videollamada de la clase o al canvas del ramo.

### sub

Permite anidar un ramo bajo el último ramo ingresado. esto es útil para agrupar laboratorios, ayudantías, y talleres como sub-ramos de un ramo deseado.

Un sub-ramo se crea usando sub(ramo(nombre, link)). Como es un ramo, puede adjuntarle su propio link.
También puede anidar ramos y sub-ramos como sub-ramos de un sub-ramo.

## Ejemplo de main.py

from horario import *

ramos.añadir(ramo("Cálculo", "link"))

ramos.añadir(sub(ramo("LAB Cálculo", "link 2")))

ramos.añadir(sub(sub(ramo("Tarea 1 LAB Cálculo", "link 2.1"))))

ramos.añadir(ramo("Dinámica", "link 3"))

ramos.guardar()
