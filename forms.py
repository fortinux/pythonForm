#!/user/bin/env python3
"""
[Add module documentation here]

Author: Fortinux
info@fortinux.com
Date: [Add date here]
"""


from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length


"""
Clase FacturaForm
La clase FacturaForm crea un formulario para rellenar una factura 
"""


class FacturaForm(FlaskForm):
    id = StringField('ID', validators=[InputRequired(),
                                       Length(min=1)])
    fecha = StringField('Fecha', validators=[InputRequired(),
                                             Length(min=3)])
    cliente = StringField('Cliente', validators=[InputRequired(),
                                                 Length(min=3, max=100)])
    nif = StringField('NIF / CIF', validators=[InputRequired(),
                                               Length(max=9)])
    descripcion = TextAreaField('Productos y servicios',
                                validators=[InputRequired(),
                                            Length(max=200)])
    base = IntegerField('Base', validators=[InputRequired()])
    iva = IntegerField('Iva', validators=[InputRequired()])
    total = IntegerField('Total', validators=[InputRequired()])
    nivel = RadioField('Nivel',
                       choices=['Básico', 'Intermedio', 'Preferencial'],
                       validators=[InputRequired()])
    disponible = BooleanField('Disponible', default='checked')
