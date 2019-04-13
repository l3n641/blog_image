from flask import Blueprint, render_template, jsonify
from flask import request
from app.constants import DEFAULT_PAGE
from app.servives import image_srv
from flask_restful import fields, marshal

image_bp = Blueprint('img_online', __name__, template_folder='templates', url_prefix='/')


@image_bp.route('/')
def index():
    page = int(request.args.get('page') or DEFAULT_PAGE)
    datas = image_srv.get_list(order={'img_id': "desc"})
    return render_template('index.html', datas=datas)


@image_bp.route('image')
def image():
    page = int(request.args.get('page') or DEFAULT_PAGE)
    datas = image_srv.get_list(order={'img_id': "desc"}, page=page)
    data_format = {
        "real_url": fields.String(attribute="real_url"),

    }
    return jsonify(marshal(datas.items, data_format))
