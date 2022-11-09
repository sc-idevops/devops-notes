import redis
r = redis.Redis(password="4jbZpRULOR",host="a0d695fd9be1245d29e24249a92561a3-1895269611.us-west-2.elb.amazonaws.com")
r.mset({"iDevOps": "Grant Is The Man"})
retrieve_value = r.get("iDevOps")
print(retrieve_value.decode("utf-8"))