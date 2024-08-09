<script>
    import { Route } from "svelte-routing";
    import Home from "../routes/Home.svelte";
    import ProductList from "../routes/ProductList.svelte";
    import ProductDetail from "../routes/ProductDetail.svelte";
    import Cart from "../routes/Cart.svelte";
  
    export let url = "";
  </script>
  
  <main class="container mx-auto mt-8 p-4">
    <Route path="/" component={Home} />
    <Route path="/products" component={ProductList} />
    <Route path="/product/:id" let:params>
      <ProductDetail id={params.id} />
    </Route>
    <Route path="/cart" component={Cart} />
  </main>