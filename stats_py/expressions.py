#!/usr/bin/python
#-*- coding:utf-8 -*-
import re


class regular_expressions():

	total_test = re.compile("(?<=总计:)(?P<value>.*?)(?=次)")
	success_test = re.compile("(?<=成功:)(?P<value>.*?)(?=次)")
	fail_test = re.compile("(?<=失败:)(?P<value>.*?)(?=次)")

	total_time = re.compile("(?<=耗时:)(?P<value>.*?)(?=\(s\))")
	average_time = re.compile("(?<=平均:)(?P<value>.*?)(?=\(s\))")

	fail_state_of_query = re.compile("(?<=查询状态:)(?P<value>.*?)(?=次)")
	fail_restrain_card = re.compile("(?<=卡片受限:)(?P<value>.*?)(?=次)")
	fail_entry_enclosure = re.compile("(?<=进入圈子:)(?P<value>.*?)(?=次)")
	fail_connect_equipment = re.compile("(?<=连接设备:)(?P<value>.*?)(?=次)")
	fail_low_battery = re.compile("(?<=设备低电:)(?P<value>.*?)(?=次)")
	fail_read_card = re.compile("(?<=读取卡片:)(?P<value>.*?)(?=次)")
	fail_check_card = re.compile("(?<=验证卡片:)(?P<value>.*?)(?=次)")
	fail_init_card = re.compile("(?<=卡初始化:)(?P<value>.*?)(?=次)")
	fail_demand_enclosure = re.compile("(?<=圈存请求:)(?P<value>.*?)(?=次)")
	fail_write_from_enclosure = re.compile("(?<=圈存写卡:)(?P<value>.*?)(?=次)")
	fail_check_from_enclosure = re.compile("(?<=圈存确认:)(?P<value>.*?)(?=次)")
	fail_resend = re.compile("(?<=重发帧数:)(?P<value>.*?)(?=次)")
	fail_cancel_operation = re.compile("(?<=取消操作:)(?P<value>.*?)(?=次)")
