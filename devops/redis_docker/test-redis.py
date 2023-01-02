import redis
r = redis.Redis()
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

potato = r.get("Bahamas")

print(potato)
