rem
rem Ce script Windows rassemble ce qu'il faut faire sur mon installation Python3.8/OpenVINO
rem our faire tourner une démo OpenVINO avec le "Neural Compute Stick 2" Intel
rem

set vino="c:\Program Files (x86)\Intel\openvino_2021\"
set py="c:\Install\Python38"
set "PATH=%py%;%py%\Scripts;%PATH%"
cd %vino%
call "bin\setupvars.bat -pyver 3.8"

cd "deployment_tools\demo"
demo_security_barrier_camera.bat -d MYRIAD -temp "c:\tmp\OpenVINO"


