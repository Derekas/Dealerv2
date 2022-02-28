# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BrandModel(models.Model):
    _name = 'dealerv2_app.brand_model'
    
    _description = 'Brand_model'

    name = fields.Char(string="Name",required=True,index=True,help="Brand Name")
    country = fields.Char(string="Country",required=True,index=True,help="Brand Country")
    description = fields.Text()

    
    brand_id=fields.One2many("dealerv2_app.articlev2_model","articlev2_ids",string="Brand")

