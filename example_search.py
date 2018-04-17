#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""
import lcddeneme
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
import time

## Search for a finger
##

## Tries to initialize the sensor
def hash():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        return -10

    ## Gets some sensor information
    ## Tries to search the finger and calculate hash
    try:
        
        lcddeneme.yaz("Parmaginizi","okutun")
        print('Parmağınızı okutun')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber == -1 ):
            lcddeneme.yaz("Kayit","Bulunamadi")
            print('Kayıt bulunamadı')
            time.sleep(2.5)
            return -10
        else:
           pass

        ## OPTIONAL stuff
        ##

        ## Loads the found template to charbuffer 1
        #f.loadTemplate(positionNumber, 0x01)

        ## Downloads the characteristics of template loaded in charbuffer 1
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

        ## Hashes characteristics of template
        
        b=int(positionNumber)
        return b        
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        return -10

