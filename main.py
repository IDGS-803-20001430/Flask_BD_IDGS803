from flask import Flask,render_template,request,Response
from flask_wtf.csrf import CSRFProtect
from flask import redirect
from flask import g
from config import DevelopmentConfig
from flask import flash
import forms

from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'),404


@app.route("/index")
def index():
    g.nombre='Daniel'
    escuela="UTL!!!"
    alumnos=["Mario","Pedro","Luis","Dario"]
    return render_template("index.html",escuela=escuela,alumnos=alumnos)


@app.route("/alumnos",methods=["GET","POST"])
def alum():
    nom=""
    apa=""
    ama=""
    mensaje = ""
    alum_form=forms.UsersForm(request.form)
    if request.method=='POST' and alum_form.validate():
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)

        print("NOMBRE: {}".format(nom))
        print("APATERNO: {}".format(apa))
        print("AMATERNO: {}".format(ama))

    return render_template("alumnos.html", form=alum_form, nom=nom, apa=apa, ama=ama)

if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()