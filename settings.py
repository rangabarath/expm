MONGO_HOST = '10.130.6.145'
MONGO_PORT = 27017
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'password'
MONGO_DBNAME = 'sampledb'
# Enable reads-GET, inserts-POST and DELETE for resources/collections
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Schema definition, based on Cerberus grammar. Check the Cerberus project
# (https://github.com/pyeve/cerberus) for details.
schema = {
    'hostname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
        'unique': True,
    },
    'ipaddress': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
    },
    'type': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
    }
}

host = {
    # 'title' tag used in item links. Defaults to the resource title minus
    'item_title': 'host',

    #additional search lookup
    # GET requests at '/host/<hostname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'hostname'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST', 'DELETE'],

    'schema': schema
}

DOMAIN = {'host': host}

#for swagger integration
X_DOMAINS = ['http://localhost:8000']
X_HEADERS = ['Content-Type', 'If-Match']
