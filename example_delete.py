#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""

from pyfingerprint.pyfingerprint import PyFingerprint


## Deletes a finger from sensor
##


## Tries to initialize the sensor
def silme(sil):    
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            pass

    except Exception as e:
        pass
    ## Gets some sensor information
   

    ## Tries to delete the template of the finger
    try:
        positionNumber = sil+1
        positionNumber = int(positionNumber)

        if ( f.deleteTemplate(positionNumber) == True ):
            return 4

    except Exception as e:
        pass
def temizle():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            pass

    except Exception as e:
        pass
    ## Gets some sensor information
   

    ## Tries to delete the template of the finger
    try:
        for i in range(2,11):
            positionNumber = i
            positionNumber = int(positionNumber)
            if ( f.deleteTemplate(positionNumber) == True ):
                if(i==10):
                   return 4

    except Exception as e:
        pass