#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20230324
# Update   : 20230324
# Function : 台北醫學大學圖書館 SD CO2 modbusRTU to JSON API

###############
#
# modbus RTU
#
###############

### tinfar SD - modbus RTU
m_rtu_connect = {'mac_port1':'/dev/tty.usbserial-1410','mac_port2':'/dev/tty.usbserial-AB0LZ3NC','linux_port':'/dev/ttyUSB0','win_port':'COM3'} 
m_rtu_para    = {'br':'9600','fc':'4','kind':'sd','tb':'modbus_sensor','protocol':'modbusRTU'}
m_rtu_sensor  = {'co2':'0x0000'}

