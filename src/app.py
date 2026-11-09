from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

def conectar_bd():
    for intento in range(10):
        try:
            conexion = mysql.connector.connect(
                host="db",
                user="root",
                password="123456",
                database="practica_db"
            )
            return conexion
        except mysql.connector.Error:
            print("Esperando a MySQL...")
            time.sleep(3)

    raise Exception("No se pudo conectar a MySQL")

@app.route("/")
def hola_mundo():
    conexion = conectar_bd()

    cursor = conexion.cursor()

    cursor.execute("SELECT 'Hola Mundo desde MySQL!'")
    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return f"""
        <h1>Hola Mundo!</h1>
        <h2>{resultado[0]}</h2>
        <p>Aplicación conectada correctamente a MySQL.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)