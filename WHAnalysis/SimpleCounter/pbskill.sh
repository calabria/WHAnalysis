#!/bin/bash

#for i in `qselect -u calabria` ; 
for i in `qselect -u calabria -q local` ;
#for i in `cat list.txt ` ;
	do qdel $i ; 
	echo $i "deleted"
done
