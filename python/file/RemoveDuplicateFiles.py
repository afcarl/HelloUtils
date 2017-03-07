# Copyright: http://my.oschina.net/duhaizhang/blog/67240

import md5
import os
import sys
from time import clock as now

def getmd5(filename):
    file_txt = open(filename, 'rb').read()
    m = md5.new(file_txt)
    return m.hexdigest()

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def getNewFile(oldfile):
    index = find(oldfile,'.')[-1]
    newfile = oldfile[:index] + '(1)' + oldfile[index:]
    return newfile

def readConfigFile(filename):
    f = open(filename, 'r')
    path_list = [line.rstrip('\n') for line in f]
    f.close()
    return path_list

def run(path_list):
    all_md5 = {}
    all_size = {}
    total_file = 0
    total_delete = 0
    start = now()

    for path in path_list:
        print('Processing dir: {}'.format(path))
        for file in os.listdir(path):
            total_file += 1
            real_path = os.path.join(path, file)
            if os.path.isfile(real_path) == True:
                size = os.stat(real_path).st_size
                name_and_md5 = [real_path,'']
                if size in all_size.keys():
                    new_md5 = getmd5(real_path)
                    if all_size[size][1] == '':
                        all_size[size][1] = getmd5(all_size[size][0])
                    if new_md5 in all_size[size]:
                        print('Remove {}'.format(real_path))
                        os.remove(real_path)
                        total_delete += 1

                        # my personal setting: only remove file name as 'aaa(1).jpg'
                        '''
                        target_file = getNewFile(file)
                        target_path = os.path.join(path, target_file)
                        if os.path.isfile(target_path) == True:
                            print('Remove {}'.format(target_file))
                            os.remove(target_path)
                            total_delete += 1
                        '''
                    else:
                        all_size[size].append(new_md5)
                else:
                    all_size[size] = name_and_md5
    end = now()
    time_last = end - start
    print('Total files:   {}'.format(total_file))
    print('Remove files:  {}'.format(total_delete))
    print('Time consumed: {} seconds'.format(time_last))

if __name__ == '__main__':
    if len(sys.argv[1]) < 2:
        print('Not input file specified.')
        sys.exit()

    input_file = sys.argv[1]
    path_list = readConfigFile(input_file)
    run(path_list)
