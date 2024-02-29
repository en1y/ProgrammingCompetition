@echo off
python.exe ../zbroj2.py <zbroj.in.%1 >output.txt
fc output.txt zbroj.out.%1
pause