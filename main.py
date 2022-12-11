import sys

import pymysql
from config import host, user, password, db_name
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5 import QtWidgets
import DialogDepartment
from DeleteDialog import Ui_DeleteDialog
from DialogAircraftInsert import Ui_DialogAircraftInsert

from DialogDepartment import Ui_DialogDeparmentInsert
from DialogEmergencyStatusInsert import Ui_DialogEmergencyStatusInsert
from EmployeeInsert import Ui_DialogEmployeeInsert
from UpdateDialog import Ui_Dialog
from request_statusInsert import Ui_DialogRequestStatusInsert

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Success!")
    print("#" * 20)
    print("")



#create Table
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users` (id int AUTO_INCREMENT," \
        #         "name varchar(32)," \
        #         "password varchar(32)," \
        #         "email varchar(32), PRIMARY KEY(id));"
        #     cursor.execute(create_table_query)
        #     print("Table created succesfully")
        #insert Data
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) values ('Anna', 'qwerty', 'anna@gmail.com')"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print("Succesfully inserted")

        #select all data from table
        # with connection.cursor() as cursor:
        #     select_all_query = "SELECT * FROM `takeoff_landing_request`"
        #     cursor.execute(select_all_query)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)
        #     print("This is the end of select_all")

        # #update data
        # with connection.cursor() as cursor:
        #     update_data_query = "UPDATE `takeoff_landing_request` SET WaitingTime='12:00:00' WHERE RequestID='1'"
        #     cursor.execute(update_data_query)
        #     connection.commit()

        #delete data
        # with connection.cursor() as cursor:
        #     delete_data_query = "DELETE FROM `takeoff_landing_request` WHERE RequestID='11'"
        #     cursor.execute(delete_data_query)
        #     connection.commit()
        #     print("succesful deletion")


except Exception as ex:
    print("Connection refused")
    print(ex)

Form, Window = uic.loadUiType("Table.ui")

table_name = ""
horizontalHeaderLabels = []
def loaddata(table_name, horizontalHeaderLabels):
    count_columns_query = f"select count(*) from information_schema.columns where table_name = '{table_name}' and table_schema = 'airportd'"
    with connection.cursor() as cursor:
        cursor.execute(count_columns_query)
        count_columns = cursor.fetchall()
    form.tableWidget.setColumnCount(count_columns[0].get('count(*)'))
    count_rows_query = f"SELECT count(*) from `{table_name}`"
    with connection.cursor() as cursor:
        cursor.execute(count_rows_query)
        count_rows = cursor.fetchall()
    form.tableWidget.setRowCount(count_rows[0].get('count(*)'))
    form.tableWidget.setHorizontalHeaderLabels(horizontalHeaderLabels)
    with connection.cursor() as cursor:
        select_all_query = f"SELECT * FROM `{table_name}`"
        cursor.execute(select_all_query)
        rows = cursor.fetchall()
        table_row = 0
        for row in rows:
            for i in range(count_columns[0].get('count(*)')):
                form.tableWidget.setItem(table_row, i, QtWidgets.QTableWidgetItem(str(row.get(horizontalHeaderLabels[i]))))
            table_row+=1
        print("This is the end of select_all")


def on_click():
    global horizontalHeaderLabels
    global table_name
    if form.radioButton.isChecked():
        table_name = "aircraft"
        horizontalHeaderLabels = ["FlightID", "ArrivalCity", "departureCity", "AircraftModelname"]
        form.label.setText("Table: aircraft")
    if form.radioButton_2.isChecked():
        table_name = "department"
        horizontalHeaderLabels = ["DepartmentID", "DepartmentName", "DepartmentDescription"]
        form.label.setText("Table: department")
    if form.radioButton_3.isChecked():
        table_name = "emergencystatus"
        horizontalHeaderLabels = ["EmergencyStatusID", "EmergencyStatusName", "EmergencyStatusDescription"]
        form.label.setText("Table: emergencystatus")
    if form.radioButton_4.isChecked():
        table_name = "employee"
        horizontalHeaderLabels = ["PersonnelID", "FIO", "JobTitle", "DepartmentID"]
        form.label.setText("Table: employee")
    if form.radioButton_5.isChecked():
        table_name = "request_status"
        horizontalHeaderLabels = ["StatusID", "StatusName", "Description"]
        form.label.setText("Table: request_status")
    loaddata(table_name, horizontalHeaderLabels)


def on_add_row():
    def on_insert_department():
        DepartmentID = ui.textEdit.toPlainText()
        DepartmentName = ui.textEdit_2.toPlainText()
        DepartmentDesc = ui.textEdit_3.toPlainText()
        with connection.cursor() as cursor:
            add_row_department_query = f"INSERT into `department` (DepartmentID, DepartmentName, DepartmentDescription) values ({DepartmentID}, '{DepartmentName}', '{DepartmentDesc}' )"
            cursor.execute(add_row_department_query)
            connection.commit()
        print("Succesful insert")
    def on_insert_aircraft():
        FlightID = ui.textEditFlightID.toPlainText()
        ArrivalCity = ui.textEditFlightID_2.toPlainText()
        DepartureCity = ui.textEditFlightID_3.toPlainText()
        AircraftModelName = ui.textEditFlightID_4.toPlainText()
        with connection.cursor() as cursor:
            add_row_aircraft_query = f"INSERT into `aircraft` (FlightID, ArrivalCity, departureCity, AircraftModelname) values ({FlightID}, '{ArrivalCity}', '{DepartureCity}', '{AircraftModelName}' )"
            cursor.execute(add_row_aircraft_query)
            connection.commit()
        print("Succesful insert")
    def on_insert_emergencystatus():
        EmergencyStatusID = ui.EmergencyStatusID.toPlainText()
        EmergencyStatusName = ui.EmergencyStatusName.toPlainText()
        EmergencyStatusDescription = ui.EmergencyStatusDescription.toPlainText()
        with connection.cursor() as cursor:
            add_row_emergencystatus_query = f"INSERT into `emergencystatus` (EmergencyStatusID, EmergencyStatusName, EmergencyStatusDescription) values ({EmergencyStatusID}, '{EmergencyStatusName}', '{EmergencyStatusDescription}')"
            cursor.execute(add_row_emergencystatus_query)
            connection.commit()
        print("Succesful insert")
    def on_insert_employee():
        PersonnelID = ui.PersonnelID.toPlainText()
        FIO = ui.FIO.toPlainText()
        JobTitle = ui.JobTitle.toPlainText()
        DepartmentID = ui.DepartmentID.toPlainText()
        with connection.cursor() as cursor:
            add_row_employee_query = f"INSERT into `employee` (PersonnelID, FIO, JobTitle, DepartmentID) values ({PersonnelID}, '{FIO}', '{JobTitle}', {DepartmentID})"
            cursor.execute(add_row_employee_query)
            connection.commit()
        print("Succesful insert")
    def on_insert_request_status():
        StatusID = ui.StatusID.toPlainText()
        StatusName = ui.StatusName.toPlainText()
        Description = ui.Description.toPlainText()
        with connection.cursor() as cursor:
            add_row_employee_query = f"INSERT into `request_status` (StatusID, StatusName, Description) values ({StatusID}, '{StatusName}', '{Description}')"
            cursor.execute(add_row_employee_query)
            connection.commit()
        print("Succesful insert")
    if form.radioButton_2.isChecked():
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.pushButton.clicked.connect(on_insert_department)
        Dialog.show()
        Dialog.exec_()
    if form.radioButton.isChecked():
        DialogAircraftInsert = QtWidgets.QDialog()
        ui = Ui_DialogAircraftInsert()
        ui.setupUi(DialogAircraftInsert)
        ui.pushButton.clicked.connect(on_insert_aircraft)
        DialogAircraftInsert.show()
        DialogAircraftInsert.exec_()
    if form.radioButton_3.isChecked():
        DialogEmergencyStatusInsert = QtWidgets.QDialog()
        ui = Ui_DialogEmergencyStatusInsert()
        ui.setupUi(DialogEmergencyStatusInsert)
        ui.pushButton.clicked.connect(on_insert_emergencystatus)
        DialogEmergencyStatusInsert.show()
        DialogEmergencyStatusInsert.exec_()
    if form.radioButton_4.isChecked():
        DialogEmployeeInsert = QtWidgets.QDialog()
        ui = Ui_DialogEmployeeInsert()
        ui.setupUi(DialogEmployeeInsert)
        ui.pushButton.clicked.connect(on_insert_employee)
        DialogEmployeeInsert.show()
        DialogEmployeeInsert.exec_()
    if form.radioButton_5.isChecked():
        DialogRequestStatusInsert = QtWidgets.QDialog()
        ui = Ui_DialogRequestStatusInsert()
        ui.setupUi(DialogRequestStatusInsert)
        ui.pushButton.clicked.connect(on_insert_request_status)
        DialogRequestStatusInsert.show()
        DialogRequestStatusInsert.exec_()





def on_update():
    def update_cell():
        table = ui.Table.toPlainText()
        column = ui.Column.toPlainText()
        newValue = ui.newValue.toPlainText()
        primaryKey = ui.PrimaryKey.toPlainText()
        PrimaryKeyValue = ui.PrimaryKeyValue.toPlainText()
        with connection.cursor() as cursor:
            update_query = f"UPDATE `{table}` SET {column}='{newValue}' WHERE {primaryKey}='{PrimaryKeyValue}'"
            cursor.execute(update_query)
            connection.commit()
        loaddata(table_name, horizontalHeaderLabels)
    UpdateDialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(UpdateDialog)
    ui.UpdateButton.clicked.connect(update_cell)
    UpdateDialog.show()
    UpdateDialog.exec_()
    # global table_name
    # if form.radioButton.isChecked():
    #     table_name = "aircraft"
    # if form.radioButton.isChecked():
    #     table_name = "department"
    #     horizontalHeaderLabelsAsRows="DepartmentID, DepartmentName, DepartmentDesccription"
    # insert_query = f"INSERT into `department` ({horizontalHeaderLabelsAsRows}) values (6, 'Test', 'Test')"
    # with connection.cursor() as cursor:
    #     cursor.execute(insert_query)
    # connection.commit()
    # on_click()
def on_delete():
    def on_delete_row():
        if form.radioButton.isChecked():
            table = "aircraft"
        if form.radioButton_2.isChecked():
            table = "department"
        if form.radioButton_3.isChecked():
            table = "emergencystatus"
        if form.radioButton_4.isChecked():
            table = "employee"
        if form.radioButton_5.isChecked():
            table = "request_status"
        PrimaryKey = ui.PrimaryKey.toPlainText()
        PrimaryKeyValue = ui.PrimaryKeyValue.toPlainText()
        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM `{table}` WHERE {PrimaryKey}='{PrimaryKeyValue}'"
            cursor.execute(delete_query)
            connection.commit()
        loaddata(table_name, horizontalHeaderLabels)
    DeleteDialog = QtWidgets.QDialog()
    ui = Ui_DeleteDialog()
    ui.setupUi(DeleteDialog)
    ui.Deleterow.clicked.connect(on_delete_row)
    DeleteDialog.show()
    DeleteDialog.exec_()


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.pushButton.clicked.connect(on_click)
form.pushButton_2.clicked.connect(on_add_row)
form.pushButton_3.clicked.connect(on_update)
form.pushButton_4.clicked.connect(on_delete)
window.show()
app.exec_()
connection.close()




