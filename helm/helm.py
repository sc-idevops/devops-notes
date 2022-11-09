import redis
r = redis.Redis(password="WRtRpAcFZq")
r.mset({"iDevOps": "Grant Is The Man"})
retrieve_value = r.get("iDevOps")
print(retrieve_value.decode("utf-8"))