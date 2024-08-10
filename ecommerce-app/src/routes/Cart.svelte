<script>
    import { cart } from '../stores/cart.js';
    import { Link } from 'svelte-routing';
    import { applyCoupon } from '../services/api.js';
  
    let couponCode = '';
    let couponError = '';
    let couponDiscount = 0;
  
    function removeItem(id) {
      cart.removeItem(id);
    }
  
    function updateQuantity(id, event) {
      const newQuantity = parseInt(event.target.value);
      if (!isNaN(newQuantity) && newQuantity > 0) {
        cart.updateQuantity(id, newQuantity);
      }
    }
  
    function getSubtotal() {
      return $cart.reduce((total, item) => total + item.price * item.quantity, 0);
    }
  
    function getTotal() {
      return (getSubtotal() - couponDiscount).toFixed(2);
    }
  
    async function handleApplyCoupon() {
      try {
        const result = await applyCoupon(couponCode);
        couponDiscount = result.discount;
        couponError = '';
      } catch (error) {
        couponError = error.message;
        couponDiscount = 0;
      }
    }
  </script>
  
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6">Your Cart</h1>
  
    {#if $cart.length === 0}
      <p>Your cart is empty.</p>
    {:else}
      <div class="bg-white shadow-md rounded my-6">
        <table class="text-left w-full border-collapse">
          <thead>
            <tr>
              <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">Product</th>
              <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">Price</th>
              <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">Quantity</th>
              <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">Total</th>
              <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">Actions</th>
            </tr>
          </thead>
          <tbody>
            {#each $cart as item}
              <tr class="hover:bg-grey-lighter">
                <td class="py-4 px-6 border-b border-grey-light">{item.name}</td>
                <td class="py-4 px-6 border-b border-grey-light">${item.price.toFixed(2)}</td>
                <td class="py-4 px-6 border-b border-grey-light">
                  <input 
                    type="number" 
                    value={item.quantity} 
                    on:input={(event) => updateQuantity(item.id, event)}
                    min="1"
                    class="border rounded px-2 py-1 w-16"
                  />
                </td>
                <td class="py-4 px-6 border-b border-grey-light">${(item.price * item.quantity).toFixed(2)}</td>
                <td class="py-4 px-6 border-b border-grey-light">
                  <button on:click={() => removeItem(item.id)} class="text-red-500 hover:text-red-700">Remove</button>
                </td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
  
      <div class="mt-8">
        <h2 class="text-2xl font-semibold mb-4">Apply Coupon</h2>
        <div class="flex items-center">
          <input
            type="text"
            bind:value={couponCode}
            placeholder="Enter coupon code"
            class="border rounded-l px-4 py-2 w-64"
          />
          <button
            on:click={handleApplyCoupon}
            class="bg-indigo-600 text-white px-4 py-2 rounded-r hover:bg-indigo-700 transition-colors duration-300"
          >
            Apply
          </button>
        </div>
        {#if couponError}
          <p class="text-red-500 mt-2">{couponError}</p>
        {/if}
      </div>
  
      <div class="text-right mt-8">
        <p class="text-xl mb-2">Subtotal: ${getSubtotal().toFixed(2)}</p>
        {#if couponDiscount > 0}
          <p class="text-xl mb-2 text-green-600">Discount: -${couponDiscount.toFixed(2)}</p>
        {/if}
        <p class="text-2xl font-bold mb-4">Total: ${getTotal()}</p>
        <Link to="/checkout" class="bg-indigo-600 text-white px-6 py-3 rounded-lg text-lg font-semibold hover:bg-indigo-700 transition-colors duration-300">
          Proceed to Checkout
        </Link>
      </div>
    {/if}
  </div>