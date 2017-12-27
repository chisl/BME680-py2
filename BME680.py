#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""BME680: Low-power gas, pressure, temperature and humidity sensor"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Bosch Sensortec"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

from BME680_constants import *

# name:        BME680
# description: Low-power gas, pressure, temperature and humidity sensor
# manuf:       Bosch Sensortec
# version:     0.1
# url:         https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BME680-DS001-00.pdf
# date:        2017-12-18


# Derive from this class and implement read and write
class BME680_Base:
	"""Low-power gas, pressure, temperature and humidity sensor"""
	# Register STATUS
	# 5.3.1.4
	#       In SPI mode complete memory page is accessed using page 0 & page 1.
	#       Register spi_mem_page is used for page selection. After power-on, spi_mem_page
	#       is in its reset state and page 0(0x00 to 0x7F) will be active. Page1 (0x7F to 0xFF)
	#       will be active on setting spi_mem_page. Please refer Table 15 for better
	#       understanding. 
	
	
	def setSTATUS(self, val):
		"""Set register STATUS"""
		self.write(REG.STATUS, val, 8)
	
	def getSTATUS(self):
		"""Get register STATUS"""
		return self.read(REG.STATUS, 8)
	
	# Bits unused_0
	# Bits spi_mem_page
	# Selects memory map page in SPI mode
	# Bits unused_1
	# Register RESET
	# 5.3.1.5
	#       Writing 0xB6 to this register initiates a soft-reset procedure, which has the
	#       same effect like power-on reset. The default value stored in this register is 0x00. 
	
	
	def setRESET(self, val):
		"""Set register RESET"""
		self.write(REG.RESET, val, 8)
	
	def getRESET(self):
		"""Get register RESET"""
		return self.read(REG.RESET, 8)
	
	# Bits Reset
	# Register Id
	# 5.3.1.6
	#       Chip id of the device 
	
	
	def setId(self, val):
		"""Set register Id"""
		self.write(REG.Id, val, 8)
	
	def getId(self):
		"""Get register Id"""
		return self.read(REG.Id, 8)
	
	# Bits chip_id
	# Register Config
	# 5.3.1.2 Enable SPI 3 wire mode
	#       5.3.2.4 IIR filter settings 
	
	
	def setConfig(self, val):
		"""Set register Config"""
		self.write(REG.Config, val, 8)
	
	def getConfig(self):
		"""Get register Config"""
		return self.read(REG.Config, 8)
	
	# Bits unused_0
	# Bits filter
	# IIR filter settings
	#           IIR filter applies to temperature and pressure data but not to humidity and gas data.
	#           The data coming from the ADC are filtered and then loaded into the data registers.
	#           The temperature and pressure result registers are updated together at the same time
	#           at the end of the measurement. IIR filter output resolution is 20 bits. The result
	#           registers are reset to value 0x80000 when the temperature and/or pressure measurements
	#           have been skipped (osrs_x=”000‟). The appropriate filter memory is kept unchanged
	#           (the value from the last measurement is kept). When the appropriate OSRS register is
	#           set back to nonzero, then the first value stored to the result registers are filtered. 
	
	# Bits unused_1
	# Bits spi_3w_en
	# Enable SPI 3 wire mode
	# Register Ctrl_meas
	# 5.3.1.3 Select sensor power mode
	#       5.3.2.2 Temperature oversampling settings
	#       5.3.2.3 Pressure oversampling settings 
	
	
	def setCtrl_meas(self, val):
		"""Set register Ctrl_meas"""
		self.write(REG.Ctrl_meas, val, 8)
	
	def getCtrl_meas(self):
		"""Get register Ctrl_meas"""
		return self.read(REG.Ctrl_meas, 8)
	
	# Bits osrs_t
	# Temperature oversampling settings 
	# Bits osrs_p
	# Pressure oversampling settings 
	# Bits mode
	# Select sensor power mode 
	# Register Ctrl_hum
	# 5.3.1.1 SPI 3 wire interrupt enable
	#       5.3.2.1 Controls over sampling setting of humidity sensor 
	
	
	def setCtrl_hum(self, val):
		"""Set register Ctrl_hum"""
		self.write(REG.Ctrl_hum, val, 8)
	
	def getCtrl_hum(self):
		"""Get register Ctrl_hum"""
		return self.read(REG.Ctrl_hum, 8)
	
	# Bits unused_0
	# Bits spi_3w_int_en
	# New data interrupt can be enabled if the device is in SPI 3 wire mode and pi_3w_int_en=1.
	#         The new data interrupt is then indicated on the SDO pad. 
	
	# Bits unused_1
	# Bits osrs_h
	# Controls over sampling setting of humidity sensor 
	# Register Ctrl_gas_1
	# 5.3.3.5 Heater profile selection
	#       5.3.3.6 Run Gas 
	
	
	def setCtrl_gas_1(self, val):
		"""Set register Ctrl_gas_1"""
		self.write(REG.Ctrl_gas_1, val, 8)
	
	def getCtrl_gas_1(self):
		"""Get register Ctrl_gas_1"""
		return self.read(REG.Ctrl_gas_1, 8)
	
	# Bits unused_0
	# Bits run_gas
	# The gas conversions are started only in appropriate mode if run_gas = ‘1’ 
	# Bits nb_conv
	# Indicates index of heater set point that will be used in forced mode 
	# Register Ctrl_gas_0
	# 5.3.3.4 Heater off 
	
	def setCtrl_gas_0(self, val):
		"""Set register Ctrl_gas_0"""
		self.write(REG.Ctrl_gas_0, val, 8)
	
	def getCtrl_gas_0(self):
		"""Get register Ctrl_gas_0"""
		return self.read(REG.Ctrl_gas_0, 8)
	
	# Bits unused_0
	# Bits heat_off
	# Turn off current injected to heater by setting bit to one 
	# Bits unused_1
	# Register Gas_wait_9
	# 5.3.3.3 Gas Sensor wait time
	#       The time between the beginning of the heat phase and the start of gas sensor resistance
	#       conversion depends on gas_wait_x setting as mentioned below. 
	
	
	def setGas_wait_9(self, val):
		"""Set register Gas_wait_9"""
		self.write(REG.Gas_wait_9, val, 8)
	
	def getGas_wait_9(self):
		"""Get register Gas_wait_9"""
		return self.read(REG.Gas_wait_9, 8)
	
	# Bits gas_wait_mult
	# Gas sensor wait time multiplication factor 
	# Bits gas_wait_val
	# 64 timer values with 1 ms step sizes, all zeros means no wait 
	# Register Gas_wait_8
	# 5.3.3.3 Gas Sensor wait time 
	
	def setGas_wait_8(self, val):
		"""Set register Gas_wait_8"""
		self.write(REG.Gas_wait_8, val, 8)
	
	def getGas_wait_8(self):
		"""Get register Gas_wait_8"""
		return self.read(REG.Gas_wait_8, 8)
	
	# Bits gas_wait_mult
	# Gas sensor wait time multiplication factor 
	# Bits gas_wait_val
	# 64 timer values with 1 ms step sizes, all zeros means no wait 
	# Register Gas_wait_7
	# 5.3.3.3 Gas Sensor wait time 
	
	def setGas_wait_7(self, val):
		"""Set register Gas_wait_7"""
		self.write(REG.Gas_wait_7, val, 8)
	
	def getGas_wait_7(self):
		"""Get register Gas_wait_7"""
		return self.read(REG.Gas_wait_7, 8)
	
	# Bits gas_wait_mult
	# Gas sensor wait time multiplication factor 
	# Bits gas_wait_val
	# 64 timer values with 1 ms step sizes, all zeros means no wait 
	# Register Gas_wait_6
	# 5.3.3.3 Gas Sensor wait time 
	
	def setGas_wait_6(self, val):
		"""Set register Gas_wait_6"""
		self.write(REG.Gas_wait_6, val, 8)
	
	def getGas_wait_6(self):
		"""Get register Gas_wait_6"""
		return self.read(REG.Gas_wait_6, 8)
	
	# Bits gas_wait_mult
	# Gas sensor wait time multiplication factor 
	# Bits gas_wait_val
	# 64 timer values with 1 ms step sizes, all zeros means no wait 
	# Register Gas_wait_5
	# 5.3.3.3 Gas Sensor wait time 
	
	def setGas_wait_5(self, val):
		"""Set register Gas_wait_5"""
		self.write(REG.Gas_wait_5, val, 8)
	
	def getGas_wait_5(self):
		"""Get register Gas_wait_5"""
		return self.read(REG.Gas_wait_5, 8)
	
	# Bits gas_wait_mult
	# Gas sensor wait time multiplication factor 
	# Bits gas_wait_val
	# 64 timer values with 1 ms step sizes, all zeros means no wait 
	# Register Gas_wait_4
	# 5.3.3.3 Gas Sensor wait time 
	
	def setGas_wait_4(self, val):
		"""Set register Gas_wait_4"""
		self.write(REG.Gas_wait_4, val, 8)
	
	def getGas_wait_4(self):
		"""Get register Gas_wait_4"""
		return self.read(REG.Gas_wait_4, 8)
	
	# Bits gas_wait_mult
	# Gas sensor wait time multiplication factor 
	# Bits gas_wait_val
	# 64 timer values with 1 ms step sizes, all zeros means no wait 
	# Register Gas_wait_3
	# 5.3.3.3 Gas Sensor wait time 
	
	def setGas_wait_3(self, val):
		"""Set register Gas_wait_3"""
		self.write(REG.Gas_wait_3, val, 8)
	
	def getGas_wait_3(self):
		"""Get register Gas_wait_3"""
		return self.read(REG.Gas_wait_3, 8)
	
	# Bits gas_wait_mult
	# Gas sensor wait time multiplication factor 
	# Bits gas_wait_val
	# 64 timer values with 1 ms step sizes, all zeros means no wait 
	# Register Gas_wait_2
	# 5.3.3.3 Gas Sensor wait time 
	
	def setGas_wait_2(self, val):
		"""Set register Gas_wait_2"""
		self.write(REG.Gas_wait_2, val, 8)
	
	def getGas_wait_2(self):
		"""Get register Gas_wait_2"""
		return self.read(REG.Gas_wait_2, 8)
	
	# Bits gas_wait_mult
	# Gas sensor wait time multiplication factor 
	# Bits gas_wait_val
	# 64 timer values with 1 ms step sizes, all zeros means no wait 
	# Register Gas_wait_1
	# 5.3.3.3 Gas Sensor wait time 
	
	def setGas_wait_1(self, val):
		"""Set register Gas_wait_1"""
		self.write(REG.Gas_wait_1, val, 8)
	
	def getGas_wait_1(self):
		"""Get register Gas_wait_1"""
		return self.read(REG.Gas_wait_1, 8)
	
	# Bits gas_wait_mult
	# Gas sensor wait time multiplication factor 
	# Bits gas_wait_val
	# 64 timer values with 1 ms step sizes, all zeros means no wait 
	# Register Gas_wait_0
	# 5.3.3.3 Gas Sensor wait time 
	
	def setGas_wait_0(self, val):
		"""Set register Gas_wait_0"""
		self.write(REG.Gas_wait_0, val, 8)
	
	def getGas_wait_0(self):
		"""Get register Gas_wait_0"""
		return self.read(REG.Gas_wait_0, 8)
	
	# Bits gas_wait_mult
	# Gas sensor wait time multiplication factor 
	# Bits gas_wait_val
	# 64 timer values with 1 ms step sizes, all zeros means no wait 
	# Register Res_heat_9
	# 5.3.3.2 Target heater resistance 
	
	def setRes_heat_9(self, val):
		"""Set register Res_heat_9"""
		self.write(REG.Res_heat_9, val, 8)
	
	def getRes_heat_9(self):
		"""Get register Res_heat_9"""
		return self.read(REG.Res_heat_9, 8)
	
	# Bits res_heat
	# Decimal value that needs to be stored for achieving target heater resistance 
	# Register Res_heat_8
	# 5.3.3.2 Target heater resistance 
	
	def setRes_heat_8(self, val):
		"""Set register Res_heat_8"""
		self.write(REG.Res_heat_8, val, 8)
	
	def getRes_heat_8(self):
		"""Get register Res_heat_8"""
		return self.read(REG.Res_heat_8, 8)
	
	# Bits res_heat
	# Decimal value that needs to be stored for achieving target heater resistance 
	# Register Res_heat_7
	# 5.3.3.2 Target heater resistance 
	
	def setRes_heat_7(self, val):
		"""Set register Res_heat_7"""
		self.write(REG.Res_heat_7, val, 8)
	
	def getRes_heat_7(self):
		"""Get register Res_heat_7"""
		return self.read(REG.Res_heat_7, 8)
	
	# Bits res_heat
	# Decimal value that needs to be stored for achieving target heater resistance 
	# Register Res_heat_6
	# 5.3.3.2 Target heater resistance 
	
	def setRes_heat_6(self, val):
		"""Set register Res_heat_6"""
		self.write(REG.Res_heat_6, val, 8)
	
	def getRes_heat_6(self):
		"""Get register Res_heat_6"""
		return self.read(REG.Res_heat_6, 8)
	
	# Bits res_heat
	# Decimal value that needs to be stored for achieving target heater resistance 
	# Register Res_heat_5
	# 5.3.3.2 Target heater resistance 
	
	def setRes_heat_5(self, val):
		"""Set register Res_heat_5"""
		self.write(REG.Res_heat_5, val, 8)
	
	def getRes_heat_5(self):
		"""Get register Res_heat_5"""
		return self.read(REG.Res_heat_5, 8)
	
	# Bits res_heat
	# Decimal value that needs to be stored for achieving target heater resistance 
	# Register Res_heat_4
	# 5.3.3.2 Target heater resistance 
	
	def setRes_heat_4(self, val):
		"""Set register Res_heat_4"""
		self.write(REG.Res_heat_4, val, 8)
	
	def getRes_heat_4(self):
		"""Get register Res_heat_4"""
		return self.read(REG.Res_heat_4, 8)
	
	# Bits res_heat
	# Decimal value that needs to be stored for achieving target heater resistance 
	# Register Res_heat_3
	# 5.3.3.2 Target heater resistance 
	
	def setRes_heat_3(self, val):
		"""Set register Res_heat_3"""
		self.write(REG.Res_heat_3, val, 8)
	
	def getRes_heat_3(self):
		"""Get register Res_heat_3"""
		return self.read(REG.Res_heat_3, 8)
	
	# Bits res_heat
	# Decimal value that needs to be stored for achieving target heater resistance 
	# Register Res_heat_2
	# 5.3.3.2 Target heater resistance 
	
	def setRes_heat_2(self, val):
		"""Set register Res_heat_2"""
		self.write(REG.Res_heat_2, val, 8)
	
	def getRes_heat_2(self):
		"""Get register Res_heat_2"""
		return self.read(REG.Res_heat_2, 8)
	
	# Bits res_heat
	# Decimal value that needs to be stored for achieving target heater resistance 
	# Register Res_heat_1
	# 5.3.3.2 Target heater resistance 
	
	def setRes_heat_1(self, val):
		"""Set register Res_heat_1"""
		self.write(REG.Res_heat_1, val, 8)
	
	def getRes_heat_1(self):
		"""Get register Res_heat_1"""
		return self.read(REG.Res_heat_1, 8)
	
	# Bits res_heat
	# Decimal value that needs to be stored for achieving target heater resistance 
	# Register Res_heat_0
	# 5.3.3.2 Target heater resistance 
	
	def setRes_heat_0(self, val):
		"""Set register Res_heat_0"""
		self.write(REG.Res_heat_0, val, 8)
	
	def getRes_heat_0(self):
		"""Get register Res_heat_0"""
		return self.read(REG.Res_heat_0, 8)
	
	# Bits res_heat
	# Decimal value that needs to be stored for achieving target heater resistance 
	# Register Idac_heat_9
	# 5.3.3.1 Heater current
	#       BME680 contains a heater control block that will inject enough current into the heater
	#       resistance to achieve the requested heater temperature. There is a control loop which
	#       periodically measures heater resistance value and adapts the value of current injected
	#       from a DAC.
	#       The heater operation could be speeded up by setting an initial heater current for a target
	#       heater temperature by using register idac_heat_x<7:0>. This step is optional since the control
	#       loop will find the current after a few iterations anyway. The current injected to the heater in
	#       mA can be calculated by: (idac_heat_7_1 + 1) / 8, where idac_heat_7_1 is the decimal value
	#       stored in idac_heat<7:1> (unsigned, value from 0 to 127). 
	
	
	def setIdac_heat_9(self, val):
		"""Set register Idac_heat_9"""
		self.write(REG.Idac_heat_9, val, 8)
	
	def getIdac_heat_9(self):
		"""Get register Idac_heat_9"""
		return self.read(REG.Idac_heat_9, 8)
	
	# Bits idac_heat
	# idac_heat of particular heater set point
	# Register Idac_heat_8
	# 5.3.3.1 Heater current 
	
	def setIdac_heat_8(self, val):
		"""Set register Idac_heat_8"""
		self.write(REG.Idac_heat_8, val, 8)
	
	def getIdac_heat_8(self):
		"""Get register Idac_heat_8"""
		return self.read(REG.Idac_heat_8, 8)
	
	# Bits idac_heat
	# idac_heat of particular heater set point
	# Register Idac_heat_7
	# 5.3.3.1 Heater current 
	
	def setIdac_heat_7(self, val):
		"""Set register Idac_heat_7"""
		self.write(REG.Idac_heat_7, val, 8)
	
	def getIdac_heat_7(self):
		"""Get register Idac_heat_7"""
		return self.read(REG.Idac_heat_7, 8)
	
	# Bits idac_heat
	# idac_heat of particular heater set point
	# Register Idac_heat_6
	# 5.3.3.1 Heater current 
	
	def setIdac_heat_6(self, val):
		"""Set register Idac_heat_6"""
		self.write(REG.Idac_heat_6, val, 8)
	
	def getIdac_heat_6(self):
		"""Get register Idac_heat_6"""
		return self.read(REG.Idac_heat_6, 8)
	
	# Bits idac_heat
	# idac_heat of particular heater set point
	# Register Idac_heat_5
	# 5.3.3.1 Heater current 
	
	def setIdac_heat_5(self, val):
		"""Set register Idac_heat_5"""
		self.write(REG.Idac_heat_5, val, 8)
	
	def getIdac_heat_5(self):
		"""Get register Idac_heat_5"""
		return self.read(REG.Idac_heat_5, 8)
	
	# Bits idac_heat
	# idac_heat of particular heater set point
	# Register Idac_heat_4
	# 5.3.3.1 Heater current 
	
	def setIdac_heat_4(self, val):
		"""Set register Idac_heat_4"""
		self.write(REG.Idac_heat_4, val, 8)
	
	def getIdac_heat_4(self):
		"""Get register Idac_heat_4"""
		return self.read(REG.Idac_heat_4, 8)
	
	# Bits idac_heat
	# idac_heat of particular heater set point
	# Register Idac_heat_3
	# 5.3.3.1 Heater current 
	
	def setIdac_heat_3(self, val):
		"""Set register Idac_heat_3"""
		self.write(REG.Idac_heat_3, val, 8)
	
	def getIdac_heat_3(self):
		"""Get register Idac_heat_3"""
		return self.read(REG.Idac_heat_3, 8)
	
	# Bits idac_heat
	# idac_heat of particular heater set point
	# Register Idac_heat_2
	# 5.3.3.1 Heater current 
	
	def setIdac_heat_2(self, val):
		"""Set register Idac_heat_2"""
		self.write(REG.Idac_heat_2, val, 8)
	
	def getIdac_heat_2(self):
		"""Get register Idac_heat_2"""
		return self.read(REG.Idac_heat_2, 8)
	
	# Bits idac_heat
	# idac_heat of particular heater set point
	# Register Idac_heat_1
	# 5.3.3.1 Heater current 
	
	def setIdac_heat_1(self, val):
		"""Set register Idac_heat_1"""
		self.write(REG.Idac_heat_1, val, 8)
	
	def getIdac_heat_1(self):
		"""Get register Idac_heat_1"""
		return self.read(REG.Idac_heat_1, 8)
	
	# Bits idac_heat
	# idac_heat of particular heater set point
	# Register Idac_heat_0
	# 5.3.3.1 Heater current 
	
	def setIdac_heat_0(self, val):
		"""Set register Idac_heat_0"""
		self.write(REG.Idac_heat_0, val, 8)
	
	def getIdac_heat_0(self):
		"""Get register Idac_heat_0"""
		return self.read(REG.Idac_heat_0, 8)
	
	# Bits idac_heat
	# idac_heat of particular heater set point
	# Register gas_r_lsb
	# 5.3.4.5 Gas resistance range
	#       5.3.4.4 Gas resistance data
	#       5.3.5.5 Gas valid status
	#       5.3.5.6 Heater Stability Status 
	
	
	def setgas_r_lsb(self, val):
		"""Set register gas_r_lsb"""
		self.write(REG.gas_r_lsb, val, 8)
	
	def getgas_r_lsb(self):
		"""Get register gas_r_lsb"""
		return self.read(REG.gas_r_lsb, 8)
	
	# Bits gas_r
	# Contains the LSB part gas resistance [1:0] of the raw gas resistance. 
	# Bits gas_valid_r
	# Gas valid bit
	#           In each TPHG sequence contains a gas measurement slot, either a real one which
	#           result is used or a dummy one to keep a constant sampling rate and predictable
	#           device timing. A real gas conversion (i.e., not a dummy one) is indicated by the
	#           gas_valid_r status register. 
	
	# Bits heat_stab_r
	# Heater stability bit
	# Bits gas_range_r
	# Contains ADC range of measured gas resistance
	# Register gas_r_msb
	# 5.3.4.4 Gas resistance data 
	
	def setgas_r_msb(self, val):
		"""Set register gas_r_msb"""
		self.write(REG.gas_r_msb, val, 8)
	
	def getgas_r_msb(self):
		"""Get register gas_r_msb"""
		return self.read(REG.gas_r_msb, 8)
	
	# Bits gas_r
	# Contains the MSB part gas resistance [9:2] of the raw gas resistance. 
	# Register hum_lsb
	# 5.3.4.3 Humidity data 
	
	def sethum_lsb(self, val):
		"""Set register hum_lsb"""
		self.write(REG.hum_lsb, val, 8)
	
	def gethum_lsb(self):
		"""Get register hum_lsb"""
		return self.read(REG.hum_lsb, 8)
	
	# Bits hum_lsb
	# Contains the LSB part [7:0] of the raw humidity measurement output data. 
	# Register hum_msb
	# 5.3.4.3 Humidity data 
	
	def sethum_msb(self, val):
		"""Set register hum_msb"""
		self.write(REG.hum_msb, val, 8)
	
	def gethum_msb(self):
		"""Get register hum_msb"""
		return self.read(REG.hum_msb, 8)
	
	# Bits hum_msb
	# Contains the MSB part [15:8] of the raw humidity measurement output data. 
	# Register temp_xlsb
	# 5.3.4.2 Temp data 
	
	def settemp_xlsb(self, val):
		"""Set register temp_xlsb"""
		self.write(REG.temp_xlsb, val, 8)
	
	def gettemp_xlsb(self):
		"""Get register temp_xlsb"""
		return self.read(REG.temp_xlsb, 8)
	
	# Bits temp_xlsb
	# Contains the XLSB part [3:0] of the raw temperature measurement output data.
	#           Contents depend on temperature resolution controlled by oversampling setting. 
	
	# Bits unused_0
	# Register temp_lsb
	# 5.3.4.2 Temp data 
	
	def settemp_lsb(self, val):
		"""Set register temp_lsb"""
		self.write(REG.temp_lsb, val, 8)
	
	def gettemp_lsb(self):
		"""Get register temp_lsb"""
		return self.read(REG.temp_lsb, 8)
	
	# Bits temp_lsb
	# Contains the LSB part [11:4] of the raw temperature measurement output data. 
	# Register temp_msb
	# 5.3.4.2 Temp data 
	
	def settemp_msb(self, val):
		"""Set register temp_msb"""
		self.write(REG.temp_msb, val, 8)
	
	def gettemp_msb(self):
		"""Get register temp_msb"""
		return self.read(REG.temp_msb, 8)
	
	# Bits temp_msb
	# Contains the MSB part [19:12] of the raw temperature measurement output data. 
	# Register press_xlsb
	# 5.3.4.1 Pressure data 
	
	def setpress_xlsb(self, val):
		"""Set register press_xlsb"""
		self.write(REG.press_xlsb, val, 8)
	
	def getpress_xlsb(self):
		"""Get register press_xlsb"""
		return self.read(REG.press_xlsb, 8)
	
	# Bits press_xlsb
	# Contains the XLSB part [3:0] of the raw pressure measurement output data.
	#           Contents depend on pressure resolution controlled by oversampling setting. 
	
	# Bits unused_0
	# Register press_lsb
	# 5.3.4.1 Pressure data 
	
	def setpress_lsb(self, val):
		"""Set register press_lsb"""
		self.write(REG.press_lsb, val, 8)
	
	def getpress_lsb(self):
		"""Get register press_lsb"""
		return self.read(REG.press_lsb, 8)
	
	# Bits press_lsb
	# Contains the LSB part [11:4] of the raw pressure measurement output data 
	# Register press_msb
	# 5.3.4.1 Pressure data 
	
	def setpress_msb(self, val):
		"""Set register press_msb"""
		self.write(REG.press_msb, val, 8)
	
	def getpress_msb(self):
		"""Get register press_msb"""
		return self.read(REG.press_msb, 8)
	
	# Bits press_msb
	# Contains the MSB part [19:12] of the raw pressure measurement output data. 
	# Register meas_status_0
	# 5.3.5.1 New data status
	#       5.3.5.2 Gas measuring status
	#       5.3.5.3 Measuring status
	#       5.3.5.4 Gas Measurement Index 
	
	
	def setmeas_status_0(self, val):
		"""Set register meas_status_0"""
		self.write(REG.meas_status_0, val, 8)
	
	def getmeas_status_0(self):
		"""Get register meas_status_0"""
		return self.read(REG.meas_status_0, 8)
	
	# Bits new_data_0
	# New data flag
	#           The measured data are stored into the output data registers at the end
	#           of each TPHG conversion phase along with status flags and index of measurement. 
	
	# Bits gas_measuring
	# Gas measuring status flag
	#           Measuring bit is set to “1‟ only during gas measurements, goes to “0‟ as soon as
	#           measurement is completed and data transferred to data registers. The registers storing
	#           the configuration values for the measurement (gas_wait_shared, gas_wait_x, res_heat_x,
	#           idac_heat_x, image registers) should not be changed when the device is measuring. 
	
	# Bits measuring
	# Measuring status flag
	#           Measuring status will be set to ‘1’ whenever a conversion (temperature, pressure,
	#           humidity and gas) is running and back to ‘0’ when the results have been transferred
	#           to the data registers. 
	
	# Bits unused_0
	# Bits gas_meas_index_0
	# Gas measurement index
	#           User can program a sequence of up to 10 conversions by setting nb_conv<3:0>.
	#           Each conversion has its own heater resistance target but 3 field registers to store
	#           conversion results. The actual gas conversion number in the measurement sequence
	#           (up to 10 conversions numbered from 0 to 9) is stored in gas_meas_index register. 
	
