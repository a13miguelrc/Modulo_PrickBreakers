__author__ = 'PrickBreakers'

from openerp.osv import fields, orm

#Empleado





#FlotaFurgonetas

class Flota(orm.model):
    _name = 'flota'
    _colums = {
        'marca':fields.selection(('marca1', 'Volkswagen'), ('marca2', 'Ford'), ('marca3', 'Renault'), 'Marca'),
        'modelo':fields.selection(('modelo1', 'Caddy'), ('modelo2', 'Transit'), ('modelo3', 'Kangoo'), 'Modelo'),
        'matricula':fields.selection(('matric1', '6584-HMN'), ('matric1', '5327-HCD'), ('matric3', '2167-DLL')),
        'hora_salida':fields.date('Hora salida'),
        'hora_llegada':fields.date('Hora llegada')
    }
