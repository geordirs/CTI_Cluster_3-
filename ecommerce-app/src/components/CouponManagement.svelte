<script>
  import { onMount } from 'svelte';
  import { getCoupons, createCoupon, updateCoupon, deleteCoupon } from '../services/api.js';

  export let showNotification;
  export let showConfirmation;

  let coupons = [];
  let error = '';
  let showModal = false;
  let editingCoupon = null;
  let currentCoupon = {
    code: '',
    discount_percent: 0,
    valid_from: '',
    valid_to: '',
    is_active: true
  };

  onMount(async () => {
    try {
      coupons = await getCoupons();
    } catch (err) {
      error = err.message;
    }
  });

  function openModal(coupon = null) {
    editingCoupon = coupon;
    if (coupon) {
      currentCoupon = {
        ...coupon,
        valid_from: coupon.valid_from.split('T')[0],
        valid_to: coupon.valid_to.split('T')[0]
      };
    } else {
      currentCoupon = {
        code: '',
        discount_percent: 0,
        valid_from: '',
        valid_to: '',
        is_active: true
      };
    }
    showModal = true;
  }

  function closeModal() {
    showModal = false;
    editingCoupon = null;
  }

  async function handleSubmit() {
    try {
      const couponData = {
        ...currentCoupon,
        valid_from: new Date(currentCoupon.valid_from + 'T00:00:00').toISOString(),
        valid_to: new Date(currentCoupon.valid_to + 'T23:59:59').toISOString()
      };

      if (editingCoupon) {
        const updatedCoupon = await updateCoupon(editingCoupon.id, couponData);
        coupons = coupons.map(c => c.id === updatedCoupon.id ? updatedCoupon : c);
        showNotification('Coupon updated successfully', 'success');
      } else {
        const createdCoupon = await createCoupon(couponData);
        coupons = [...coupons, createdCoupon];
        showNotification('Coupon created successfully', 'success');
      }
      closeModal();
    } catch (err) {
      error = err.message;
      showNotification(err.message, 'error');
    }
  }

  async function handleDeleteCoupon(id) {
    showConfirmation('Are you sure you want to delete this coupon?', async () => {
      try {
        await deleteCoupon(id);
        coupons = coupons.filter(c => c.id !== id);
        showNotification('Coupon deleted successfully', 'success');
      } catch (err) {
        showNotification(err.message, 'error');
      }
    });
  }
</script>

<div class="container mx-auto p-4">
  <h2 class="text-2xl font-semibold mb-4">Coupon Management</h2>
  
  {#if error}
      <p class="text-red-500 mb-4">{error}</p>
  {/if}

  <button on:click={() => openModal()} class="bg-blue-500 text-white px-4 py-2 rounded mb-4">
      Add New Coupon
  </button>

  <div class="overflow-x-auto">
      <table class="min-w-full bg-white">
          <thead class="bg-gray-100">
              <tr>
                  <th class="py-2 px-4 text-left">Code</th>
                  <th class="py-2 px-4 text-left">Discount %</th>
                  <th class="py-2 px-4 text-left">Valid From</th>
                  <th class="py-2 px-4 text-left">Valid To</th>
                  <th class="py-2 px-4 text-left">Active</th>
              </tr>
          </thead>
          <tbody>
              {#each coupons as coupon (coupon.id)}
                  <tr class="border-t">
                      <td class="py-2 px-4">{coupon.code}</td>
                      <td class="py-2 px-4">{coupon.discount_percent}%</td>
                      <td class="py-2 px-4">{new Date(coupon.valid_from).toLocaleDateString()}</td>
                      <td class="py-2 px-4">{new Date(coupon.valid_to).toLocaleDateString()}</td>
                      <td class="py-2 px-4">{coupon.is_active ? 'Yes' : 'No'}</td>
                  </tr>
              {/each}
          </tbody>
      </table>
  </div>

  {#if showModal}
      <div class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" id="my-modal">
          <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
              <h3 class="text-lg font-semibold mb-4">{editingCoupon ? 'Edit Coupon' : 'Add New Coupon'}</h3>
              <form on:submit|preventDefault={handleSubmit}>
                  <div class="mb-4">
                      <label for="code" class="block text-sm font-medium text-gray-700">Code</label>
                      <input id="code" type="text" bind:value={currentCoupon.code} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4">
                      <label for="discount_percent" class="block text-sm font-medium text-gray-700">Discount Percentage</label>
                      <input id="discount_percent" type="number" bind:value={currentCoupon.discount_percent} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4">
                      <label for="valid_from" class="block text-sm font-medium text-gray-700">Valid From</label>
                      <input id="valid_from" type="date" bind:value={currentCoupon.valid_from} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4">
                      <label for="valid_to" class="block text-sm font-medium text-gray-700">Valid To</label>
                      <input id="valid_to" type="date" bind:value={currentCoupon.valid_to} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4 flex items-center">
                      <input id="is_active" type="checkbox" bind:checked={currentCoupon.is_active} class="rounded border-gray-300 text-indigo-600 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                      <label for="is_active" class="ml-2 block text-sm font-medium text-gray-700">Is Active</label>
                  </div>
                  <div class="flex justify-end">
                      <button type="button" on:click={closeModal} class="mr-2 px-4 py-2 bg-gray-300 text-gray-800 rounded-md hover:bg-gray-400">Cancel</button>
                      <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">{editingCoupon ? 'Update Coupon' : 'Add Coupon'}</button>
                  </div>
              </form>
          </div>
      </div>
  {/if}
</div>