import time
import sys
# make sure module is in the path
sys.path.append('/home/pi/lcd')
import lcd
def yaz(satır1,satır2,a=2):
    lcd.lcd_init()
    lcd.GPIO.output(lcd.LED_ON, True)
    time.sleep(1)
    lcd.GPIO.output(lcd.LED_ON, False)
    time.sleep(1)
    lcd.GPIO.output(lcd.LED_ON, True)
    time.sleep(1)
    # set cursor to line 1
    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    # display text centered on line 1
    lcd.lcd_string(satır1, a)
    # set cursor to line 2
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    # display additional text on line 2
    lcd.lcd_string(satır2, a)
    
 
