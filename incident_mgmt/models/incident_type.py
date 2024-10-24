from odoo import models, fields, api


class IncidentType(models.Model):
    _name = "incident.type"
    _description = "Incident Type"

    name = fields.Char(string="Name", required=True)

        
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Incident Type with this name already exists!'),
    ]
