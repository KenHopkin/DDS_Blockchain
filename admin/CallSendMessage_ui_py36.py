# -*- coding: gb2312 -*-

# �����ʱ����Ҫʹ�õ�����:  pyinstaller -D CallSendMessage_ui_py36.py --collect-all websockets
#
# �����ɺ��������ļ�ͬ�ļ��е� contract.txt, contract_ABI, pwd_user.txt   ���������ִ���ļ���ͬ���ļ���
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from SendMessage_ui_py36 import *
import sendmsg_module


class MyMainWindow(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_clicked)

    def pushButton_clicked(self):
        # domain_id
        domain_id = self.lineEdit.text()
        self.printf(self.lineEdit.text())
        # sender_id
        sender_id = self.lineEdit_2.text()
        self.printf(self.lineEdit_2.text())
        # receiver_id
        receiver_id = self.lineEdit_3.text()
        self.printf(self.lineEdit_3.text())

        # message
        message = self.lineEdit_4.text()
        self.printf(self.lineEdit_4.text())

        flag = self.comboBox.currentIndex()
        self.printf(str(self.comboBox.currentIndex()))
        msg_sent = sendmsg_module.send_message(domain_id, sender_id, receiver_id, message, flag)
        if flag == 0:
            self.printf("����:" + msg_sent)
        self.printf("��Ϣ���ͳɹ�")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())