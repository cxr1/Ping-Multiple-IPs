import subprocess
import time
 
rack1_pdu_ip = ["192.168.244.138", "192.168.244.138", "192.168.244.138"]
rack2_pdu_ip = ["192.168.244.158", "192.168.244.158", "192.168.244.158"]
rack3_pdu_ip = ["192.168.244.178", "192.168.244.178", "192.168.244.178"]
 
 
def choose_ip(first, end):
    rack_pdu_ip = []
    for ip in range(first, end + 1):
        rack_pdu_ip.append(eval("rack" + str(first) + "_pdu_ip"))
        first += 1
    return rack_pdu_ip
 
 
def ping_ip(first, end):
    start_time = time.time()
    for ip_list in choose_ip(first, end):
        print(" ")
        print('RACK' + str(first))
        first += 1
        for ip in ip_list:
            res = subprocess.call('ping -n 2 -w 5 %s' % ip, stdout=subprocess.PIPE)
            print(ip, "\033[1;32m True \033[0m" if res == 0 else "\033[1;31m False \033[0m")
    print('执行所用时间：%s' % (time.time() - start_time))
 
 
ping_ip(1, 3)  # ping_ip(1, 3)代表从"RACK1"到"RACK3"
