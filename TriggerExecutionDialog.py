# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rando\PycharmProjects\MySQLInterface\TriggerExecutionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TriggerDialog(object):
    def setupUi(self, TriggerDialog):
        TriggerDialog.setObjectName("TriggerDialog")
        TriggerDialog.resize(400, 300)
        self.label = QtWidgets.QLabel(TriggerDialog)
        self.label.setGeometry(QtCore.QRect(96, 140, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(TriggerDialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(TriggerDialog)
        QtCore.QMetaObject.connectSlotsByName(TriggerDialog)

    def retranslateUi(self, TriggerDialog):
        _translate = QtCore.QCoreApplication.translate
        TriggerDialog.setWindowTitle(_translate("TriggerDialog", "Dialog"))
        self.pushButton.setText(_translate("TriggerDialog", "I see!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TriggerDialog = QtWidgets.QDialog()
    Triggerui = Ui_TriggerDialog()
    Triggerui.setupUi(TriggerDialog)
    TriggerDialog.show()
    sys.exit(app.exec_())
