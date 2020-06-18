from PyQt5 import QtWidgets
from capture_image import Ui_MainWindow
from capture_frames import capture_self
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.start_toolButton.clicked.connect(self.start)
        self.stop_toolButton.clicked.connect(self.stop)

    # 开始采集
    def start(self):
        # 获取图片数量
        image_num = self.image_line.text()
        if image_num == '':
            self.showMessageBox()
        else:
            btn = capture_self()
            p=btn.save_frames(image_num)  #
            if p==1:
                self.MessageBox()

    # 停止采集
    def stop(self):
        # 获取图片数量
        image_num = self.image_line.text()
        if image_num == '':
            self.showMessageBox()
        else:
            btn = capture_self()
            file_name=btn.save_video()  #
            self.player = QMediaPlayer()
            self.player.setVideoOutput(self.color_widget)
            if file_name != '':
                self.MBox()


    def showMessageBox(self):
        res_3 = QMessageBox.warning(self, "警告", "请添加图片数量，再执行该操作！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def MessageBox(self):
        res_3 = QMessageBox.information(self, '信息', '图片采集完成，请保存')
    def MBox(self):
        res_3 = QMessageBox.information(self, '信息', '视频保存完成')
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())