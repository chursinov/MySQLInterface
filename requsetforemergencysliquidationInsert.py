# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rando\PycharmProjects\MySQLInterface\requsetforemergencysliquidationInsert.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogEmergencyInsert(object):
    def setupUi(self, DialogEmergencyInsert):
        DialogEmergencyInsert.setObjectName("Dialog")
        DialogEmergencyInsert.resize(400, 413)
        self.requsetforemergencysliquidationButton = QtWidgets.QPushButton(DialogEmergencyInsert)
        self.requsetforemergencysliquidationButton.setGeometry(QtCore.QRect(110, 350, 181, 28))
        self.requsetforemergencysliquidationButton.setObjectName("requsetforemergencysliquidationButton")
        self.FlightID = QtWidgets.QTextEdit(DialogEmergencyInsert)
        self.FlightID.setGeometry(QtCore.QRect(210, 40, 151, 31))
        self.FlightID.setObjectName("FlightID")
        self.PersonnelID = QtWidgets.QTextEdit(DialogEmergencyInsert)
        self.PersonnelID.setGeometry(QtCore.QRect(210, 90, 151, 31))
        self.PersonnelID.setObjectName("PersonnelID")
        self.RequestID = QtWidgets.QTextEdit(DialogEmergencyInsert)
        self.RequestID.setGeometry(QtCore.QRect(210, 140, 151, 31))
        self.RequestID.setObjectName("RequestID")
        self.WaitingTime = QtWidgets.QTextEdit(DialogEmergencyInsert)
        self.WaitingTime.setGeometry(QtCore.QRect(210, 190, 151, 31))
        self.WaitingTime.setObjectName("WaitingTime")
        self.EmergencyStatuID = QtWidgets.QTextEdit(DialogEmergencyInsert)
        self.EmergencyStatuID.setGeometry(QtCore.QRect(210, 240, 151, 31))
        self.EmergencyStatuID.setObjectName("EmergencyStatuID")
        self.label = QtWidgets.QLabel(DialogEmergencyInsert)
        self.label.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogEmergencyInsert)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DialogEmergencyInsert)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(DialogEmergencyInsert)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(DialogEmergencyInsert)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 101, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(DialogEmergencyInsert)
        QtCore.QMetaObject.connectSlotsByName(DialogEmergencyInsert)

    def retranslateUi(self, DialogEmergencyInsert):
        _translate = QtCore.QCoreApplication.translate
        DialogEmergencyInsert.setWindowTitle(_translate("Dialog", "Dialog"))
        self.requsetforemergencysliquidationButton.setText(_translate("Dialog", "Insert into `requsetforemergency`"))
        self.label.setText(_translate("Dialog", "FlightID"))
        self.label_2.setText(_translate("Dialog", "PersonnelID"))
        self.label_3.setText(_translate("Dialog", "RequestID"))
        self.label_4.setText(_translate("Dialog", "WaitingTime"))
        self.label_5.setText(_translate("Dialog", "EmergencyStatusID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogEmergencyInsert = QtWidgets.QDialog()
    ui = Ui_DialogEmergencyInsert()
    ui.setupUi(DialogEmergencyInsert)
    DialogEmergencyInsert.show()
    sys.exit(app.exec_())
