selfpath=./`dirname $0`
last_comp=`ls $selfpath/../competitions | cut -b -2 | sort | tail -1`
new_comp=`expr $last_comp + 1 | awk '{printf("%02d",$0)}'`_$1
topath=$selfpath/../competitions/$new_comp
mkdir $topath -p
mkdir $topath/algs -p
mkdir $topath/data/train -p
mkdir $topath/data/test -p
mkdir $topath/temp -p
echo "## $1" > $topath/README.md
mkdir $topath/tools/common -p
cp $selfpath/* $topath/tools/common
cp $selfpath/new_alg.sh $topath/algs
mkdir $topath/$1/ -p
ln -s ../../../zhiliao $topath/$1/zhiliao
touch $topath/$1/__init__.py
