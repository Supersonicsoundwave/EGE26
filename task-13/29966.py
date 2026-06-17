from ipaddress import *


net = ip_network('146.180.173.153/255.192.0.0', False)
print(''.join(str(max(net.hosts())).split('.')))
