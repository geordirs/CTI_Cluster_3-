BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> bd91751cf99c

CREATE TABLE coupons (
    id SERIAL NOT NULL, 
    code VARCHAR, 
    discount_percent FLOAT, 
    is_active BOOLEAN, 
    valid_from TIMESTAMP WITH TIME ZONE, 
    valid_to TIMESTAMP WITH TIME ZONE, 
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
    PRIMARY KEY (id)
);

CREATE UNIQUE INDEX ix_coupons_code ON coupons (code);

CREATE INDEX ix_coupons_id ON coupons (id);

CREATE TABLE products (
    id SERIAL NOT NULL, 
    name VARCHAR, 
    description VARCHAR, 
    price FLOAT, 
    stock_quantity INTEGER, 
    low_stock_threshold INTEGER, 
    is_active BOOLEAN, 
    category VARCHAR, 
    image_url VARCHAR, 
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
    PRIMARY KEY (id)
);

CREATE INDEX idx_product_name_description ON products USING gin (to_tsvector('english', name), to_tsvector('english', description));

CREATE INDEX ix_products_category ON products (category);

CREATE INDEX ix_products_id ON products (id);

CREATE INDEX ix_products_name ON products (name);

CREATE TABLE users (
    id SERIAL NOT NULL, 
    username VARCHAR, 
    email VARCHAR, 
    password_hash VARCHAR, 
    is_active BOOLEAN, 
    is_admin BOOLEAN, 
    PRIMARY KEY (id)
);

CREATE UNIQUE INDEX ix_users_email ON users (email);

CREATE INDEX ix_users_id ON users (id);

CREATE UNIQUE INDEX ix_users_username ON users (username);

CREATE TABLE cart_items (
    id SERIAL NOT NULL, 
    user_id INTEGER, 
    product_id INTEGER, 
    quantity INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(product_id) REFERENCES products (id), 
    FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE INDEX ix_cart_items_id ON cart_items (id);

CREATE TABLE notifications (
    id SERIAL NOT NULL, 
    user_id INTEGER, 
    message VARCHAR, 
    is_read BOOLEAN, 
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
    PRIMARY KEY (id), 
    FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE INDEX ix_notifications_id ON notifications (id);

