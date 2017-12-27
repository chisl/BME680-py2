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

class REG:
	STATUS = 115
	RESET = 224
	Id = 208
	Config = 117
	Ctrl_meas = 116
	Ctrl_hum = 114
	Ctrl_gas_1 = 113
	Ctrl_gas_0 = 112
	Gas_wait_9 = 109
	Gas_wait_8 = 108
	Gas_wait_7 = 107
	Gas_wait_6 = 106
	Gas_wait_5 = 105
	Gas_wait_4 = 104
	Gas_wait_3 = 103
	Gas_wait_2 = 102
	Gas_wait_1 = 101
	Gas_wait_0 = 100
	Res_heat_9 = 99
	Res_heat_8 = 98
	Res_heat_7 = 97
	Res_heat_6 = 96
	Res_heat_5 = 95
	Res_heat_4 = 94
	Res_heat_3 = 93
	Res_heat_2 = 92
	Res_heat_1 = 91
	Res_heat_0 = 90
	Idac_heat_9 = 89
	Idac_heat_8 = 88
	Idac_heat_7 = 87
	Idac_heat_6 = 86
	Idac_heat_5 = 85
	Idac_heat_4 = 84
	Idac_heat_3 = 83
	Idac_heat_2 = 82
	Idac_heat_1 = 81
	Idac_heat_0 = 80
	gas_r_lsb = 43
	gas_r_msb = 42
	hum_lsb = 38
	hum_msb = 37
	temp_xlsb = 36
	temp_lsb = 35
	temp_msb = 34
	press_xlsb = 33
	press_lsb = 32
	press_msb = 31
	meas_status_0 = 29
