# -*- coding: utf-8 -*-
from odoo import api, exceptions ,fields, models
import pudb
"""
    The citadel of the seven kingdoms, located in Oldtown would like to use Odoo to manage the training of its future maesters.\n",
    
    In this system, the citadel wants to create and edit classes, with different levels. \n",
    They would like to handle different sessions given by different maesters at different moments. \n",
    It would be nice to register the attendees of those sessions. \n",
    Maester Aemon thinks it would be a good idea to differentiate the sessions in preparation from the ones that will actually be given, as well as having a way to archive the sessions, so they can find what they need as quickly as you can find a book in the Citadel's Library, which is the largest in Westeros.\n",
    
    Hint: To have access to the models in the UI, you can add a menu from the models table in the UI in debug mode (go to Settings/Technical/Models, pick your model and click on Create a Menu).\n",
    Technical Hint: Do not forget to import the api, models and fields and your different files+\n",
    
"""
class Session(models.Model):
    """handle different sessions given by different maesters at different moments."""
    _name = 'openacademy.session'
    _inherit = ['mail.thread']
    _description = 'Session handled by maesters.'

    name = fields.Char(required = True, search = '_search_session_name')
    duration = fields.Integer(string = 'Duration of a session. Set by default at 60min', default = 60, search = '_search_session_duration', required = False)
    isGiven = fields.Boolean(default=True, help="Set true if session is currently given or ready to be given, True by default.") 
    isActive = fields.Boolean(default=True, help="Set true if session is currently active. True by default.")
    state = fields.Selection([('draft', "Draft"), ('confirmed', "Confirmed"), ('done', "Done")], default='draft')

    teacher_id = fields.Many2one('res.partner', string = "Teacher of a session")
    lecture_id = fields.Many2one('openacademy.lecture', ondelete = 'cascade', string = 'Lecture of a session', required = True )
    level = fields.Selection(related='lecture_id.level', readonly = True)
    
    attendee_ids = fields.Many2many('res.partner', string = 'Students following the lecture.')
    attendees_count = fields.Integer(compute='_count_attendees', string = 'number of attendees', store = True)
    maxSeats = fields.Integer(string = 'number max of seats', required = True)
    seats = fields.Float(compute='_check_taken_seats', store=True, string = 'number of seats taken')            

    @api.depends('maxSeats', 'attendee_ids')
    def _check_taken_seats(self):
        #pudb.set_trace()
        for session in self:
            if not session.maxSeats:
                session.seats = 0.0
            else:
                session.seats = 100*len(session.attendee_ids) / session.maxSeats

    @api.depends('attendee_ids')
    def _count_attendees(self):
        for session in self:
            session.attendees_count = len(session.attendee_ids)  

    def _warning(self, title, message):
        return {'warning': {
            'title':   title,
            'message': message,
        }}

    #Write in the chatter
    @api.multi
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
            rec.message_post(body="Session %s of the lecture %s reset to draft" % (rec.name, rec.lecture_id.name))
    
    #Write in the chatter
    @api.multi
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'
            rec.message_post(body="Session %s of the lecture %s confirmed" % (rec.name, rec.lecture_id.name))

    #Write in the chatter
    @api.multi
    def action_done(self):
        for rec in self:
            rec.state = 'done'
            rec.message_post(body="Session %s of the lecture %s done" % (rec.name, rec.lecture_id.name))

    #If more than 50% of person, switch state to confirm:
    def _auto_transition(self):
        for rec in self:
            if rec.seats >= 50.0 and rec.state == 'draft':
                rec.action_confirm()
    
    @api.multi
    def write(self, vals):
        res = super(Session, self).write(vals)
        for rec in self:
            rec._auto_transition()
        if vals.get('teacher_id'):
            self.message_subscribe([vals['teacher_id']])
        return res

    @api.model
    def create(self, vals):
        res = super(Session, self).create(vals)
        res._auto_transition()
        if vals.get('teacher_id'):
            res.message_subscribe([vals['teacher_id']])
        return res

class Lecture(models.Model):
    _name = "openacademy.lecture"
    _description="Lecture Model"
    

    name = fields.Char(string='Lecture for student', required=True, search='_search_lecture_name')
    description = fields.Text()

    teacher_id = fields.Many2one('res.partner', string = "Teacher of Lecture")
    session_ids = fields.One2many('openacademy.session', 'lecture_id', string='Sessions of a Lecture')
    session_count = fields.Integer(compute="_count_session", string="Count Sessions")
    attendees_count = fields.Integer(compute="_count_attendee", string="Count attendees")
    #test = len(self.mapped('session_ids.attendee_ids'))
	
    level = fields.Selection([
        ('1', 'Beginner'),
        ('2', 'Elementary'),
        ('3', 'Pre-Intermediate'),
        ('4', 'Intermediate'),
        ('5', 'Upper-Intermediate'),
        ('6', 'Advanced')
    ],string = 'Difficulty level of Lecture', required=True, search='_search_level', default='1')

    #PasClair?
    @api.multi
    def open_attendees(self):
        self.ensure_one()
        attendee_ids = self.session_ids.mapped('attendee_ids')
        return {
            'name':      'Attendees of %s' % (self.name),
            'type':      'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'domain':    [('id', 'in', attendee_ids.ids)],
        }

    @api.depends('session_ids')
    def _count_session(self):
        for course in self:
            course.session_count = len(course.session_ids)

    @api.depends('session_ids.attendees_count')
    def _count_attendee(self):
        for course in self:
            course.attendees_count = len(course.mapped('session_ids.attendee_ids'))
    
