#coding=utf-8

import os
import os.path
from os.path import join, getsize
import sys
import time

def read_input_folder_list(filename):
    #f = open(filename, 'r')
    f = open(filename, 'r', encoding='utf-8')
    lines = [line.rstrip('\n') for line in f]
    f.close()
    
    movie_dir_map = list()
    for line in lines:
        input_dir_path = line
        dir_name = line.split('\\')[-1]
        movie_dir_map.append((dir_name, input_dir_path))
    
    return movie_dir_map

def getdirsize(dir):
    # size = 0L
    size = 0
    for root, dirs, files in os.walk(dir):
        #print("{},{},{}".format(root, dirs, files))
        size += sum([getsize(join(root, name)) for name in files])
        return size

def preprocess_md_file(md_file):
    cur_year = time.strftime('%Y',time.localtime(time.time()))
    cur_month = time.strftime('%m',time.localtime(time.time()))
    # cur_month_abbr = time.strftime('%b',time.localtime(time.time()))
    cur_day = time.strftime('%d',time.localtime(time.time()))

    md_file.write('---\n')
    md_file.write('layout: post\n')
    md_file.write('categories: leisure\n')
    md_file.write('title: My Movie Collections\n')
    md_file.write('date: {:d}-{:d}-{:d}\n'.format(int(cur_year), int(cur_month), int(cur_day)))
    # md_file.write('date: 2015-07-04\n')
    md_file.write('---\n\n')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python WalkOnMovieList.py input_folder_list.txt output_folder_list.txt')
        exit(1)
    cur_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    #md_name = '/path/to/dir/{:s}-my-movie-collections.md'.format(cur_date)
    #md_file = open(md_name, 'w')
    #preprocess_md_file(md_file)
    
    input_folder_list = sys.argv[1]
    output_folder_list = sys.argv[2]
    movie_dir_map = read_input_folder_list(input_folder_list)
    
    movie_list_file = open(output_folder_list, 'w')

    movie_cnt = 0
    for idx, item in enumerate(movie_dir_map):
        rootdir_name, rootdir = item
        
        movie_list = os.listdir(rootdir)

        #md_file.write('## {:s}\n\n'.format(rootdir))
        movie_list_file.write('{}\n'.format(rootdir_name))

        cur_dir_movie_cnt = 0
        for line in movie_list:
            filepath = os.path.join(rootdir, line)
            filesize = 0
            if os.path.isdir(filepath):
                filesize = getdirsize(filepath)
                print('({:d}) {:s} [{:.2f}G]'.format(movie_cnt, line, float(filesize)/1024/1024/1024))

                movie_cnt += 1
                cur_dir_movie_cnt += 1
                #write_line = '({:d}) {:s} [{:.2f}G]  <br />\n'.format(movie_cnt, line, float(filesize)/1024/1024/1024)
                #write_line = '({:d}) {:s} [{:.2f}G]\n'.format(movie_cnt, line, float(filesize)/1024/1024/1024)
                write_line = '({:d})\t{:s}\t[{:.2f}G]\n'.format(cur_dir_movie_cnt, line, float(filesize)/1024/1024/1024)
                movie_list_file.write(write_line)

                #md_file.write(write_line)

        #md_file.write('\n')

    #md_file.close()
    movie_list_file.close()
