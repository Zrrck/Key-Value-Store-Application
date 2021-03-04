import redis
import json
def server(environ, start_response):

    data = b''

    r = redis.StrictRedis()

    def resp(start_response, code, headers=[('Content-type', 'application/json')], body=b''):
      start_response(code, headers)
      return [body]

    def scan_keys(r):
        results = []
        result = {}
        for key in r.scan_iter("*"):
            result[key.decode('utf-8')] = r.get(key).decode('utf-8')

            # result.extend(r.get(key))
            # result.extend(b' ')
            results.append(result)
        return json.dumps(result)

    def delete_keys(r):
        for key in r.scan_iter("*"):
            r.delete(key)


    id = environ['RAW_URI'][6:]

    if id != '':

        if environ['REQUEST_METHOD'] == 'GET':
            value = r.get(id)
            if value is None:
                return resp(start_response,'404 Not Found')
            return resp(start_response,'200 OK',body = value)
            

        if environ['REQUEST_METHOD'] == 'HEAD':
            if r.exists(id):
                return resp(start_response,'200 OK')
            return resp(start_response,'404 Not Found')

        if environ['REQUEST_METHOD'] == 'DELETE':
            value = r.get(id)
            if value is None:
                return resp(start_response,'500 Internal Server Error')
            r.delete(id)
            return resp(start_response,'200 OK')


    if environ['REQUEST_METHOD'] == 'GET':
        data = scan_keys(r)
        if data:
            return resp(start_response,'200 OK',body = data.encode('utf-8'))
        return resp(start_response,'204 No Content')

    if environ['REQUEST_METHOD'] == 'PUT':
        key,value = environ['wsgi.input'].read().decode('UTF-8').split(':')
        if r.exists(key):
            return resp(start_response,'409 Conflict')
        r.set(key,value)

        return resp(start_response,'201 Created')

    if environ['REQUEST_METHOD'] == 'DELETE':
        if r.dbsize() != 0:
            delete_keys(r)
            return resp(start_response,'200 OK',body = bytes(data))
        return resp(start_response,'204 No Content')


    return iter([data])

