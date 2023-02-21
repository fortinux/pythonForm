"""
[Add module documentation here]

Author: Fortinux
info@fortinux.com
Date: [Add date here]
"""


from flask import Flask, render_template, redirect, url_for
from forms import FacturaForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'


lista_facturas = [{
    'id': '0001',
    'fecha': '01/01/2023',
    'cliente': 'Juan Perez',
    'nif': '47045321P',
    'descripcion': 'Learn Python basics',
    'base': 100,
    'iva': 21,
    'total': 121,
    'available': True,
    'level': 'Beginner'
    }]


@app.route('/', methods=('GET', 'POST'))
def index():
    form = FacturaForm()
    if form.validate_on_submit():
        lista_facturas.append({'id': form.id.data,
                             'fecha': form.fecha.data,
                             'cliente': form.cliente.data,
                             'nif': form.nif.data,
                             'descripcion': form.descripcion.data,
                             'base': form.base.data,
                             'iva': form.iva.data,
                             'total': form.total.data,
                             'disponible': form.available.data,
                             'nivel': form.nivel.data
                             })
        return redirect(url_for('facturas'))
    return render_template('index.html', form=form)


@app.route('/facturas/')
def facturas():
    return render_template('facturas.html', lista_facturas=lista_facturas)


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
