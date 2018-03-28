from flask import Blueprint
from flask_restful import Api
from details import Inventorymethods,Categorymethods
from model import adddetail,categories



api_bp= Blueprint('api',__name__)
api=Api(api_bp)


api.add_resource(Inventorymethods,'/adddetail')
api.add_resource(Inventorymethods,'/adddetail/<string:Category>',endpoint='adddetail')
api.add_resource(Categorymethods,'/categories',endpoint='categories')
