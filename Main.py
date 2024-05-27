from sys import argv as sysargv, exit as sysexit
from PyQt5.QtCore import Qt, QCoreApplication
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
nuitka

更新日志：
V1.0 2023.09.07：
开发环境为python3.11.2+pyqt5 5.15.9
V2.0 2023.09.12：
添加反转位移序列、识别反向点时可手动选点删除
添加了计算骨架曲线、刚度退化和强度退化曲线
结果输出中增加了导出到“数据汇总.xlxs”
V3.0 2024.05.15
优化ui逻辑
增加功能：通过滞回曲线反向点对滞回环进行分圈
修复bug：输出结果中强度退化曲线的横纵坐标相同
增加了部分代码的类型注解和文档注释
V3.1 2024.05.20
修复曲线单调化时在某些情况下会有bug
修复软件图标丢失问题
V3.2 2024.05.21
修复软件图标丢失问题
"""
