from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Función para establecer conexión con la base de datos MySQL
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root", 
        database="inventiendas"
    )

@app.route('/')
def inicio():
    """ Módulo de Consulta: Lista todos los productos y sus atributos completos """
    db = conectar()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM producto ORDER BY id_producto DESC")
    mis_productos = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('index.html', productos=mis_productos)

@app.route('/registrar', methods=['POST'])
def registrar():
    """ 
    Módulo de Registro (HU#1): Captura todos los campos requeridos en el diseño.
    Incluye: Nombre, Código de Barra, Categoría, Precios y Stocks.
    """
    nombre = request.form['nombre']
    codigo = request.form['codigo_barra']
    cat = request.form['categoria']
    p_compra = request.form['precio_compra']
    p_venta = request.form['precio_venta']
    stock = request.form['stock']
    minimo = request.form['stock_minimo']
    
    db = conectar()
    cursor = db.cursor()
    # Inserción alineada con la tabla PRODUCTO del diagrama de clases
    sql = """INSERT INTO producto (id_negocio, nombre, codigo_barra, categoria, precio_compra, precio_venta, stock, stock_minimo) 
            VALUES (1, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (nombre, codigo, cat, p_compra, p_venta, stock, minimo))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    """ Módulo de Actualización: Modifica los datos existentes del producto seleccionado """
    db = conectar()
    cursor = db.cursor()
    sql = """UPDATE producto SET nombre=%s, codigo_barra=%s, categoria=%s, precio_compra=%s, precio_venta=%s, stock=%s, stock_minimo=%s 
             WHERE id_producto=%s"""
    cursor.execute(sql, (request.form['nombre'], request.form['codigo_barra'], request.form['categoria'], 
                         request.form['precio_compra'], request.form['precio_venta'], 
                         request.form['stock'], request.form['stock_minimo'], id))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('inicio'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    """ Módulo de Eliminación: Borra el registro de la base de datos por su ID """
    db = conectar()
    cursor = db.cursor()
    cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id,))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)