import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import requests
from bs4 import BeautifulSoup


def Count(a):
    if len(a) == 3:
        return a[:2]
    else:
        return a[:1]


 

html2 = requests.get('https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=2022+%EC%88%98%EB%8A%A5+%EB%94%94%EB%8D%B0%EC%9D%B4')
soup2 = BeautifulSoup(html2.text, 'html.parser')
date = soup2.select_one('#main_pack > section.sc_new.cs_suneung._cs_CSAT > div > div.api_cs_wrap > div.sn_box > div > dl > dd:nth-child(2)').text




nowdate = datetime.now()
datelist = date.split()
yy = datelist[0]
global mm
mm = datelist[1]
dd = datelist[2]
yy = int(yy[:4])
mm = int(Count(mm))
dd = int(Count(dd))
sat = datetime(yy, mm, dd, 8, 10, 0)


Sat_D_day = sat - nowdate
Sat_D_day_day = str(Sat_D_day.days)
Sat_D_day_Hour = str(round(Sat_D_day.seconds / 3600))
print(Sat_D_day_Hour)





class suneung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        daylabel = QLabel(Sat_D_day_day + '일', self)
        font1 = daylabel.font()
        font1.setFamily('궁서체')
        font1.setPointSize(50)
        font1.setBold(True)
        daylabel.setFont(font1)
        daylabel.setAlignment(Qt.AlignCenter)


        hour = QLabel(Sat_D_day_Hour+ '시간 남음', self)
        hour.setAlignment(Qt.AlignCenter)
        font2 = hour.font()
        font2.setFamily('맑은 고딕')
        font2.setPointSize(20)
        hour.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(daylabel)
        layout.addWidget(hour)
 


        self.setLayout(layout)

        self.setWindowIcon(QIcon('resource\se.png'))
        self.setWindowTitle('인서울 드가자~')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = suneung()
    sys.exit(app.exec_())
