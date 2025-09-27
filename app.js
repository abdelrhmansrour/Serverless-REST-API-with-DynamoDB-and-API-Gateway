const API_URL = 'https://bcw1ekyme4.execute-api.us-east-1.amazonaws.com/dev';

async function fetchItems() {
  const response = await fetch(API_URL);
  const items = await response.json();

  const list = document.getElementById('todoList');
  list.innerHTML = '';

  items.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item.title;

    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = '❌';
    deleteBtn.onclick = () => deleteItem(item.id);

    li.appendChild(deleteBtn);
    list.appendChild(li);
  });
}

async function addItem() {
  const input = document.getElementById('todoInput');
  const title = input.value.trim();
  if (!title) return;

  await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title })
  });

  input.value = '';
  fetchItems();
}

async function deleteItem(id) {
  await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
  fetchItems();
}

// Load items on page load
window.onload = fetchItems;

