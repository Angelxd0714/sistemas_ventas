
const deletes=(id)=>{
    $.ajax({
        url:`/categoria/delete/${id}`,
        type:"DELETE",
        headers: {
            'X-CSRFToken': getCookie('csrftoken')  // Añade el token CSRF como encabezado
        },
        success:(data)=>{
            alert("Categoria eliminada",data);
        },
        error:(error)=>{
            console.log(error);
        }
    })
}
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
