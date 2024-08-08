<script>
  import { Router, Route, Link} from 'svelte-routing';
  import Header from './components/Header.svelte';
  import Home from './routes/Home.svelte';
  import ProductList from './routes/ProductList.svelte';
  import ProductDetail from './routes/ProductDetail.svelte';
  import Cart from './routes/Cart.svelte';
  import Login from "./routes/Login.svelte";

  export let url = '';
</script>


<Router {url}>
  <nav class="bg-gray-800 text-white p-4">
    <Link to="/" class="mr-4">Home</Link>
    <Link to="/products" class="mr-4">Products</Link>
    <Link to="/login">Login</Link>
  </nav>

  <main>
    <Route path="/" component={Home} />
    <Route path="/products" component={ProductList} />
    <Route path="/login" component={Login} />
</Router>