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

class Book(models.Model):
    _name = 'library.book'
    _description = 'Books'

    name = fields.Char(string='Name of a book', required = True, )
    authors = fields.Many2many('library.person',  string = '', help = 'Author(s) might have written multiples books. Many2many relationships with library.person')
    editionYear = fields.Integer('Year of edition', required = True) #Only expecting a year of edition
    ISBN = fields.Integer('Code integer ISBN', required = True)

    # /!\ If you need to access the data, better to specify it in the Person Model (even if it's not forced to do so)
    rental_ids = fields.One2many('library.rental', 'book_id', string='Book Rentals')
