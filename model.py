import datetime
from flask_mongoengine import MongoEngine
from marshmallow import Schema, fields,pre_load,validate
from flask_marshmallow import Marshmallow
ma=Marshmallow()
db= MongoEngine()


class adddetail(db.Document):
    Product_Name=db.StringField()
    Vendor_Name=db.StringField()
    #Date_of_Purchase=db.DateTimeField()
    stock_id=db.StringField()
    Invoice_No=db.IntField()

    # meta = {'indexes': [
    #     {'fields': ['$Product_Name', "$Vendor_Name"],
    #      'default_language': 'english',
    #      'weights': {'Product_Name': 10, 'Vendor_Name': 2}
    #     }
    # ]}

class categories(db.Document):
    #Serial_No=db.IntField()
    Category_Name=db.StringField()
    # Last_updated = db.DateTimeField(verbose_name=u'Last_updated',required=True)

    # def save(self, *args, **kwargs):
    #     if not self.Last_updated:
    #          self.Last_updated = datetime.datetime.now()
    #     return super(categories, self).save(*args, **kwargs)
    
class categoryschema(ma.Schema):
    #Serial_No=fields.Integer()
    Category_Name=fields.String(required=True)
    


class add_details_schema(ma.Schema):
    Product_Name=fields.String()
    Vendor_Name=fields.String()
    #Date_of_Purchase=fields.DateTime()
    Stock_Id=fields.String()
    Invoice_No=fields.Int()
    

    
class Login(db.document):
    username=fields.String()
    password=fields.String()

    
    
    





