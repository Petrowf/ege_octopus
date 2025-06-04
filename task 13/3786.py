from ipaddress import ip_network, ip_address
ip = '232.126.150.18'
mask = '255.255.240.0'
net = ip_network(f'{ip}/{mask}',0)
print(int(ip_address(ip))-int(net.network_address))