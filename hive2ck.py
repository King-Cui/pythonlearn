import datetime,os,time,sys

#today = datetime.date.today()
#oneday = datetime.timedelta(days=1)
#date1 = today - oneday
#ck_dt = "{0}".format(date1)  # {ck_dt}
# ck_dt = sys.argv[1]

ck_dt = '2022-06-30'

sleep = f""" sleep 5s"""
# tableua to superset(全量)
cmd1 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf7.jar --parameters '{{"database":"caizhi_daoshu","table":"dm_tab_to_sup_staff_moment_statistics_df","isLocalOrTest":"produce","fields":"fcorp_id,fstaff_id,fdate,fuser_id,staff_name,dept_ffull_name,moment_staff_share_num,moment_client_view_num","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/daoshu/dm_tab_to_sup_staff_moment_statistics_df"}}';
"""
cmd2 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf7.jar --parameters '{{"database":"caizhi_daoshu","table":"dm_tab_to_sup_sentence_record_df","isLocalOrTest":"produce","fields":"fcorp_id,fstaff_id,fdesc,fcontent,fcopy_count,fsend_count,fcreate_time,fremark,fuser_id,fname,ffull_name","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/daoshu/dm_tab_to_sup_sentence_record_df"}}'; 
"""
cmd3 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf7.jar --parameters '{{"database":"caizhi_daoshu","table":"dm_tab_to_sup_festivalcare_df","isLocalOrTest":"produce","fields":"fdate,fcorp_id,fstaff_id,fcorp_name,staff_name,fuser_id,dept,fobj_id,fname,fis_open,fstsff_send_count,fclient_view_count","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/dm_tab_to_sup_festivalcare_df"}}';
"""
cmd4 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf7.jar --parameters '{{"database":"caizhi_daoshu","table":"dm_tab_to_sup_staff_share_poster_df","isLocalOrTest":"produce","fields":"first_times,fdate,fstaff_id,fcorp_id,fobj_id,fposter_name,foperator,fposter_type,fstaff_name,fuser_id,ffull_name,fcorp_name","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/daoshu/dm_tab_to_sup_staff_share_poster_df"}}';
"""

#KPI （分区）
cmd5 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"bi_certificate_fund_manager_d","isLocalOrTest":"produce","fields":"fdate,fcorp_id,fcorp_name,active_staff_uv,fis_status,timerange_data","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_certificate_fund_manager_d/dt={ck_dt}"}}'
"""

cmd6 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"bi_certificate_fund_manager_w","isLocalOrTest":"produce","fields":"fdate,fcorp_id,fcorp_name,active_staff_uv,fis_status,timerange_data","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_certificate_fund_manager_w/dt={ck_dt}"}}'
"""

cmd7 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"bi_tob_master_products_month","isLocalOrTest":"produce","fields":"fdate,ftype,rate_actived,dt_count,rate_activem","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_tob_master_products_month/dt={ck_dt}"}}';
"""

cmd8 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"bi_tob_master_products_week","isLocalOrTest":"produce","fields":"fdate,ftype,rate_actived,dt_count,rate_activem","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_tob_master_products_week/dt={ck_dt}"}}';
"""

cmd9 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"bi_toc_fcorp_operation_month","isLocalOrTest":"produce","fields":"fdate,fcorp_id,fcorp_name,month,last_month,last2_month,add_months,add_lastmonths,fclient_new_num,last_fclient_new_num,last2_fclient_new_num,fclient_action_times,last_fclient_action_times,fstaff_share_times,last_fstaff_share_times,fclient_share_num,fclient_product_num,funnel_ratio,fclient_sharee_num,fclient_fund_num,fund_funnel_ratio,month_fclient_fund_pv,last_month_fclient_fund_pv,fstaff_share_pv,last_fstaff_share_pv","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_toc_fcorp_operation_month/dt={ck_dt}"}}'
"""

cmd10 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"bi_toc_master_all_products_90d_week","isLocalOrTest":"produce","fields":"ftype,fc_uv,fc_pv,fc_avg_interaction,fdate","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_toc_master_all_products_90d_week/dt={ck_dt}"}}'
"""

cmd11 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"dm_tenwit_bigdata_month","isLocalOrTest":"produce","fields":"fmonth,fcorp_id,fcorp_name,fis_corp_vip,fcorp_vip_account,fis_active,fstaff_all_num,fstaff_bigb_num,fstaff_nobigb_num,fstaff_active_num,fstaff_active_bigb_num,fstaff_active_nobigb_num,fclient_num,fclient_active_num","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/dm_tenwit_bigdata_month/dt={ck_dt}"}}'
"""

cmd15 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf7.jar --parameters '{{"database":"caizhi_daoshu","table":"bi_toc_master_all_products_month","isLocalOrTest":"produce","fields":"ftype,fc_uv,fc_pv,fc_avg_interaction,fdate","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_toc_master_all_products_month/dt={ck_dt}"}}';
"""

