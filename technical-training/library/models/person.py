# -*- coding: utf-8 -*-
from odoo import api, fields, models

"""
    Brussels' library wants to use Odoo to manage their books and customers. 
    The librarians want to record new books, with the standard information: authors, editors, year of edition, ISBN, etc. 
    For their customers, they want to manage them, create a new one, and include some standard information like name, address, emails, and other information. 
    They want to visualize what customers rented on their profile, as well as seeing the customers on the books without being able to change it.

    Hint: You want to be able have multiple authors for a book.
    Hint: You want to be able to have customers renting multiple books.

"""

class Person(models.Model):
    _name = 'library.person'
    _description = 'Person Model'

    
    name = fields.Char(required = True, search = '_search_person_name')
    isCustomer = fields.Boolean(default=True, help='Set true if person is a customer, True by default.')
    isAuthor = fields.Boolean(default = False, help = 'Set True is person is an author, False by default.')

    address = fields.Many2many('library.address', help="Multiples persons can have multiples address: shipping, home, work, ...")  
    authors = fields.Many2many('library.book',  string = '', help = 'Author(s) might have written multiples books. Many2many relationships with library.book')

    # /!\ If you need to access the data, better to specify it in the Person Model (even if it's not forced to do so)
    rental_ids = fields.One2many('library.rental', 'person_id', string='Person Rentals')


class Address(models.Model):
    _description = 'Address Model'
    _name = 'library.address'

    name = fields.Char('Name')
    surname = fields.Char('Surname')
    street = fields.Char('street1')
    zip = fields.Integer('zip')
    city = fields.Char('city')
    country = fields.Char('country')
    email = fields.Char('email')

    person = fields.Many2many('library.person', help="Multiples persons can have multiples address: shipping, home, work, ...", readonly = True)