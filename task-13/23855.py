from ipaddress import *


net = ip_network('172.95.116.174/255.255.192.0', False)
print(sum(int(num) for num in str(min(net.hosts())).split('.')))
