document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario); 
  });
  
  function validarFormulario(evento) {
    evento.preventDefault();
    var Nombre = document.getElementById('name').value;
    if(Nombre.length == 0) {
      alert('No has escrito nada');
      return;
    }
    var email = document.getElementById('email').value;
    if (email.length == 0) {
      alert('no ha escrito nada');
      return;
    }
    this.submit();
  }