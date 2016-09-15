#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from subprocess import Popen, PIPE, call
from os.path import dirname, realpath
from sys import exit

def update():
	cmd = 'git pull'
	p = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
	out, err = p.communicate()
	if err:
		print('Error while pull')
		print(err)
		print("--------")
	if out:
		Popen(dirname(realpath(__file__)) + "/self_update.py", shell=True)
		exit("exit to restart")

if __name__ == "__main__":
	update()
