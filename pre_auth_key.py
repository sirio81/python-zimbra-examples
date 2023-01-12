#!/usr/bin/env python3

import pythonzimbra.communication
from pythonzimbra.communication import Communication
import pythonzimbra.tools
from pythonzimbra.tools import auth

# url of your zimbra server.
url  = 'https://your.server.tld:7071/service/admin/soap'
comm = Communication(url)
user = 'john.doe@domain.tld'
preauth_key = '12345678901234567890...'


usr_token = auth.authenticate(
    url,
    user,
    preauth_key,
)


info_request = comm.gen_request(token=usr_token)

info_request.add_request(
    'GetFolderRequest',
    {
        'folder': {
            'path': '/inbox'
        }
    },
    'urn:zimbraMail'
)

info_response = comm.send_request(info_request)
print(info_response.get_response())
