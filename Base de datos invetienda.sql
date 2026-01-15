USE inventiendas;

-- CREAR TABLA NEGOCIO
CREATE TABLE negocio (
  id_negocio INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL
);

-- CREAR TABLA ROL
CREATE TABLE rol (
  id_rol INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL
);

-- CREAR TABLA USUARIO
CREATE TABLE usuario (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  id_negocio INT NOT NULL,
  id_rol INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  estado TINYINT NOT NULL DEFAULT 1,
  FOREIGN KEY (id_negocio) REFERENCES negocio(id_negocio),
  FOREIGN KEY (id_rol) REFERENCES rol(id_rol)
);

-- CREAR TABLA PROVEEDOR
CREATE TABLE proveedor (
  id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
  id_negocio INT NOT NULL,
  nombre_empresa VARCHAR(100) NOT NULL,
  nit VARCHAR(50) NOT NULL,
  telefono VARCHAR(20),
  nombre_asesor VARCHAR(100),
  FOREIGN KEY (id_negocio) REFERENCES negocio(id_negocio)
);

-- CREAR TABLA PRODUCTO
CREATE TABLE producto (
  id_producto INT AUTO_INCREMENT PRIMARY KEY,
  id_negocio INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  codigo_barra VARCHAR(100) UNIQUE,
  categoria VARCHAR(100),
  precio_compra DECIMAL(10,2) NOT NULL,
  precio_venta DECIMAL(10,2) NOT NULL,
  stock INT NOT NULL DEFAULT 0,
  stock_minimo INT NOT NULL DEFAULT 5, -- <--- ESTA ES LA QUE FALTA
  FOREIGN KEY (id_negocio) REFERENCES negocio(id_negocio)
);

-- CREAR TABLA VENTA
CREATE TABLE venta (
  id_venta INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT NOT NULL,
  fecha DATETIME NOT NULL,
  total DECIMAL(12,2) NOT NULL,
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

-- CREAR TABLA DETALLE VENTA
CREATE TABLE detalle_venta (
  id_detalle INT AUTO_INCREMENT PRIMARY KEY,
  id_venta INT NOT NULL,
  id_producto INT NOT NULL,
  cantidad INT NOT NULL,
  precio_unitario DECIMAL(10,2) NOT NULL,
  subtotal DECIMAL(12,2) NOT NULL,
  FOREIGN KEY (id_venta) REFERENCES venta(id_venta),
  FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);
USE inventiendas;
INSERT INTO negocio (nombre) VALUES ('Negocio Demo');
INSERT INTO rol (nombre) VALUES
('Administrador'),
('Cajero'),
('Invitado');
INSERT INTO usuario (id_negocio, id_rol, nombre, correo, password, estado)
VALUES
(1, 1, 'Administrador del Sistema', 'admin@demo.com', '123456', 1);
INSERT INTO proveedor (id_negocio, nombre_empresa, nit, telefono, nombre_asesor)
VALUES
(1, 'Distribuidora López', '900123456', '3001234567', 'Carlos López'),
(1, 'Alimentos del Valle', '901987654', '3029876543', 'Ana Torres');
INSERT INTO producto (id_negocio, nombre, codigo_barra, categoria, precio_compra, precio_venta, stock, stock_minimo)
VALUES
(1, 'Arroz Diana 1KG', '7701234567890', 'Granos', 2500, 3500, 50, 10),
(1, 'Aceite Premier 1L', '7709876543210', 'Aceites', 8000, 10500, 20, 5),
(1, 'Atún Van Camp´s', '7701122334455', 'Enlatados', 3500, 5000, 30, 8);


USE inventiendas;
SELECT * FROM producto;
