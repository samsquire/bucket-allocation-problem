from math import ceil
from operator import itemgetter
from pprint import pprint
buckets = {
  "user": [
    {"name": "users-bucket1", "start": 0, "end": 5000},
    {"name": "users-bucket2", "start": 5001, "end": 10000},
    {"name": "users-bucket3", "start": 10001, "end": 15000}
  ],
  "server": [
    {"name": "server-bucket1", "start": 0, "end": 3},
    {"name": "server-bucket2", "start": 4, "end": 7},
    {"name": "server-bucket3", "start": 8, "end": 10}
  ],
    "thread": [
    {"name": "threads-bucket1", "start": 0, "end": 4},
    {"name": "threads-bucket2", "start": 5, "end": 9},
    {"name": "threads-bucket3", "start": 10, "end": 14}
  ]
}

users_size = 5000
server_size = 3
thread_size = 4

sizes = {
  "user": users_size,
  "server": 3,
  "thread": 4
}

buckets2 = {
  "buckets": [
    {"type": "user", "name": "users-bucket1", "start": 0, "end": users_size * 1},
    {"type": "user", "name": "users-bucket2", "start": (users_size * 1) + 1, "end": (users_size * 2)},
    {"type": "user", "name": "users-bucket3", "start": (users_size * 2) + 1, "end": (users_size * 3)},

    {"type": "server", "name": "server-bucket1", "start": 0, "end": server_size * 1},
    {"type": "server", "name": "server-bucket2", "start": (server_size * 1) + 1, "end": (server_size * 2)},
    {"type": "server","name": "server-bucket3", "start": (server_size * 2) + 1, "end": (server_size * 3)},
    {"type": "thread", "name": "threads-bucket1", "start": 0, "end": thread_size * 1},
    {"type": "thread", "name": "threads-bucket2", "start": (thread_size * 1) + 1, "end": (thread_size * 2)},
    {"type": "thread", "name": "threads-bucket3", "start": (thread_size * 2) + 1, "end": (thread_size * 3)}
  ]
}

buckets2["buckets"].sort(key=itemgetter("start"), reverse=True)

def route2(routing_information):
  buckets = {}
  for item in buckets2["buckets"]:
    if item["end"] >= routing_information[item["type"]]:
      buckets[item["type"]] = item["name"]
  return buckets

def route(routing_information):
  results = []
  for route in routing_information:
    for search in buckets[route[0]]:
      if route[1] > search["start"] and route[1] <= search["end"]:
        results.append(search)
  return results

def route3(routing_information):
  buckets = {}
  for key, value in routing_information.items():
    buckets[key] = ceil(value / sizes[key])
  return buckets

print(route([("server", 3), ("user", 5607), ("thread", 11)]))
print(route2(
  { "server": 3, "user": 5607, "thread": 11}
))
print(route3(
  { "server": 3, "user": 5607, "thread": 11}
))

bucket_lookup = {}
for kind in ["thread", "server", "user"]:
  bucket_lookup[kind] = {}  
  for index in range(0, 10):
    bucket_lookup[kind][index] = {"bucket": index}
    for innerkind in ["thread", "server", "user"]:
      bucket_lookup[kind][index][innerkind] = {}

for index in range(0, 10):
  for kind in ["thread", "server", "user"]:  
    for innerkind in ["thread", "server", "user"]:
      
      for subindex in range(0, 10):    
        bucket_lookup[kind][index][innerkind][subindex] = bucket_lookup[innerkind][subindex]
         
print(bucket_lookup["thread"][0]["server"][0]["user"][0]["bucket"])

servers = ["server", "server", "server"]
containers = ["app", "database", "jobs"]
threadTypes = ["recv", "send"]
threads = range(0, 3)
sockets = ["socket1", "socket2", "socket3"]
for server_index, server in enumerate(servers):
  for container_index, container in enumerate(containers):
    for type_index, thread_type in enumerate(threadTypes):
      for thread_index, thread in enumerate(threads):
         print("{}{}".format(server, server_index), "{}{}".format(container, container_index), "{}{}{}".format("thread", thread_index, thread_type))