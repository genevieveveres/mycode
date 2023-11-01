#!/usr/bin/env python3
import shutil
import os

def main():
    #Tell the program to start in the home user directory
    os.chdir('/home/student/mycode/')

    #move the file to storage folder
    shutil.move('raynor.obj', 'ceph_storage/')

    #prompt the user to rename the file, then proceed with the renaming
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
