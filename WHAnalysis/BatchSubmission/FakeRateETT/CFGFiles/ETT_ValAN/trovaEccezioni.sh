#!/bin/bash
rm out.txt

for i in `ls -l */* | awk '{print $9}'`; do

	#echo $i
	#cat $i | grep 'Exception'
	allora=`cat $i | grep 'Exception'`
	#echo $allora
	
	if cat $i | grep 'Exception' ; then echo "qsub -q local $i" >> out.txt
	fi

done
