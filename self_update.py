#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from subprocess import Popen, PIPE, call
import git

def update():
	cmd = 'git pull'
	p = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
	out, err = p.communicate()
	if err:
		print('Error while getting local hash')
		print(err)
		error_code += 1
	elif out:
		print('Try to update')
		args = sys.argv[:]
		print(args)
		print('Re-spawning %s' % ' '.join(args))
		args.insert(0,sys.executable)
		os.execv(sys.executable, args)

def main():
	remote_hash = ''
	local_hash = ''
	error_code = 0
	cmd = 'git rev-parse HEAD'
	p = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
	out, err = p.communicate()
	if out:
 		local_hash = out.split()[0]
	if err:
		print('Error while getting local hash')
		print(err)
		error_code += 1
	cmd = 'git ls-remote https://github.com/hexbat/test_self_update.git HEAD'
	p = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
	out, err = p.communicate()
	if out:
		remote_hash = out.split()[0]
	if err:
		print('Error while getting remote hash')
		print(err)
		error_code += 1
	print(local_hash)
	print(remote_hash)
	if (local_hash != remote_hash) and (error_code == 0):
		print('Found update')
		update()
	
if __name__ == "__main__":
	main()

