from odoo import models, fields, api, exceptions

class wizard(models.TransientModel):
    _name = "openacademy.wizard"
    _description = "Wizard to add attendees to sessionh."

    session_id = fields.Many2one("openacademy.session", string = "Sessions", required = True)
    attendee_ids = fields.Many2many("res.partner", string=" Attendees")

    #??
    @api.model
    def default_get(self, fields):
        res = super(Wizard, self).default_get(fields)
        res.update({'attendee_ids': [(6, 0, self._context.get('active_ids', []))]})
        return res

    @api.model
    def create(self, vals):
        res = super(Wizard, self).create(vals)
        return res

    @api.multi
    def subscribe(self):
        for session in self.session_id:
            session.attendee_ids |= self.attendee_ids
        return {}