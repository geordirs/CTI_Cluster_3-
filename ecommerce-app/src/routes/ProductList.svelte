<script>
    import { onMount } from 'svelte';
    import { Link } from 'svelte-routing';
    import { getProducts } from '../services/api.js';
    import AddToCartButton from '../components/AddToCartButton.svelte';
  
    let products = [];
    let error = null;
  
    onMount(async () => {
      try {
        products = await getProducts();
      } catch (err) {
        console.error('Error fetching products:', err);
        error = 'Failed to load products. Please try again later.';
      }
    });
  </script>
  
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6 text-indigo-900">Our Products</h1>
    
    {#if error}
      <p class="text-red-500">{error}</p>
    {:else if products.length === 0}
      <p class="text-center text-gray-600">Loading products...</p>
    {:else}
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each products as product}
          <div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow duration-300">
            <img src={product.image_url} alt={product.name} class="w-full h-64 object-cover"/>
            <div class="p-6">
              <h2 class="text-xl font-semibold mb-2 text-indigo-900">{product.name}</h2>
              <p class="text-gray-600 mb-4">${product.price.toFixed(2)}</p>
              <div class="flex justify-between items-center">
                <Link to={`/product/${product.id}`} class="text-indigo-600 hover:text-indigo-800 transition-colors duration-300">
                  View Details
                </Link>
                <AddToCartButton {product} />
              </div>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>    