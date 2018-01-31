from eve import Eve
from eve_swagger import swagger, add_documentation
import os

SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
application = Eve(settings=SETTINGS_PATH)
application.register_blueprint(swagger)

# required. See http://swagger.io/specification/#infoObject for details.
application.config['SWAGGER_INFO'] = {
    'title': 'Data Source API',
    'version': '1.0',
    'description': 'Provides Rest API for MongoDB database',
    'termsOfService': 'DS',
    'schemes': ['http', 'https'],
}

# optional. Will use flask.request.host if missing.
application.config['SWAGGER_HOST'] = 'http://datasource-cosmos.app.caascloud.net'

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
    application.run()
