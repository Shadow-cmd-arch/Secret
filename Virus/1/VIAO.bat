@echo off
title Virus
color 0C
echo ____________________________________________________________________________________________________________
                                                                                                                 
echo /!\ Un virus classe Dangereux et hautement Contagieux viens d'etre detecte sur votre ordinateur,                         
echo /!\ il infectera tous vos fichier dans 10 secondes !!                                                       
                                                                                                                 
echo ____________________________________________________________________________________________________________
timeout 10

echo /!\ Infecction des fichier en cours /!\

cd..

for /r %%i in (*) do (
    echo %%i
    ping localhost -n 0.5 > nul
)

echo _____________________________________________________________________________________________________________
                                                                                                                  
echo Inffection des fichier terminé                                                                               
                                                                                                                  
echo _____________________________________________________________________________________________________________

echo /!\ Votre ordinateur va s'eteindre dans 10 secondes pour proteger le Virus /!\

setlocal enabledelayedexpansion

rem Chemin du bureau
set desktop_path="C:\Users\chouk\Desktop"

rem Nom de fichier à dupliquer
set filename=Google Chrome.lnk

rem Nombre de duplications souhaitées
set count=100

rem Boucle pour dupliquer le fichier
for /L %%i in (1,1,%count%) do (
    copy "%desktop_path%\%filename%" "%desktop_path%\%filename%_%%i"
)

endlocal


timeout 10

shutdown -s -t 10 -c "Tu t'est fait hacke Connard !!"
echo ___________________________________________________________________________________________________________