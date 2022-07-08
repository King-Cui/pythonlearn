# import datetime, calendar
#
# time = datetime.datetime.now()
# first_day_month = datetime.date(time.year, time.month, 1)
#
# # 上月最后一天
# date2 = first_day_month - datetime.timedelta(days=1)
# # 上月第一天
# date1 = datetime.date(date2.year, date2.month, 1)
#
# # 上月最后一天
# date4 = first_day_month - datetime.timedelta(days=1)
# # 上月第一天
# date3 = datetime.date(date4.year, date4.month, 1)
#
# # 上月 月份
# # last_month = date2.month
# last_month = (time + datetime.timedelta(days=-time.day)).strftime('%Y-%m')
# # dt=datetime.datetime.strftime(last_month,"%Y-%m")
#
# dt=datetime.date.today()
#
# file_name = '_data.xlsx'
# file_name_new = str(last_month) + file_name
# print(file_name_new)
#
# # dt = datetime.date.today() + datetime.timedelta(-1)

import time 
import datetime
# import arrow
# nows = arrow.now()
# date1 = nows.shift(days=-1).format("YYYY-MM-DD")
# print(date1)
# date01 = datetime.date.today()
# date02=date01.shift(days=-1)
# print(date01)
# today = datetime.date.today()
# oneday = datetime.timedelta(days=1)
# date1=today - oneday
# print(date1)

import datetime
today = datetime.date.today()
oneday = datetime.timedelta(days=1)
date1 = today - oneday
ck_dt = "{0}".format(date1)  # {ck_dt}
hdfs_path = "hdfs://10.0.138.2:4007/warehouse/dm/bi_eventingpaper_corp_dept_staff_day/dt={0}".format(ck_dt) # {hdfs_path}

print(hdfs_path)
#
# import os
# import datetime
# today = datetime.date.today()
# oneday = datetime.timedelta(days=1)
# date1 = today - oneday
# ck_database = "caizhi_daoshu" # {ck_database}
# ck_table = "bi_eventingpaper_corp_dept_staff_day" # {ck_table}
# ck_dt = "{0}".format(date1)  # {ck_dt}
#
# isLocalOrTest = "produce" # {isLocalOrTest}  # {ck_fields}
# ck_fields = "fdate,fcorp_id,fcorp_name,dept_id,dept_ffull_name,fstaff_id,fstaff_id_encrypt,fuser_id,fuser_id_encrypt,fstaff_name,fstaff_view_pv,fstaff_view_uv,fstaff_share_pv,fstaff_share_uv,fstaff_bullish_pv,fstaff_bearish_pv,fstaff_vote_pv,fclient_view_pv,fclient_view_uv,fclient_share_pv,fclient_share_uv,fclient_bullish_pv,fclient_bearish_pv,fclient_vote_pv"
# hdfs_path = "hdfs://10.0.138.2:4007/warehouse/dm/bi_eventingpaper_corp_dept_staff_day/dt= {0}".format(ck_dt) # {hdfs_path}
# cmd=f"""
# flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster  --yarnslots 4  --yarnjobManagerMemory 2048  --yarntaskManagerMemory 2048  --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar  --parameters '{{"database":"{ck_database}","table":"{ck_table}","isLocalOrTest":"{isLocalOrTest}","fields":"{ck_fields}","dt":"{ck_dt}","path":"{hdfs_path}"}}'"""
# print(cmd)
# os.system(cmd)


