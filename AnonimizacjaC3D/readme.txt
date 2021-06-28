
argumenty do programu

-p <ścieżka do pliku> 						może być też ścieżką do folderu wtedy wszystkie pliki w tym folderze i podfolderach zostaną zanonimizowane
-d <scieżka do zapisu>						miejsce w którym zostaną zapisane zanonimizowane pliki, domyślnie jest to folder znajdujący się w folderze z programem o nazwie Plikizanonimizowane
-n <łańcuch znaków do zanonimizowania>		nazwa która zostanie zastąpiona podczas anonimizacji
-a <łańcuch znaków zastępujący -n>			nazwa która będzie zastępowała poprzednią nazwę czyli nazwę w argumencie -n, domyślnie jest to "ANON"



program wymaga zainstalowania oprogramowania anaconda lub miniconda (mniejsza wersja miniconda waży ok 50mb zamiast 500mb): 		
ANACONDA: 	https://www.anaconda.com/products/individual
MINICONDA: 	https://docs.conda.io/en/latest/miniconda.html

WINDOWS
włączyć jako administrator cmd z anacondą czyli anaconda prompt albo anaconda powershell prompt
należy utworzyć środowisko z python 3.8 np. 				conda create --name py38 python=3.8
włączyć środowisko: 										conda activate py38
pobrać bibliotekę ezc3d: 									conda install -c conda-forge ezc3d
teraz można użyć programu używając środowiska py38:			python <ścieżka do AnonimizacjaC3D.py> -p plik.c3d -n im_nazw
Aby wyjść ze środowiska należy wpisać conda deactivate.
Anaconda można usunąć poprzez panel sterowania.


LINUX

Nie używać sudo podczas instalacji.
Po zainstalowaniu anaconda należy zrestartować terminal.
Po zrestartowaniu terminala należy wpisać:				conda config --set auto_activate_base false
co spowoduje że środowisko anacondy nie będzie się automatycznie włączało podczas włączania terminala.
To samo co windows tylko zamiast w cmd to w terminalu wpisujemy komendy.
Aby wyjść ze środowiska należy wpisać conda deactivate.



Aby usunąć anaconda z linuxa należy usunąć folder z anaconda: rm -rf ~/anaconda3
Następnie usunąć wpisy anacondy z pliku 	~/.bashrc




BIBLIOTEKI:
ezc3d: https://github.com/pyomeca/ezc3d
reszta bibliotek znajduje się w Python Standard Library