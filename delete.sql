-- Eliminar todos los productos existentes
DELETE FROM products;

-- Crear 10 nuevos productos de tecnología
INSERT INTO products (name, description, price, category, stock_quantity, image_url) VALUES
('Laptop Ultradelgada', 'Laptop ligera y potente para profesionales', 1299.99, 'Computadoras', 30, 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853'),
('Smartphone 5G', 'Teléfono inteligente con la última tecnología 5G', 899.99, 'Móviles', 50, 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9'),
('Auriculares Inalámbricos', 'Auriculares con cancelación de ruido y sonido premium', 249.99, 'Audio', 40, 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e'),
('Tablet de Diseño', 'Tablet con lápiz óptico para diseñadores y artistas', 799.99, 'Tablets', 25, 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0'),
('Smartwatch Deportivo', 'Reloj inteligente con GPS y monitor cardíaco', 299.99, 'Wearables', 35, 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1'),
('Cámara DSLR', 'Cámara profesional para fotografía y video', 1499.99, 'Fotografía', 20, 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd'),
('Altavoz Inteligente', 'Altavoz con asistente de voz integrado', 129.99, 'Audio', 45, 'https://images.unsplash.com/photo-1543512214-318c7553f230'),
('Monitor Curvo', 'Monitor de 34 pulgadas para gaming y productividad', 599.99, 'Periféricos', 15, 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf'),
('Teclado Mecánico', 'Teclado para gaming con iluminación RGB', 149.99, 'Periféricos', 30, 'https://images.unsplash.com/photo-1511467687858-23d96c32e4ae'),
('Drone con Cámara 4K', 'Drone para fotografía aérea y videografía', 799.99, 'Fotografía', 10, 'https://images.unsplash.com/photo-1473968512647-3e447244af8f');