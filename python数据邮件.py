# encoding=utf-8
import smtplib
import string
import arrow
import pymysql
import datetime
import os,stat
import pandas as pd
import time
from pandas import DataFrame
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication


def create_report(host,port,user,passwd,db,sql,file_name):
    conn = pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db)
    cursor = conn.cursor() # 创建游标
    cursor.execute(sql)
    result = cursor.fetchall() # 获取执行结果
    result = [list(x) for x in result]

    col_result = cursor.description # 获取查询结果的字段描述
    columns = [x[0] for x in col_result]
    data = pd.DataFrame(result,columns = columns)
    file_name_new = str(datetime.date.today()) + file_name
    data.to_excel(file_name_new,index=False)

    cursor.close() # 关闭游标
    conn.close() # 关闭连接


def send_email(file_name_new,host_server,sender,receiver,Cc_receiver,mail_title,content,pwd):
    for i in range(5):
        try:
            # 传入邮件发送者，接受者，抄送者邮箱以及主题
            message = MIMEMultipart()
            message['From'] = sender
            receivers = receiver.split(',')
            message['To'] = ','.join(receivers)
            message['Cc'] = Cc_receiver
            message['Subject'] =Header(mail_title,'utf-8')
            pwd = pwd

            # 添加邮件内容
            message.attach(MIMEText(content, 'html'))


            # 读取文件
            with open(file_name_new,'rb') as file:
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
    host = '10.0.96.17'
    port = 3306
    user = 'yeqianglin'
    passwd = 'hVF#g_CU9#JhFmeB'
    db = 'db_caizhi_manage'

    sql = """
    select 
    d.Fgroup_wx_id 群id,
    replace(replace(d.Fgroup_name, char(13), ''), char(10), '') 群名称, 
    d.Fgroup_owner 群主id,
    d.Fgroup_owner_name 群主名称, 
    d.Fuser_id 用户userid,
    d.funion_id 用户unionid,
    d.Fentry_time 入群时间,
    d.Fexit_time 退群时间,
    d.Fstatus 在群状态,
    c.fopen_id 用户openid,
    c.Fname 用户昵称
    from
    (select a.Fcorp_id,a.Fgroup_wx_id,a.Fgroup_name,a.Fgroup_owner,a.Fgroup_owner_name,b.fuser_id,b.funion_id,b.Fentry_time,
    b.Fexit_time,b.Fstatus,b.Fadd_friend_time,b.Fis_deleted
    from t_group_info a join t_group_user_info b 
    where a.Fcorp_id=b.Fcorp_id and a.Fcorp_id='wx09c7b557e3f3691f' and a.Fgroup_wx_id=b.Fgroup_wx_id 
    and b.Fcorp_id='wx09c7b557e3f3691f' and a.Fis_deleted= 0  and b.Fis_deleted=0 and b.ftype=2 and b.Funion_id !='') d LEFT JOIN t_visitor c 
    ON d.funion_id=c.funion_id and d.Fcorp_id=c.Fcorp_id and c.Fcorp_id='wx09c7b557e3f3691f'
    union ALL
    select a.Fgroup_wx_id,replace(replace(a.Fgroup_name, char(13), ''), char(10), ''),a.Fgroup_owner,a.Fgroup_owner_name, b.Fuser_id,b.funion_id,b.Fentry_time,b.Fexit_time,
    b.Fstatus,'',''
    from t_group_info a join t_group_user_info b 
    where a.Fgroup_wx_id=b.Fgroup_wx_id and a.Fcorp_id='wx09c7b557e3f3691f' and a.Fis_deleted=0 and b.Fis_deleted=0
    and b.Funion_id=''            
    """

    dt = datetime.date.today()
    # 发送邮件参数设置
    host_server = 'smtp.exmail.qq.com'
    sender = 'databot@tenwit.com'
    pwd = "PJjhGNyjQs7Rhhxp"
    receiver = 'zhangl5@bocommlife.com,panh@bocommlife.com,wangds@bocommlife.com,zhuol@bocommlife.com,hujiahai@tenwit.com,yeqianglin@tenwit.com'
    Cc_receiver = 'yeqianglin@tenwit.com'
    mail_title = '【交银人寿】群信息数据回传{}'.format(dt.strftime('%Y-%m-%d'))  # 邮件标题
    content = "<p>各位好：</p>  <p> 附件是截至今天群和用户数据，请查收！</p>"
    file_name = 'data.xlsx'
    file_name_new = str(datetime.date.today()) + file_name

    create_report(host, port, user, passwd, db, sql, file_name)
    send_email(file_name_new, host_server, sender, receiver, Cc_receiver, mail_title, content, pwd)