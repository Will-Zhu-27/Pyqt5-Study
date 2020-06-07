import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ColumnSort(QWidget):
    def __init__(self):
        super(ColumnSort, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("按列排序")
        self.resize(430, 230)
        layout = QVBoxLayout()

        # 创建一个表格对象
        self.tableWidget = QTableWidget()

        # 设置行列数
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)

        layout.addWidget(self.tableWidget)

        # 设置表头的行标签
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '年龄'])
        # 创建单元格对象
        Item1 = QTableWidgetItem('老王')
        self.tableWidget.setItem(0, 0, Item1)

        Item2 = QTableWidgetItem("男")
        self.tableWidget.setItem(0, 1, Item2)

        Item3 = QTableWidgetItem('30')
        self.tableWidget.setItem(0, 2, Item3)


        Item1 = QTableWidgetItem('隔壁老王')
        self.tableWidget.setItem(1, 0, Item1)

        Item2 = QTableWidgetItem("男")
        self.tableWidget.setItem(1, 1, Item2)

        Item3 = QTableWidgetItem('32')
        self.tableWidget.setItem(1, 2,  Item3)


        Item1 = QTableWidgetItem('隔壁小王')
        self.tableWidget.setItem(2, 0, Item1)

        Item2 = QTableWidgetItem("女")
        self.tableWidget.setItem(2, 1, Item2)

        Item3 = QTableWidgetItem('18')
        self.tableWidget.setItem(2, 2, Item3)

        self.button = QPushButton("排序")
        self.button.clicked.connect(self.order)

        # 设置默认为降序排列
        self.orderType = Qt.DescendingOrder
        layout.addWidget(self.button)


        self.setLayout(layout)

    def order(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder

        # 设置排序方式 sortItems(列， 排序方式)
        self.tableWidget.sortItems(2, self.orderType)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ColumnSort()
    main.show()
    sys.exit(app.exec_())
