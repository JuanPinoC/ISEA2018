# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Empleado(models.Model):
	_name = 'peti.empleado'

	name = fields.Char(string="Nombres y Apellidos")
	dni = fields.Char(string="DNI")
	cargo = fields.Char(string="Cargo")
	area = fields.Many2one('peti.area', string = "Área")
	tareas = fields.Many2many('peti.tarea')

class Recurso(models.Model):
	_name = 'peti.recurso'

	name = fields.Char(string="Nombre")
	tipo = fields.Char(string="Tipo")
	area = fields.Many2one('peti.area', string = "Área")
	tareas = fields.Many2many('peti.tarea')

class Area(models.Model):
	_name = 'peti.area'

	name = fields.Char(string="Nombre")
	descripcion = fields.Char(string="Descripción")
	empleados = fields.One2many('peti.empleado','area', string = "Empleados")
	recursos = fields.One2many('peti.recurso','area', string = "Recursos")

class Tarea(models.Model):
	_name = 'peti.tarea'

	name = fields.Char(string="Nombre")
	descripcion = fields.Char(string="Descripcion")
	horas = fields.Integer(string="Horas/Hombre")
	recursos = fields.Many2many('peti.recurso')
	empleados = fields.Many2many('peti.empleado')