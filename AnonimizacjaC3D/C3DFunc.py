from ezc3d import c3d
from pathlib import Path
import logging
import re
import os


def c3d_anon(args, logger=None):
    if logger is None:
        logging.basicConfig( level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s' )
        logger = logging.getLogger( __name__ )
    # TODO: Otworzyc plik
    c3dFilePath = Path( args["p"] )
    anon = args["a"]
    logger.debug( f"c3dFilePath = {str( c3dFilePath )}" )
    c3dObject = c3d( str( c3dFilePath ) )
    # TODO: Znalezc miejsca zawierajace dane do anonimizacji i je zanonimizowac
    regexString = r"^(.*?)(" + args["n"] + r")(.*?)$"
    logger.debug( f"RegexString: {regexString}" )
    regexObject = re.compile( regexString, re.IGNORECASE )
    subCount = 0
    fileInfoAppendix = f"\n\nFILE: {c3dFilePath}"

    # TODO: nazwa pliku
    newc3dFileName = c3dFilePath.name
    matchObject = regexObject.match( c3dFilePath.name )
    if matchObject is not None:
        newc3dFileName = regexObject.sub( r"\1" + anon + r"\3", str( c3dFilePath.name ) )
        logger.debug( f"{c3dFilePath.name} --> {newc3dFileName}" )
        fileInfoAppendix += f"\n\tIn newc3dFileName: {c3dFilePath.name} --> {newc3dFileName}"
        subCount += 1

    # TODO: sprawdzanie parametrów pliku

    for key2d in list( c3dObject["parameters"].keys() ):
        for key3d in list( c3dObject["parameters"][key2d].keys() ):
            logger.debug(
                f"c3dObject[\"parameters\"][{key2d}][{key3d}].keys(): {list( c3dObject['parameters'][key2d][key3d].keys() )}" )
            if 'value' in c3dObject["parameters"][key2d][key3d].keys():
                valueList = c3dObject["parameters"][key2d][key3d]["value"]
                logger.debug( f"valueList:{valueList}" )
                if len( valueList ) > 0:
                    if not isinstance( valueList[0], str ):
                        logger.debug( f"valueList[0]={valueList[0]} is not a string" )
                        continue
                for i in range( len( valueList ) ):
                    mo = regexObject.match( valueList[i] )
                    if mo is not None:
                        newString = regexObject.sub( r"\1" + anon + r"\3", valueList[i] )
                        oldString = c3dObject["parameters"][key2d][key3d]["value"][i]
                        c3dObject["parameters"][key2d][key3d]["value"][i] = newString
                        logger.debug( oldString + " --> " + newString )
                        fileInfoAppendix += f"\n\tIn c3dObject[\"parameters\"][\"{key2d}\"][\"{key3d}\"][\"value\"][{i}]: " + oldString + " --> " + newString
                        subCount += 1
            elif key3d == "__METADATA__":
                description = c3dObject["parameters"][key2d][key3d]["DESCRIPTION"]
                mo = regexObject.match( description )
                if mo is not None:
                    newString = regexObject.sub( r"\1" + anon + r"\3", description )
                    oldString = c3dObject["parameters"][key2d][key3d]["DESCRIPTION"]
                    c3dObject["parameters"][key2d][key3d]["DESCRIPTION"] = newString
                    logger.debug( oldString + " --> " + newString )
                    fileInfoAppendix += f"\n\tIn c3dObject[\"parameters\"][\"{key2d}\"][\"{key3d}\"][\"DESCRIPTION\"]: " + oldString + " --> " + newString
                    subCount += 1

    logging.info( f"Liczba zanonimizowanych elementów: {subCount}" )
    fileInfoAppendix += f"\nLiczba zanonimizowanych elementów: {subCount}\n"

    # TODO: Zapisac plik w odpowiednim folderze wraz z plikiem informacyjnym z miejscami zanonimizowanymi
    newc3dFilePath = Path( args["d"] ) / newc3dFileName
    fileInfoPath = Path( args["d"] ) / "fileInfo.txt"

    logger.debug( f"New file path: {newc3dFilePath}" )
    logger.debug( f"fileInfo.txt path: {fileInfoPath}" )


    os.makedirs( os.path.dirname( newc3dFilePath ), exist_ok=True )

    c3dObject.write( str( newc3dFilePath ) )

    if not fileInfoPath.exists():
        fileInfoFile = open( fileInfoPath, "w+" )
    else:
        fileInfoFile = open( fileInfoPath, "a" )

    fileInfoFile.write( fileInfoAppendix )
    fileInfoFile.close()
