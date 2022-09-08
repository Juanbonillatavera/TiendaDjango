$(function (){
    var name, email, phone;
    var name = document.getElementById('name').value;
    var email= document.getElementById('email').value;
    var phone = document.getElementById('phone').value
    $(".btnAction").on('click', function (){
        name = $(".name").val();
        email = $(".email").val();
        phone = $(".phone").val();
        console.log();
        if (name.length == 0||email.length == 0||phone.length == 0) {
            alert("el dato esta vacio");
            return
        }
        this.submit();

    });
});