selfpath=./`dirname $0`
last_exp=`ls $selfpath | grep exp | grep -v .sh | cut -b 4- | sort | tail -1`
new_exp=exp`expr $last_exp + 1 | awk '{printf("%02d",$0)}'`
topath=$selfpath/$new_exp
mkdir $topath -p
ln -s ../../data $topath/
mkdir $topath/code -p
mkdir $topath/result -p 
