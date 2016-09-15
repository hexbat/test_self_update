#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from subprocess import Popen, PIPE, call
import git

def update():
	cmd = 'git pull'
	p = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
	out, err = p.communicate()
	if err:
		print('Error while pull')
		print(err)
		error_code += 1
	elif out:
		Popen("self_update.py", shell=True)
		sys.exit("exit to restart")

if __name__ == "__main__":
	update()
