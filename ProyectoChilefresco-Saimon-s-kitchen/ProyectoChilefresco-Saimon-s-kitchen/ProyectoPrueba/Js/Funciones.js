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

document.addEventListener('DOMContentLoaded', function () {
    var loginForm = document.getElementById('loginForm');
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form submission
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        if (username === 'admin' && password === '123') {
            // Update the button text to "Account"
            console.log("Inicio de sesión con éxito " + username);
            var loginButton = document.getElementById('loginButton');
            loginButton.innerText = 'Account';
            loginButton.removeAttribute('data-bs-toggle'); // Remove the data-bs-toggle attribute
            loginButton.removeAttribute('data-bs-target'); // Remove the data-bs-target attribute

            // Redirect the user to the "CUENTA" HTML page
            window.location.href = '../Html/CUENTA.html';
        } else {
            // If login fails, you can display an error message or perform any other action
            window.alert('Contraseña inválida.');
        }
    });
});
    let map;

    async function initMap() {
      const { Map } = await google.maps.importLibrary("maps");
    
      map = new Map(document.getElementById("map"), {
        center: { lat:-41.344223830903864, lng:-72.94481119420918},
        zoom: 8,
      });
    }
    
    initMap();