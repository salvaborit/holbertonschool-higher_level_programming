const list = document.querySelector('.my_list');

const addItemBtn = document.querySelector('#add_item');
const removeItemBtn = document.querySelector('#remove_item');
const clearListBtn = document.querySelector('#clear_list');

addItemBtn.addEventListener('click', () => addItem());
removeItemBtn.addEventListener('click', () => removeItem());
clearListBtn.addEventListener('click', () => clearList());

function addItem () {
  const newItem = document.createElement('li');
  newItem.innerText = 'Item';
  list.append(newItem);
}

function removeItem () {
  list.lastChild.remove();
}

function clearList () {
  for (item of document.querySelectorAll('.my_list li')) {
    item.remove();
  }
}
