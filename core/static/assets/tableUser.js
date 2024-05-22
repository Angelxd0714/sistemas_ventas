let url = "/static/json/lenguage.json"
$(document).ready(function () {
    $.ajax({
        url: url,
        dataType: "json",
        success: function (data) {
            $('#example2').DataTable({
               
                "language": data, // Utiliza directamente el objeto data como la configuración de lenguaje
                processing: true, // Agrega esto si quieres mostrar un indicador de procesamiento
                destroy: true,
                responsive: true,
                layout: {
                    topStart: {
                        buttons: [{
                            text: "Insertar",
                            className:"btn btn-primary",
                            action: function (e, dt, node, config) {
                               $("#dataModal").modal("show");
                            }
                        }
                        ]
                    }
                },
                ajax: (
                    {
                        url: window.location.pathname,
                        type: "POST",
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken')  // Añade el token CSRF como encabezado
                        },
                        data: {
                            "action": "searchdata",
                        },
                        dataSrc: ""
                    }

                ),
                columns: [
                    { data: "id_cliente" },
                    { data: "dni" },
                    { data: "nombres" },
                    { data: "apellidos" },
                    { data: "fecha_nac" },
                    { data: "direccion" },
                    { data: "imagen_usuario" },
                    { data: "sexo" },
                ],
                columnsDefs: [
                    {
                        targets: [0],
                        class: "text-center",
                        searchable: false,
                        render: function (data, type, row) {
                            return data
                        }
                    },
                    {
                        targets: [6],
                        class: "text-center",
                        searchable: false,
                        render: function (data, type, row) {
                            return `<img src="${data}"/ alt="">`
                        }
                    },
                    {
                        targets: [2],
                        class: "text-center",
                        searchable: false,
                        render: function (data, type, row) {
                            return data
                        }
                    },
                    {
                        targets: [3],
                        class: "text-center",
                        searchable: false,
                        render: function (data, type, row) {
                            return data
                        }
                    },
                    {
                        targets: [4],
                        class: "text-center",
                        searchable: false,
                        render: function (data, type, row) {
                            return data
                        }
                    },
                    {
                        targets: [5],
                        class: "text-center",
                        searchable: false,
                        render: function (data, type, row) {
                            return data
                        }
                    },
                    {
                        targets: [1],
                        class: "text-center",
                        searchable: false,
                        render: function (data, type, row) {
                            return data
                        }
                    },
                    {
                        targets: [7],
                        class: "text-center",
                        searchable: false,
                        render: function (data, type, row) {
                            return data
                        }
                    }




                ],
                initComplete: function (settings, json) {

                },
                
            })
        }
    })

})
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
