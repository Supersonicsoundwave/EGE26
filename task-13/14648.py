from ipaddress import *


ip1 = ip_address('218.48.192.56')
ip2 = ip_address('218.48.192.0')
cnt = 0
for mask in range(16, 25):
    net = ip_network(f'218.48.192.0/{mask}', False)
    if ip1 in net.hosts() and net.network_address == ip2 and len(tuple(net.hosts())) >= 500:
        cnt += 1
print(cnt)

