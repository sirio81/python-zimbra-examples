#!/usr/bin/env python3

import pythonzimbra.communication
from pythonzimbra.communication import Communication
import pythonzimbra.tools
from pythonzimbra.tools import auth


# url of your zimbra server
url  = 'https://your.server.tld:7071/service/admin/soap'
comm = Communication(url)
admin_name = 'admin@domain.tld'
admin_password = 'VerySecretOne'

admin_token = auth.authenticate(
    url,
    admin_name,
    admin_password,
    admin_auth=True,
    use_password=True
)

request = comm.gen_request(token=admin_token)
request.add_request(
    'DelegateAuthRequest',
    {
        'account': {
            'by': 'name',
            '_content': 'another.user@somedomain.tld'
        }
    },
    'urn:zimbraAdmin'
)
response = comm.send_request(request)
new_token = response.get_response()['DelegateAuthResponse']['authToken']['_content']

request = comm.gen_request(token=new_token)
request.add_request(
    'GetFolderRequest',
    {
        'folder': {
            'path': '/inbox'
        }
    },
    'urn:zimbraMail'
)
response = comm.send_request(request)
print(response.get_response())
