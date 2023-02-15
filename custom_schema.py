import colander
import json



class Custom_string(colander.SchemaType):

    def __init__(self, encoding=None, allow_empty=False):
        self.encoding = encoding
        self.allow_empty = allow_empty

    def serialize(self, node, appstruct):
        if appstruct is None:
            return None

        try:
            result = appstruct
            result_custom = "Customized data"
            if not isinstance(result_custom, str):
                result_custom = str(result_custom)
            # if self.encoding:
            #     result = result.encode(self.encoding)
            return result_custom
        except Exception as e:
            raise e
            

    def deserialize(self, node, cstruct):
        if cstruct == '' and self.allow_empty:
            return ''

        # if not cstruct:
        #     return None

        try:
            if isinstance(cstruct, str) or isinstance(cstruct, bool):
                custom_cstruct="custom cstruct"
                return cstruct
            # if self.encoding and isinstance(cstruct, bytes):
            #     return str(cstruct, self.encoding)
        except Exception as e:
            raise e



data = {
    "name" : "gaurav",
    "id" : "hello"
}

class Personal(colander.MappingSchema):
    id = colander.SchemaNode(Custom_string())
    name = colander.SchemaNode(Custom_string())
    
schema=Personal()

deserialize = schema.deserialize(data)


print(deserialize)
