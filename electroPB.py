from openerp.osv import fields, orm

#Empleado
class Empleado(orm.Model):
    _name = 'empleados.empleado'
    _columns = {
        'nif': fields.char('NIF', size=9, required=True),
        'nombre': fields.char('Nombre', size=20),
        'apellidos': fields.char('Apellidos', size=50),
        'direccion': fields.char('Direccion', size=50),
        'fecha_nacimiento': fields.date('Fecha Nacimiento'),
        'telefono': fields.char('Telefono', size=9),
        'image': fields.binary('Imagen', help='Seleccionar imagen aqui')
    }
    # Orden para que nos muestre primero las ultimas personas
    _order = 'id desc'

    # Restriccion unica al campo NIF
    _sql_constraints = [
        ('nif_unique', 'unique(nif)', 'El NIF debe ser unico'),
    ]
Empleado()

#FlotaFurgonetas
class Furgoneta(orm.model):
    _name = 'furgonetas.furgoneta'
    _colums = {
        'marca':fields.selection((('marca1', 'Volkswagen'), ('marca2', 'Ford'), ('marca3', 'Renault')), 'Marca'),
        'modelo':fields.selection((('modelo1', 'Caddy'), ('modelo2', 'Transit'), ('modelo3', 'Kangoo')), 'Modelo'),
        'matricula':fields.selection((('matric1', '6584-HMN'), ('matric1', '5327-HCD'), ('matric3', '2167-DLL')),'Matricula')
    }
Furgoneta()

#HojaDeServicio
#class HojaServicio(orm.Model):
#    _name = 'hojas.hoja'
#    _columns = {
#        'empleado_id':fields.many2one('empleados.empleado','Empleado'),
#        'hora_salida':fields.date('Hora salida'),
#        'hora_llegada':fields.date('Hora llegada'),
#        'furgoneta_id':fields.many2one('furgonetas.furgoneta','Furgoneta'),
#        'servicio_id':fields.one2manyfields.one2many('servicios.servicio.descripcion','servicios.servicio_id','Servicios')
#    }
#HojaServicio()

#Servicio
#class Servicio(orm.Model):
#   _name = 'servicios.servicio'
#    _columns = {
#        'codigo':fields.integer('Codigo'),
#        'tipo':fields.selection((('REP','Reparacion'), ('E','Entrega'), ('REC','Recogida')),'Tipo'),
#        'ubicacion':fields.selection((('D','A Domicilio'), ('T','Taller')),'Ubicacion'),
#        'electrodomestico':fields.char('Electrodomestico',size=40),
#        'descripcion':fields.char('Descripcion',size=120),
#        'direccion':fields.char('Direccion',size=50),
#    }
#Servicio()