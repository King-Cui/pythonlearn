#!/usr/local/python3.7.9/bin/python3
import datetime
import time
import os


begin = datetime.date(2022,5,23)
end = datetime.date(2022,5,23)
d = begin
ck_database = "caizhi_bigdata"                 #{ck_database}
ck_table = "dm_intended_customers_dynamics_di" #{ck_table}
isLocalOrTest = "produce"                      #{isLocalOrTest}#{ck_fields}
ck_fields = "fid,fcorp_id,fstaff_id,fopen_id,fvisit_user_id,fvisit_user_type,funion_id,fstaff_client_id,fsnapshot_id,fnews_info_id,fobj_id,fread_record_id,ftype,fsub_type,fnick_name,fdescribe,fis_readed,fis_deleted,fcreate_by,fdate_created,flast_updated,fauto_id,finfo_type,fproduct_name,fproduct_type_id,fproduct_type_name,fbusiness_type"
delta = datetime.timedelta(days=1)
while d <= end:
        ck_dt =d.strftime("%Y-%m-%d")
        hdfs_path = "hdfs://10.1.32.4:4007/warehouse/dm/dm_intended_customers_dynamics_di/dt={0}".format(ck_dt)
        cmd = f"""flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster  --yarnslots 1  --yarnjobManagerMemory 1024  --yarntaskManagerMemory 1024  --parallelism 1 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar  --parameters '{{"database":"{ck_database}","table":"{ck_table}","isLocalOrTest":"{isLocalOrTest}","fields":"{ck_fields}","dt":"{ck_dt}","path":"{hdfs_path}"}}'"""
        print(cmd)
        # os.system(cmd)
        # d += delta
