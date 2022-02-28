# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Articlev2Model(models.Model):
    _name = 'dealerv2_app.articlev2_model'
    _inherit="dealer_app.article_model"
    _description = 'dealerv2_app.articlev2_app'

    articlev2_ids=fields.Many2one("dealerv2_app.brand_model",string="Brand")
