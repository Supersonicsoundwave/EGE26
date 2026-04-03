from ipaddress import ip_network


def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('1') >= ip[16:].count('1')


for A in range(256):
    if '01' not in f'{int(A):08b}':
        net = ip_network(f'238.51.1.202/255.255.{A}.0', False)
        if all(f(ip) for ip in net):
            print(A)
            break
            