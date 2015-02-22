from openerp.osv import fields, orm

#Empleado
class Empleado(orm.Model):
    _name = 'empleados.empleado'
    _rec_name = 'nombre' #Indica que campo es el que guarda para mostrar por defecto
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

SELECTION_LIST_1 = (('MV1','Caddy'), ('MV2','Transporter'))
SELECTION_LIST_2 = (('MF1','Transit'), ('MF2','Tourneo'))
SELECTION_LIST_3 = (('MR1','Kangoo'), ('MR2','Traffic'))

class Furgoneta(orm.Model):
    _name = 'furgonetas.furgoneta'
    _rec_name = 'modelo'
    _columns = {
        'marca':fields.selection((('marca1', 'Volkswagen'), ('marca2', 'Ford'), ('marca3', 'Renault')), 'Marca'),
        'modelo':fields.char('Modelo',size=20),
        'matricula':fields.char('Matricula', size=8),
        'image': fields.binary('Imagen', help='Seleccionar imagen aqui')
    }
    def _set_list_data(self, cr, uid, ids, marca):
        if marca == 'marca1':
            v = {'modelo': 'Caddy'}
            return {'value': v}
        elif marca == 'marca2':
            v = {'modelo': 'Transit'}
            return {'value': v}
        elif marca == 'marca3':
            v = {'modelo': 'Kangoo'}
            return {'value': v}
Furgoneta()

#Servicio
class Servicio(orm.Model):
    _name = 'servicios.servicio'
    _rec_name = 'codigo'
    _columns = {
        'codigo':fields.integer('Codigo'),
        'tipo':fields.selection((('REP','Reparacion'), ('E','Entrega'), ('REC','Recogida')),'Tipo'),
        'ubicacion':fields.selection((('D','A Domicilio'), ('T','Taller')),'Ubicacion'),
        'electrodomestico':fields.char('Electrodomestico',size=40),
        'descripcion':fields.char('Descripcion',size=120),
        'direccion':fields.char('Direccion',size=50),
        'hoja_id': fields.many2one('hojas.hoja', 'Hoja de Servicio')
    }
Servicio()

#HojaDeServicio
class HojaServicio(orm.Model):
    _name = 'hojas.hoja'
    _columns = {
        'empleado_id':fields.many2one('empleados.empleado','Empleado'),
        'hora_salida':fields.date('Hora salida'),
        'hora_llegada':fields.date('Hora llegada'),
        'furgoneta_id':fields.many2one('furgonetas.furgoneta','Furgoneta'),
        'servicio_ids':fields.one2many('servicios.servicio','hoja_id','Servicios')
    }
HojaServicio()


