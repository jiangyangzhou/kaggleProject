selfpath=./`dirname $0`
last_alg=`ls $selfpath |grep -v ".sh" | cut -b -2 | sort | tail -1`
new_alg=`expr $last_alg + 1 | awk '{printf("%02d",$0)}'`_$1
topath=$selfpath/$new_alg
mkdir $topath/code -p
mkdir $topath/exps -p
pd=`cd $topath/../..;pwd`
comp_name=`basename $pd | cut -b 4-`
ln -s ../../../../../zhiliao $topath/code/zhiliao
ln -s ../../../$comp_name $topath/code/$comp_name
ln -s ../../data $topath/data
cp  $selfpath/../tools/common/new_exp.sh $topath/exps
touch $topath/config.json
