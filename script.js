document.getElementById("title").innerHTML="Demo";
document.getElementById("image").src="demo/HorarioUC.jpg";


// class Tabla
function Tabla() {
    this.elementos=[]
    this.display=function() {
        document.write("");
    };
};

// class Ramo
function Ramo(nombre, link) {
    this.nombre = nombre;
    this.link = link;
    this.add = function() {
      document.write("");
    };
};

