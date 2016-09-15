#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from subprocess import Popen, PIPE, call
import git

def main():
  cmd = 'git rev-parse HEAD'
  p = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
  out, err = p.communicate()
  if out:
    local_hash = out
  if err:
    print('Error while getting local hash')
    print(err)
  cmd = 'git ls-remote https://github.com/hexbat/test_self_update.git HEAD'
  p = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
  out, err = p.communicate()
  if out:
    remote_hash = out.split()[0]
  if err:
    print('Error while getting remote hash')
    print(err)
  
  print(local_hash)
  print(remote_hash)
  

if __name__ == "__main__":
    main()

