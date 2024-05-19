
$("#formdata").on("submit", ()=>{
    event.preventDefault();
    
    let nombre_producto = $("#nombre_producto").val();
    let precio = $("#precio_producto").val();
    let stock = $("#stock").val();
    let categoria = $("#categoria_campo option:selected").val();
    let pvp = $("#pvp").val();
    let imagen = $("#imagen_producto").prop("files")[0]; // Obtener el archivo de imagen
    console.log(categoria);
    // Crear un objeto FormData para enviar datos y archivos
    let formData = new FormData();
    formData.append("nombre_producto", nombre_producto);
    formData.append("precio_producto", precio);
    formData.append("stock", stock);
    formData.append("categoria", categoria);
    formData.append("imagen_producto", imagen);
    formData.append("pvp", pvp);
    console.log(formData.forEach((item)=>{
        console.log(item);
    }))
    $.ajax({
        url: "create",
        type: "POST",
        headers: {
            'X-CSRFToken': getCookie('csrftoken')  // Añade el token CSRF como encabezado
        },
        data: formData,
        processData: false, // Evitar que jQuery procese los datos
        contentType: false, // Evitar que jQuery establezca el tipo de contenido
        success: (data) => {
           swalt("Se guardo con exito",{
            title: "Guardado",
            showIcon: true,
            icon: "success"
           }) ;
            
            
        },
        error: (error) => {
             swalt("Error al guardar",{
            title: "Error",
            showIcon: true,
            icon: "danger"
           }) ;
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
