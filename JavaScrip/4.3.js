//Tipo String
var nombre = "Tiziana";
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;

//Tipo numerico
var numero = 3000;
console.log(typeof numero);

//Tipo Object
var objeto = {
    nombre : "Tiziana ",
    apellido : " Calvo",
    telefono : "2604225020"
}

console.log(typeof objeto);

//Tipo de dato boolean
var bandera = true;
console.log(bandera);

//Tipo de dato funcion
function miFuncion(t){40}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);