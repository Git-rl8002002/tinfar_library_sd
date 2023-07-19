#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20230324
# Update   : 20230324
# Function : 台北醫學大學圖書館 SD CO2 modbusRTU to JSON API

import minimalmodbus , json , time , logging , sys , os
from control.dao import *

####################################################################################################################################
#
# monitor
#
####################################################################################################################################
class monitor: 
    
    ########
    # log 
    ########
    log_format = '%(asctime)s : %(message)s'
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d %H:%M:%S")

    #########
    # init
    #########
    def __init__(self):
        self.monitor_sd()

    #########
    # main
    #########
    def monitor_sd(self):
        
        ### record time
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        ### port 
        if sys.platform == 'win32':
            jnc_sd = minimalmodbus.Instrument(port=m_rtu_connect['win_port'] , slaveaddress=1 , mode=minimalmodbus.MODE_RTU)
        elif sys.platform == 'darwin':
            jnc_sd = minimalmodbus.Instrument(port=m_rtu_connect['mac_port2'] , slaveaddress=1 , mode=minimalmodbus.MODE_RTU)

        jnc_sd.serial.baudrate = m_rtu_para['br']
        jnc_sd.serial.timeout = 1
        jnc_sd.clear_buffers_before_each_transaction = True
        jnc_sd.close_port_after_each_call = True
        jnc_sd.debug = False

        try:
            ###  show SD read register val
            sd_val1 = jnc_sd.read_register(int(m_rtu_sensor['co2'],16),functioncode=int(m_rtu_para['fc']))
            
            ### json format
            json_val = json.dumps({'date':r_time, 'sd-co2':str(sd_val1)} , sort_keys=True , indent=4 , separators=(',',':'))
            print(json_val)

            ### save json file
            if sys.platform == 'win32':
                pass
            elif sys.platform == 'darwin':
                with open('/Users/user/eclipse-workspace/tinfar/library_sd/json/sd.json' , 'a') as file:
                    file.write(json_val)
            

        except Exception as e:
            logging.info('< Error > monitor sd : ' + str(e))
        finally:
            jnc_sd.serial.close()

####################################################################################################################################
#
# main
#
####################################################################################################################################
if __name__ == "__main__":
    run = monitor()