import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from textIndex import fileIndex, sortbyCount


class TableModel(QAbstractTableModel):
    header = ['word', 'count']

    def __init__(self, dataList):
        QAbstractTableModel.__init__(self)
        super(TableModel, self).__init__()
        self.dataList = dataList

    def rowCount(self, parent=None):
        return len(self.dataList)

    def columnCount(self, parent=None):
        return 2

    def data(self, index, role=None):
        if role == Qt.DisplayRole or role is None:
            return self.dataList[index.row()][index.column()]

    def headerData(self, section, orientation, role=None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable


class Main(QMainWindow):
    def __init__(self, fnme, *args):
        super(Main, self).__init__(*args)

        self.tb = QTableView(self)
        self.tb.setModel(TableModel(sortbyCount(fileIndex(fnme))))
        self.tb.clicked.connect(self.onClicked)
        self.setCentralWidget(self.tb)

        self.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignCenter,
                                            QSize(225, 500), QApplication.desktop().availableGeometry()
                                            ))
        self.setWindowTitle('text index: ' + fnme)
        self.show()

    def onClicked(self):
        dataItem = self.tb.model().data(self.tb.currentIndex())
        print('selected: ', dataItem)


app = QApplication(sys.argv)
mw = Main('bible.txt')
exit(app.exec_())
