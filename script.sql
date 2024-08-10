-- Crear la tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    is_admin BOOLEAN DEFAULT FALSE
);

-- Crear la tabla de productos
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price FLOAT NOT NULL,
    stock_quantity INTEGER NOT NULL,
    low_stock_threshold INTEGER DEFAULT 10,
    is_active BOOLEAN DEFAULT TRUE,
    category VARCHAR(255),
    image_url TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Crear la tabla de notificaciones
CREATE TABLE IF NOT EXISTS notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    message TEXT,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Crear la tabla de elementos del carrito
CREATE TABLE IF NOT EXISTS cart_items (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER
);

-- Crear la tabla de cupones
CREATE TABLE IF NOT EXISTS coupons (
    id SERIAL PRIMARY KEY,
    code VARCHAR(255) UNIQUE NOT NULL,
    discount_percent FLOAT,
    is_active BOOLEAN DEFAULT TRUE,
    valid_from TIMESTAMPTZ,
    valid_to TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Crear la tabla de órdenes
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    status VARCHAR(255) CHECK (status IN ('pending', 'processing', 'shipped', 'delivered')) DEFAULT 'pending',
    total_amount FLOAT,
    coupon_id INTEGER REFERENCES coupons(id)
);

-- Crear la tabla de elementos de la orden
CREATE TABLE IF NOT EXISTS order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER,
    price FLOAT
);

-- Crear la tabla de reseñas
CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    product_id INTEGER REFERENCES products(id),
    rating INTEGER,
    comment TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Crear la tabla de recomendaciones
CREATE TABLE IF NOT EXISTS recommendations (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    recommended_product_id INTEGER REFERENCES products(id),
    score FLOAT
);

-- Crear índices para mejorar el rendimiento de las consultas
CREATE INDEX IF NOT EXISTS idx_product_name_description ON products (name, description);

-- Insertar datos en la tabla `products`
INSERT INTO products (name, description, price, stock_quantity, low_stock_threshold, category, image_url, is_active)
VALUES
('Wireless Mouse', 'Ergonomic wireless mouse with adjustable DPI.', 25.99, 100, 10, 'Electronics', 'https://m.media-amazon.com/images/I/61Np01l8Y3L._AC_SX679_.jpg', true),
('Bluetooth Headphones', 'Noise-cancelling over-ear headphones with 20-hour battery life.', 89.99, 50, 5, 'Electronics', 'https://m.media-amazon.com/images/I/71yCbvuWJtL._AC_SL1500_.jpg', true),
('Gaming Keyboard', 'Mechanical RGB gaming keyboard with programmable keys.', 69.99, 75, 8, 'Electronics', 'https://m.media-amazon.com/images/I/81XbB6kOshL._AC_SX679_.jpg', true),
('4K Monitor', '27-inch 4K UHD monitor with IPS display.', 299.99, 30, 3, 'Electronics', 'https://m.media-amazon.com/images/I/81dDZyJQ-UL._AC_SX679_.jpg', true),
('USB-C Hub', 'Multiport USB-C hub with HDMI, USB, and SD card slots.', 34.99, 150, 15, 'Electronics', 'https://m.media-amazon.com/images/I/61u48FEsprL._AC_SX679_.jpg', true),
('Portable Charger', '10000mAh portable charger with dual USB ports.', 19.99, 200, 20, 'Electronics', 'https://m.media-amazon.com/images/I/71+WJdO5TzL._AC_SX679_.jpg', true),
('Smartwatch', 'Waterproof smartwatch with heart rate monitor and GPS.', 149.99, 40, 4, 'Wearables', 'https://m.media-amazon.com/images/I/61+4pCHl0IL._AC_SX679_.jpg', true),
('Fitness Tracker', 'Activity tracker with sleep monitoring and step counter.', 49.99, 120, 12, 'Wearables', 'https://m.media-amazon.com/images/I/61fEwLULjlL._AC_SX679_.jpg', true),
('Laptop Sleeve', 'Water-resistant laptop sleeve with cushioned interior.', 17.99, 180, 18, 'Accessories', 'https://m.media-amazon.com/images/I/81lPhzghpGL._AC_SX679_.jpg', true),
('Wireless Charger', 'Fast wireless charger compatible with Qi-enabled devices.', 29.99, 90, 9, 'Accessories', 'https://m.media-amazon.com/images/I/71s0V76cSfL._AC_SX679_.jpg', true),
('Noise-Cancelling Earbuds', 'True wireless earbuds with active noise cancellation.', 79.99, 60, 6, 'Wearables', 'https://m.media-amazon.com/images/I/71wYH0+VUpL._AC_SX679_.jpg', true),
('Smart Home Speaker', 'Voice-controlled smart speaker with built-in assistant.', 99.99, 70, 7, 'Home', 'https://m.media-amazon.com/images/I/71Jw1yH0oIL._AC_SX679_.jpg', true),
('Wi-Fi Range Extender', 'Dual-band Wi-Fi range extender with external antennas.', 45.99, 110, 11, 'Electronics', 'https://m.media-amazon.com/images/I/61m4df2VyGL._AC_SX679_.jpg', true),
('Tablet Stand', 'Adjustable tablet stand with 360-degree rotation.', 14.99, 140, 14, 'Accessories', 'https://m.media-amazon.com/images/I/61BIl2-SgUL._AC_SX679_.jpg', true),
('External SSD', '1TB portable SSD with USB 3.1 Gen 2 interface.', 129.99, 25, 2, 'Storage', 'https://m.media-amazon.com/images/I/61U55oeK5jL._AC_SX679_.jpg', true),
('Wireless Presenter', 'Bluetooth wireless presenter with laser pointer.', 24.99, 130, 13, 'Accessories', 'https://m.media-amazon.com/images/I/61OOGb6VBZL._AC_SX679_.jpg', true),
('Portable Projector', '1080p portable projector with built-in speakers.', 219.99, 35, 3, 'Home', 'https://m.media-amazon.com/images/I/71qfMQQr6vL._AC_SX679_.jpg', true),
('Smart Light Bulb', 'Color-changing smart light bulb with app control.', 12.99, 160, 16, 'Home', 'https://m.media-amazon.com/images/I/61-R0d+oDbL._AC_SX679_.jpg', true),
('Bluetooth Speaker', 'Waterproof Bluetooth speaker with 12-hour playtime.', 39.99, 85, 8, 'Audio', 'https://m.media-amazon.com/images/I/81TR4zOkOuL._AC_SX679_.jpg', true),
('Wireless Charging Pad', 'Slim wireless charging pad with fast charge support.', 22.99, 105, 10, 'Accessories', 'https://m.media-amazon.com/images/I/71Gn8CeX3dL._AC_SX679_.jpg', true);

-- Insertar datos de ejemplo en la tabla de cupones
INSERT INTO coupons (code, discount_percent, is_active, valid_from, valid_to, created_at)
VALUES
('DISCOUNT10', 10.00, TRUE, '2024-08-01 00:00:00', '2024-12-31 23:59:59', NOW()),
('SUMMER20', 20.00, TRUE, '2024-06-01 00:00:00', '2024-08-31 23:59:59', NOW());

-- Insertar datos de ejemplo en la tabla de usuarios
INSERT INTO users (username, email, password_hash, is_active, is_admin)
VALUES
('grdy', 'grdy@example.com', 'grdy', TRUE, TRUE),
('user', 'user@example.com', 'user', TRUE, FALSE);
