import os
import stat
#site_file = open('sites_to_block','r')
#list = site_file.read().splitlines()
#host_file = open('/etc/hosts','a')

def checkFile(input_file):
	if os.stat(input_file).st_size==0:
		sys.exit('Empty input file')
	else:
		site_file = open(f'{input_file}','r')
		site_list = site_file.read().splitlines()
	return site_list

def uniqueList(site_list):
	st = set(site_list)
	un = list(st)
	return un

def blockSite(l,hot_file):
	x = 0
	host_file = open(f'{hot_file}','a') 
	for i in l:
		host_file.write(f'127.0.0.1	{i}\n')
		host_file.write(f'::1	{i}\n')
		x += 1
	print(f'Blocked {x} sites')

def lockInputFile(input_file):
	val = os.stat(input_file).st_mode
	if val == 33188:
		os.chmod(input_file,stat.S_IRWXU)
	return os.stat(input_file).st_mode

def main():
	site_file = 'sites_to_block'
	host_file = '/etc/hosts'
	a = checkFile(site_file)
	b = uniqueList(a)
	c = blockSite(b,host_file)
	d = lockInputFile(site_file)
	print(c)

if __name__ == "__main__":
	main()
