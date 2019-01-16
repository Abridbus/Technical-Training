# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date, datetime

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

class Task(models.Model):
    _name = 'coopplanning.task'
    _description = 'Task Model'

    name = fields.Selection([
        (1, 'Loading truck'),
        (2, 'Handle the PoS'),
        (3, 'Distributing the Goods'),
        (4, 'Chatting with the customers'),
        (5, 'Learn to the cat how to read'),
        (6, 'Aquapiscine'),
        (7, '*Nothing*'),
    ], required = True, readonly = False)

    taskVolunteer_ids = fields.One2many('coopplanning.taskvolunteer', 'task_id', help = 'ID of TaskVolunteer')
    taskType = fields.Char()
    startDate = fields.Float()
    endDate = fields.Float()


class TaskVolunteer(models.Model):
    _name = 'coopplanning.taskvolunteer'
    _description = 'Tasks for Volunteers'

    #name = fields.Char(string='Task Volunteer', required = True )

    startDate = fields.Float(string = 'Date for start of task.')
    endDate = fields.Float(string = 'Date for end of task.')
    duration = 2.0 - 1.0

    task_id = fields.Many2one('coopplanning.task', help = 'ID of task')
    volunteer_id = fields.Many2one('coopplanning.volunteer', help = 'ID of Volunteer')
    
    """
    Date Type : (for later & duration is not going to be calculated like this !! Find how)
    startDate = fields.Date(string = 'Date for start of task.')
    endDate = fields

    #ToBeTested : 
    duration = endDate - startDate
    """