<script lang="ts">
  import { onMount } from 'svelte';
  import { getProducts, createProduct, updateProduct, deleteProduct } from '../services/api.js';

  export let showNotification: (message: string, type?: 'success' | 'error') => void;
  export let showConfirmation: (message: string, onConfirm: () => void) => void;

  let products = [];
  let error = '';
  let showModal = false;
  let editingProduct = null;
  let currentProduct = {
    name: '',
    description: '',
    price: 0,
    stock_quantity: 0,
    low_stock_threshold: 0,
    category: '',
    image_url: '',
    is_active: true
  };

  onMount(async () => {
    try {
      products = await getProducts();
    } catch (err) {
      error = err.message;
    }
  });

  function openModal(product = null) {
    editingProduct = product;
    if (product) {
      currentProduct = { ...product };
    } else {
      currentProduct = {
        name: '',
        description: '',
        price: 0,
        stock_quantity: 0,
        low_stock_threshold: 0,
        category: '',
        image_url: '',
        is_active: true
      };
    }
    showModal = true;
  }

  function closeModal() {
    showModal = false;
    editingProduct = null;
  }

  async function handleSubmit() {
    try {
      if (editingProduct) {
        const updatedProduct = await updateProduct(editingProduct.id, currentProduct);
        products = products.map(p => p.id === updatedProduct.id ? updatedProduct : p);
        showNotification('Product updated successfully', 'success');
      } else {
        const createdProduct = await createProduct(currentProduct);
        products = [...products, createdProduct];
        showNotification('Product created successfully', 'success');
      }
      closeModal();
    } catch (err) {
      showNotification(err.message, 'error');
      error = err.message;
    }
  }

  async function handleDeleteProduct(id: number) {
    showConfirmation('Are you sure you want to delete this product?', async () => {
      try {
        await deleteProduct(id);
        products = products.filter(p => p.id !== id);
        showNotification('Product deleted successfully', 'success');
      } catch (err) {
        showNotification(err.message, 'error');
      }
    });
  }
  

</script>

<div class="container mx-auto p-4">
  <h2 class="text-2xl font-semibold mb-4">Product Management</h2>
  
  {#if error}
      <p class="text-red-500 mb-4">{error}</p>
  {/if}

  <button on:click={() => openModal()} class="bg-blue-500 text-white px-4 py-2 rounded mb-4">
      Add New Product
  </button>

  <div class="overflow-x-auto">
      <table class="min-w-full bg-white">
          <thead class="bg-gray-100">
              <tr>
                  <th class="py-2 px-4 text-left">Name</th>
                  <th class="py-2 px-4 text-left">Price</th>
                  <th class="py-2 px-4 text-left">Stock</th>
                  <th class="py-2 px-4 text-left">Category</th>
                  <th class="py-2 px-4 text-left">Actions</th>
              </tr>
          </thead>
          <tbody>
              {#each products as product (product.id)}
                  <tr class="border-t">
                      <td class="py-2 px-4">{product.name}</td>
                      <td class="py-2 px-4">${product.price}</td>
                      <td class="py-2 px-4">{product.stock_quantity}</td>
                      <td class="py-2 px-4">{product.category}</td>
                      <td class="py-2 px-4">
                          <button on:click={() => openModal(product)} class="mr-2 bg-yellow-500 text-white p-2 rounded">Edit</button>
                          <button on:click={() => handleDeleteProduct(product.id)} class="bg-red-500 text-white p-2 rounded">Delete</button>
                      </td>
                  </tr>
              {/each}
          </tbody>
      </table>
  </div>

  {#if showModal}
      <div class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" id="my-modal">
          <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
              <h3 class="text-lg font-semibold mb-4">{editingProduct ? 'Edit Product' : 'Add New Product'}</h3>
              <form on:submit|preventDefault={handleSubmit}>
                  <div class="mb-4">
                      <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                      <input id="name" type="text" bind:value={currentProduct.name} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4">
                      <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                      <textarea id="description" bind:value={currentProduct.description} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"></textarea>
                  </div>
                  <div class="mb-4">
                      <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                      <input id="price" type="number" step="0.01" bind:value={currentProduct.price} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4">
                      <label for="stock_quantity" class="block text-sm font-medium text-gray-700">Stock Quantity</label>
                      <input id="stock_quantity" type="number" bind:value={currentProduct.stock_quantity} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4">
                      <label for="low_stock_threshold" class="block text-sm font-medium text-gray-700">Low Stock Threshold</label>
                      <input id="low_stock_threshold" type="number" bind:value={currentProduct.low_stock_threshold} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4">
                      <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
                      <input id="category" type="text" bind:value={currentProduct.category} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4">
                      <label for="image_url" class="block text-sm font-medium text-gray-700">Image URL</label>
                      <input id="image_url" type="text" bind:value={currentProduct.image_url} required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  </div>
                  <div class="mb-4 flex items-center">
                      <input id="is_active" type="checkbox" bind:checked={currentProduct.is_active} class="rounded border-gray-300 text-indigo-600 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                      <label for="is_active" class="ml-2 block text-sm font-medium text-gray-700">Is Active</label>
                  </div>
                  <div class="flex justify-end">
                      <button type="button" on:click={closeModal} class="mr-2 px-4 py-2 bg-gray-300 text-gray-800 rounded-md hover:bg-gray-400">Cancel</button>
                      <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">{editingProduct ? 'Update Product' : 'Add Product'}</button>
                  </div>
              </form>
          </div>
      </div>
  {/if}
</div>