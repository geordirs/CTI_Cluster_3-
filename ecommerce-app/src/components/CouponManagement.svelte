<script>
    import { onMount } from 'svelte';
    import { getCoupons, createCoupon, updateCoupon, deleteCoupon } from '../services/api.js';
  
    let coupons = [];
    let newCoupon = { code: '', discount: 0, expiry_date: '' };
    let editingCoupon = null;
  
    onMount(async () => {
      coupons = await getCoupons();
    });
  
    async function handleCreateCoupon() {
      await createCoupon(newCoupon);
      coupons = await getCoupons();
      newCoupon = { code: '', discount: 0, expiry_date: '' };
    }
  
    async function handleUpdateCoupon() {
      await updateCoupon(editingCoupon.id, editingCoupon);
      coupons = await getCoupons();
      editingCoupon = null;
    }
  
    async function handleDeleteCoupon(id) {
      if (confirm('Are you sure you want to delete this coupon?')) {
        await deleteCoupon(id);
        coupons = await getCoupons();
      }
    }
  </script>
  
  <div>
    <h2 class="text-2xl font-semibold mb-4">Coupon Management</h2>
  
    <div class="mb-8">
      <h3 class="text-xl font-semibold mb-2">Add New Coupon</h3>
      <input bind:value={newCoupon.code} placeholder="Coupon Code" class="mb-2 p-2 border rounded" />
      <input bind:value={newCoupon.discount} type="number" placeholder="Discount Amount" class="mb-2 p-2 border rounded" />
      <input bind:value={newCoupon.expiry_date} type="date" placeholder="Expiry Date" class="mb-2 p-2 border rounded" />
      <button on:click={handleCreateCoupon} class="bg-green-500 text-white p-2 rounded">Add Coupon</button>
    </div>
  
    <div>
      <h3 class="text-xl font-semibold mb-2">Coupon List</h3>
      {#each coupons as coupon (coupon.id)}
        <div class="mb-4 p-4 border rounded">
          <h4 class="font-semibold">{coupon.code}</h4>
          <p>Discount: ${coupon.discount}</p>
          <p>Expires: {new Date(coupon.expiry_date).toLocaleDateString()}</p>
          <button on:click={() => editingCoupon = {...coupon}} class="mr-2 bg-blue-500 text-white p-2 rounded">Edit</button>
          <button on:click={() => handleDeleteCoupon(coupon.id)} class="bg-red-500 text-white p-2 rounded">Delete</button>
        </div>
      {/each}
    </div>
  
    {#if editingCoupon}
      <div class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" id="my-modal">
        <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
          <h3 class="text-lg font-semibold mb-4">Edit Coupon</h3>
          <input bind:value={editingCoupon.code} class="mb-2 p-2 border rounded w-full" />
          <input bind:value={editingCoupon.discount} type="number" class="mb-2 p-2 border rounded w-full" />
          <input bind:value={editingCoupon.expiry_date} type="date" class="mb-2 p-2 border rounded w-full" />
          <button on:click={handleUpdateCoupon} class="bg-blue-500 text-white p-2 rounded">Update</button>
          <button on:click={() => editingCoupon = null} class="ml-2 bg-gray-500 text-white p-2 rounded">Cancel</button>
        </div>
      </div>
    {/if}
  </div>