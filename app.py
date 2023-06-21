from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = ""
app.config["MYSQL_DATABASE_DB"] = "sitio"
mysql.init_app(app)


@app.route("/")
def inicio():
    return render_template("indexSitio.html")


@app.route("/libros")
def libros():
    return render_template("sitio/books.html")


@app.route("/nosotros")
def nosotros():
    return render_template("sitio/about.html")


@app.route("/admin")
def admin_index():
    return render_template("admin/indexAdmin.html")


@app.route("/admin/signin")
def admin_signin():
    return render_template("admin/login.html")


@app.route("/admin/libros", methods=["GET", "POST"])
def admin_libros():
    if request.method == "POST":
        # Handle the sign-in form submission
        # Perform authentication and redirect to appropriate page
        
        # Example: Redirect to "/admin/libros" after successful sign-in
        return redirect("/admin/libros")
    
    # Handle GET request for rendering the "/admin/libros" page
    conexion = mysql.connect()
    print(conexion)
    return render_template("admin/books.html")



@app.route("/admin/libros/guardar", methods=["POST"])
def admin_libros_guardar():
    nombre = request.form["txtNombre"]
    imagen = request.files["txtImagen"]
    url = request.form["txtUrl"]
    sql = "INSERT INTO `libros` (`id`, `nombre`, `imagen`, `url`) VALUES (NULL, %s, %s, %s);"
    datos = (nombre, imagen.filename, url)
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()

    # Obtener los datos guardados en la base de datos
    sql = "SELECT * FROM `libros`"
    cursor.execute(sql)
    libros = cursor.fetchall()

    return render_template("admin/books.html", libros=libros)


@app.route("/admin/libros/eliminar", methods=["POST"])
def admin_libros_eliminar():
    libro_id = request.form["id"]
    
    # Lógica para eliminar el libro con el ID proporcionado
    
    return redirect("/admin/libros")

@app.route("/admin/libros/eliminar-todo", methods=["POST"])
def admin_libros_eliminar_todo():
    eliminar_todo = request.form.get("eliminar_todo")
    
    if eliminar_todo == "true":
        # Lógica para eliminar todos los datos
        
        return redirect("/admin/libros")

###
###@app.route("/admin/libros/guardar", methods=["POST"])
###def admin_libros_guardar():
###    nombre = request.form["txtNombre"]
###    imagen = request.files["txtImagen"]
###    url = request.form["txtUrl"]
###    sql = "INSERT INTO `libros` (`id`, `nombre`, `imagen`, `url`) VALUES (NULL, %s, %s, %s);"
###    datos = (nombre, imagen.filename, url)
###    conexion = mysql.connect()
###    cursor = conexion.cursor()
###    cursor.execute(sql, datos)
###    conexion.commit()
###
###    print(nombre)
###    print(imagen)
###    print(url)
###
###    return render_template("admin/books.html")
###

if __name__ == "__main__":
    app.run(debug=True)
