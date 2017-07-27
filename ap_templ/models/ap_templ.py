# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ap_templ(models.Model):
    _name = 'ap.templ'
    _description = u'模板'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    name = fields.Char(string=u'名称')
    active = fields.Boolean(string=u'有效', default=True)
    date = fields.Date(string=u'日期')

    city = fields.Char(string=u'城市')
    postcode = fields.Char(string=u'邮编')
    province = fields.Char(string=u'省份')
    image = fields.Binary(string=u'图片')

    state = fields.Selection([
        ('draft', u'草稿'),
        ('review', u'等待审核'),
        ('down', u'已完成'),
        ('send', u'发送邮件'),
        ('cancel', u'取消')
    ], string='Status', index=True, realonly=True, default='draft',
        track_visibility='onchange', copy=False,
        help=u" * 'draft' 制单.\n"
             u" * 'review' 制单完成后提交审核.\n"
             u" * 'down' 主管部门审核.\n"
             u" * 'send' 是否发送邮件.\n"
             u" * 'cancel' 取消制单'.")

    @api.multi
    def action_draft(self):
        self.write({'state': 'draft'})

    @api.multi
    def action_down(self):
        self.write({'state': 'down'})


    @api.multi
    def action_cancel(self):
        self.write({'state': 'cancel'})


    @api.multi
    def action_review(self):
        self.write({'state': 'review'})


    @api.multi
    def action_box(self):
        self.write({'state': 'draft'})

class ap_templ_sub(models.Model):
    _name = "ap.templ.sub"
    _description = u'模板sub'

    name = fields.Char(string=u'名称sub')



