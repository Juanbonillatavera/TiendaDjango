
/**
 * cambia la cantidad del producto en el carrito
 * @param {int } id: Pk del registro del producto em el carrito 
 */

function cambiarCantidad(id){
    let cantidad= document.getElementById('cantidad'+ id).value;
    let url = "http://localhost:8000/productos/camabiarCantidad";
    let datos = {
        'id': id,
        'cantidad': cantidad

    };
    mensajeAjax(url, datos, cambiarCantidadResp)
}

function cambiarCantidadResp(data){
    alert(data['mensaje'])
}


//******** Funciones Auxiliares  */

/**
 * consulta Ajax al servidor por metodo post
 * 
 * @param {*} urlserver : Direccion de envio
 * @param {*} datos : Data en formato javascripth object
 * @param {*} callBackFunction: Funsion de retorno
 */

function mensajeAjax(urlserver,datos,callBackFunction) {
    
    const csrftoken = getCookie('csrftoken')
    fetch(urlserver,{
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(datos)//  JavaScript object of data to POST

    })

        .then(response => response.json()) //convierte la respuesta JSON en data 
        .then(data =>{

            callBackFunction(data)
        })
        .catch((error )=> {
            console.error('Error:', JSON.stringify(error));
        });
}


/**
 * 
 * @param {*} name Nombre de la cokiee
 * @returns el contenido de la cokiee 
 */

function getCookie(name) {

    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {

        const cookies= document.cookie.split(";");
        for (let i=0 ; i < cookies.length; i++){
            const cookie = document.cookies[i].trim();
            
            // DOES THIS COKIE STRING BEGIN WITH THE NAME WE WANT ?

            if (cookie.substring(0,name.length+1)=== (name + "=")){
                cookieValue = decodeURIComponent(cookie.substring(name.length +1));
                break;
            }
            
        }
    }
    return cookieValue;
    
}
