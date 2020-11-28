import smtplib,sys
import pandas as pd
from email.mime.text import MIMEText
from email.utils import formatdate

# csvファイルの読み込み
df = pd.read_csv("./sample.csv") # こちら変更してください

address_li   = df.email
user_name_li = df.username
number       = user_name_li.size

FROM_ADDRESS = '自分のメールアドレス'  # こちら変更してください
MY_PASSWORD  = '上記のパスワード' # こちら変更してください
SUBJECT      = 'メールタイトル' # こちら変更してください

def create_message(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From']    = from_addr
    msg['To']      = to_addr
    msg['Date']    = formatdate()
    return msg

def send(from_addr, to_addrs, msg):
    # 今回のプログラムの場合、send関数の内部でpythonからGmailにてプログラムを送信する際に、smtplib.SMTP('smtp.gmail.com', 587)といった記述が必要です。
    # そこでsmtplibのsendmail関数を使用しています。
    # smtplibからgoogleアカウントにログインする処理やSSLにて接続するための関数を呼び出しています。
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()

for i in range(number):
    BODY = """{0}様
メールの文章です。
""".format(str(user_name_li[i]))
    subject = SUBJECT
    body    = BODY
    to_addr = address_li[i]
    msg = create_message(FROM_ADDRESS, to_addr, subject, body)
    send(FROM_ADDRESS, to_addr, msg)
    print(user_name_li[i])
    print(i)
    print("送信完了しました")
