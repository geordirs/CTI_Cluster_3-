import { writable } from 'svelte/store';

function createAuth() {
  const { subscribe, set, update } = writable({
    isAuthenticated: false,
    username: null,
    isAdmin: false
  });

  return {
    subscribe,
    login: (username, isAdmin) => {
      set({ isAuthenticated: true, username, isAdmin });
      localStorage.setItem('auth', JSON.stringify({ isAuthenticated: true, username, isAdmin }));
    },
    logout: () => {
      set({ isAuthenticated: false, username: null, isAdmin: false });
      localStorage.removeItem('auth');
    },
    checkAuth: () => {
      const auth = localStorage.getItem('auth');
      if (auth) {
        set(JSON.parse(auth));
      }
    }
  };
}

export const auth = createAuth();