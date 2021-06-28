import re
import os
from pathlib import Path
import logging


def text_anon(args, logger=None):
    if logger is None:
        logging.basicConfig( level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s' )
        logger = logging.getLogger( __name__ )
    textFilePath = Path( args["p"] )
    anon = args["a"]
    logger.debug( f"textFilePath = {str( textFilePath )}" )

    subCount = 0
    fileInfoAppendix = f"\n\nFILE: {str( textFilePath )}"

    # TODO:Sprawdzić nazwe pliku

    regexString = r"^(.*?)" + args["n"] + r"(.*?)$"
    logger.debug( f"RegexString: {regexString}" )
    regexObject = re.compile( regexString, re.IGNORECASE )
    newtextFileName = textFilePath.name
    matchObject = regexObject.match( textFilePath.name )
    if matchObject is not None:
        newtextFileName = regexObject.sub( r"\1" + anon + r"\2", str( textFilePath.name ) )
        logger.debug( f"textFilePath.name --> {newtextFileName}" )
        fileInfoAppendix += f"\n\tIn newtextFileName: {textFilePath.name} --> {newtextFileName}"
        subCount += 1

    # nowy regex dla formatow w plikach tekstowych
    fileSuffix = Path( textFilePath ).suffix
    regexSuffixSwitch = {".enf": r"^(.*?=.*?)(" + args["n"] + r")(.*?)$",
                         ".mp": r"^(\$.*?)(" + args["n"] + r")(.*?=.*?)$"}
    regexSubStringSwitch = {".enf": r"\1" + anon + r"\3", ".mp": r"\1" + anon + r"\3"}

    regexString = regexSuffixSwitch[fileSuffix]
    subString = regexSubStringSwitch[fileSuffix]
    regexObject = re.compile( regexString, re.IGNORECASE )

    # TODO: otworzyć plik

    textFile = open( textFilePath )

    # TODO:znalezc miejsca i je zanonimizowac
    strline = textFile.readline()
    newtextFileString = ""
    lineNumber = 0
    while strline:
        oldstring = strline
        matchObject = regexObject.match( strline )
        newstring = regexObject.sub( subString, strline )
        if matchObject is not None:
            logger.debug( f"{oldstring} --> {newstring}" )
            fileInfoAppendix += f"\nIn text file, at line {lineNumber} : {oldstring} --> {newstring}"
            subCount += 1
        newtextFileString += newstring
        strline = textFile.readline()
        lineNumber += 1

    logging.info( f"Liczba zanonimizowanych elementów: {subCount}" )
    fileInfoAppendix += f"\nLiczba zanonimizowanych elementów: {subCount}\n"
    # TODO: zamknac plik
    textFile.close()

    # TODO: Zapisac plik w odpowiednim folderze wraz z plikiem informacyjnym z miejscami zanonimizowanymi
    newtextFilePath = Path( args["d"] ) / newtextFileName
    fileInfoPath = Path( args["d"] ) / "fileInfo.txt"

    logger.debug( f"New file path: {newtextFilePath}" )
    logger.debug( f"fileInfo.txt path: {fileInfoPath}" )

    os.makedirs( os.path.dirname( newtextFilePath ), exist_ok=True )

    newtextFile = open( newtextFilePath, "w" )
    newtextFile.write( newtextFileString )
    newtextFile.close()

    if not fileInfoPath.exists():
        fileInfoFile = open( fileInfoPath, "w+" )
    else:
        fileInfoFile = open( fileInfoPath, "a" )

    fileInfoFile.write( fileInfoAppendix )
    fileInfoFile.close()
