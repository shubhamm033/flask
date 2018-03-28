from flask import request,jsonify
from flask_restful import Resource
from model import adddetail, db,categories, categoryschema, add_details_schema
import json


categories_schema= categoryschema(many=True)
categories_schema= categoryschema()

details_schema=add_details_schema(many=True)
details_schema=add_details_schema()
class Inventorymethods(Resource):
    def get(self, Category=None):

        
        if Category:
            details=adddetail.objects(Category=Category)
            return jsonify({'detail':details})
        else:
            details = adddetail.objects.all()
            print details
        # return jsonify(products)
            return jsonify({'detail': details})




    def post(self):
        json_data=request.get_json(force=True)
        if not json_data:
            return {'response':'no data provided' }
        data, errors =details_schema.load(json_data)
        if errors:
            return errors
        adddetail(**json_data).save()

        #result = details_schema.dump(category).data

        return { "status": 'success'}

    def search(self,query):
        document = adddetail.objects.search_text(query)
        print(document)






class Categorymethods(Resource):
    def get(self):
        all_categories = categories.objects.all()
        #data = categories_schema.load(all_categories)

        
        
        return jsonify({'response': all_categories})

    def post(self):
        json_data=request.get_json(force=True)
        if not json_data:
            return {'response':'no data provided' }
        data, errors = categories_schema.load(json_data)
        if errors:
            return errors
        category = categories.objects(Category_Name=data['Category_Name'])
        if category:
            return {'message': 'Category already exists'}
        
        category=categories(Category_Name=json_data['Category_Name'])
        categories(**json_data).save()

        result = categories_schema.dump(category).data

        return {"status": 'success', 'data':result}

class Loginmethods(Resource):

    def get(self):
        return jsonify({'response':'success'})

    def post(self):
        



            



    

        
        