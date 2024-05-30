$(document).ready(function () {
    let nombre = $("#nombre");
    let email = $("#email");
    let pass1 = $("#pass1");
    let pass2 = $("#pass2");

    $("#validar").click(function () {
        console.log(nombre.val());
        console.log(email.val());
        console.log(pass1.val());
        console.log(pass2.val());
        if (validarDatos(nombre,pass1,pass2) && validarCorreo(email.val())) {
            console.log("funciona")
        }else{
            console.log("no funciona")
        }
    
    })
    
    function validarDatos(nombre, pass1, pass2) {

        if (String(nombre).length >= 10) {
            document.getElementById("nombre").style.border = "1px solid green"
        }
        else {
            document.getElementById("nombre").style.border = "1px solid red"
            return false;
        }

        if (String(pass1).length >= 8) {
            document.getElementById("pass1").style.border = "1px solid green"
        } else {
            document.getElementById("pass1").style.border = "1px solid red"
            return false;
        }
        if (String(pass2) === String(pass1)) {
            document.getElementById("pass2").style.border = "1px solid green"
        }
        else {
            document.getElementById("pass2").style.border = "1px solid red"
            return false;
        }
        return true;
    }

    function validarCorreo(email) {
        let expReg = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
        let valido = expReg.test(email);

        if (valido) {
            alert("El correo electronico es valido")
            return true;
        }
        else {
            alert("El correo electronico no es valido")
            return false;
        }

    }

    $("#reg").click(function () {
        location.href = "http://127.0.0.1:3000/index.html";

    })

    

    $("#validarCorreo").click(function () {
        console.log(email.val());
    })
})