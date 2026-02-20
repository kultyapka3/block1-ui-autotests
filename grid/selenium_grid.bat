@echo off
setlocal

start "Selenium Grid Hub" java -jar selenium-server-4.40.0.jar hub
timeout /t 5 /nobreak > NUL

start "Node 1" java -jar selenium-server-4.40.0.jar node --hub http://26.188.133.184:4444 --port 5555
start "Node 2" java -jar selenium-server-4.40.0.jar node --hub http://26.188.133.184:4444 --port 6666
start "Node 3" java -jar selenium-server-4.40.0.jar node --hub http://26.188.133.184:4444 --port 7777
start "Node 4" java -jar selenium-server-4.40.0.jar node --hub http://26.188.133.184:4444 --port 8888
start "Node 5" java -jar selenium-server-4.40.0.jar node --hub http://26.188.133.184:4444 --port 9999

echo Selenium Grid has been launched. Hub: http://26.188.133.184:4444/ui/
