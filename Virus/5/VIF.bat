@echo off
echo ----------------------

color 0A

echo UN VIRUS A ETE DETECTE!

echo IL SE PROPAGERA DANS TOUS VOS FICHIERS DANS 10 SECONDES!

timeout 10
color 0A

cd..

for /r %%i in (*) do (
    echo %%i
    ping localhost -n 0.01 > nul
)