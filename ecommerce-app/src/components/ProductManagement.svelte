<script>
    import { onMount } from 'svelte';
    import { getProducts, createProduct, updateProduct, deleteProduct } from '../services/api.js';
  
    let products = [];
    let newProduct = { name: '', price: '', description: '', image_url: '' };
    let editingProduct = null;
  
    onMount(async () => {
      products = await getProducts();
    });
  
    async function handleCreateProduct() {
      await createProduct(newProduct);
      products = await getProducts();
      newProduct = { name: '', price: '', description: '', image_url: '' };
    }
  
    async function handleUpdateProduct() {
      await updateProduct(editingProduct.id, editingProduct);
      products = await getProducts();
      editingProduct = null;
    }
  
    async function handleDeleteProduct(id) {
      if (confirm('Are you sure you want to delete this product?')) {
        await deleteProduct(id);
        products = await getProducts();
      }
    }
  </script>
  
  <div>
    <h2 class="text-2xl font-semibold mb-4">Product Management</h2>
  
    <div class="mb-8">
      <h3 class="text-xl font-semibold mb-2">Add New Product</h3>
      <input bind:value={newProduct.name} placeholder="Name" class="mb-2 p-2 border rounded" />
      <input bind:value={newProduct.price} type="number" placeholder="Price" class="mb-2 p-2 border rounded" />
      <input bind:value={newProduct.description} placeholder="Description" class="mb-2 p-2 border rounded" />
      <input bind:value={newProduct.image_url} placeholder="Image URL" class="mb-2 p-2 border rounded" />
      <button on:click={handleCreateProduct} class="bg-green-500 text-white p-2 rounded">Add Product</button>
    </div>
  
    <div>
      <h3 class="text-xl font-semibold mb-2">Product List</h3>
      {#each products as product (product.id)}
        <div class="mb-4 p-4 border rounded">
          <h4 class="font-semibold">{product.name}</h4>
          <p>Price: ${product.price}</p>
          <button on:click={() => editingProduct = {...product}} class="mr-2 bg-blue-500 text-white p-2 rounded">Edit</button>
          <button on:click={() => handleDeleteProduct(product.id)} class="bg-red-500 text-white p-2 rounded">Delete</button>
        </div>
      {/each}
    </div>
  
    {#if editingProduct}
      <div class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" id="my-modal">
        <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
          <h3 class="text-lg font-semibold mb-4">Edit Product</h3>
          <input bind:value={editingProduct.name} class="mb-2 p-2 border rounded w-full" />
          <input bind:value={editingProduct.price} type="number" class="mb-2 p-2 border rounded w-full" />
          <input bind:value={editingProduct.description} class="mb-2 p-2 border rounded w-full" />
          <input bind:value={editingProduct.image_url} class="mb-2 p-2 border rounded w-full" />
          <button on:click={handleUpdateProduct} class="bg-blue-500 text-white p-2 rounded">Update</button>
          <button on:click={() => editingProduct = null} class="ml-2 bg-gray-500 text-white p-2 rounded">Cancel</button>
        </div>
      </div>
    {/if}
  </div>