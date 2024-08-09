<script>
    import { cart } from '../stores/cart.js';
    import { createOrder } from '../services/api.js';
    import { navigate } from 'svelte-routing';
  
    let address = '';
    let city = '';
    let zipCode = '';
    let cardNumber = '';
    let cardExpiry = '';
    let cardCVC = '';
  
    async function handleCheckout() {
      const orderItems = $cart.map(item => ({
        product_id: item.id,
        quantity: item.quantity
      }));
  
      try {
        const order = await createOrder({
          items: orderItems,
          shipping_address: `${address}, ${city}, ${zipCode}`
        });
  
        cart.clearCart();
        navigate('/order-confirmation', { state: { orderId: order.id } });
      } catch (error) {
        console.error('Error creating order:', error);
        alert('Failed to create order. Please try again.');
      }
    }
  </script>
  
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-8 text-indigo-900">Checkout</h1>
  
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <div>
        <h2 class="text-2xl font-semibold mb-4 text-indigo-800">Shipping Information</h2>
        <div class="mb-4">
          <label for="address" class="block text-gray-700 mb-2">Address</label>
          <input type="text" id="address" bind:value={address} class="w-full px-3 py-2 border rounded-md">
        </div>
        <div class="mb-4">
          <label for="city" class="block text-gray-700 mb-2">City</label>
          <input type="text" id="city" bind:value={city} class="w-full px-3 py-2 border rounded-md">
        </div>
        <div class="mb-4">
          <label for="zipCode" class="block text-gray-700 mb-2">Zip Code</label>
          <input type="text" id="zipCode" bind:value={zipCode} class="w-full px-3 py-2 border rounded-md">
        </div>
      </div>
  
      <div>
        <h2 class="text-2xl font-semibold mb-4 text-indigo-800">Payment Information</h2>
        <div class="mb-4">
          <label for="cardNumber" class="block text-gray-700 mb-2">Card Number</label>
          <input type="text" id="cardNumber" bind:value={cardNumber} class="w-full px-3 py-2 border rounded-md">
        </div>
        <div class="mb-4">
          <label for="cardExpiry" class="block text-gray-700 mb-2">Expiry Date</label>
          <input type="text" id="cardExpiry" bind:value={cardExpiry} class="w-full px-3 py-2 border rounded-md">
        </div>
        <div class="mb-4">
          <label for="cardCVC" class="block text-gray-700 mb-2">CVC</label>
          <input type="text" id="cardCVC" bind:value={cardCVC} class="w-full px-3 py-2 border rounded-md">
        </div>
      </div>
    </div>
  
    <div class="mt-8">
      <button 
        on:click={handleCheckout}
        class="bg-indigo-600 text-white px-6 py-3 rounded-lg text-lg font-semibold hover:bg-indigo-700 transition-colors duration-300"
      >
        Place Order
      </button>
    </div>
  </div>