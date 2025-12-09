const API_BASE = 'http://127.0.0.1:8000'; // замените на ваш URL, если другой

// Switch tabs
document.querySelectorAll('.tab-button').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));

    button.classList.add('active');
    document.getElementById(`${button.dataset.tab}-tab`).classList.add('active');
  });
});

// CLIENTS
const loadClients = async () => {
  const res = await fetch(`${API_BASE}/clients/`);
  const clients = await res.json();
  const tbody = document.querySelector('#clients-table tbody');
  tbody.innerHTML = '';
  clients.forEach(client => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${client.id}</td>
      <td>${client.name}</td>
      <td>${client.phone}</td>
      <td>${client.email}</td>
      <td>
        <button onclick="editClient(${client.id})">Edit</button>
        <button onclick="deleteClient(${client.id})">Delete</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
};

document.getElementById('create-client-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData);

  try {
    await fetch(`${API_BASE}/clients/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    e.target.reset();
    loadClients();
  } catch (err) { console.error(err); }
});

const editClient = async (id) => {
  const res = await fetch(`${API_BASE}/clients/${id}`);
  const client = await res.json();

  document.querySelector('#update-client-form input[name="id"]').value = client.id;
  document.querySelector('#update-client-form input[name="name"]').value = client.name;
  document.querySelector('#update-client-form input[name="phone"]').value = client.phone;
  document.querySelector('#update-client-form input[name="email"]').value = client.email;

  document.getElementById('update-client-form-container').style.display = 'block';
};

document.getElementById('update-client-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const id = formData.get('id');
  const data = {};
  for (let [key, val] of formData.entries()) {
    if (key !== 'id' && val !== '') data[key] = val;
  }

  await fetch(`${API_BASE}/clients/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  document.getElementById('update-client-form-container').style.display = 'none';
  loadClients();
});

document.getElementById('cancel-update-client').addEventListener('click', () => {
  document.getElementById('update-client-form-container').style.display = 'none';
});

const deleteClient = async (id) => {
  if (confirm('Are you sure?')) {
    await fetch(`${API_BASE}/clients/${id}`, { method: 'DELETE' });
    loadClients();
  }
};

// DEALS
const loadDeals = async () => {
  const res = await fetch(`${API_BASE}/deals/`);
  const deals = await res.json();
  const tbody = document.querySelector('#deals-table tbody');
  tbody.innerHTML = '';
  deals.forEach(deal => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${deal.id}</td>
      <td>${deal.title}</td>
      <td>${deal.amount}</td>
      <td>${deal.status}</td>
      <td>${deal.client_id}</td>
      <td>
        <button onclick="editDeal(${deal.id})">Edit</button>
        <button onclick="deleteDeal(${deal.id})">Delete</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
};

document.getElementById('create-deal-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData);

  try {
    await fetch(`${API_BASE}/deals/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    e.target.reset();
    loadDeals();
  } catch (err) { console.error(err); }
});

const editDeal = async (id) => {
  const res = await fetch(`${API_BASE}/deals/${id}`);
  const deal = await res.json();

  document.querySelector('#update-deal-form input[name="id"]').value = deal.id;
  document.querySelector('#update-deal-form input[name="title"]').value = deal.title;
  document.querySelector('#update-deal-form input[name="amount"]').value = deal.amount;
  document.querySelector('#update-deal-form input[name="status"]').value = deal.status;
  document.querySelector('#update-deal-form input[name="client_id"]').value = deal.client_id;

  document.getElementById('update-deal-form-container').style.display = 'block';
};

document.getElementById('update-deal-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const id = formData.get('id');
  const data = {};
  for (let [key, val] of formData.entries()) {
    if (key !== 'id' && val !== '') data[key] = val;
  }

  await fetch(`${API_BASE}/deals/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  document.getElementById('update-deal-form-container').style.display = 'none';
  loadDeals();
});

document.getElementById('cancel-update-deal').addEventListener('click', () => {
  document.getElementById('update-deal-form-container').style.display = 'none';
});

const deleteDeal = async (id) => {
  if (confirm('Are you sure?')) {
    await fetch(`${API_BASE}/deals/${id}`, { method: 'DELETE' });
    loadDeals();
  }
};

// USERS
const loadUsers = async () => {
  const res = await fetch(`${API_BASE}/users/`);
  const users = await res.json();
  const tbody = document.querySelector('#users-table tbody');
  tbody.innerHTML = '';
  users.forEach(user => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${user.id}</td>
      <td>${user.name}</td>
      <td>${user.email}</td>
      <td>
        <button onclick="editUser(${user.id})">Edit</button>
        <button onclick="deleteUser(${user.id})">Delete</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
};

document.getElementById('create-user-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData);

  try {
    await fetch(`${API_BASE}/users/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    e.target.reset();
    loadUsers();
  } catch (err) { console.error(err); }
});

const editUser = async (id) => {
  const res = await fetch(`${API_BASE}/users/${id}`);
  const user = await res.json();

  document.querySelector('#update-user-form input[name="id"]').value = user.id;
  document.querySelector('#update-user-form input[name="name"]').value = user.name;
  document.querySelector('#update-user-form input[name="email"]').value = user.email;

  document.getElementById('update-user-form-container').style.display = 'block';
};

document.getElementById('update-user-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const id = formData.get('id');
  const data = {};
  for (let [key, val] of formData.entries()) {
    if (key !== 'id' && val !== '') data[key] = val;
  }

  await fetch(`${API_BASE}/users/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  document.getElementById('update-user-form-container').style.display = 'none';
  loadUsers();
});

document.getElementById('cancel-update-user').addEventListener('click', () => {
  document.getElementById('update-user-form-container').style.display = 'none';
});

const deleteUser = async (id) => {
  if (confirm('Are you sure?')) {
    await fetch(`${API_BASE}/users/${id}`, { method: 'DELETE' });
    loadUsers();
  }
};

// Load all on start
loadClients();
loadDeals();
loadUsers();