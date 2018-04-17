#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""
import lcddeneme
import hashlib
import time
from pyfingerprint.pyfingerprint import PyFingerprint


## Enrolls new finger
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
        exit(1)

    ## Gets some sensor information
    ## Tries to enroll new finger
    try:
        lcddeneme.yaz("Parmaginizi","okutun")
        print('Parmağınızı okutun')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Checks if finger is already enrolled
        result = f.searchTemplate()
        positionNumber = result[0]

        if ( positionNumber >= 0 ):
            lcddeneme.yaz("Parmak izi", "Zaten kayitli")
            print('Parmak izi Zaten kayıtlı')
            return -10
        lcddeneme.yaz("Parmaginizi","cekin")
        print('Parmağınızı çekin')
        time.sleep(2)
        lcddeneme.yaz("Parmaginizi","Tekrar okutun")
        print('Parmağınızı tekrar okutun')

        ## Wait that finger is read again
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 2
        f.convertImage(0x02)

        ## Compares the charbuffers
        if ( f.compareCharacteristics() == 0 ):
            raise Exception('Parmak izi Algılanamadı')
            return -10
        ## Creates a template
        f.createTemplate()

        ## Saves template at new position number
        positionNumber = f.storeTemplate()
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
        b=int(positionNumber)
        return (b)
    except Exception as e:
        print('İşlem başarısız')
        print(str(e))
        return -10