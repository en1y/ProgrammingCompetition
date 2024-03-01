@echo off
python.exe ../Wordle.py <wordle.in.%1 >output.txt
fc output.txt wordle.out.%1
pause