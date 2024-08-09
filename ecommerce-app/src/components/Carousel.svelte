<script>
  import { onMount, onDestroy } from 'svelte';
  import { Link } from 'svelte-routing';

  export let items = [];
  let currentIndex = 0;
  let interval;

  function next() {
    currentIndex = (currentIndex + 1) % items.length;
  }

  function prev() {
    currentIndex = (currentIndex - 1 + items.length) % items.length;
  }

  onMount(() => {
    interval = setInterval(next, 5000);
  });

  onDestroy(() => {
    if (interval) clearInterval(interval);
  });
</script>

<div class="relative overflow-hidden rounded-lg shadow-lg" style="height: 400px;">
  {#if items.length > 0}
    {#each items as item, i}
      <div 
        class="absolute inset-0 transition-opacity duration-500 ease-in-out flex items-center justify-center"
        style="opacity: {i === currentIndex ? 1 : 0}; pointer-events: {i === currentIndex ? 'auto' : 'none'};"
      >
        <img src={item.image_url} alt={item.name} class="w-full h-full object-cover absolute inset-0"/>
        <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent p-6">
          <h3 class="text-2xl font-semibold text-white mb-2">{item.name}</h3>
          <p class="text-gray-300 mb-4">${item.price.toFixed(2)}</p>
          <Link to={`/product/${item.id}`} class="bg-white text-indigo-600 px-4 py-2 rounded-md hover:bg-indigo-100 transition-colors duration-300">
            View Details
          </Link>
        </div>
      </div>
    {/each}
    <button 
      class="absolute top-1/2 left-4 transform -translate-y-1/2 bg-white bg-opacity-50 rounded-full p-2 hover:bg-opacity-75 transition-colors duration-300"
      on:click={prev}
    >
      &#10094;
    </button>
    <button 
      class="absolute top-1/2 right-4 transform -translate-y-1/2 bg-white bg-opacity-50 rounded-full p-2 hover:bg-opacity-75 transition-colors duration-300"
      on:click={next}
    >
      &#10095;
    </button>
  {:else}
    <div class="flex items-center justify-center h-full bg-gray-200 text-gray-500">
      No items to display
    </div>
  {/if}
</div>