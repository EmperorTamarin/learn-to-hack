# change user host port variables according to your configs.


from paramiko import SSHClient
from scp import SCPClient

def main():
	filename = input('Enter the name of the file to download : ')

	user = '<username>'	
	host = 'ip-address'
	port = 'port-number(int)'

	ssh = SSHClient()
	ssh.load_system_host_keys()

	ssh.connect(hostname=host, port=port, username=user)

	scp = SCPClient(ssh.get_transport())

	scp.get(str(filename))

	scp.close()


main()

