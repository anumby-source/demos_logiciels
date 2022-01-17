# Installation de OpenVINO

## installation sur PC pour commencer

On démarre:

https://docs.openvino.ai/2021.4/openvino_docs_install_guides_installing_openvino_windows.html

Problèmes:
- j'avais déjà Python 3.10.xx installé, il faut absolument installer python <= 3.8 et en ajoutant pynum

Etapes
- piloter l'installation dans un CMD en définissant le vars d'env localement
- Microsoft Visual Studio* 2019 with MSBuild
- CMake 3.14 or higher 64-bit
- Python - 64-bit
- "Intel Distribution of OpenVINO™ toolkit for Windows
- installation du driver Neural Kit "C:\Program Files (x86)\Intel\openvino_2021\inference_engine\external\MovidiusDriver"
- "C:\Program Files (x86)\Intel\openvino_2021\bin\setupvars.bat"

Démos
- https://docs.openvino.ai/2021.4/openvino_docs_get_started_get_started_scripts.html
- C:\Program Files (x86)\Intel\openvino_2021/deployment_tools/demo
- > set PATH=c:\Install\Python38;%PATH%
  > demo_squeezenet_download_convert_run.bat -d MYRIAD    (pour utiliser le chip Neural)

Problèmes:
- on doit changer la zone de stockage des fichiers temporaires car par défaut, il utilise un espace protégé
- > set BUILD_FOLDER=%USERPROFILE%\Documents\Intel\OpenVINO
  > set BUILD_FOLDER=c:\tmp\OpenVINO
- corriger la version de MSBUILD pour utiliser la version actuelle
- > if "!VS_MAJOR_VER!"=="17" set "MSBUILD_VERSION=17 2022"

OK ==>

classid probability label
------- ----------- -----
817     0.6708984   sports car, sport car
479     0.1922607   car wheel
511     0.0936890   convertible
436     0.0216064   beach wagon, station wagon, wagon, estate car, beach waggon, station waggon, waggon
751     0.0075760   racer, race car, racing car
656     0.0049667   minivan
717     0.0027428   pickup, pickup truck
581     0.0019779   grille, radiator grille
468     0.0014219   cab, hack, taxi, taxicab
661     0.0008779   Model T

