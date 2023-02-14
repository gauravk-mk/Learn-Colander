import colander
from pprint import pprint
import inspect
import yaml

# stream = open("data.yaml","r")
# dictionary = yaml.load(stream)
# for key, value in dictionary.items():
#     print (key + " : " + str(value))
 



class Friend(colander.TupleSchema):
    rank = colander.SchemaNode(colander.Int(),
                               validator=colander.Range(0, 9999))
    name = colander.SchemaNode(colander.String())
    print("Friend is here")

class Phone(colander.MappingSchema):
    location = colander.SchemaNode(colander.String(),
                                   validator=colander.OneOf(['home', 'work','office']))
    number = colander.SchemaNode(colander.String())

class Friends(colander.SequenceSchema):
    friend = Friend()

class Phones(colander.SequenceSchema):
    phone = Phone()

class Person(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    age = colander.SchemaNode(colander.Int(),
                              validator=colander.Range(0, 200))
    friends = Friends()
    phones = Phones()
    print("Person is here ")


class Attachment(colander.MappingSchema):
    file = colander.SchemaNode(colander.String())
    path = colander.SchemaNode(colander.String())

class Attachments(colander.SequenceSchema):
    attachment= Attachment()

#list of string 

class User(colander.MappingSchema):
    _id: colander.SchemaNode(colander.String())
    toEmails: colander.SchemaNode(colander.List())
    ccEmails: colander.SchemaNode(colander.List())
    attachments = Attachments()
    monitoringId = colander.SchemaNode(colander.String())
    userId = colander.SchemaNode(colander.String())
    tid = colander.SchemaNode(colander.String())
    eid = colander.SchemaNode(colander.String())
    fromEmail = colander.SchemaNode(colander.String())
    channel = colander.SchemaNode(colander.String())
    subject = colander.SchemaNode(colander.String())
    status = colander.SchemaNode(colander.String(),
                                    validator=colander.OneOf(['Sent', 'Pending','Failed']))
    emailIdentifier = colander.SchemaNode(colander.String())
    userAction = colander.SchemaNode(colander.Bool())
    createdAt = colander.SchemaNode(colander.String())
    updatedAt = colander.SchemaNode(colander.String())
    _v = colander.SchemaNode(colander.Int())


schema = User()
deserialize = schema.deserialize(data)


print(deserialize)









# cstruct = {
#     'name': 'keith',
#     'age': 20,
#     'friends': [(1, 'jim'), (2, 'bob'), (3, 'joe'), (4, 'fred')],
#     'phones': [{'location': 'office', 'number': '555-1212'},
#                {'location': 'work', 'number': '555-8989'}],
# }

# schema = Person()

# try:
#     deserialize = schema.deserialize(cstruct)
#     print(deserialize)
# except colander.Invalid as e:
#     errors = e.asdict()
#     print(errors)
# print(deserialized)

# print(dictionary)



# person = Person()
# person.name = "navjyot"
# person.age = 9
# person.friends = {("101", "Saurabh")}
# person.phones = [{'location': 'home', 'number': '555-1212'},
#                 {'location': 'work', 'number': '555-8989'}],

# person.name="Gaurav"
# pprint(inspect.getmembers(person))
