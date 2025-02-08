@rem Script de compilare pentru proiect
@echo off
g++ -c -o header.o header.cpp
g++ -c -o main.o main.cpp
g++ -o main main.o header.o
main.exe
@echo on
pause