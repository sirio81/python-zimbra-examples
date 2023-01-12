# python-zimbra-examples
Usage examples of the python-zimbra library

Here are some examples to clarify what you read from

https://github.com/Zimbra-Community/python-zimbra

Bear in mind that when you authenticate using the preAuthKey the zimbraLastLogonTimestamp get's updated.
You may want to use delegate authentication then, also to avoid creating a preAuthKey for each domain you wish to manage.

I have some concerns about batch_requests.
It seems they don't work as expected.
