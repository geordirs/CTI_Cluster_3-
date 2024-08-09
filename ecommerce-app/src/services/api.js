const API_URL = 'http://localhost:8000';  // Ajusta esto a la URL de tu backend

const handleResponse = async (response) => {
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || 'An error occurred');
  }
  return response.json();
};

const getAuthHeader = () => {
  const token = localStorage.getItem('token');
  return token ? { 'Authorization': `Bearer ${token}` } : {};
};

export const getProducts = async () => {
  const response = await fetch(`${API_URL}/products/`);
  return handleResponse(response);
};

export const getProduct = async (id) => {
  const response = await fetch(`${API_URL}/products/${id}/`);
  return handleResponse(response);
};

export const createProduct = async (productData) => {
  const response = await fetch(`${API_URL}/products/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeader()
    },
    body: JSON.stringify(productData)
  });
  return handleResponse(response);
};

export const applyCoupon = async (couponCode) => {
  const response = await fetch(`${API_URL}/coupons/apply`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeader()
    },
    body: JSON.stringify({ code: couponCode })
  });
  return handleResponse(response);
};

export const createOrder = async (orderData) => {
  const response = await fetch(`${API_URL}/orders/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeader()
    },
    body: JSON.stringify(orderData)
  });
  return handleResponse(response);
};

export const updateProduct = async (id, productData) => {
  const response = await fetch(`${API_URL}/products/${id}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeader()
    },
    body: JSON.stringify(productData)
  });
  return handleResponse(response);
};

export const deleteProduct = async (id) => {
  const response = await fetch(`${API_URL}/products/${id}/`, {
    method: 'DELETE',
    headers: getAuthHeader()
  });
  return handleResponse(response);
};

export const getUsers = async () => {
  const response = await fetch(`${API_URL}/users/`, {
    headers: getAuthHeader()
  });
  return handleResponse(response);
};

export const createUser = async (userData) => {
  const response = await fetch(`${API_URL}/users/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeader()
    },
    body: JSON.stringify(userData)
  });
  return handleResponse(response);
};

export const updateUser = async (id, userData) => {
  const response = await fetch(`${API_URL}/users/${id}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeader()
    },
    body: JSON.stringify(userData)
  });
  return handleResponse(response);
};

export const deleteUser = async (id) => {
  const response = await fetch(`${API_URL}/users/${id}/`, {
    method: 'DELETE',
    headers: getAuthHeader()
  });
  return handleResponse(response);
};

export const getCoupons = async () => {
  const response = await fetch(`${API_URL}/coupons/`, {
    headers: getAuthHeader()
  });
  return handleResponse(response);
};

export const createCoupon = async (couponData) => {
  const response = await fetch(`${API_URL}/coupons/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeader()
    },
    body: JSON.stringify(couponData)
  });
  return handleResponse(response);
};

export const updateCoupon = async (id, couponData) => {
  const response = await fetch(`${API_URL}/coupons/${id}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeader()
    },
    body: JSON.stringify(couponData)
  });
  return handleResponse(response);
};

export const deleteCoupon = async (id) => {
  const response = await fetch(`${API_URL}/coupons/${id}/`, {
    method: 'DELETE',
    headers: getAuthHeader()
  });
  return handleResponse(response);
};

// Otras funciones existentes (login, register, etc.) permanecen sin cambios