cmd16 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"bi_tob_fcorp_rate_actived_month","isLocalOrTest":"produce","fields":"fdate,fcorp_id,fcorp_name,rate_actived_b,rate_actived_nopaper,rate_actived_share","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_tob_fcorp_rate_actived_month/dt={ck_dt}"}}';
"""


cmd17 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"bi_tob_rate_actived_month","isLocalOrTest":"produce","fields":"fdate,ftype,rate_actived,rate_actived_bb,rate_actived_b","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_tob_rate_actived_month/dt={ck_dt}"}}';
"""

cmd18 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"bi_certificate_fund_manager_m","isLocalOrTest":"produce","fields":"fdate,fcorp_id,fcorp_name,active_staff_uv,fis_status,timerange_data","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_certificate_fund_manager_m/dt={ck_dt}"}}';
"""

cmd21 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"dm_community_kpi_detailed_statistics_report_90d","isLocalOrTest":"produce","fields":"fcorp_name,fcorp_id,fgroup_wx_id,fgroup_name,fgroup_owner_name,fgroup_member_count,click_cnt","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/dm_community_kpi_detailed_statistics_report_90d/dt={ck_dt}"}}';
"""


cmd22 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048  --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar  --parameters '{{"database":"caizhi_daoshu","table":"bi_number_microfinance_employees_month","isLocalOrTest":"produce","fields":"fcorp_id,fcorp_name,fmonth_worth_staff_cnt,ftotal_date_fstaff_cnt,fdate_cnt,favg_final_staff_cnt","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_number_microfinance_employees_month/dt={ck_dt}"}}';
"""

cmd23 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048  --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar  --parameters '{{"database":"caizhi_daoshu","table":"bi_zhejiang_tnumber_microfinance_employees_month","isLocalOrTest":"produce","fields":"fcorp_id,fcorp_name,fmonth_worth_staff_cnt,ftotal_date_fstaff_cnt,fdate_cnt,favg_final_staff_cnt","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/bi_zhejiang_tnumber_microfinance_employees_month/dt={ck_dt}"}}';
"""

cmd24 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_bi","table":"bi_corp_overview_week","isLocalOrTest":"produce","fields":"fcorp_id,fcorp_name,ftotal_client,ftotal_staff,fadd_client,fclient_pv,fclient_visit_pv,fclient_potential_pv,fclient_customer_pv,fclient_uv,fclient_visit_uv,fclient_potential_uv,fclient_customer_uv,fmanager_pv,fmanager_uv,fstaff_pv,fstaff_uv,fstaff_taskmodule_pv,fstaff_taskpagelist_pv,fstaff_taskpagedetail_pv,fstaff_taskmodule_uv,fstaff_taskpagelist_uv,fstaff_taskpagedetail_uv,fdistrubution_task_count,fdate","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dws/bi_corp_overview_week/dt={ck_dt}"}}'
"""

cmd25 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_bi","table":"bi_corp_overview_month","isLocalOrTest":"produce","fields":"fcorp_id,fcorp_name,ftotal_client,ftotal_staff,fadd_client,fclient_pv,fclient_visit_pv,fclient_potential_pv,fclient_customer_pv,fclient_uv,fclient_visit_uv,fclient_potential_uv,fclient_customer_uv,fmanager_pv,fmanager_uv,fstaff_pv,fstaff_uv,fstaff_taskmodule_pv,fstaff_taskpagelist_pv,fstaff_taskpagedetail_pv,fstaff_taskmodule_uv,fstaff_taskpagelist_uv,fstaff_taskpagedetail_uv,fdistrubution_task_count,fdate","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dws/bi_corp_overview_month/dt={ck_dt}"}}'
"""


#PI 项目（全量）

cmd12 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"dm_pi_staff_task_detail_data","isLocalOrTest":"produce","fields":"fdate,fcorp_id,fcorp_name,fdept_id,fdept_path,fstaff_id,fname,ftask_info_id,ftask_name,flevel_name,fcustomer_channel_type","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/dm_pi_staff_task_detail_data"}}';
"""

cmd13 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"dm_pi_staff_task_summary","isLocalOrTest":"produce","fields":"fdate,ftask_info_id,ftask_name,flevel_name,fcustomer_channel_type,finish_staff_count,unfinish_staff_count","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/dm_pi_staff_task_summary"}}';
"""

cmd14 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"dm_pi_staff_mode_statistic_df","isLocalOrTest":"produce","fields":"fcorp_id,fcorp_name,fstaff_id,fstaff_name,fdept_id,fdept_path,ftask_total_count,ftask_finished_count,ftodo_tasks_num,fcumtomer_total_count,fcumtomer_finished_count,fdate,fmode_id,fmode_name,flevel_ids,flevel_name,fcustomer_channel_type","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/dm_pi_staff_mode_statistic_df"}}';
"""

#magic_page
cmd19 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"dm_magic_group_staff_1d_bi","isLocalOrTest":"produce","fields":"fcorp_id,fcorp_name,fstaff_id,fstaff_name,fuser_id,fuser_aes_id,ftitle,fcolumn_id,fjump_type,fgroup_name,fgroup_id,fexp_count,fclick_count,fshare_count,fdate","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/dm_magic_group_staff_1d_bi/dt={ck_dt}"}}';
"""

