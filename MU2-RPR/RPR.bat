
@echo off
title MU2 Recovery Partition Removal
echo Welcome to the MU2 Recovery Partition Removal Script
pause

rem List the Disks
rem Create Script for Disk Part
echo > dplist.txt LIST DISK

diskpart /s dplist.txt

rem Choose the Disk
set /p Disk=Please choose a disk:
if "%Disk%"=="" goto :eof

rem Create Script for Disk Part
echo > dpchoose.txt LIST DISK
echo >> dpchoose.txt Select disk %Disk%
echo >> dpchoose.txt list partition
echo >> dpchoose.txt exit

diskpart /s dpchoose.txt

rem Choose the Partition to Remove
set /p Part=Please choose a partition:
if "%Part%"=="" goto :eof

rem Create Script for Disk Part
echo > pchoose.txt LIST DISK
echo >> pchoose.txt Select disk %Disk%
echo >> pchoose.txt list partition
echo >> pchoose.txt select partition %Part%
echo >> pchoose.txt delete partition override
echo >> pchoose.txt exit

diskpart /s pchoose.txt
pause 
exit
