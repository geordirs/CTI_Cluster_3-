const API_URL = 'http://localhost:8000';  // Ajusta esto a la URL de tu backend

export const getProducts = async () => {
    const response = await fetch(`${API_URL}/products`);
    return response.json();
  };
  
  export const getProduct = async (id) => {
    const response = await fetch(`${API_URL}/products/${id}`);
    return response.json();
  };

export const createProduct = async (productData) => {
  const response = await fetch(`${API_URL}/products`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(productData),
  });
  return response.json();
};

// Añade más funciones para otras operaciones de la API según sea necesario