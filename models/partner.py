from odoo import models, fields


class Partner(models.Model):
    _name = "partner"

    name = fields.Char(required=1)
    tasks_ids = fields.Many2many('todo')
    id = fields.Char()
    email = fields.Char()

    _sql_constraints = [
        ('unique_name', 'unique (name)', 'Name must be unique')
    ]
