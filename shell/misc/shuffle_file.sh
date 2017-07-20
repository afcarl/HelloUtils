FILE=$1

for i in {1..100}
do
    shuf ${FILE} > __tmp.txt
    cat __tmp.txt > ${FILE}
done
