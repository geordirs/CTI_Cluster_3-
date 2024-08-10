<script>
  import { Link, navigate } from "svelte-routing";
  import { auth } from '../stores/auth.js';
  import { cart } from '../stores/cart.js';

  export let openLoginModal;

  function logout() {
    auth.logout();
  }

  function goToAdmin() {
    navigate('/admin');
  }

  $: cartItemCount = $cart.reduce((total, item) => total + item.quantity, 0);
</script>

<nav class="bg-white shadow-md">
  <div class="container mx-auto px-4">
    <div class="flex justify-between items-center py-4">
      <Link to="/" class="text-2xl font-bold text-indigo-900">LuxeCommerce</Link>
      <div class="space-x-4">
        <Link to="/products" class="text-gray-600 hover:text-indigo-900">Products</Link>
        <Link to="/cart" class="text-gray-600 hover:text-indigo-900">Cart ({cartItemCount})</Link>
        {#if $auth.isAuthenticated}
          {#if $auth.isAdmin}
            <button on:click={goToAdmin} class="bg-indigo-500 hover:bg-indigo-700 text-white py-2 px-4 rounded">
              Panel Admin
            </button>
          {/if}
          <span class="text-gray-600">Welcome, {$auth.username}!</span>
          <button on:click={logout} class="bg-red-500 hover:bg-red-700 text-white py-2 px-4 rounded">
            Logout
          </button>
        {:else}
          <button on:click={openLoginModal} class="bg-indigo-500 hover:bg-indigo-700 text-white py-2 px-4 rounded">
            Login
          </button>
        {/if}
      </div>
    </div>
  </div>
</nav>