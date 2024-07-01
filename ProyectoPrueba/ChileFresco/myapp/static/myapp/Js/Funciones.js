const btnAbrirModal = document.querySelector("#btn-abrir-modal");
const modal = document.querySelector("#exampleModal");

btnAbrirModal.addEventListener("click", () => {
    console.log("it's modaling time")
    var myModal = new bootstrap.Modal(modal);
    myModal.show();
});


function limpiar_campos(){
    console.log("Campos limpiados") 
    document.getElementById('nombre').value = ' ';
    document.getElementById('email').value = ' ';
    document.getElementById('rut').value = ' ';
    document.getElementById('tlf').value = ' ';
    document.getElementById('city').value = ' ';
    document.getElementById('comment').value = ' ';
    

}

function validarCampos() {
    console.log("Validando datos de formulario")
    var nombre = document.getElementById('nombre').value;
    var email = document.getElementById('email').value;
    var rut = document.getElementById('rut').value;
    var tlf = document.getElementById('tlf').value;
    var city = document.getElementById('city').value;

    if (nombre.trim() === '') {
        document.getElementById('nombre').value = '';
        alert('Por favor, ingresa tu nombre.');
        return;
    }
    if (email.trim() === '') {
        document.getElementById('email').value = '';
        alert('Por favor, ingresa tu email.');
        return;
    }
    if (rut.trim() === '') {
        document.getElementById('rut').value = '';
        alert('Por favor, ingresa tu rut/pasaporte.');
        return;
    }
    if (tlf.trim() === '') {
        document.getElementById('tlf').value = '';
        alert('Por favor, ingresa tu telefono.');
        return;
    }
    if (city.trim() === '') {
        document.getElementById('city').value = '';
        alert('Por favor, ingresa tu ciudad.');
        return;
    }
    if (mensaje !==""){
        alert (mensaje);
        return;
    }
    window.alert("Datos de formulario ingresados correctamente "+nombre)
    limpiar_campos();

}

/* filtro productos */
filterSelection("all");
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("filterDiv");
  if (c == "all") c = "";
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}


/*google maps api*/
/*AIzaSyBM2nMYgnN2PTeUjnZhPj3nSma_HxXA7sk*/ 

function initMap() {
    var location = {lat: -41.34427977478903, lng: -72.94484012945983};
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: location
    });
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
}