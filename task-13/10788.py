from ipaddress import *


ip1 = ip_address('201.44.240.33')
ip2 = ip_address('201.44.240.107')
cnt = 0
for mask in range(10, 31):
    net = ip_network(f'{ip1}/{mask}', False)
    if ip1 in net.hosts() and ip2 in net.hosts() and f'{int(net.network_address):032b}'.count('1') >= 5:
        cnt += 1
print(cnt)
