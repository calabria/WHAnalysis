#!/bin/csh

mkdir #__tmpPath
cd #__pathCFG
cmsenv
cmsRun #__nameCFG 

cmsenv
cd #__tmpPath

set rootFiles=(`/bin/ls *.root`)
foreach rootFile (${rootFiles})
rfcp ${rootFile} #__castorPath
end
