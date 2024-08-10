import { writable } from 'svelte/store';

function createCart() {
  const { subscribe, set, update } = writable([]);

  return {
    subscribe,
    addItem: (product, quantity) => update(items => {
      const existingItem = items.find(item => item.id === product.id);
      if (existingItem) {
        return items.map(item => 
          item.id === product.id 
            ? { ...item, quantity: item.quantity + quantity }
            : item
        );
      }
      return [...items, { ...product, quantity }];
    }),
    removeItem: (id) => update(items => items.filter(item => item.id !== id)),
    updateQuantity: (id, quantity) => update(items =>
      items.map(item => 
        item.id === id ? { ...item, quantity } : item
      )
    ),
    clearCart: () => set([])
  };
}

export const cart = createCart();