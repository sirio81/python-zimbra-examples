#!/usr/bin/env python3

import pythonzimbra.communication
from pythonzimbra.communication import Communication
import pythonzimbra.tools
from pythonzimbra.tools import auth


# url to your zimbra server
url  = 'https://your.server.tld:7071/service/admin/soap'
comm = Communication(url)
admin_name = 'admin@doman.com'
admin_password = 'VerySecretOne'

admin_token = auth.authenticate(
    url,
    admin_name,
    admin_password,
    admin_auth=True,
    use_password=True
)

info_request = comm.gen_request(token=admin_token)

# This request requires admin priviledge.
info_request.add_request(
    'SearchDirectoryRequest',
    {
        'query': '(&(objectClass=zimbraAccount)(zimbraAccountStatus=closed))',
        'domain': 'somedomain.tld',
        'applyCos': 0
    },
    'urn:zimbraAdmin'
)

info_response = comm.send_request(info_request)
pprint(info_response.get_response())
