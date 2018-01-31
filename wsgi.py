from eve import Eve
from eve_swagger import swagger, add_documentation

app = Eve()
app.register_blueprint(swagger)

# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': 'Data Source API',
    'version': '1.0',
    'description': 'Provides Rest API for MongoDB database',
    'termsOfService': 'DS',
    'schemes': ['http', 'https'],
}

# optional. Will use flask.request.host if missing.
app.config['SWAGGER_HOST'] = 'http://datasource-cosmos.app.caascloud.net'

# optional. Add/Update elements in the documentation at run-time without deleting subtrees.
add_documentation({'paths': {'/status': {'get': {'parameters': [
    {
        'in': 'query',
        'name': 'foobar',
        'required': False,
        'description': 'special query parameter',
        'type': 'string'
    }]
}}}})

if __name__ == '__main__':
    app.run()
