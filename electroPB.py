from openerp.osv import fields, orm, osv

#Empleado
class Empleados(osv.Model):
    _name = 'hr.employee'
    _inherit='hr.employee'
    _columns = {
        'hojas_servicio_ids':fields.one2many('hojas.hoja','empleado_id','Hojas de Servicio')
    }
Empleados()

#FlotaFurgonetas
#SELECTION_LIST_1 = (('MV1','Caddy'), ('MV2','Transporter'))
#SELECTION_LIST_2 = (('MF1','Transit'), ('MF2','Tourneo'))
#SELECTION_LIST_3 = (('MR1','Kangoo'), ('MR2','Traffic'))
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
        'electrodomestico':fields.char('Electrodomestico',size=40),
        'descripcion':fields.char('Descripcion',size=120),
        'reparado':fields.boolean('Reparado'),
        'direccion':fields.char('Direccion',size=50),
        'hoja_id': fields.many2one('hojas.hoja', 'Hoja de Servicio'),
        'cliente_id':fields.many2one('res.partner','Cliente')
    }
Servicio()

#HojaDeServicio
class HojaServicio(orm.Model):
    _name = 'hojas.hoja'
    _columns = {
        'empleado_id':fields.many2one('hr.employee','Empleado'),
        'hora_salida':fields.datetime('Hora salida'),
        'hora_llegada':fields.datetime('Hora llegada'),
        'furgoneta_id':fields.many2one('furgonetas.furgoneta','Furgoneta'),
        'servicio_ids':fields.one2many('servicios.servicio','hoja_id','Servicios')
    }
HojaServicio()

#Clientes
class Cliente(osv.Model):
    _name = 'res.partner'
    _inherit='res.partner'
    _columns = {
        'servicio_ids':fields.one2many('servicios.servicio','cliente_id','Servicios')
    }
Cliente()
