class document():
    def __init__(self,name):
        self.name=name
    def write(self,tag):
        return "done"
        
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


