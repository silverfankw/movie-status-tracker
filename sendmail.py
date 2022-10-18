from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendmail():
    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "[System generated] Black Panther is on sale now !!"  #郵件標題
    content["from"] = "silverfankw@gmail.com" #寄件者
    content["to"] = ", ".join(["silverfankw@gmail.com", "tonylo19961128@gmail.com"]) #收件者
    content.attach(MIMEText("This is not SPAM!!! Link should be https://www.emperorcinemas.com/en/ticketing/movie_detail/showing/1853"))  

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("silverfankw@gmail.com", "")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Email Send OK.")
        except Exception as e:
            print("Error message: ", e)


if __name__ == "__main__":
    sendmail()