import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QVBoxLayout,
                             QTableWidgetItem, QHeaderView)


class BaseModel(QWidget):
    def __init__(self):
        super(BaseModel, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.table = QTableWidget(3, 3)
        # self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Name', 'Model Type', 'Date'])
        first_line = ('honese', 'Model1D', '2020-04-15')
        for i in range(0, 3):
            table_item = QTableWidgetItem(first_line[i])
            self.table.setItem(0, i, table_item)

        # table内容不可编辑
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # table选中高亮一整行
        self.table.setSelectionBehavior(QTableWidget.SelectRows)

        # table仅能选中一个目标
        self.table.setSelectionMode(QTableWidget.SingleSelection)

        # table不显示网格
        self.table.setShowGrid(False)

        # table表头平铺并动态扩展
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.table.horizontalHeader().setHighlightSections(True)
        self.table.setCornerButtonEnabled(False)
        self.table.horizontalHeader().sectionDoubleClicked.connect(
            lambda: print('header clicked'))
        self.table.horizontalHeader().setSectionsClickable(False)
        # self.table.verticalHeader().setHighlightSections(True)
        self.table.verticalHeader().doubleClicked.connect(lambda: print(
            "vertical header clicked"))
        self.table.doubleClicked.connect(lambda: print('clicked'))
        self.table.horizontalHeader().doubleClicked.connect(lambda: print(
            'horizontal header clicked'))
        self.table.itemDoubleClicked.connect(lambda: print("item clicked"))

        self.table.cellDoubleClicked.connect(lambda: print("cell clicked"))
        v_box = QVBoxLayout()
        v_box.addWidget(self.table)
        self.setLayout(v_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = BaseModel()
    model.show()
    sys.exit(app.exec_())
