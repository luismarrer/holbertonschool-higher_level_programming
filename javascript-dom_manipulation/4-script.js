const button = document.getElementById('add_item');
button.addEventListener('click', function() {
    const list = document.getElementsByClassName('my_list');
    const item = document.createElement('li');
    item.textContent = "Item";
    list[0].appendChild(item);
});