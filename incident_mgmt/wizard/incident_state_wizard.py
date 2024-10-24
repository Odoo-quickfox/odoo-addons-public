from odoo import api, models, fields, _
from odoo.exceptions import ValidationError, UserError

class TeamIncidentState(models.TransientModel):
    _name = "team.incidents.state"
    _description = "Team Incident State Change"

    @api.model
    def default_get(self, fields):
        result = super(TeamIncidentState, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        active_model = self.env.context.get('active_model')
        team_incidents = self.env['team.incidents'].sudo().browse(active_id)
        if not active_model == 'team.incidents' or not active_id:
            raise UserError(_('You cannot proceed with wrong data!'))

        result['team_incidents_id'] = self.env.context.get('active_id')
        return result

    team_incidents_id = fields.Many2one('team.incidents', 'Team Incidents', readonly=True, required=True)
    reason=fields.Text('Please mention a reason ',required=True)
    
    def action_confirm(self):
        if self.team_incidents_id:
            if self.env.context.get('resolve',False):   
                self.team_incidents_id.sudo().write({
                    'state':'resolved'
                })
                if self.reason:
                    message_body = f"""
                        <div style="background-color: #d4edda; padding: 10px; border-radius: 5px;">
                            <strong>Reason for Resolving this incident is:</strong><br/>
                            {self.reason}
                        </div>
                    """
                    self.team_incidents_id.message_post(body=f'Reason for Resolving this incident is:\n {self.reason}', message_type='notification')

            if self.env.context.get('cancel',False):   
                self.team_incidents_id.sudo().write({
                    'state':'cancelled'
                })
                if self.reason:
                    message_body = f"""
                        <div style="background-color: #d4edda; padding: 10px; border-radius: 5px;">
                            <strong>Reason for Cancelling this incident is:</strong><br/>
                            {self.reason}
                        </div>
                    """
                    self.team_incidents_id.message_post(body=f'Reason for Cancelling this incident is:  \n {self.reason}', message_type='notification')
            
        return True
