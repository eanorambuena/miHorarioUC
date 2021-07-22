class Tabla():
    def __init__(self,nombre, link):
        self.elementos=[]
    def display(self):
        document.write("")

class Ramo():
    def __init__(self,nombre, link):
        self.nombre=nombre
        self.link=link
    def add(self):
      document.write("")

import subprocess, sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'git+https://github.com/PythonForChange/Egg.git'])

import Egg

document=Egg.pyegg.Document("template")
document.addTag("h1","Hi","aqui")
document.write("xd","2")