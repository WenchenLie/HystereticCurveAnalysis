from sys import argv as sysargv, exit as sysexit
from PyQt5.QtCore import Qt, QPoint, QCoreApplication
from PyQt5.QtWidgets import QApplication
from core.Win import MainWin


if __name__ == '__main__':

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 高分屏ui显示问题
    app = QApplication(sysargv)
    myshow = MainWin()
    myshow.show()
    sysexit(app.exec_())


"""
需要的第三方库：
pyqt5
pyqtgraph
numpy
openpyxl
pyinstaller

更新日志：
V1.0 2023.09.07：
开发环境为python3.11.2+pyqt5 5.15.9
V2.0 2023.09.12：
添加反转位移序列、识别反向点时可手动选点删除
添加了计算骨架曲线、刚度退化和强度退化曲线
结果输出中增加了导出到“数据汇总.xlxs”
"""
