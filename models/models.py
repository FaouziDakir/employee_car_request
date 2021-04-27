# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class employee_car_request(models.Model):
#     _name = 'employee_car_request.employee_car_request'
#     _description = 'employee_car_request.employee_car_request'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
