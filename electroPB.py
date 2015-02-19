__author__ = 'PrickBreakers'

from openerp.osv import fields, orm

#Empleado
class Empleado(orm.Model):
    _name = 'empleado'
    _columns = {
        'nombre':fields.char('Nombre',size=20),
        'apellidos':fields.char('Apellidos',size=50),
        'direccion':fields.char('Direccion',size=50),
        'fecha_nacimiento':fields.date('Fecha Nacimiento'),
        'telefono':fields.char('Telefono',size=9),
        'servicio_id':fields.one2many('servicio.codigo','servicio_id','Hoja_de_Servicio')
    }


#Servicio
class Servicio(orm.Model):
    _name = 'servicio'
    _columns = {
        'codigo':fields.integer('Codigo'),
        'tipo':fields.selection((('REP','Reparacion'), ('E','Entrega'), ('REC','Recogida')),'Tipo'),
        'ubicacion':fields.selection((('D','A Domicilio'), ('T','Taller')),'Ubicacion'),
        'electrodomestico':fields.char('Electrodomestico',size=40),
        'descripcion':fields.char('Descripcion',size=120),
        'direccion':fields.char('Direccion',size=50),
        'empleado_id':fields.many2one('empleado','Empleado')
    }
Servicio()


#FlotaFurgonetas
class Furgoneta(orm.model):
    _name = 'furgoneta'
    _colums = {
        'marca':fields.selection((('marca1', 'Volkswagen'), ('marca2', 'Ford'), ('marca3', 'Renault')), 'Marca'),
        'modelo':fields.selection((('modelo1', 'Caddy'), ('modelo2', 'Transit'), ('modelo3', 'Kangoo')), 'Modelo'),
        'matricula':fields.selection((('matric1', '6584-HMN'), ('matric1', '5327-HCD'), ('matric3', '2167-DLL')),'Matricula'),
        'hora_salida':fields.date('Hora salida'),
        'hora_llegada':fields.date('Hora llegada'),
        'usuario': fields.many2one('empleado','Usuario', ondelete='cascade')
    }
