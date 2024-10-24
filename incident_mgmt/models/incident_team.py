# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _


class IncidentTeam(models.Model):
    _name = 'incident.team'
    _inherit=['mail.thread','mail.activity.mixin'] 
    _description = 'Incident Team'
    
    name = fields.Char(string="Name", required=True)
    department_id=fields.Many2one('hr.department', string="Department")
    manager_id=fields.Many2one('res.users', string="Manager",default=lambda self: self.env.user)
    parent_id=fields.Many2one('incident.team', string="Parent Team")
    description=fields.Text("Description")
    members_ids=fields.Many2many('res.users', string="Members")
    active=fields.Boolean("Active",default=True)
    child_ids = fields.One2many('incident.team', 'parent_id', string="Child Teams")
    incidents_ids = fields.One2many('team.incidents', 'team_id', string="Teams Incidents")
    incidents_count = fields.Integer(string="Incidents Count",readonly=True, compute='_compute_incidents_count', store=True)
    
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Incident Team with this name already exists!'),
    ]
    
    
    @api.depends('incidents_ids','child_ids')
    def _compute_incidents_count(self):
        for team in self:
            team.incidents_count = len(team.incidents_ids)

    def projects_action(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'incidents',
            'view_mode': 'list,form',
            'res_model': 'team.incidents',
            'domain': [('team_id', '=', self.id)],
            'context': {'default_team_id': self.id}
        }

    def toggle_active(self):
        for team in self:
            team.active = not team.active