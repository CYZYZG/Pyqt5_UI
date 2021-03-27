import smtplib
import email
#负责构造文本
from email.mime.text import MIMEText
#负责构造图片
from email.mime.image import MIMEImage
#负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header
class email_fun():
    def __init__(self):
    ####设置邮箱域名、发件人邮箱、邮箱授权码、收件人邮箱

    #SMTP服务器，这里使用163邮箱
    mail_host='smtp.163.com'
    #发件人邮箱
    mail_sender="lzig000@163.com"
    #邮箱授权码
    mail_license='DGJIPSTWACHDYEXV'
    #收件人邮箱，可以是多个人
    mail_receivers=['1078596492@qq.com','2550816610@qq.com']

    ####构建MIMEMultipart对象代表邮件本身，可往里添加文本、图、附件
    mm=MIMEMultipart('related')

    ####设置邮件头部内容
    #邮件主题
    subject_content="""Python邮件测试"""
    #设置发送者，注意严格遵守格式，里面邮箱为发件人邮箱
    mm['From']="sender_name<lzig000@163.com>"
    #设置接收者，注意严格遵守格式，里面邮箱为收件件人邮箱
    mm['To']="receiver_1_name<1078596492@qq.com>,receiver_2_name<2550816610@qq.com>"
    #设置邮件主题
    mm['Subject']=Header(subject_content,'utf-8')

    ####添加正文文本
    #邮件正文内容
    body_content="""你好，这是一个测试邮件！"""
    #构造文本，参数1：正文内容，参数2：文本格式，参数3：编码方式
    massage_text=MIMEText(body_content,"plain","utf-8")
    #向MIMEMultipart对象中添加文本对象
    mm.attach(massage_text)

    '''
    ####添加图片
    #二进制读取图片
    image_data=open('a.jpg','rb')
    #设置读取获取的二进制数据
    message_image=MIMEImage(image_data.read())
    #关闭刚才打开的文件
    image_data.close()
    #添加到邮件中去
    mm.attach(message_image)
    
    
    ####添加附件(excel表格为例)
    #构造附件
    atta=MIMETEXT(open("sample.xlsx",'rb').read(),'base64','utf-8')
    #设置附件信息
    attached['Content-Disposition']='attachment;filename="sample.xlsx"'
    #添加附件到邮箱中去
    mm.attach(atta)
    '''

    ####发送邮件
    #创建SMTP对象
    stp=smtplib.SMTP()
    #设置发件人邮箱的域名和端口，端口地址为25
    stp.connect(mail_host,25)
    #set)debuglevel(1)可以打印出和SMTP服务器的交互的所欲信息
    stp.set_debuglevel(1)
    #登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权
    stp.login(mail_sender,mail_license)
    #发送邮件，传递参数1：发件人邮箱地址，2收件人邮箱地址，3：把邮件内容格式改为str
    stp.sendmail(mail_sender,mail_receivers,mm.as_string())
    print("邮件发送成功")
    #关闭SMTP对象
    stp.quit()