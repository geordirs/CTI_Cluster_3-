<script>
    import { onMount } from 'svelte';
    import { getProduct } from '../services/api.js';
    import { cart } from '../stores/cart.js';
  
    export let id;
  
    let product = null;
    let error = null;
    let quantity = 1;
  
    onMount(async () => {
      try {
        product = await getProduct(id);
      } catch (err) {
        console.error('Error fetching product:', err);
        error = 'Failed to load product details. Please try again later.';
      }
    });
  
    function addToCart() {
      cart.addItem(product, quantity);
      alert(`Added ${quantity} ${product.name}(s) to cart!`);
    }
  </script>
  
  <div class="container mx-auto px-4 py-8">
    {#if error}
      <p class="text-red-500">{error}</p>
    {:else if !product}
      <p class="text-center text-gray-600">Loading product details...</p>
    {:else}
      <div class="bg-white shadow-lg rounded-lg overflow-hidden">
        <div class="md:flex">
          <div class="md:flex-shrink-0 md:w-1/2">
            <div class="h-0 pb-[100%] relative">
              <img src={product.image_url} alt={product.name} class="absolute h-full w-full object-cover"/>
            </div>
          </div>
          <div class="p-8 md:w-1/2">
            <h1 class="text-3xl font-bold text-indigo-900 mb-4">{product.name}</h1>
            <p class="text-2xl text-indigo-600 mb-4">${product.price.toFixed(2)}</p>
            <div class="bg-gray-100 p-4 rounded-lg mb-6">
              <h2 class="text-xl font-semibold mb-2 text-indigo-800">Product Description</h2>
              <p class="text-gray-700">{product.description}</p>
            </div>
            <div class="mb-6">
              <h2 class="text-xl font-semibold mb-2 text-indigo-800">Specifications</h2>
              <ul class="list-disc list-inside text-gray-700">
                <li>Category: {product.category}</li>
                <li>Stock: {product.stock_quantity} units</li>
              </ul>
            </div>
            <div class="flex items-center mb-4">
              <label for="quantity" class="mr-2 text-gray-700">Quantity:</label>
              <input 
                type="number" 
                id="quantity" 
                bind:value={quantity} 
                min="1" 
                max={product.stock_quantity}
                class="border rounded px-2 py-1 w-16 text-gray-700"
              />
            </div>
            <button 
              on:click={addToCart}
              class="bg-indigo-600 text-white px-6 py-3 rounded-lg text-lg font-semibold hover:bg-indigo-700 transition-colors duration-300"
            >
              Add to Cart
            </button>
          </div>
        </div>
      </div>
    {/if}
  </div>