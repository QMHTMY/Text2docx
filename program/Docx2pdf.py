#!/usr/bin/python3
# coding: utf-8
# Author: Shieber
# Date: 2019.07.24
# transfer docx to pdf
# -a option means transfer all docx files in the current directory to pdf.
#

import sys,time
from os.path import  basename 
from subprocess import call

def trans2pdf():
    argv = sys.argv
    if len(sys.argv) < 2:
        script = basename(argv[0])
        print('Usage: %s name.docx or %s -a'%(script,script))
        sys.exit(-1)

    if '-a' == argv[1] or '--all' == argv[1]:
        order = 'libreoffice --invisible --convert-to pdf *.docx 1>/dev/null 2>&1'
    else:
        if argv[1].endswith('.docx'):
            order = 'libreoffice --invisible --convert-to pdf %s 1>/dev/null 2>&1'%argv[1]
        else:
            print('Error, file type does not match!')
            sys.exit(-1)

    call(order,shell=True)

if __name__ == '__main__':
    start = time.time()
    trans2pdf()
    end = time.time()
    print('耗时：%.2f(s)'%(end-start))
