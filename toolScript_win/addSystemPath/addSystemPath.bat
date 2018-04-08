REM "run as administrator" is needed
echo %PATH% >> path.bak

REM set PATH=%PATH%;%SystemRoot%\system32
REM set PATH=%PATH%;%SystemRoot%
REM set PATH=%PATH%;%SystemRoot%\System32\Wbem
REM set PATH=%PATH%;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0






REM quick start directory

set PATH=%PATH%;G:\software\Program Files (x86) portable\_quickStart

REM python3 
set PATH=%PATH%;G:\software\Program_Files\anacoda3
set PATH=%PATH%;G:\software\Program_Files\anacoda3\Scripts

REM gcc and clang
set PATH=%PATH%;G:\software\Program_Files\msys2\usr\bin

REM pandoc
set PATH=%PATH%;G:\software\Program Files (x86) portable\_Reading_Editing\Pandoc


setx /M PATH "%PATH%"
echo "adding finished"

