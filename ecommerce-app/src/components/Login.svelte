<script>
  import { auth } from '../stores/auth.js';
  import { createEventDispatcher } from 'svelte';

  export let showModal = false;

  const dispatch = createEventDispatcher();

  let username = '';
  let password = '';
  let error = '';

  async function handleSubmit() {
    try {
      const response = await fetch('http://localhost:8000/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`,
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Login response:', data);  // Para depuración
        const role = data.is_admin ? 'admin' : 'user';
        auth.login(data.username, role);
        dispatch('close');
      } else {
        error = 'Invalid username or password';
      }
    } catch (err) {
      console.error('Login error:', err);
      error = 'An error occurred. Please try again.';
    }
  }

  function closeModal() {
    dispatch('close');
  }
</script>

<!-- ... resto del código ... -->