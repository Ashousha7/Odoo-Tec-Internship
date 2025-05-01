from odoo import models, fields

class TaskItem(models.Model):
    _name = 'task.item'
    _description = 'Task Item'

    name = fields.Char(string="Title")
    description = fields.Text(string="Description")
