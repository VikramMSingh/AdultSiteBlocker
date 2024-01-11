site_file = open('sites_to_block','r')
list = site_file.read().splitlines()
host_file = open('/etc/hosts','a')
#host_file = open('hosts_test','a')
for i in list:
	host_file.write(f'127.0.0.1	{i}\n')
	host_file.write(f'::1	{i}\n')
	print(f'Blocked {i}')
