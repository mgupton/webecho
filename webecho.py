from bottle import run, post, request, response, get, route, put, delete
from json import dumps
import json

@get('/')
def data():
    postdata = request.json
    try:
        rv = {"method": request.method, "data": postdata}
    except:
        raise ValueError
    response.content_type = 'application/json'
    print(rv)
    return dumps(rv)

@post('/')
def data():
    postdata = request.json
    try:
        rv = {"method": request.method, "data": postdata}
    except:
        raise ValueError
    response.content_type = 'application/json'
    print(rv)
    return dumps(rv)


run(host='0.0.0.0', port=8090)
