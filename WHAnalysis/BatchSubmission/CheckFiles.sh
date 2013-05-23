#!/bin/bash

for i in `ls -l ./CFGFiles/ETT/TauPlusX_Run*/* | grep '.csh.o' | awk '{print $9}'`; do

	echo $i
	cat $i 


done
