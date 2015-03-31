#!/usr/bin/python
#-*- coding:utf-8 -*-

import re,os
from expressions import regular_expressions as res
#import expressions.regular_expressions as res

files_path = "txt_files"
files = os.listdir(files_path)

dic = {'total_test':0,'success_test':0,'fail_test':0,
	'average_time':0,
	'fail_state_of_query':0,
	'fail_restrain_card':0,
	'fail_entry_enclosure':0,
	'fail_connect_equipment':0,
	'fail_low_battery':0,
	'fail_read_card':0,
	'fail_check_card':0,
	'fail_init_card':0,
	'fail_demand_enclosure':0,
	'fail_write_from_enclosure':0,
	'fail_check_from_enclosure':0,
	'fail_resend':0,
	'fail_cancel_operation':0
		}

total_test_time = 0

for file in files:
	f = os.path.join(files_path, file)
	txt = open(f, "r")
	
	for line in txt:

		line = line.replace(' ', '')

		if res.total_test.search(line):
			value = res.total_test.search(line)
			dic['total_test'] += int(value.group('value'))
			
		elif res.success_test.search(line):
			value = res.success_test.search(line)
			dic['success_test'] += int(value.group('value'))

		elif res.fail_test.search(line):
			value = res.fail_test.search(line)
			dic['fail_test'] += int(value.group('value'))

		elif res.total_time.search(line):
			value = res.total_time.search(line)
			total_test_time += float(value.group('value'))

		elif res.fail_state_of_query.search(line):
			value = res.fail_state_of_query.search(line)
			dic['fail_state_of_query'] += int(value.group('value'))

		elif res.fail_restrain_card.search(line):
			value = res.fail_restrain_card.search(line)
			dic['fail_restrain_card'] += int(value.group('value'))

		elif res.fail_entry_enclosure.search(line):
			value = res.fail_entry_enclosure.search(line)
			dic['fail_entry_enclosure'] += int(value.group('value'))

		elif res.fail_connect_equipment.search(line):
			value = res.fail_connect_equipment.search(line)
			dic['fail_connect_equipment'] += int(value.group('value'))

		elif res.fail_low_battery.search(line):
			value = res.fail_low_battery.search(line)
			dic['fail_low_battery'] += int(value.group('value'))

		elif res.fail_read_card.search(line):
			value = res.fail_read_card.search(line)
			dic['fail_read_card'] += int(value.group('value'))

		elif res.fail_check_card.search(line):
			value = res.fail_check_card.search(line)
			dic['fail_check_card'] += int(value.group('value'))

		elif res.fail_init_card.search(line):
			value = res.fail_init_card.search(line)
			dic['fail_init_card'] += int(value.group('value'))

		elif res.fail_demand_enclosure.search(line):
			value = res.fail_demand_enclosure.search(line)
			dic['fail_demand_enclosure'] += int(value.group('value'))

		elif res.fail_write_from_enclosure.search(line):
			value = res.fail_write_from_enclosure.search(line)
			dic['fail_write_from_enclosure'] += int(value.group('value'))


		elif res.fail_check_from_enclosure.search(line):
			value = res.fail_check_from_enclosure.search(line)
			dic['fail_check_from_enclosure'] += int(value.group('value'))

		elif res.fail_resend.search(line):
			value = res.fail_resend.search(line)
			dic['fail_resend'] += int(value.group('value'))

		elif res.fail_cancel_operation.search(line):
			value = res.fail_cancel_operation.search(line)
			dic['fail_cancel_operation'] += int(value.group('value'))

dic['average_time'] = total_test_time/dic['total_test']

for key in dic:
	print key, ': ', dic[key]


