<script>
    import { fade } from 'svelte/transition';
    import { createEventDispatcher } from 'svelte';
  
    export let message = '';
    export let type = 'success';
  
    const dispatch = createEventDispatcher();
  
    function close() {
      dispatch('close');
    }
  
    setTimeout(close, 3000); // Cierra automáticamente después de 3 segundos
  </script>
  
  <div 
    transition:fade
    class="fixed bottom-4 right-4 p-4 rounded-lg shadow-lg {type === 'success' ? 'bg-green-500' : 'bg-red-500'} text-white"
  >
    <p>{message}</p>
    <button on:click={close} class="absolute top-1 right-2 text-white">&times;</button>
  </div>