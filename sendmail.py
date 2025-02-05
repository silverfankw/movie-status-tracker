from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendmail(movie_title, movie_url):
    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "[System Generated] " + movie_title + " is on sale now !!"  #郵件標題
    content["from"] = "silverfankw@gmail.com" #寄件者
    content["to"] = ", ".join(["silverfankw@gmail.com", "tonylo19961128@gmail.com"]) #收件者
    #content["to"] = ", ".join(["silverfankw@gmail.com"]) #收件者

    content.attach(MIMEText("Hi all,\n\nTicket is now available at " + movie_url))  

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("silverfankw@gmail.com", "piblvqlukwpusvhb")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Email Sent.")
        except Exception as e:
            print("Error message: ", e)


if __name__ == "__main__":
    sendmail()