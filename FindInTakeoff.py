# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rando\PycharmProjects\MySQLInterface\FindInTakeoff.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FindTakeoffDialog(object):
    def setupUi(self, FindTakeoffDialog):
        FindTakeoffDialog.setObjectName("FindTakeoffDialog")
        FindTakeoffDialog.resize(400, 545)
        self.comboBoxColumn = QtWidgets.QComboBox(FindTakeoffDialog)
        self.comboBoxColumn.setGeometry(QtCore.QRect(240, 60, 111, 22))
        self.comboBoxColumn.setObjectName("comboBoxColumn")
        self.comboBoxColumn.addItem("")
        self.comboBoxColumn.addItem("")
        self.comboBoxColumn.addItem("")
        self.comboBoxColumn.addItem("")
        self.comboBoxColumn.addItem("")
        self.textEditValue = QtWidgets.QTextEdit(FindTakeoffDialog)
        self.textEditValue.setGeometry(QtCore.QRect(240, 100, 131, 31))
        self.textEditValue.setObjectName("textEditValue")
        self.tableWidget = QtWidgets.QTableWidget(FindTakeoffDialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 210, 371, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(FindTakeoffDialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 480, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(FindTakeoffDialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FindTakeoffDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(FindTakeoffDialog)
        QtCore.QMetaObject.connectSlotsByName(FindTakeoffDialog)

    def retranslateUi(self, FindTakeoffDialog):
        _translate = QtCore.QCoreApplication.translate
        FindTakeoffDialog.setWindowTitle(_translate("FindTakeoffDialog", "Dialog"))
        self.comboBoxColumn.setItemText(0, _translate("FindTakeoffDialog", "RequestID"))
        self.comboBoxColumn.setItemText(1, _translate("FindTakeoffDialog", "FlightID"))
        self.comboBoxColumn.setItemText(2, _translate("FindTakeoffDialog", "PersonnelID"))
        self.comboBoxColumn.setItemText(3, _translate("FindTakeoffDialog", "WaitingTime"))
        self.comboBoxColumn.setItemText(4, _translate("FindTakeoffDialog", "StatusID"))
        self.pushButton.setText(_translate("FindTakeoffDialog", "Find"))
        self.label.setText(_translate("FindTakeoffDialog", "Find by column"))
        self.label_2.setText(_translate("FindTakeoffDialog", "Value to find"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FindTakeoffDialog = QtWidgets.QDialog()
    FindTakeoffDialogUi = Ui_FindTakeoffDialog()
    FindTakeoffDialogUi.setupUi(FindTakeoffDialog)
    FindTakeoffDialog.show()
    sys.exit(app.exec_())
