main_dir=/path/to/dir/

find ${main_dir} -type d | rename -v "s/\ //g"
find ${main_dir} -type d | rename -v "s/\{/_/g"
find ${main_dir} -type d | rename -v "s/\}//g"
find ${main_dir} -type d | rename -v "s/\'//g"
find ${main_dir} -type d | rename -v "s/,/_/g"

find ${main_dir} | rename -v "s/\ //g"
find ${main_dir} | rename -v "s/\{/_/g"
find ${main_dir} | rename -v "s/\}//g"
find ${main_dir} | rename -v "s/\'//g"
find ${main_dir} | rename -v "s/,/_/g"

find ${main_dir} | rename -v "s/副本/copy/g"

# remove *.db
rm `find ${main_dir} -type f | grep "\.db"`

# remove invalid images
#rm `cat ${bad_image_list}`
