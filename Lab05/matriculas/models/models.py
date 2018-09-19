# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class matriculas(models.Model):
#     _name = 'matriculas.matriculas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Area(models.Model):
     _name = 'matriculas.area'

     name = fields.Char(string="Nombre")
     curso_ids = fields.One2many('matriculas.curso','area_id', string="Cursos")

class Curso(models.Model):
     _name = 'matriculas.curso'

     name = fields.Char(string="Nombre")
     duracion = fields.Integer(string="Duracion")
     descripcion = fields.Text(string="Descripción")
     area_id = fields.Many2one('matriculas.area', string="Área")

class Matricula(models.Model):
     _name = 'matriculas.matricula'

     name = fields.Char()
     fecha_matricula = fields.Date(string="Fecha de matricula")
     alumno_id = fields.Many2one('matriculas.alumno', string="Alumno")
     curso_id = fields.Many2one('matriculas.curso', string="Módulo")

class Alumno(models.Model):
     _name = 'matriculas.alumno'

     name = fields.Char(string="Nombre y Apellidos")
     dni = fields.Char(string="DNI")
     fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
     celular = fields.Char(string="Celular")
     email = fields.Char(string="Email")
     matricula_ids = fields.One2many('matriculas.matricula', 'alumno_id', string="Matriculas del Alumno")