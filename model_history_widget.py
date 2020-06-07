import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QVBoxLayout,
                             QTableWidgetItem, QHeaderView)



class ModelHistoryWidget(QTableWidget):
    def __init__(self):
        super(QTableWidget, self).__init__()
        self.current_sort_type = Qt.AscendingOrder
        self.header_tuple = ('Name', 'Model Type', 'Date')
        self.init_ui()

    def init_ui(self):
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['Name', 'Model Type', 'Date'])
        self.horizontalHeader().sectionClicked.connect(self.update_order)
        # table内容不可编辑
        self.setEditTriggers(QTableWidget.NoEditTriggers)

        # table选中高亮一整行
        self.setSelectionBehavior(QTableWidget.SelectRows)

        # table仅能选中一个目标
        self.setSelectionMode(QTableWidget.SingleSelection)

        # table不显示网格
        self.setShowGrid(False)

        # table表头平铺并动态扩展
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.load_items()
        self.sortItems(2, self.current_sort_type)

    def update_order(self, index):
        if self.current_sort_type == Qt.AscendingOrder:
            self.current_sort_type = Qt.DescendingOrder
        else:
            self.current_sort_type = Qt.AscendingOrder

        self.sortItems(index, self.current_sort_type)

    def load_items(self):
        data_list = [('c', 'Model1D', '2014-04-27'),
                     ('a', 'Model2D', '2017-09-09'),
                     ('b', 'Model1D', '2015-12-27'),
                     ('b', 'Model1D', '2015-08-19'),
                     ('b', 'Model1D', '2014-08-09'),
                     ('c', 'Model3D', '2019-09-29'),
                     ('a', 'Model3D', '2020-03-27'),
                     ]
        self.setRowCount(len(data_list))
        for i in range(len(data_list)):
            for j in range(len(data_list[i])):
                item = QTableWidgetItem(data_list[i][j])
                item.setTextAlignment(Qt.AlignCenter)
                self.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = ModelHistoryWidget()
    model.show()
    sys.exit(app.exec_())

