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
('Drone con Cámara 4K', 'Drone para fotografía aérea y videografía', 799.99, 'Fotografía', 10, 'https://images.unsplash.com/photo-1473968512647-3e447244af8f'),
('Consola de Videojuegos', 'Última generación de consola para gaming', 499.99, 'Gaming', 25, 'https://images.unsplash.com/photo-1486401899868-0e435ed85128'),
('Impresora 3D', 'Impresora 3D para prototipado rápido y hobby', 399.99, 'Impresión', 15, 'https://images.unsplash.com/photo-1524661135-423995f22d0b'),
('Router WiFi 6', 'Router de alta velocidad con la última tecnología WiFi', 199.99, 'Redes', 30, 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31'),
('Disco Duro Externo', 'Almacenamiento portátil de 2TB', 89.99, 'Almacenamiento', 40, 'https://images.unsplash.com/photo-1531492746076-161ca9bcad58'),
('Proyector 4K', 'Proyector de cine en casa con resolución 4K', 999.99, 'Video', 10, 'https://images.unsplash.com/photo-1478720568477-152d9b164e26'),
('Tarjeta Gráfica', 'GPU de alto rendimiento para gaming y diseño', 699.99, 'Componentes PC', 20, 'https://images.unsplash.com/photo-1591488320449-011701bb6704'),
('Micrófono USB', 'Micrófono de condensador para streaming y podcast', 129.99, 'Audio', 25, 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc'),
('Cargador Inalámbrico', 'Base de carga inalámbrica para smartphones', 39.99, 'Accesorios', 50, 'https://images.unsplash.com/photo-1622043945901-dc9858044d7a'),
('Webcam HD', 'Cámara web de alta definición para videoconferencias', 79.99, 'Periféricos', 35, 'https://images.unsplash.com/photo-1622959858115-dcccb902a24c'),
('Teclado Plegable', 'Teclado Bluetooth plegable para dispositivos móviles', 59.99, 'Accesorios', 30, 'https://images.unsplash.com/photo-1598662779094-110c2bad80b5'),
('Ratón Ergonómico', 'Ratón vertical para reducir la fatiga de la muñeca', 69.99, 'Periféricos', 40, 'https://images.unsplash.com/photo-1527814050087-3793815479db'),
('Dispositivo de Streaming', 'Reproductor multimedia para streaming en TV', 89.99, 'Video', 30, 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1'),
('Batería Externa', 'Powerbank de 20000mAh para carga rápida', 49.99, 'Accesorios', 60, 'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5'),
('Kit de Hogar Inteligente', 'Set de dispositivos para automatización del hogar', 299.99, 'Domótica', 20, 'https://images.unsplash.com/photo-1558002038-1055907df827'),
('Escáner Portátil', 'Escáner de documentos compacto y portátil', 129.99, 'Oficina', 15, 'https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6'),
('Gafas de Realidad Virtual', 'Dispositivo VR inmersivo para juegos y experiencias', 399.99, 'Realidad Virtual', 20, 'https://images.unsplash.com/photo-1622979135225-d2ba269cf1ac'),
('Servidor NAS', 'Almacenamiento en red para hogar u oficina pequeña', 349.99, 'Almacenamiento', 10, 'https://images.unsplash.com/photo-1601737487795-dab272f52420'),
('Lector de Libros Electrónicos', 'E-reader con pantalla de tinta electrónica', 129.99, 'Lectura', 35, 'https://images.unsplash.com/photo-1510166089176-b57564a542b1'),
('Adaptador USB-C Hub', 'Hub multiusos para portátiles con USB-C', 59.99, 'Accesorios', 45, 'https://images.unsplash.com/photo-1612696877544-9365bdc31b98');
-- Borrar los usuarios existentes
DELETE FROM users;

-- Insertar datos de ejemplo con contraseñas hasheadas
INSERT INTO users (username, email, password_hash, is_active, is_admin)
VALUES
('grdy', 'grdy@example.com', '$2b$12$hQlZp7SCm7mYRT8GpI7cSuEdmR8HpMycuOQmFMg0R5rYf0Z2BDAYu', TRUE, TRUE),
('user', 'user@example.com', '$2b$12$k6R/ju7k7v6fMf6G9lX8vOCexzhKUzO9ZrgmEmY8CMqYiwviyHKHq', TRUE, FALSE);
