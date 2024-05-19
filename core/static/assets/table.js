let data = "/static/json/lenguage.json"
$(document).ready(function () {
    $.ajax({
        url: data,
        dataType: "json",
        success: function(data) {
            $('#example').DataTable({
                "language": data, // Utiliza directamente el objeto data como la configuración de lenguaje
                "processing": true, // Agrega esto si quieres mostrar un indicador de procesamiento
                "destroy": true 

            })
        }
    })
})