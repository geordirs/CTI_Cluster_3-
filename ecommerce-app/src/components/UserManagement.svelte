<script>
    import { onMount } from 'svelte';
    import { getUsers, createUser, updateUser, deleteUser } from '../services/api.js';
  
    let users = [];
    let newUser = { username: '', email: '', password: '', is_admin: false };
    let editingUser = null;
  
    onMount(async () => {
      users = await getUsers();
    });
  
    async function handleCreateUser() {
      await createUser(newUser);
      users = await getUsers();
      newUser = { username: '', email: '', password: '', is_admin: false };
    }
  
    async function handleUpdateUser() {
      await updateUser(editingUser.id, editingUser);
      users = await getUsers();
      editingUser = null;
    }
  
    async function handleDeleteUser(id) {
      if (confirm('Are you sure you want to delete this user?')) {
        await deleteUser(id);
        users = await getUsers();
      }
    }
  </script>
  
  <div>
    <h2 class="text-2xl font-semibold mb-4">User Management</h2>
  
    <div class="mb-8">
      <h3 class="text-xl font-semibold mb-2">Add New User</h3>
      <input bind:value={newUser.username} placeholder="Username" class="mb-2 p-2 border rounded" />
      <input bind:value={newUser.email} type="email" placeholder="Email" class="mb-2 p-2 border rounded" />
      <input bind:value={newUser.password} type="password" placeholder="Password" class="mb-2 p-2 border rounded" />
      <label>
        <input type="checkbox" bind:checked={newUser.is_admin} />
        Is Admin
      </label>
      <button on:click={handleCreateUser} class="bg-green-500 text-white p-2 rounded">Add User</button>
    </div>
  
    <div>
      <h3 class="text-xl font-semibold mb-2">User List</h3>
      {#each users as user (user.id)}
        <div class="mb-4 p-4 border rounded">
          <h4 class="font-semibold">{user.username}</h4>
          <p>Email: {user.email}</p>
          <p>Admin: {user.is_admin ? 'Yes' : 'No'}</p>
          <button on:click={() => editingUser = {...user}} class="mr-2 bg-blue-500 text-white p-2 rounded">Edit</button>
          <button on:click={() => handleDeleteUser(user.id)} class="bg-red-500 text-white p-2 rounded">Delete</button>
        </div>
      {/each}
    </div>
  
    {#if editingUser}
      <div class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" id="my-modal">
        <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
          <h3 class="text-lg font-semibold mb-4">Edit User</h3>
          <input bind:value={editingUser.username} class="mb-2 p-2 border rounded w-full" />
          <input bind:value={editingUser.email} type="email" class="mb-2 p-2 border rounded w-full" />
          <label>
            <input type="checkbox" bind:checked={editingUser.is_admin} />
            Is Admin
          </label>
          <button on:click={handleUpdateUser} class="bg-blue-500 text-white p-2 rounded">Update</button>
          <button on:click={() => editingUser = null} class="ml-2 bg-gray-500 text-white p-2 rounded">Cancel</button>
        </div>
      </div>
    {/if}
  </div>