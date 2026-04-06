from ipaddress import *


def f(ip):
    ip = f'{int(ip):032b}'
    return ip[16:24].count('0') > ip[24:].count('0')


cnt = 0
for A in range(256):
    ip_host = ip_address(f'246.81.65.{A}')
    net = ip_network(f'{ip_host}/255.255.255.224', False)
    if ip_host not in [net.broadcast_address, net.network_address]:
        if all(f(ip) for ip in net.hosts()):
            cnt += 1
print(cnt)
