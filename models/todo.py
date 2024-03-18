from odoo import models, fields, api


class ToDo(models.Model):
    _name = "todo"
    _description = 'Task Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    task_name = fields.Char(required=1, default='new')
    assign_to = fields.Many2many('partner')
    id = fields.Integer()
    description = fields.Text()
    due_date = fields.Date()
    state = fields.Selection([
        ('new','New'),
        ('in_progress','In_Progress'),
        ('completed','Completed'),
    ],default='new')
    line_ids = fields.One2many('todo.line', 'todo_id')




    def action_new(self):
        for rec in self:
            print("inside new action")
            # this is a documontation
            rec.state = 'new'
    def action_in_progress(self):
        for rec in self:
            print("inside in_progress action") #logic
            #we will use write method write use dictionary to set state = pending
            rec.write({
                'state':'in_progress'
            })
    def action_completed(self):
        for rec in self:
            print("inside completed action")
            rec.state = 'completed'

class ToDoLine(models.Model):
    _name = "todo.line"
    todo_id = fields.Many2one('todo')
    inquiry = fields.Char()

'''
@api.onchange('id')
    def _compute_auto(self):
        for rec in self:
            rec.id += 1
'''