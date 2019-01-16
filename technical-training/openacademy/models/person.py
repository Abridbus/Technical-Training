# -*- coding: utf-8 -*-
from odoo import api, fields, models
"""
    The citadel of the seven kingdoms, located in Oldtown would like to use Odoo to manage the training of its future maesters.\n",
    
    In this system, the citadel wants to create and edit classes, with different levels. \n",
    They would like to handle different sessions given by different maesters at different moments. \n",
    It would be nice to register the attendees of those sessions. \n",
    Maester Aemon thinks it would be a good idea to differentiate the sessions in preparation from the ones that will actually be given, as well as having a way to archive the sessions, so they can find what they need as quickly as you can find a book in the Citadel's Library, which is the largest in Westeros.\n",
    
    Hint: To have access to the models in the UI, you can add a menu from the models table in the UI in debug mode (go to Settings/Technical/Models, pick your model and click on Create a Menu).\n",
    Technical Hint: Do not forget to import the api, models and fields and your different files+\n",
    
"""

class Person(models.Model):
    _description = 'Person Model'
    _inherit = "res.partner"
    
    #name = fields.Char(required = True, search = '_search_person_name')
    isInstructor = fields.Boolean(default=False, help="Set true if is Instructor, False default.")
    """Link session to Person"""
    session_ids = fields.Many2many("openacademy.session", string = 'Sessions', readonly=True)
