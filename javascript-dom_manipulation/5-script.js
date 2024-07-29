const button = document.getElementById('update_header');
button.addEventListener('click', function() {
    const header = document.querySelector('header');
    header.textContent = "New Header!!!";
});