# =================================================================
# PROGRAMA: Sistema de Gestión de Inventario - Módulo Producto
# EVIDENCIA: GA7-220501096-AA3-EV01
# APRENDIZ: Dann Esteban Gutierrez Callejas
# DESCRIPCIÓN: Implementación de CRUD sincronizado con Diseño
# =================================================================

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de conexión basada en el Diagrama de Clases
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root", # <--- Coloca tu clave de MySQL
        database="inventiendas"
    )

@app.route('/')
def inicio():
    """ 
    Módulo de Consulta: Lista todos los productos registrados.
    Cumple con la visualización de la entidad PRODUCTO del diagrama.
    """
    try:
        db = conectar()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM producto ORDER BY id_producto DESC")
        mis_productos = cursor.fetchall()
        cursor.close()
        db.close()
        return render_template('index.html', productos=mis_productos)
    except mysql.connector.Error as err:
        return f"Error de conexión: {err}"

@app.route('/registrar', methods=['POST'])
def registrar():
    """ 
    CUMPLIMIENTO HU#1: Registrar productos con código de barras.
    CUMPLIMIENTO HU#3: Definir umbral de stock mínimo para alertas.
    """
    # Captura de datos desde el formulario web
    nombre = request.form['nombre']
    codigo = request.form['codigo_barra']
    cat = request.form['categoria']
    p_venta = request.form['precio_venta']
    p_compra = request.form['precio_compra']
    cantidad = request.form['stock']
    minimo = request.form['stock_minimo']
    id_negocio = 1 # ID por defecto para pruebas

    try:
        db = conectar()
        cursor = db.cursor()
        # Query SQL estructurada según la tabla PRODUCTO del diagrama
        sql = """INSERT INTO producto (id_negocio, nombre, codigo_barra, categoria, 
                 precio_compra, precio_venta, stock, stock_minimo) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (id_negocio, nombre, codigo, cat, p_compra, p_venta, cantidad, minimo)
        
        cursor.execute(sql, valores)
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('inicio'))
    except mysql.connector.Error as err:
        return f"Error al insertar: {err}"

@app.route('/eliminar/<int:id>')
def eliminar(id):
    """ Módulo de baja de productos (Borrado lógico/físico) """
    db = conectar()
    cursor = db.cursor()
    cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id,))
    db.commit()
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)