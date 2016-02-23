# Copyright: http://my.oschina.net/duhaizhang/blog/67240

import md5
import os
from time import clock as now
def getmd5(filename):
    file_txt = open(filename,'rb').read()
    m = md5.new(file_txt)
    return m.hexdigest()

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
    
def getNewFile(oldfile):
    index=find(oldfile,'.')[-1]
    newfile=oldfile[:index]+'(1)'+oldfile[index:]
    return newfile
    
def main():
    #path = raw_input("path: ")
    path = 'E:/path_to_files'
    all_md5 = {}
    all_size = {}
    total_file=0
    total_delete=0
    start=now()
    # only remove file name as 'aaa(1).jpg'
    for file in os.listdir(path):
        total_file += 1
        real_path=os.path.join(path,file)
        #print real_path
        if os.path.isfile(real_path) == True:
            size = os.stat(real_path).st_size
            name_and_md5=[real_path,'']
            if size in all_size.keys():
                new_md5 = getmd5(real_path)
                if all_size[size][1]=='':
                    all_size[size][1]=getmd5(all_size[size][0])
                if new_md5 in all_size[size]:
                    print 'Remove ',file
                    #os.remove(real_path)
                    total_delete += 1
                    
                    # my personal setting
                    '''
                    target_file=getNewFile(file)
                    target_path = os.path.join(path,target_file)
                    if os.path.isfile(target_path) == True:
                        print 'Remove ',target_file
                        os.remove(target_path)
                        total_delete += 1
                    '''
                else:
                    all_size[size].append(new_md5)
            else:
                all_size[size]=name_and_md5
    end = now()
    time_last = end - start
    print 'Total files:   ',total_file
    print 'Remove files:  ',total_delete
    print 'Time consumed: ',time_last,' seconds'
     
if __name__=='__main__': 
    main()