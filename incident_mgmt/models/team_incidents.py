# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _


class TeamIncidents(models.Model):
    _name = 'team.incidents'
    _inherit=['mail.thread','mail.activity.mixin'] 
    _description = 'Team Incident'
    
    name = fields.Char(string="Incident Title", required=True)
    team_id=fields.Many2one('incident.team', string="Team")
    involved_user_id=fields.Many2one('res.users', string="Person Involved")
    incident_type_id=fields.Many2one('incident.type', string="Type of Incident")
    attention_type=fields.Selection(string="How did the incident come to your attention?", selection=[('involved', 'Was Involved'), ('reported', 'Reported to me')],
    default='involved'
    )
    description=fields.Text("Description")
    active=fields.Boolean("Active",default=True)
    incident_date=fields.Date(string="Incident Date",default=fields.Date.today())
    state=fields.Selection(string="Status", selection=[('open', 'Open'), ('cancelled', 'Cancelled'),('resolved','Resolved')],default='open')    


    def print_followers(self):
        for incident in self:
            print(self.env.user.partner_id)
            print("###################")
            print(incident.name)
            followers = incident.message_follower_ids
            follower_names = followers.mapped('name')
            # print(followers in [self.env.user.partner_id.id])
            print(".....................")
            print([self.env.user.partner_id.id])
            print(",,,,,,,,,,,,,,,,,,,,,,,,")
            print(self.env.user.partner_id.ids)
            print(followers)  