from ping3 import ping
from concurrent.futures import ThreadPoolExecutor
 
ips = ["192.168.244.138", "192.168.244.138", "192.168.244.138",
       "192.168.244.158", "192.168.244.158", "192.168.244.158",
       "192.168.244.178", "192.168.244.178", "192.168.244.178"]
 
 
def pings(ips):
    ips_status = dict()
    with ThreadPoolExecutor(max_workers=500) as pool:
        results = pool.map(ping, ips)
    for index, result in enumerate(results):
        ip = ips[index]
        if type(result) == float:
            ips_status[ip] = True
        else:
            ips_status[ip] = False
    return ips_status
 
 
ips_status = pings(ips)
# print(ips_status)
 
i = 0
for key, value in ips_status.items():
    if i % 3 == 0:
        print("\n" + "RACK" + " " + str(int((i + 3) / 3)))
    print(key, "\033[1;32m True \033[0m" if value == 1 else "\033[1;31m False \033[0m")
    i += 1
