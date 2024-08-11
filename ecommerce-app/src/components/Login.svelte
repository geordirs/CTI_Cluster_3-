<script>
  import { auth } from '../stores/auth.js';
  import { createEventDispatcher } from 'svelte';

  export let showModal = false; // Mantenemos esta línea
  const dispatch = createEventDispatcher();

  let username = '';
  let password = '';
  let error = '';

  async function handleSubmit() {
    try {
      //const response = await fetch('http://localhost:8000/token', {
      const response = await fetch('https://web-production-b61f.up.railway.app/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`,
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Login response:', data);  // Temporal para depuración
        localStorage.setItem('token', data.access_token);
        auth.login(data.username, data.is_admin);
        dispatch('close');
      } else {
        error = 'Invalid username or password';
      }
    } catch (err) {
      error = 'An error occurred. Please try again.';
    }
  }

  function closeModal() {
    dispatch('close');
  }
</script>

{#if showModal}
  <div class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" id="my-modal">
    <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
      <h3 class="text-lg font-medium leading-6 text-gray-900 mb-4">Login</h3>
      <form on:submit|preventDefault={handleSubmit}>
        <input bind:value={username} type="text" placeholder="Username" class="w-full p-2 mb-4 border rounded">
        <input bind:value={password} type="password" placeholder="Password" class="w-full p-2 mb-4 border rounded">
        {#if error}
          <p class="text-red-500 mb-4">{error}</p>
        {/if}
        <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Login</button>
      </form>
      <button on:click={closeModal} class="mt-4 w-full bg-gray-300 text-gray-800 p-2 rounded">Close</button>
    </div>
  </div>
{/if}