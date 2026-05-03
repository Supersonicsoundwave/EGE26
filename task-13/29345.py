from ipaddress import *


net = ip_network('68.203.243.87/255.255.224.0', False)
print(sum(int(n) for n in str(max(net.hosts())).split('.')))
