//const API_URL = 'http://localhost:8000';
//const API_URL = import.meta.env.VITE_API_URL;
const API_URL = "https://web-production-b61f.up.railway.app";;

async function fetchData() {
  const response = await fetch(`${API_URL}/endpoint`);
  const data = await response.json();
  return data;
}

const getAuthHeader = () => {
  const token = localStorage.getItem('token');
  return token ? { 'Authorization': `Bearer ${token}` } : {};
};

const handleResponse = async (response) => {
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'An error occurred');
  }
  return response.json();
};

// Products
export const getProducts = async () => {
  const response = await fetch(`${API_URL}/products/`, {
    headers: getAuthHeader()
  });
  return handleResponse(response);
};

export const getProduct = async (id) => {
  const response = await fetch(`${API_URL}/products/${id}`, {
    headers: getAuthHeader()
  });
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

export const updateProduct = async (id, productData) => {
  const response = await fetch(`${API_URL}/products/${id}`, {
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
  const response = await fetch(`${API_URL}/products/${id}`, {
    method: 'DELETE',
    headers: getAuthHeader()
  });
  return handleResponse(response);
};

// Users
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

// Coupons
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
  const response = await fetch(`${API_URL}/coupons/${id}`, {
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
  const response = await fetch(`${API_URL}/coupons/${id}`, {
    method: 'DELETE',
    headers: getAuthHeader()
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

//Orders

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