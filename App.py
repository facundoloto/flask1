from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
mysql = MySQL()
app = Flask(__name__)

# Mysql Connection

app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'acme'
mysql.init_app(app)


# settings
app.secret_key = "key"

# routes
@app.route('/')
def Index(): #esta fucniona sirve para cargar todos los datos de la tabla user y enviarselas al index.html
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM user')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts = data)#renderiza html

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        contraseña = request.form['contraseña']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (Nombre,Apellido,Email,Contraseña) VALUES (%s,%s,%s,%s)", (nombre,apellido,email,contraseña))
        mysql.connection.commit()
        flash('usuario agregado')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM user WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        contraseña = request.form['contraseña']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE user
            SET Nombre = %s,
                Apellido = %s,
                Email = %s,
                Contraseña=%s
            WHERE id = %s
        """, (nombre,apellido,email,contraseña, id))
        flash('Usuario modificado')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM user WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Usuario eliminado')
    return redirect(url_for('Index'))

# starting the app
if __name__ == "__main__":
    app.run(port=5500, debug=True)
