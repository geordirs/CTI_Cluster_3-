<script>
    import { cart } from '../stores/cart.js';
    import ToastNotification from './ToastNotification.svelte';
  
    export let product;
  
    let showNotification = false;
  
    function addToCart() {
      cart.addItem(product, 1);
      showNotification = true;
    }
  
    function closeNotification() {
      showNotification = false;
    }
  </script>
  
  <button 
    on:click={addToCart}
    class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 transition-colors duration-300 text-sm"
  >
    Add to Cart
  </button>
  
  {#if showNotification}
    <ToastNotification 
      message={`Added ${product.name} to cart!`} 
      on:close={closeNotification}
    />
  {/if}