cmd20 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster --yarnslots 4 --yarnjobManagerMemory 2048 --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_daoshu","table":"dm_magic_page_staff_1d_bi","isLocalOrTest":"produce","fields":"fcorp_id,fcorp_name,fstaff_id,fstaff_name,fuser_id,fuser_aes_id,ftitle,fcolumn_id,fpage_count,fdate","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/dm_magic_page_staff_1d_bi/dt={ck_dt}"}}';
"""

#hive to clickhouse
cmd26 = f"""
flink run --class com.tenwit.realtime.app.daoshu.hive2clickhouse --jobmanager yarn-cluster  --yarnslots 4  --yarnjobManagerMemory 2048  --yarntaskManagerMemory 2048 --parallelism 2 --detached --yarnname daoshu /data/flink/daoshu/jars/realtime_daoshu_wyf9_fdt.jar --parameters '{{"database":"caizhi_bigdata","table":"dm_intended_customers_dynamics_di","isLocalOrTest":"produce","fields":"fid,fcorp_id,fstaff_id,fopen_id,fvisit_user_id,fvisit_user_type,funion_id,fstaff_client_id,fsnapshot_id,fnews_info_id,fobj_id,fread_record_id,ftype,fsub_type,fnick_name,fdescribe,fis_readed,fis_deleted,fcreate_by,fdate_created,flast_updated,fauto_id,finfo_type,fproduct_name,fproduct_type_id,fproduct_type_name,fbusiness_type","dt":"{ck_dt}","path":"hdfs://10.0.138.2:4007/warehouse/dm/dm_intended_customers_dynamics_di/dt={ck_dt}"}}';
"""


dict_list = {}
dict_list[cmd1] = 'tableua to superset'
dict_list[cmd2] = 'tableua to superset'
dict_list[cmd3] = 'tableua to superset'
dict_list[cmd4] = 'tableua to superset'
dict_list[cmd5] = 'KPI'
dict_list[cmd6] = 'KPI'
dict_list[cmd7] = 'KPI'
dict_list[cmd8] = 'KPI'
dict_list[cmd9] = 'KPI'
dict_list[cmd21] = 'KPI'
dict_list[cmd10] = 'KPI'
dict_list[cmd11] = 'KPI'
dict_list[cmd15] = 'KPI'
dict_list[cmd16] = 'xxxx'
dict_list[cmd17] = 'KPI'
dict_list[cmd18] = 'KPI'
dict_list[cmd22] = 'KPI'
dict_list[cmd23] = 'KPI'
dict_list[cmd24] = 'KPI'
dict_list[cmd25] = 'KPI'
dict_list[cmd12] = 'PI'
dict_list[cmd13] = 'PI'
dict_list[cmd14] = 'PI'
dict_list[cmd19] = 'magic_page'
dict_list[cmd20] = 'magic_page'
dict_list[cmd26] = 'hive to clickhouse'
# "table":"dm_pi_staff_mode_statistic_df"
key_only = ['xxxx']
# key_only = ['KPI','tableua to superset','magic_page','hive to clickhouse']
for key in dict_list.keys():
    if len(key_only) != 0 and dict_list[key] not in key_only:
        continue

    print("start run",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print(dict_list[key],":")
    print(key)
    print(key.split("--")[-1])
    # os.system(key)

    print("finished run",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print("")
    print("sleep 5s ...")
    # os.system(sleep)

print("all finished")

#日志
# # tableua to superset
# print("tableua to superset")
# print(cmd1)
# print(cmd2)
# print(cmd3)
# print(cmd4)
# #KPI
# print("KPI")
# print(cmd5)
# print(cmd6)
# print(cmd7)
# print(cmd8)
# print(cmd9)
# print(cmd10)
# print(cmd11)
# #PI
# print("PI")
# print(cmd12)
# print(cmd13)
# print(cmd14)



#执行
# # tableua to superset （11：30调度完成 12点执行）
# os.system(cmd1)
# os.system(sleep)
# os.system(cmd2)
# os.system(sleep)
# os.system(cmd3)
# os.system(sleep)
# os.system(cmd4)
# #KPI （12：30调度完成  13点执行）
# os.system(sleep)
# os.system(cmd5)
# os.system(sleep)
# os.system(cmd6)
# os.system(sleep)
# os.system(cmd7)
# os.system(sleep)
# os.system(cmd8)
# os.system(sleep)
# os.system(cmd9)
# os.system(sleep)
# os.system(cmd10)
# os.system(sleep)
# os.system(cmd11)
# os.system(sleep)
# #PI （9：30调度完成 10点执行）
# os.system(cmd12)
# os.system(sleep)
# os.system(cmd13)
# os.system(sleep)
# os.system(cmd14)

