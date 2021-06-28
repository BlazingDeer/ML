#! python3
# program do animizacji plików c3d i niektórych plików powiązanych

from pathlib import Path
import logging, argparse
import C3DFunc
import textFunc
import xmlFunc
import os

logging.basicConfig( level=logging.INFO, format=' %(asctime)s -  %(levelname)s -  %(message)s' )
logger = logging.getLogger( __name__ )


# TODO: Przetworzyć argv oraz sprawdzic czy pliki i foldery istnieją
def is_valid_filePath(filepath):
    filepath = Path( filepath )
    if filepath.exists() and (filepath.is_file() or filepath.is_dir()):
        return filepath
    else:
        raise argparse.ArgumentTypeError( f"Ścieżka {filepath} nie jest plikiem lub nie istnieje!" )


def is_valid_destinationPath(destPath):
    destPath = Path( destPath )
    os.makedirs( destPath, exist_ok=True )
    if destPath.is_dir():
        return destPath
    else:
        raise argparse.ArgumentTypeError( f"Ścieżka {destPath} nie jest folderem!" )


parser = argparse.ArgumentParser( description="Anonimizacja plików .C3D" )
parser.add_argument( "-p", metavar="filepath", type=is_valid_filePath, required=True,
                     help="(path) Ścieżka pliku do zanonimizowania. Może być też ścieżką do folderu wtedy wszystkie pliki w tym folderze i podfolderach zostaną zanonimizowane" )
parser.add_argument( "-d", metavar="destination_path", default=Path().cwd() / "PlikiZanonimizowane",
                     type=is_valid_destinationPath,
                     help="(destination) Ścieżka do folderu w którym będzie zapisany zanonimizowany plik." )
parser.add_argument( "-n", metavar="name", type=str, required=True,
                     help="(name) Wartość string która zostanie zastąpiona podczas anonimizacji." )
parser.add_argument( "-a", default="ANON", metavar="ANON", type=str,
                     help="(anon) Wartość string wstawiana zamiast (name)." )
argumenty = vars( parser.parse_args() )
logger.info( f"{argumenty}" )


# funckja do anonimizaowania plikow
def anon(args, logger):
    # TODO: Sprawdzic koncowke pliku
    # .xml .system .xcp .vsk .history to xml
    filePath = args["p"]
    fileSuffix = Path( filePath ).suffix
    suffixSwitch = {".c3d": C3DFunc.c3d_anon,
                    ".enf": textFunc.text_anon,
                    ".mp": textFunc.text_anon,
                    ".xml": xmlFunc.xml_anon,
                    ".system": xmlFunc.xml_anon,
                    ".xcp": xmlFunc.xml_anon,
                    ".vsk": xmlFunc.xml_anon,
                    ".history": xmlFunc.xml_anon}

    # TODO: Odpowiednia funkcja dla odpowiedniego rozszerzenia pliku

    if fileSuffix in suffixSwitch.keys():
        suffixSwitch[f"{fileSuffix}"]( args, logger )
    else:
        print( f"\n\n{argumenty['p']} Nie obsługiwany typ pliku: {fileSuffix}\n\n" )


# TODO: Jeżeli podana ścieżka jest folderem to anonimizujemy pliki znajdujace sie w tym folderze lub podfolderach
ppath = Path( argumenty["p"] )

if ppath.is_dir():
    for root, dirs, files in os.walk( ppath ):
        for file in files:
            filePath = os.path.join( root, file )
            argumenty["p"] = filePath
            anon( argumenty, logger )
            print( f"Plik {filePath} został zanonimizowany." )
    print( "\nWszystkie pliki zostały zanonimizowane." )
else:
    anon( argumenty, logger )
    print( f"Plik {argumenty['p']} został zanonimizowany." )
