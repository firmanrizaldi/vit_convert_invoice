#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
import time

class convert_invoice(models.Model):

    _name = "vit.convert_invoice"
    name = fields.Char( required=True, string="Nama Debitur",  help="")
    peminjam = fields.Char( string="Nama Peminjam",  help="")
    buka_peminjam = fields.Char( string="Bunga Peminjam Pertahun ",  help="")
    jangka_waktu = fields.Char( string="Jangka Waktu Pinjaman (Bulan)",  help="")
    tgl_pencairan = fields.Date( string='Tanggal Pencairan',
        default=lambda self: time.strftime("%Y-%m-%d"))
    periode_peminjaman = fields.Date( string='Periode Pinjaman',
        default=lambda self: time.strftime("%Y-%m-%d"))
    mulai_pembayaran = fields.Integer( string="Mulai Pembayaran Pinjaman (Bulan)",  help="")
    bulan = fields.Integer( string="Bulan",  help="")
    periode = fields.Date( string='Periode',
        default=lambda self: time.strftime("%Y-%m-%d"))
    saldo_awal = fields.Float( string="Saldo awal",  help="")
    pokok = fields.Float( string="Pokok",  help="")
    bunga = fields.Float( string="Bunga",  help="")
    saldo_akhir = fields.Float( string="Saldo Akhir",  help="")
    status = fields.Char( string="Status",  help="")
    tanggal = fields.Date( string='Tanggal',
        default=lambda self: time.strftime("%Y-%m-%d"))
    is_invoice = fields.Boolean( string="Is invoice",  help="")


    @api.model
    def convert_invoice(self,values):
        # Mengambil Object
        object_convert = self.env['vit.convert_invoice']
        object_invoice = self.env['account.invoice']
        object_partner = self.env['res.partner']
        object_account = self.env['account.account'] #COA
        object_product = self.env['product.product']

        # Search record pada object
        records = object_convert.search([('status', '=', 'OPEN'), ('is_invoice', '=', False)])  # kondisi search

        for record in records:
            partner_id      = object_partner.search([('name', '=', record.name)])
            product_pokok   = object_product.search([('name', '=', 'Produk Pokok')])
            product_cicilan = object_product.search([('name', '=', 'Produk Cicilan')])
            account_pokok   = product_pokok.property_account_income_id
            account_cicilan = product_cicilan.property_account_income_id

            invoice_line_ids = [
                (0, 0, {
                    'product_id'    : product_pokok.id,  # product_id dari variabel search object_product
                    'name'          : product_pokok.name,
                    'quantity'      : 1,
                    'price_unit'    : record.pokok,
                    'account_id'    : account_pokok.id,
                }),
                (0, 0, {
                    'product_id'    : product_cicilan.id,
                    'name'          : product_cicilan.name,
                    'quantity'      : 1,
                    'price_unit'    : record.pokok,
                    'account_id'    : account_cicilan.id,
                }),
            ]

            data = {
                'partner_id'      : partner_id.id,
                'date_invoice'    : record.periode,
                'invoice_line_ids': invoice_line_ids,
            }
            object_invoice.create(data)
            record.is_invoice=True


