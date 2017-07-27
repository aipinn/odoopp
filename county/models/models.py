# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Province(models.Model):
    _name = "county.province"

    name = fields.Char(string=u"省份名称", required=True)
    remark = fields.Text(string=u"备注")
    description = fields.Html(string=u"描述", strip_style=True)
    area = fields.Float(string=u"面积")
    code = fields.Char(string=u"省份代码")
    # Boolean
    isEdge = fields.Boolean(string=u"边界")
    active = fields.Boolean(default=True, string=u"是否显示")
    # 整型
    quantity = fields.Integer(string=u"人数")
    add_date = fields.Date(string=u"添加日期", default=fields.date.today(), copy=True)
    news_date = fields.Datetime(string=u"最新动态日期", default=fields.datetime.now())
    # 添加序列号为只读,在保存时自动生成
    seq = fields.Char(string=u'编号', default='New')

    # @api.model
    # def get_level(self):
    #     return [(0, u'直辖市'),(1,u'普通'),(2,u'自治区')]

    city_level = fields.Selection([
        (0, u'直辖市'),
        (1, u'普通'),
        (2, u'自治区')
    ], string=u"等级")

    admin_ids = fields.Many2one('res.users', string=u'管理员', default=lambda self: self.env.user)
    function = fields.Char(related='admin_ids.partner_id.function', string='职位', store=True, readonly=True)
    city_indexes = fields.One2many('county.city', 'city_index', string=u'城市信息')

    # m2m = fields.Many2many('res.partner', string=u'联系人')
    m2m = fields.Many2many('res.partner', 'county_province_res_allen_rel', 'province_id', 'partner_id', string='联系人')

    state = fields.Selection([
        ('draft', u'草稿'),
        ('review', u'等待审核'),
        ('down', u'已完成'),
        ('cancel', u'取消'),
    ], string=u'状态', default='draft')

    # 创建拦截及自动编号: 点击保存按钮时拦截点击事件对字段值进行修改
    @api.model
    def create(self, vals):
        # case 1. 修改area为某个值
        # vals['area'] = 666
        # print '打印当前界面元素'+vals,
        # result = super(Province,self).create(vals)
        # return result

        # case 2. 根据条件修改值
        # print  vals.get('county') + '333333333333'
        # if vals.get('county') == u'中国':
        #     vals['county'] = 'China'
        # result = super(Province, self).create(vals)
        # return result

        # case 3. 自动编码eg:订单
        print vals.get('seq')  # 因为是只读属性,所以无法传值,打印None
        if vals.get('seq', 'New') == 'New':
            print self.env['ir.sequence']
            print self.env['ir.sequence'].next_by_code(self._name)
            vals['seq'] = self.env['ir.sequence'].next_by_code('county.province') or 'New'
        result = super(Province, self).create(vals)
        return result

    @api.multi
    def write(self, vals):
        print vals, '1111111111'
        # 当人数超过一亿备注自动修改为:人口众多啊,啊啊啊啊啊
        if vals.has_key('quantity'):
            pass
            if vals['quantity'] > 100000000:
                vals['remark'] = u'人口众多啊,啊啊啊啊啊'
        return super(Province, self).write(vals)

    @api.multi
    def unlink(self):
        for order in self:
            # 超级管理员随意操作, 否则只有draft可以删除
            if self._uid == 1:
                pass
            else:
                if order.state != 'draft':
                    raise UserWarning('Draft order do not delete !')
        return super(Province, self).unlink()

    @api.multi
    def read(self, fields=None, load='_classic_read'):

        print u'I am coming !'
        print fields  # [u'name', u'isEdge', u'quantity', u'code', u'area', u'remark', u'add_date', u'news_date', u'admin_ids']
        # tree中只显示部分字段,form也一样
        # fields = [u'name', u'isEdge', u'quantity', u'code', u'area', u'remark']

        return super(Province, self).read(fields=fields, load=load)

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
    def action_search(self):
        pass

        # 浏览查看
        object = self.env['res.partner'].browse([1, 3, 4, 5])
        for obj in object:
            print  'name:' + obj.name
            print 'company name' + obj.company_id.name

            # 修改
            # object = self.env['county.province'].search([('name','=','湖南')])
            # value = {
            #     'name':'湖南省',
            #     'state':'cancel'
            # }
            # object.write(value)

            # 查询
            # object = self.env['ir.model'].search([],limit=5)
            # for obj in object:
            #     print obj.name

            # 创建一条记录
            # value = {
            #     'name':'香港',
            #     'county':'中国',
            #     'isEdge':'1'
            # }
            # self.env['county.province'].create(value)

    total = fields.Float(compute='_compute_total', string=u'GDP总计', )

    @api.depends('city_indexes.gdp')
    def _compute_total(self):
        acc = 0.00
        for record in self.city_indexes:
            acc += record.gdp

        self.total = acc


class City(models.Model):
    _name = "county.city"
    _log_access = False
    sequence = fields.Integer(string=u'排序', default=0, help='.')
    name = fields.Char(string=u"城市名称", required=True)
    postcode = fields.Char(string=u"邮编")

    city_index = fields.Many2one('county.province', string=u'省份', ondelete='cascade', copy=False, index=True)

    gdp = fields.Float(string='GDP', required=True, default=0.00)
