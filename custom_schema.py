import colander
import json

from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)


class DisplayAnswerObject(colander.MappingSchema):
    nam = colander.SchemaNode(colander.String())
    answer = colander.SchemaNode(colander.String())

# class displayanswerobj(colander.MappingSchema):
#     displayanswe = DisplayAnswerObject()

class Custom_string(colander.SchemaType):


    def __init__(self, DisplayAnswerObject, encoding=None, allow_empty=False):
        self.objec = DisplayAnswerObject
        # self.objec 
        self.encoding = encoding
        self.allow_empty = allow_empty

    def serialize(self, node, appstruct):
        if appstruct is None:
            return None

        try:
            result = appstruct
            if isinstance(result, dict):
                print("ser is dict")
                return self.objec.serialize(result)

            # if not isinstance(result, str):
            #     result = str(result)

            # token = f.encrypt(result.encode())
            # print(token)
            return result
        except Exception as e:
            raise e
            

    def deserialize(self, node, cstruct):
        if cstruct == '' and self.allow_empty:
            return ''

        try:
            if isinstance(cstruct, (str)):
                print("string")
                return cstruct
            
            if isinstance(cstruct, dict):
                print("deser is dict", self.objec)
                return self.objec.deserialize(cstruct)
               
            # if self.encoding and isinstance(cstruct, bytes):
            #     return str(cstruct, self.encoding)
        except Exception as e:
            raise e




class Personal(colander.MappingSchema):
    id = colander.SchemaNode(colander.String())
    displayanswer = colander.SchemaNode(Custom_string(DisplayAnswerObject()))

    # displayanswer = DisplayAnswerObject()
    
schema=Personal()

# serialize = schema.serialize(data)

fl=open("new.json")
data = json.load(fl)

# print(serialize)
# print("**********")

deserialize = schema.deserialize(data)

print("printing serialized data",deserialize)
