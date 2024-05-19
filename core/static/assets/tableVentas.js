let urls = "/static/json/lenguage.json"
$(document).ready(function () {
    $.ajax({
        url: urls,
        dataType: "json",
        success: function(data) {
            $('#example3').DataTable({
                "language": data, // Utiliza directamente el objeto data como la configuración de lenguaje
                "processing": true, // Agrega esto si quieres mostrar un indicador de procesamiento
                "destroy": true 

            })
        },
        ajax:''

    })
})