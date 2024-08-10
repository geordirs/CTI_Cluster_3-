<script>
  import { onMount } from 'svelte';
  import { Router, Route } from "svelte-routing";
  import Nav from "./components/Nav.svelte";
  import Home from "./routes/Home.svelte";
  import ProductList from "./routes/ProductList.svelte";
  import ProductDetail from "./routes/ProductDetail.svelte";
  import Cart from "./routes/Cart.svelte";
  import Login from "./components/Login.svelte";
  import Checkout from "./routes/Checkout.svelte";
  import AdminPanel from "./routes/AdminPanel.svelte";
  import { auth } from './stores/auth.js';

  export let url = "";
  let showLoginModal = false;
  
  function openLoginModal() {
    showLoginModal = true;
  }

  function closeLoginModal() {
    showLoginModal = false;
  }

  onMount(() => {
    auth.checkAuth();
  });

</script>

<Router {url}>
  <Nav {openLoginModal} />

  <main class="mt-8 mb-16">
    <Route path="/" component={Home} />
    <Route path="/products" component={ProductList} />
    <Route path="/product/:id" let:params>
      <ProductDetail id={params.id} />
    </Route>
    <Route path="/cart" component={Cart} />
    <Route path="/checkout" component={Checkout} />
    <Route path="/admin" component={AdminPanel} />
  </main>

  <Login showModal={showLoginModal} on:close={closeLoginModal} />
</Router>