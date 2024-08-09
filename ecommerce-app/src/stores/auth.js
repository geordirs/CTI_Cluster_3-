import { writable } from 'svelte/store';

function createAuth() {
  const { subscribe, set, update } = writable({
    isAuthenticated: false,
    username: null,
    role: null
  });

  return {
    subscribe,
    login: (username, role) => {
      set({ isAuthenticated: true, username, role });
      localStorage.setItem('auth', JSON.stringify({ isAuthenticated: true, username, role }));
    },
    logout: () => {
      set({ isAuthenticated: false, username: null, role: null });
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