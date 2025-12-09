@echo off
set tempfile=C:\software\cygwin\tmp\path

@rem Note that in Python REs, to indicate a literal backslash, you still need to use two backslashes
@rem because the RE engine re-interpolates the RE argument.
C:\Python\Python3.10\python.exe -c "import os, re; path=os.environ['PATH']; path=re.sub(r'Python[\d.]+', r'"%1"', path); path=re.sub(r';$', '', path); print(path, sep='', end='')" > %tempfile%
 
set /p PATH= < %tempfile%
path
echo.
%2 --version
del %tempfile%
prompt $P$_$+$G$S
