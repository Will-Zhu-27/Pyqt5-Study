import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QVBoxLayout,\
    QTableWidgetItem)


class BaseModel(QWidget):
    def __init__(self):
        super(BaseModel, self).__init__()
        self.init_ui()

    def init_ui(self):
        table = QTableWidget(3, 3)
        table.setHorizontalHeaderLabels(['Name', 'Model Type', 'Date'])
        first_line = ('honese', 'Model1D', '2020-04-15')
        for i in range(0, 3):
            table_item = QTableWidgetItem(first_line[i])
            table.setItem(0, i, table_item)

        v_box = QVBoxLayout()
        v_box.addWidget(table)
        self.setLayout(v_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = BaseModel()
    model.show()
    sys.exit(app.exec_())