let url = "/static/json/lenguage.json"
$(document).ready(function () {
    $.ajax({
        url: url,
        dataType: "json",
        success: function (data) {
            var table = $('#example2').DataTable({
                "language": data,
                processing: true,
                destroy: true,
                responsive: true,
                layout: {
                    topStart: {
                        buttons: [{
                            text: "Insertar",
                            className: "btn btn-primary",
                            action: function (e, dt, node, config) {
                                $("#dataModal").modal("show");
                            }
                        }]
                    }
                },
                ajax: {
                    url: window.location.pathname,
                    type: "POST",
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    data: function (d) {
                        d.action = 'searchdata';
                    },
                    dataSrc: ""
                },
                columns: [
                    { data: "id_cliente" },
                    { data: "dni" },
                    { data: "nombres" },
                    { data: "apellidos" },
                    { data: "fecha_nac" },
                    { data: "direccion" },
                    { data: "imagen_usuario" },
                    { data: "sexo" }
                ],
                columnDefs: [
                    { targets: [0, 1, 2, 3, 4, 5, 7], className: "text-center", searchable: false },
                    {
                        targets: [6],
                        className: "text-center",
                        searchable: false,
                        render: function (data) {
                            return `<img src="${data}" alt="">`;
                        }
                    }
                ]
            });

            $("#formdataCliente").on('submit', function (e) {
                e.preventDefault();
                let dni = $("#dni")
                let nombres = $("#nombres").val()
                let apellidos = $("#apellidos").val()
                let fecha_nac = $("#fecha_nac").val()
                let direccion = $("#direccion").val()
                let imagen_usuario = $("#imagen_usuario").prop("files")[0]
                let sexo = $("#sexo option:selected") 
                var data = new FormData();
                data.append("dni",dni)
                data.append("nombres",nombres)
                data.append("apellidos",apellidos)
                data.append("fecha_nac",fecha_nac)
                data.append("imagen_usuario",imagen_usuario)
                data.append("direccion", direccion)
                data.append("sexo",sexo)
                
                $.ajax({
                    url: "create",
                    type: "POST",
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    data: data,
                    processData: false,
                    contentType: false,
                    success: function (response) {
                        console.log("Success:", response);
                        $("#dataModal").modal("hide");
                        table.ajax.reload(null, false);
                    },
                    error: function (error) {
                        console.log("Error:", error);
                    }
                });
            });
        }
    });
});
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Busca el token CSRF en las cookies
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
