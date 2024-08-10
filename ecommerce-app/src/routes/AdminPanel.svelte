<script lang="ts">
  import { onMount } from 'svelte';
  import { auth } from '../stores/auth.js';
  import { navigate } from 'svelte-routing';
  import ProductManagement from '../components/ProductManagement.svelte';
  import UserManagement from '../components/UserManagement.svelte';
  import CouponManagement from '../components/CouponManagement.svelte';
  import Notification from '../components/Notification.svelte';

  let activeTab: 'products' | 'users' | 'coupons' = 'products';
  let notification = { message: '', type: 'success' as const, visible: false };
  let confirmationModal = { visible: false, message: '', onConfirm: null as (() => void) | null };

  onMount(() => {
    console.log('AdminPanel mounted, auth state:', $auth);
    if (!$auth.isAdmin) {
      navigate('/');
    }
  });

  function setActiveTab(tab: typeof activeTab) {
    activeTab = tab;
  }

  function showNotification(message: string, type: 'success') {
    notification = { message, type, visible: true };
  }

  function showConfirmation(message: string, onConfirm: () => void) {
    confirmationModal = { visible: true, message, onConfirm };
  }

  function handleConfirm() {
    if (confirmationModal.onConfirm) {
      confirmationModal.onConfirm();
    }
    confirmationModal.visible = false;
  }

  function handleCancel() {
    confirmationModal.visible = false;
  }

</script>

<div class="container mx-auto px-4 py-8">
  <h1 class="text-3xl font-bold mb-6">Admin Panel</h1>

  <div class="mb-6">
    <button 
      class="mr-4 {activeTab === 'products' ? 'text-indigo-600 font-bold' : 'text-gray-600'}" 
      on:click={() => setActiveTab('products')}
    >
      Products
    </button>
    <button 
      class="mr-4 {activeTab === 'users' ? 'text-indigo-600 font-bold' : 'text-gray-600'}" 
      on:click={() => setActiveTab('users')}
    >
      Users
    </button>
    <button 
      class="{activeTab === 'coupons' ? 'text-indigo-600 font-bold' : 'text-gray-600'}" 
      on:click={() => setActiveTab('coupons')}
    >
      Coupons
    </button>
  </div>

  {#if activeTab === 'products'}
    <ProductManagement {showNotification} {showConfirmation} />
  {:else if activeTab === 'users'}
    <UserManagement {showNotification} {showConfirmation} />
  {:else if activeTab === 'coupons'}
    <CouponManagement {showNotification} {showConfirmation} />
  {/if}
</div>

{#if notification.visible}
  <Notification message={notification.message} type={notification.type} />
{/if}

{#if confirmationModal.visible}
  <div class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" id="confirmation-modal">
    <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
      <h3 class="text-lg font-medium leading-6 text-gray-900 mb-4">Confirmation</h3>
      <p class="mb-4">{confirmationModal.message}</p>
      <div class="flex justify-end">
        <button on:click={handleCancel} class="mr-2 px-4 py-2 bg-gray-300 text-gray-800 rounded-md hover:bg-gray-400">Cancel</button>
        <button on:click={handleConfirm} class="px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600">Confirm</button>
      </div>
    </div>
  </div>
{/if}