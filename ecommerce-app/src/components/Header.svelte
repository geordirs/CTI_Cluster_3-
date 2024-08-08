<script>
    import { Link } from 'svelte-routing';
  </script>
  
  <header class="bg-blue-600 text-white">
    <nav class="container mx-auto px-4 py-4 flex justify-between items-center">
      <Link to="/" class="text-2xl font-bold">E-Commerce</Link>
      <ul class="flex space-x-4">
        <li><Link to="/products">Products</Link></li>
        <li><Link to="/cart">Cart</Link></li>
      </ul>
    </nav>
  </header>