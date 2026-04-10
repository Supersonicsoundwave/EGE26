from ipaddress import *


ip1 = ip_address('157.127.182.76')
ip2 = ip_address('157.127.190.80')
for mask in range(10, 31):
    net = ip_network(f'{ip1}/{mask}', False)
    if ip1 in net.hosts() and ip2 not in net:
        print(mask)
        break
