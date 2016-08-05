#coding=utf-8

import os
import os.path
from os.path import join, getsize
import time

movie_dir_map = [
    ['E:/CODING/PYTHON/WalkOnMovieList/G_movie_list.txt',           'G:/Movie/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/G_series_movie_list.txt',    'G:/Series Movie/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/L_movie_list.txt',           'L:/Movie/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/L_movie_asia_list.txt',      'L:/Movie(Asia)/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/L_movie_comics_list.txt',    'L:/Movie(Comics)/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/J_series_game_of_throne_list.txt',     'J:/Series/Game of Thrones/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/J_series_tbbt_list.txt',     'J:/Series/The Big Bang Theory/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/J_series_list.txt',          'J:/Japanese TV/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/K_series_list.txt',          'K:/Series/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/M_movie_list.txt',           'M:/Movie/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/M_series_movie_list.txt',    'M:/Series Movie/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/N_movie_list.txt',           'N:/Movie/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/N_series_movie_list.txt',    'N:/Series Movie/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/N_animation_movie_list.txt', 'N:/Animation Movie/'],
    ['E:/CODING/PYTHON/WalkOnMovieList/N_documentary_list.txt',     'N:/Documentary/']
]

def getdirsize(dir):
    # size = 0L
    size = 0
    for root, dirs, files in os.walk(dir):
        print("{},{},{}".format(root, dirs, files))
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
    cur_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    md_name = '/path/to/dir/{:s}-my-movie-collections.md'.format(cur_date)
    md_file = open(md_name, 'w')
    preprocess_md_file(md_file)

    movie_cnt = 0
    for idx, item in enumerate(movie_dir_map):
        list_file, rootdir = item
        movie_list_file = open(list_file, 'w')
        movie_list = os.listdir(rootdir)

        md_file.write('## {:s}\n\n'.format(rootdir))

        for line in movie_list:
            filepath = os.path.join(rootdir, line)
            filesize = 0
            if os.path.isdir(filepath):
                filesize = getdirsize(filepath)
                print('({:d}) {:s} [{:.2f}G]'.format(movie_cnt, line, float(filesize)/1024/1024/1024))

                movie_cnt += 1
                write_line = '({:d}) {:s} [{:.2f}G]  <br />\n'.format(movie_cnt, line, float(filesize)/1024/1024/1024)
                movie_list_file.write(write_line)

                md_file.write(write_line)

        movie_list_file.close()
        md_file.write('\n')

    md_file.close()
