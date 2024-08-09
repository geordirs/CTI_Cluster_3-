<script>
    import { onMount } from 'svelte';
    import { auth } from '../stores/auth.js';
    import { navigate } from 'svelte-routing';
    import ProductManagement from '../components/ProductManagement.svelte';
    import UserManagement from '../components/UserManagement.svelte';
    import CouponManagement from '../components/CouponManagement.svelte';
  
    let activeTab = 'products';
  
    onMount(() => {
      if ($auth.role !== 'admin') {
        navigate('/');
      }
    });
  
    function setActiveTab(tab) {
      activeTab = tab;
    }
  </script>
  
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6">Panel de Administración</h1>
  
    <div class="mb-6">
      <button 
        class="mr-4 {activeTab === 'products' ? 'text-indigo-600 font-bold' : 'text-gray-600'}" 
        on:click={() => setActiveTab('products')}
      >
        Productos
      </button>
      <button 
        class="mr-4 {activeTab === 'users' ? 'text-indigo-600 font-bold' : 'text-gray-600'}" 
        on:click={() => setActiveTab('users')}
      >
        Usuarios
      </button>
      <button 
        class="{activeTab === 'coupons' ? 'text-indigo-600 font-bold' : 'text-gray-600'}" 
        on:click={() => setActiveTab('coupons')}
      >
        Cupones
      </button>
    </div>
  
    {#if activeTab === 'products'}
      <ProductManagement />
    {:else if activeTab === 'users'}
      <UserManagement />
    {:else if activeTab === 'coupons'}
      <CouponManagement />
    {/if}
  </div>