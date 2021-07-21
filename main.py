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


from github_com.PythonForChange.Egg import Document


document=Document("template")
document.addTag("h1","Hi","aqui")
document.write("xd","2")