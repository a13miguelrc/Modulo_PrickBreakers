__author__ = 'PrickBreakers'

from openerp.osv import fields, orm

#Empleado
class Empleado(orm.Model):
    _name = 'empleado'
    _columns = {
        'nombre':fields.char('Nombre',size=20),
        'apellidos':fields.char('Apellidos',size=50),
        'direccion':fields.char('Direcci�n',size=50),
        'fecha_nacimiento':fields.date('Fecha Nacimiento'),
        'telefono':fields.char('Tel�fono',size=9),
        'servicio_id':fields.one2many('servicio.codigo','servicio_id','Hoja_de_Servicio')
    }


#Servicio
class Servicio(orm.Model):
    _name = 'servicio'
    _columns = {
        'codigo':fields.integer('C�digo'),
        'tipo':fields.selection((('REP','Reparaci�n'), ('E','Entrega'), ('REC','Recogida')),'Tipo'),
        'ubicacion':fields.selection((('D','A Domicilio'), ('T','Taller')),'Ubicaci�n'),
        'electrodomestico':fields.char('Electrodom�stico',size=40),
        'descripcion':fields.char('Descripci�n',size=120),
        'direccion':fields.char('Direcci�n',size=50),
        'empleado_id':fields.many2one('empleado','Empleado')
    }
Servicio()


#FlotaFurgonetas
class Flota(orm.model):
    _name = 'flota'
    _colums = {
        'marca':fields.selection((('marca1', 'Volkswagen'), ('marca2', 'Ford'), ('marca3', 'Renault')), 'Marca'),
        'modelo':fields.selection((('modelo1', 'Caddy'), ('modelo2', 'Transit'), ('modelo3', 'Kangoo')), 'Modelo'),
        'matricula':fields.selection((('matric1', '6584-HMN'), ('matric1', '5327-HCD'), ('matric3', '2167-DLL')),'Matr�cula'),
        'hora_salida':fields.date('Hora salida'),
        'hora_llegada':fields.date('Hora llegada')
    }
