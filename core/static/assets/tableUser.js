$(document).ready(function() {
    $('#example2').DataTable({
        "language": {
            "emptyTable": "No hay datos disponibles",
            "url": "//cdn.datatables.net/plug-ins/1.10.24/i18n/Spanish.json" // URL del archivo de traducción
        },
        "processing": true, // Agrega esto si quieres mostrar un indicador de procesamiento
        "destroy": true // Esto destruirá la tabla existente y creará una nueva al inicializar DataTables
    })});