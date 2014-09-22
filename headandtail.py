__author__ = 'quek'

import subprocess
import os

def getHeadTail(file_name):
    """
    this function should return the head and tail of a file
    :return:
    """
    head = subprocess.check_output(['head','-1', file_name]).split('\t')[0]
    tail = subprocess.check_output(['tail', '-1', file_name]).split('\t')[0]
    return head, tail

def renameFile(file_name):
    """
    rename file into
    :param file_name: file name to rename
    :return: rename input file, add prefix and suffix
    """
    (head, tail) = getHeadTail(file_name)
    new_file = "%s_%s_%s" % (file_name, head, tail)
    os.rename(file_name, new_file)

if __name__ == '__main__':
    ### chnage to 'test' to the list drive outoput
    file_list = ['test/%s' % x for x in os.listdir('test')]
    for file in file_list:
        renameFile(file)