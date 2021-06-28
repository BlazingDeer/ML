import xml.etree.ElementTree as ET
import os
import re
from pathlib import Path
import logging


def xml_anon(args, logger=None):
    if logger is None:
        logging.basicConfig( level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s' )
        logger = logging.getLogger( __name__ )
    xmlFilePath = Path( args["p"] )
    anon = args["a"]
    logger.debug( f"xmlFilePath = {str( xmlFilePath )}" )
    subCount = 0
    fileInfoAppendix = f"\n\nFILE: {str( xmlFilePath )}"

    # TODO: otworzyć plik
    xmlFile = ET.parse( xmlFilePath )
    xmlRoot = xmlFile.getroot()

    # TODO: sprawdzić nazwę pliku (stworzyc regex)
    regexString = r"^(.*?)" + args["n"] + r"(.*?)$"
    logger.debug( f"RegexString: {regexString}" )
    regexObject = re.compile( regexString, re.IGNORECASE )
    newxmlFileName = xmlFilePath.name
    matchObject = regexObject.match( xmlFilePath.name )
    if matchObject is not None:
        newxmlFileName = regexObject.sub( r"\1" + anon + r"\2", str( xmlFilePath.name ) )
        logger.debug( f"textFilePath.name --> {newxmlFileName}" )
        fileInfoAppendix += f"\n\tIn newxmlFileName: {xmlFilePath.name} --> {newxmlFileName}"
        subCount += 1

    # TODO: przeszukać wszystkie atrybuty we wszystkich tagach oraz w zawartosci tagu
    for elem in xmlRoot.iter():
        # sprawdz zawartosc tekstu w tagu
        elemText = elem.text
        if elemText:
            matchObject = regexObject.match( elemText )
            if matchObject is not None:
                newText = regexObject.sub( r"\1" + anon + r"\2", elemText )
                elem.text = newText
                subCount += 1
                logger.debug( f"{elem.tag} text: {elemText} --> {newText}" )
                fileInfoAppendix += f"\n\tIn {elem.tag} text: {elemText} --> {newText}"

        # sprawdz zawartosc atrybutów tagu
        attributes = elem.attrib
        for key, val in attributes.items():
            matchObject = regexObject.match( val )
            if matchObject is not None:
                newVal = regexObject.sub( r"\1" + anon + r"\2", val )
                elem.set( key, newVal )
                subCount += 1
                logger.debug( f"{elem.tag} {key}: {val} --> {newVal}" )
                fileInfoAppendix += f"\n\tIn {elem.tag} {key}: {val} --> {newVal}"

    logging.info( f"Liczba zanonimizowanych elementów: {subCount}" )
    fileInfoAppendix += f"\nLiczba zanonimizowanych elementów: {subCount}\n"

    # TODO: zapisać plik xml oraz fileInfo
    newxmlFilePath = Path( args["d"] ) / newxmlFileName
    fileInfoPath = Path( args["d"] ) / "fileInfo.txt"

    logger.debug( f"New file path: {newxmlFilePath}" )
    logger.debug( f"fileInfo.txt path: {fileInfoPath}" )

    os.makedirs( os.path.dirname( newxmlFilePath ), exist_ok=True )

    xmlFile.write( newxmlFilePath, xml_declaration=True, encoding="utf-8" )

    if not fileInfoPath.exists():
        fileInfoFile = open( fileInfoPath, "w+" )
    else:
        fileInfoFile = open( fileInfoPath, "a" )

    fileInfoFile.write( fileInfoAppendix )
    fileInfoFile.close()
