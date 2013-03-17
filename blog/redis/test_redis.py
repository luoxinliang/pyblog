import redis

def test():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set("x", "ljfldjflsaj")
    print r.get("x")
    
test()