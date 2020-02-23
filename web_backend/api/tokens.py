from pymemcache.client import base

client = base.Client('localhost')

client.set('some_key', 'some value')

client.get('some_key')

print(client)