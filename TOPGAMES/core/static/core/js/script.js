$(document).ready(function() {

    $.validator.addMethod("minAge", function(value, element, min) {
        var today = new Date();
        var birthDate = new Date(value);
        var age = today.getFullYear() - birthDate.getFullYear();
        var m = today.getMonth() - birthDate.getMonth();
        if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        return age >= min;
    }, "Debes ser mayor de 13 años para registrarte.");


    $("#registroForm").validate({
        rules: {
            nombreCompleto: "required",
            nombreUsuario: "required",
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 6,
                maxlength: 18
            },
            confirmPassword: {
                required: true,
                equalTo: "#password"
            },
            fechaNacimiento: {
                required: true,
                minAge: 13
            },
            region: "required"
        },
        messages: {
            nombreCompleto: "Por favor, ingresa tu nombre completo.",
            nombreUsuario: "Por favor, ingresa un nombre de usuario.",
            email: {
                required: "Por favor, ingresa tu correo electrónico.",
                email: "Por favor, ingresa un correo electrónico válido."
            },
            password: {
                required: "Por favor, ingresa una contraseña.",
                minlength: "La contraseña debe tener al menos 6 caracteres.",
                maxlength: "La contraseña no puede exceder los 18 caracteres."
            },
            confirmPassword: {
                required: "Por favor, confirma tu contraseña.",
                equalTo: "Las contraseñas no coinciden."
            },
            fechaNacimiento: {
                required: "Debes ingresar tu fecha de nacimiento.",
                minAge: "Debes ser mayor de 13 años para registrarte."
            },
            region: "Por favor selecciona tu región."
        },
        submitHandler: function(form) {
            form.submit();
        }
    });
});
