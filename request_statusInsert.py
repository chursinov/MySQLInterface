# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rando\PycharmProjects\MySQLInterface\request_statusInsert.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogRequestStatusInsert(object):
    def setupUi(self, DialogRequestStatusInsert):
        DialogRequestStatusInsert.setObjectName("DialogRequestStatusInsert")
        DialogRequestStatusInsert.resize(400, 470)
        self.StatusID = QtWidgets.QTextEdit(DialogRequestStatusInsert)
        self.StatusID.setGeometry(QtCore.QRect(190, 40, 171, 31))
        self.StatusID.setObjectName("StatusID")
        self.Description = QtWidgets.QTextEdit(DialogRequestStatusInsert)
        self.Description.setGeometry(QtCore.QRect(190, 140, 171, 31))
        self.Description.setObjectName("Description")
        self.StatusName = QtWidgets.QTextEdit(DialogRequestStatusInsert)
        self.StatusName.setGeometry(QtCore.QRect(190, 90, 171, 31))
        self.StatusName.setObjectName("StatusName")
        self.pushButton = QtWidgets.QPushButton(DialogRequestStatusInsert)
        self.pushButton.setGeometry(QtCore.QRect(130, 417, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(DialogRequestStatusInsert)
        self.label.setGeometry(QtCore.QRect(60, 50, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogRequestStatusInsert)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DialogRequestStatusInsert)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 61, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(DialogRequestStatusInsert)
        QtCore.QMetaObject.connectSlotsByName(DialogRequestStatusInsert)

    def retranslateUi(self, DialogRequestStatusInsert):
        _translate = QtCore.QCoreApplication.translate
        DialogRequestStatusInsert.setWindowTitle(_translate("DialogRequestStatusInsert", "Dialog"))
        self.pushButton.setText(_translate("DialogRequestStatusInsert", "Insert into `request_status`"))
        self.label.setText(_translate("DialogRequestStatusInsert", "StatusID"))
        self.label_2.setText(_translate("DialogRequestStatusInsert", "StatusName"))
        self.label_3.setText(_translate("DialogRequestStatusInsert", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogRequestStatusInsert = QtWidgets.QDialog()
    ui = Ui_DialogRequestStatusInsert()
    ui.setupUi(DialogRequestStatusInsert)
    DialogRequestStatusInsert.show()
    sys.exit(app.exec_())
