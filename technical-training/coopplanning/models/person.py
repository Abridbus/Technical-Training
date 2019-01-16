# -*- coding: utf-8 -*-
from odoo import api, fields, models
#from datetime import datetime

"""
A non profit organisation needs your help. 
They would like to use Odoo to organize the work of their volunteers. 
They are managing a cooperative shop selling local products. 
The cooperative split all the work in smaller tasks that are coming every week like loading a truck, handling the point of sale, distributing the goods, etc. 
They have various type of volunteers, some are able to take responsibilities for recurring tasks, some can only take over a task every now and then.
Not every task can be handled by only one person. In the end, every job has to be done.

They would like to have a system in which they can check day-to-day if they have enough volunteers. 
They would have recurring tasks and one-shot tasks handled by their volunteers. For now you can assume that every volunteer handles the task in a recurring way 2-3 hours per week at a time.

"""

class Volunteer(models.Model):
    _name = 'coopplanning.volunteer'
    _description = 'Volunteer Model'
    #_inherit = 'coopplanning.person'

    name = fields.Char(required = True, search = '_search_person_name')
    taskVolunteer_ids = fields.One2many('coopplanning.taskvolunteer','volunteer_id', help = 'ID of TaskVolunteer')
    address = fields.Many2many('coopplanning.address', help="Multiples persons can have multiples address: shipping, home, work, ...")  

"""
class Person(models.Model):
    _name = 'coopplanning.person'
    _description = 'Person Model'
    
    name = fields.Char(required = True, search = '_search_person_name')
    isCustomer = fields.Boolean(default=True, help='Set true if person is a customer, True by default.')

    address = fields.Many2many('library.address', help="Multiples persons can have multiples address: shipping, home, work, ...")  

"""

class Address(models.Model):
    _name = 'coopplanning.address'
    _description = 'Address Model'

    name = fields.Char('Name')
    surname = fields.Char('Surname')
    street = fields.Char('street1')
    zip = fields.Integer('zip')
    city = fields.Char('city')
    country = fields.Char('country')
    email = fields.Char('email')

    person = fields.Many2many('coopplanning.volunteer', help="Multiples persons can have multiples address: shipping, home, work, ...", readonly = True)