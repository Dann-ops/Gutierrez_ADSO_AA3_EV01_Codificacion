from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Función para conectar a la base de datos
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root", # <--- Reemplaza con tu contraseña
        database="inventiendas"
    )

@app.route('/')
def inicio():
    try:
        db = conectar()
        # Usamos dictionary=True para que los resultados sean fáciles de leer en el HTML
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM producto ORDER BY id_producto DESC")
        mis_productos = cursor.fetchall()
        cursor.close()
        db.close()
        return render_template('index.html', productos=mis_productos)
    except mysql.connector.Error as err:
        return f"<h1>Error de conexión: {err}</h1>"

@app.route('/registrar', methods=['POST'])
def registrar():
    # Recibimos los datos del formulario HTML
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    p_compra = request.form['precio_compra']
    p_venta = request.form['precio_venta']
    stock = request.form['stock']
    id_negocio = 1 # Usamos el ID del negocio demo que creaste en Workbench

    try:
        db = conectar()
        cursor = db.cursor()
        
        # Sentencia SQL según tu estructura de tabla
        sql = """INSERT INTO producto (id_negocio, nombre, categoria, precio_compra, precio_venta, stock) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (id_negocio, nombre, categoria, p_compra, p_venta, stock)
        
        cursor.execute(sql, valores)
        db.commit() # Importante para guardar los cambios
        
        cursor.close()
        db.close()
        # Después de guardar, regresamos a la página principal para ver el cambio
        return redirect(url_for('inicio'))
    
    except mysql.connector.Error as err:
        return f"<h1>Error al guardar: {err}</h1><a href='/'>Regresar</a>"

@app.route('/eliminar/<int:id>')
def eliminar(id):
    try:
        db = conectar()
        cursor = db.cursor()
        cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id,))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('inicio'))
    except mysql.connector.Error as err:
        return f"Error al eliminar: {err}"

@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    # Recibimos todos los datos posibles para actualizar
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    p_compra = request.form['precio_compra']
    p_venta = request.form['precio_venta']
    stock = request.form['stock']
    
    try:
        db = conectar()
        cursor = db.cursor()
        # SQL que actualiza todos los campos del producto seleccionado
        sql = """UPDATE producto 
                 SET nombre = %s, categoria = %s, precio_compra = %s, precio_venta = %s, stock = %s 
                 WHERE id_producto = %s"""
        valores = (nombre, categoria, p_compra, p_venta, stock, id)
        
        cursor.execute(sql, valores)
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('inicio'))
    except mysql.connector.Error as err:
        return f"Error al actualizar: {err}"

if __name__ == '__main__':
    app.run(debug=True)