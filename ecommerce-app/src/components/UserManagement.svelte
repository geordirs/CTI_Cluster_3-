<script lang="ts">
  import { onMount } from 'svelte';
  import { getUsers, createUser } from '../services/api.js';

  export let showNotification: (message: string, type?: 'success' | 'error') => void;
  export let showConfirmation: (message: string, onConfirm: () => void) => void;

  let users = [];
  let error = '';
  let showModal = false;
  let newUser = { username: '', email: '', password: '' };

  onMount(async () => {
    try {
      users = await getUsers();
    } catch (err) {
      error = err.message;
    }
  });

  async function handleCreateUser() {
    showConfirmation('Are you sure you want to create this user?', async () => {
      try {
        const createdUser = await createUser(newUser);
        users = [...users, createdUser];
        newUser = { username: '', email: '', password: '' };
        showModal = false;
        showNotification('User created successfully', 'success');
      } catch (err) {
        showNotification(err.message, 'error');
      }
    });
  }

  function openModal() {
    showModal = true;
  }

  function closeModal() {
    showModal = false;
  }
</script>

<div class="container mx-auto p-4">
  <h2 class="text-2xl font-semibold mb-4">User Management</h2>
  
  {#if error}
      <p class="text-red-500 mb-4">{error}</p>
  {/if}

  <button on:click={openModal} class="bg-blue-500 text-white px-4 py-2 rounded mb-4">
      Add New User
  </button>

  <div class="overflow-x-auto">
      <table class="min-w-full bg-white">
          <thead class="bg-gray-100">
              <tr>
                  <th class="py-2 px-4 text-left">Username</th>
                  <th class="py-2 px-4 text-left">Email</th>
              </tr>
          </thead>
          <tbody>
              {#each users as user (user.id)}
                  <tr class="border-t">
                      <td class="py-2 px-4">{user.username}</td>
                      <td class="py-2 px-4">{user.email}</td>
                  </tr>
              {/each}
          </tbody>
      </table>
  </div>

  {#if showModal}
      <div class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" id="my-modal">
          <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
              <h3 class="text-lg font-semibold mb-4">Add New User</h3>
              <form on:submit|preventDefault={handleCreateUser}>
                  <div class="mb-4">
                      <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
                      <input id="username" type="text" bind:value={newUser.username} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4">
                      <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
                      <input id="email" type="email" bind:value={newUser.email} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4">
                      <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
                      <input id="password" type="password" bind:value={newUser.password} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="flex justify-end">
                      <button type="button" on:click={closeModal} class="mr-2 px-4 py-2 bg-gray-300 text-gray-800 rounded-md hover:bg-gray-400">Cancel</button>
                      <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">Add User</button>
                  </div>
              </form>
          </div>
      </div>
  {/if}
</div>