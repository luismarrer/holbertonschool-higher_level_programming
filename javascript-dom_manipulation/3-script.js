const button = document.getElementById("toggle_header");
button.addEventListener("click", function() {
    if (document.querySelector('header').classList.contains('green')) {
        document.querySelector('header').classList.replace('green', 'red');
    } else {
        document.querySelector('header').classList.replace('red', 'green');
    }
});