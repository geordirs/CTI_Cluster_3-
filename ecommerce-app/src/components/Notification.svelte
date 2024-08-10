<script>
    import { fade } from 'svelte/transition';
    import { onMount, onDestroy } from 'svelte';
  
    export let message = '';
    export let type = 'success'; // 'success', 'error', 'warning'
    export let duration = 3000;
  
    let visible = true;
    let timer;
  
    function close() {
      visible = false;
    }
  
    $: if (message) {
      visible = true;
      if (timer) clearTimeout(timer);
      timer = setTimeout(() => {
        visible = false;
      }, duration);
    }
  
    onDestroy(() => {
      if (timer) clearTimeout(timer);
    });
  </script>
  
  {#if visible}
    <div 
      transition:fade={{ duration: 300 }}
      class="fixed bottom-4 right-4 p-4 rounded-lg shadow-lg {type === 'success' ? 'bg-green-500' : type === 'error' ? 'bg-red-500' : 'bg-yellow-500'} text-white"
    >
      <p>{message}</p>
      <button on:click={close} class="absolute top-1 right-2 text-white">&times;</button>
    </div>
  {/if}