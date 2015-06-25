from BaseHTTPServer import HTTPServer
import json

from pysimplesoap.server import SoapDispatcher, SOAPHandler
import redis


__author__ = 'Lecks'


def create(key, value):
    if not r.exists(key):
        r.set(key, value)
        return json.dumps({"isOk": True, "msg": "Object successfully created"})

    return json.dumps({"isOk": False, "msg": "Key already exists"})


def read(key):
    if r.exists(key):
        return json.dumps({"isOk": True, "msg": r.get(key)})

    return json.dumps({"isOk": False, "msg": "Key does not exists"})


def update(key, value):
    if r.exists(key):
        r.set(key, value)
        return json.dumps({"isOk": True, "msg": "Object successfully updated"})

    return json.dumps({"isOk": False, "msg": "Key does not exists"})


def delete(key):
    if r.exists(key):
        r.delete(key)
        return json.dumps({"isOk": True, "msg": "Object successfully deleted"})

    return json.dumps({"isOk": False, "msg": "Key does not exists"})


dispatcher = SoapDispatcher('my_dispatcher')

dispatcher.register_function('Create', create, returns={'Result': str}, args={'key': str, 'value': str})
dispatcher.register_function('Read', read, returns={'Result': str}, args={'key': str})
dispatcher.register_function('Update', update, returns={'Result': str}, args={'key': str, 'value': str})
dispatcher.register_function('Delete', delete, returns={'Result': str}, args={'key': str})

print "WSDL"
#print dispatcher.wsdl()
print "Connect to redis... (localhost:6379)"
r = redis.StrictRedis(host='localhost')
print "Starting server... (localhost:8000)"
httpd = HTTPServer(("", 8000), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()