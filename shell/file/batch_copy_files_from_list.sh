file_list=$1
dst_dir=$2

for x in `cat $file_list`
do
    echo $x
    cp --parents $x $dst_dir
done
