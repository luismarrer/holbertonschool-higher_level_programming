const button = document.getElementById("red_header");
button.addEventListener("click", function() {
    const header = document.querySelector('header')
    header.classList.add('red')
});