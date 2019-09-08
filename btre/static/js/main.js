const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//to timeout message
setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000);
