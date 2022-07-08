# encoding=utf-8
import smtplib
import string
import arrow
import pymysql
import datetime, calendar
import os, stat
import pandas as pd
import time
from pandas import DataFrame
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication


def create_report(host, port, user, passwd, db, sql, file_name):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
    cursor = conn.cursor()  # 创建游标
    cursor.execute(sql)
    result = cursor.fetchall()  # 获取执行结果
    result = [list(x) for x in result]

    col_result = cursor.description  # 获取查询结果的字段描述
    columns = [x[0] for x in col_result]
    data = pd.DataFrame(result, columns=columns)
    file_name_new = str(last_month) + file_name
    data.to_excel(file_name_new, index=False)

    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接


def send_email(file_name_new, host_server, sender, receiver, Cc_receiver, mail_title, content, pwd):
    for i in range(5):
        try:
            # 传入邮件发送者，接受者，抄送者邮箱以及主题
            message = MIMEMultipart()
            message['From'] = sender
            receivers = receiver.split(',')
            message['To'] = ','.join(receivers)
            message['Cc'] = Cc_receiver
            message['Subject'] = Header(mail_title, 'utf-8')
            pwd = pwd

            # 添加邮件内容
            message.attach(MIMEText(content, 'html'))

            # 读取文件
            with open(file_name_new, 'rb') as file:
                datas = file.read()

            # 添加附件
            annex = MIMEApplication(datas)
            annex["Content-Disposition"] = 'attachment; filename=' + file_name_new
            # annex.add_header('Content-Dispostion','attachment',file_name=file_name_new)
            message.attach(annex)

            # 发送邮件
            smtp = SMTP_SSL(host_server)  # ssl登录连接到邮件服务器
            smtp.set_debuglevel(1)  # 0是关闭，1是开启debug
            smtp.ehlo(host_server)  # 跟服务器打招呼
            smtp.login(sender, pwd)
            smtp.sendmail(sender, receivers, message.as_string())
            smtp.quit()
            print("1")
            time.sleep(2)
            break
        except smtplib.SMTPException:
            time.sleep(2)
            print("0")


if __name__ == '__main__':
    # host = '10.0.96.17'
    # host = 'sh-cdbrg-lsrf1qn4.sql.tencentcdb.com'
    # port = 3306
    # port = 60833
    # user = 'emr_readonly'
    # passwd = 'qpD0IgEMFx2YXFo07vr83cVOd6Wo3VdvZU'
    # db = 'db_caizhi_manage'
    host = '10.0.138.2'
    port = 7001
    user = 'hadoop'
    passwd = 'hadooptenwit666'
    db = 'caizhi_bigdata'

    # nows = arrow.now()
    # date1 = nows.shift(days=-1).format("YYYY-MM-DD")
    # date2 = nows.format("YYYY-MM-DD")

    # date3 = nows.shift(days=-1).format("YYYY-MM-DD")
    # date4 = nows.format("YYYY-MM-DD")

    # dt = datetime.date.today()

    # today = datetime.date.today()
    # last_month = today + datetime.timedelta(days=-today.day)
    # # last_month.month                                     # 月份，out: 1
    # dt=datetime.datetime.strftime(last_month,"%Y-%m")
    today = datetime.datetime.now()

    first_day_month = datetime.date(today.year, today.month, 1)

    # 上月最后一天
    date2 = first_day_month - datetime.timedelta(days=1)
    # 上月第一天
    date1 = datetime.date(date2.year, date2.month, 1)

    # 上月最后一天
    date4 = first_day_month - datetime.timedelta(days=1)
    # 上月第一天
    date3 = datetime.date(date4.year, date4.month, 1)

    # 上月 月份
    last_month = (today + datetime.timedelta(days=-today.day)).strftime('%Y-%m')

    sql = """
    select
	a.publish_task_count as '下发任务数量',
	b.finish_task_count as '任务完成数量',
	b.finish_task_count/a.publish_task_count*100+'%' as '平均任务完成率' 
from 
(
--下发任务
select 
    'a' xx ,
	 count(fstaff_id) as publish_task_count 
from caizhi_bigdata.dwd_task_staff_df
where fcorp_id='ww5f03d548ea0cdb35'
and Flevel > 1 and Fis_deleted = 0
and ((fstart_time >= '{0}' and fstart_time < '{1}' )
    or (fend_time >= '{0}' and fend_time < '{1}'))
) a 
join 
(
--完成任务
select 
    'a' yy ,
    count(1) as finish_task_count 
from caizhi_bigdata.dwd_task_progress_df
where Fcorp_id = 'ww5f03d548ea0cdb35' 
and Fis_parent = 0 
and Fstatus = 'FINISHED' and Fis_deleted = 0
and ((fstart_time >= '{2}' and fstart_time < '{3}' )
    or (fend_time >= '{2}' and fend_time < '{3}')) 
) b 
on a.xx = b.yy
    """.format(date1, date2, date3, date4)

    # 发送邮件参数设置
    host_server = 'smtp.exmail.qq.com'
    sender = 'databot@tenwit.com'
    pwd = "PJjhGNyjQs7Rhhxp"
    # receiver = 'zhumengjiao@tenwit.com,cuishijie@tenwit.com'
    receiver = 'cuishijie@tenwit.com'
    Cc_receiver = 'cuishijie@tenwit.com'
    mail_title = '【宁波银行】多个应用模块的使用数据{}'.format(last_month)  # 邮件标题
    content = "<p>各位好：</p>  <p> 附件是任务的使用数据，请查收！</p>"
    file_name = '_data.xlsx'
    file_name_new = str(last_month) + file_name

    create_report(host, port, user, passwd, db, sql, file_name)
    send_email(file_name_new, host_server, sender, receiver, Cc_receiver, mail_title, content, pwd)
