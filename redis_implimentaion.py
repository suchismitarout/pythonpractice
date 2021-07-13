import redis

r = redis.Redis()
r.set('name', 'deepak')
print(r.get('name'))


print(r.get('location'))