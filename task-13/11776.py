from ipaddress import *


net = ip_network('235.86.56.0/255.255.248.0')
cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip[-2:] == '11':
        cnt += 1
print(cnt)
