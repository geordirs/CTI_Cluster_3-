<script>
    import { onMount } from 'svelte';
    import { Link } from 'svelte-routing';
    import { getProducts } from '../services/api.js';
    import Carousel from '../components/Carousel.svelte';
    import AddToCartButton from '../components/AddToCartButton.svelte';
  
    let allProducts = [];
    let latestProducts = [];
    let featuredProducts = [];
  
    onMount(async () => {
      try {
        allProducts = await getProducts();
        latestProducts = [...allProducts].reverse().slice(0, 5); // Toma los últimos 5 productos
        featuredProducts = allProducts.slice(0, 6); // Toma los primeros 3 productos como destacados
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    });
  </script>
  
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-5xl font-bold mb-12 text-center text-indigo-900">Discover Luxury</h1>
    
    {#if latestProducts.length > 0}
      <div class="mb-16">
        <h2 class="text-3xl font-semibold mb-6 text-indigo-800">Latest Arrivals</h2>
        <Carousel items={latestProducts} />
      </div>
    {:else}
      <p>No products available</p>
    {/if}
  
    {#if featuredProducts.length > 0}
  <div class="mb-16">
    <h2 class="text-3xl font-semibold mb-6 text-indigo-800">Featured Products</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      {#each featuredProducts as product}
        <div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow duration-300">
          <img src={product.image_url} alt={product.name} class="w-full h-64 object-cover"/>
          <div class="p-6">
            <h3 class="text-xl font-semibold mb-2 text-indigo-900">{product.name}</h3>
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
  </div>
{/if}
  
    <div class="text-center">
      <Link to="/products" class="bg-gray-200 text-indigo-800 px-6 py-3 rounded-md font-semibold hover:bg-gray-300 transition-colors duration-300">
        Explore All Products
      </Link>
    </div>
    <div class="mb-16">
        <h2 class="text-3xl font-semibold mb-6 text-indigo-800">Special Offers</h2>
        <div class="bg-indigo-600 text-white p-8 rounded-lg text-center">
          <h3 class="text-2xl font-bold mb-4">Summer Sale!</h3>
          <p class="text-xl mb-4">Get 20% off on all summer essentials</p>
          <Link to="/products" class="bg-white text-indigo-600 px-6 py-3 rounded-md font-semibold hover:bg-indigo-100 transition-colors duration-300">
            Shop Now
          </Link>
        </div>
      </div>
  </div>

  