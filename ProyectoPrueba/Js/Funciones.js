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
