import eggdriver as ed

def ramo(nombre, link):
        return f"<li><a href=\"{link}\">{nombre}</a></li>"

def sub(ramo):
    return f"<ul>{ramo}</ul>"

class Ramos():
    def __init__(self):
        self.text = ""
    def añadir(self, ramo):
        self.text += ramo + "\n"
    def guardar(self):
        document = ed.Document("template")
        document.write(self.text, "ramos")

ramos = Ramos()    


