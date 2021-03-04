# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class VisitController(http.Controller):

    @http.route('/api/visits', auth='public', method=['GET'], csrf=False)
    def get_visits(self, **kw):
        try:
            visits = http.request.env['custom_crm.visit'].sudo().search_read([], ['id', 'name', 'customer', 'done'])
            res = json.dumps(visits, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    @http.route('/api/ws001ok', auth='public', method=['GET'], csrf=False)
    def get_ws001ok(self, **kw):
        try:
			res = '{"Token": "20210219120000", "RespCode":0, "RespMessage":"OC recibidas correctamente"}'
            print('res: ', str(res))
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
			print('error: ', str(e))
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=500)
			
    @http.route('/api/ws001error', auth='public', method=['GET'], csrf=False)
    def get_ws001error(self, **kw):
        try:
			res = '{"Token": "20210219120000", "RespCode":-1, "RespMessage":"Error de conexión"}'
            print('res: ', str(res))
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
			print('error: ', str(e))
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=500)

