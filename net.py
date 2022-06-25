from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.177.5',  #Your Server IP
    'username': 'aisyah', #your Server Username
    'password': 'crystaleye1', #your server password
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('uname -a')
print(output)
