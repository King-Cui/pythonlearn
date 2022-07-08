import time
import os
import datetime


while(True):
    d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '19:35', '%Y-%m-%d%H:%M')
    d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '19:55', '%Y-%m-%d%H:%M')
    # print(d_time)
    # print(d_time1)
    #当前时间
    n_time = datetime.datetime.now()
    # print(n_time)
    # 判断当前时间是否在范围时间内
    if n_time > d_time and n_time < d_time1:
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        date1 = today - oneday
        ck_database = "caizhi_daoshu"  # {ck_database}
        ck_table = "bi_eventingpaper_corp_dept_staff_day"  # {ck_table}
        ck_dt = date1
        isLocalOrTest = "produce"  # {isLocalOrTest}
        ck_fields = "fdate,fcorp_id,fcorp_name,dept_id,dept_ffull_name,fstaff_id,fstaff_id_encrypt,fuser_id,fuser_id_encrypt,fstaff_name,fstaff_view_pv,fstaff_view_uv,fstaff_share_pv,fstaff_share_uv,fstaff_bullish_pv,fstaff_bearish_pv,fstaff_vote_pv,fclient_view_pv,fclient_view_uv,fclient_share_pv,fclient_share_uv,fclient_bullish_pv,fclient_bearish_pv,fclient_vote_pv"
        hdfs_path = "hdfs://10.0.138.2:4007/warehouse/dm/bi_eventingpaper_corp_dept_staff_day/dt={0}".format(ck_dt)  # {hdfs_path}
        cmd = f"""flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster  --yarnslots 4  --yarnjobManagerMemory 2048  --yarntaskManagerMemory 2048  --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar  --parameters '{{"database":"{ck_database}","table":"{ck_table}","isLocalOrTest":"{isLocalOrTest}","fields":"{ck_fields}","dt":"{ck_dt}","path":"{hdfs_path}"}}'"""
        print(cmd)
        # os.system(cmd)
        time.sleep(3600)
