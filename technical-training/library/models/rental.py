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

class Rental(models.Model):
    _name = 'library.rental'
    _description = 'Rented books'

    book_id = fields.Many2one('library.book', help = 'ID of rented books.')
    person_id = fields.Many2one('library.person', help = 'ID of person who rented books.')

    person_name = fields.Char(related='person_id.name', string = 'salut name :')

    startRentDate = fields.Date('First day of rent for a book')
    endRentDate = fields.Date('Last day of rent for a book')

