# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rando\PycharmProjects\MySQLInterface\FindInReqEmerg.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FindInRequestEmergDialog(object):
    def setupUi(self, FindInRequestEmergDialog):
        FindInRequestEmergDialog.setObjectName("FindInRequestEmergDialog")
        FindInRequestEmergDialog.resize(400, 483)
        self.comboBoxColumn = QtWidgets.QComboBox(FindInRequestEmergDialog)
        self.comboBoxColumn.setGeometry(QtCore.QRect(250, 70, 111, 22))
        self.comboBoxColumn.setObjectName("comboBoxColumn")
        self.comboBoxColumn.addItem("")
        self.comboBoxColumn.addItem("")
        self.comboBoxColumn.addItem("")
        self.comboBoxColumn.addItem("")
        self.comboBoxColumn.addItem("")
        self.textEditValue = QtWidgets.QTextEdit(FindInRequestEmergDialog)
        self.textEditValue.setGeometry(QtCore.QRect(230, 120, 131, 31))
        self.textEditValue.setObjectName("textEditValue")
        self.tableWidget = QtWidgets.QTableWidget(FindInRequestEmergDialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 210, 371, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(FindInRequestEmergDialog)
        self.label.setGeometry(QtCore.QRect(50, 80, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FindInRequestEmergDialog)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(FindInRequestEmergDialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 430, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(FindInRequestEmergDialog)
        QtCore.QMetaObject.connectSlotsByName(FindInRequestEmergDialog)

    def retranslateUi(self, FindInRequestEmergDialog):
        _translate = QtCore.QCoreApplication.translate
        FindInRequestEmergDialog.setWindowTitle(_translate("FindInRequestEmergDialog", "Dialog"))
        self.comboBoxColumn.setItemText(0, _translate("FindInRequestEmergDialog", "FlightID"))
        self.comboBoxColumn.setItemText(1, _translate("FindInRequestEmergDialog", "PersonnelID"))
        self.comboBoxColumn.setItemText(2, _translate("FindInRequestEmergDialog", "RequestID"))
        self.comboBoxColumn.setItemText(3, _translate("FindInRequestEmergDialog", "WaitingTime"))
        self.comboBoxColumn.setItemText(4, _translate("FindInRequestEmergDialog", "EmergencyStatusID"))
        self.label.setText(_translate("FindInRequestEmergDialog", "Find by column"))
        self.label_2.setText(_translate("FindInRequestEmergDialog", "Value to find"))
        self.pushButton.setText(_translate("FindInRequestEmergDialog", "Find"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FindInRequestEmergDialog = QtWidgets.QDialog()
    FindInRequestEmergDialogUi = Ui_FindInRequestEmergDialog()
    FindInRequestEmergDialogUi.setupUi(FindInRequestEmergDialog)
    FindInRequestEmergDialog.show()
    sys.exit(app.exec_())
