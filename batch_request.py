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


requests_id = []
info_request = comm.gen_request(token=usr_token)
batch_request = comm.gen_request(token=usr_token, set_batch=True)

requests_id.append(batch_request.add_request(
    'GetFolderRequest',
    {
        'folder': {
            'path': '/inbox'
        }
    },
    'urn:zimbraMail'
    )
)

requests_id.append(batch_request.add_request(
    'GetFolderRequest',
    {
        'folder': {
            'path': '/sent'
        }
    },
    'urn:zimbraMail'
    )
)

batch_response = comm.send_request(batch_request)

for request_id in requests_id:
    print(batch_response.get_response(request_id))
