from concurrent.futures import thread
import json
import math
from random import random
from statistics import quantiles
from time import time
from UI_mainwindow import Ui_mainwindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QWidget, QTableWidgetItem, QMessageBox


class GUI(Ui_mainwindow):

    # Init and setup window
    def __init__(self) -> None:
        super().__init__()
        self.mainwindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainwindow)
        self.setupSignal()

    # Add event to buttons and menu items
    def setupSignal(self) -> None:
        # Buttons
        self.btn_solve.clicked.connect(self.btn_solve_clicked)
        self.btn_addInput.clicked.connect(self.btn_addInput_clicked)
        self.btn_deleteInput.clicked.connect(self.btn_deleteInput_clicked)
        self.btn_exportInput.clicked.connect(self.btn_exportInput_clicked)
        self.btn_randomInput.clicked.connect(self.btn_randomInput_clicked)

        # Actions in Menu File
        self.actionImportDataToExist.triggered.connect(
            self.actionImportDataToExist_triggered)
        self.actionImportDataToNew.triggered.connect(
            self.actionImportDataToNew_triggered)
        self.actionExportInput.triggered.connect(
            self.btn_exportInput_clicked)
        self.actionExit.triggered.connect(self.actionExit_triggered)

        # Actions in Menu Edit
        self.actionAddInput.triggered.connect(self.btn_addInput_clicked)
        self.actionDeleteSelectedInput.triggered.connect(
            self.btn_deleteInput_clicked)
        self.actionSolve.triggered.connect(self.btn_solve_clicked)
        self.actionChangeMaximumWeight.triggered.connect(
            self.actionChangeMaximumWeight_triggered)
        self.actionChangeAlgorithm.triggered.connect(
            self.actionChangeAlgorithm_triggered)

    # Show the window
    def show(self) -> None:
        self.mainwindow.show()

    '''
    ---- When buttons click ----
    '''

    # Button solve clicked
    def btn_solve_clicked(self, checked) -> None:
        import sys
        import os
        SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(os.path.dirname(SCRIPT_DIR))

        import Algorithms.Algorithms as algorithms

        algorithm = None
        try:
            data = self.exportInputToJson()
            C = data["maximum weight"]
            W = data["table"]["Weight"]
            P = data["table"]["Price"]
            indexes = []
        except:
            self.showMessageBox("Error", QMessageBox.critical,
                                "Error when read input!")
            return
        try:
            match self.cbb_algorithm.currentText():
                case "Dynamic Programing":
                    algorithm = algorithms.DynamicPrograming
                case "Greedy":
                    algorithm = algorithms.GreedyProgram
                case "Backtrack":
                    algorithm = algorithms.Backtrack
                case "Branch and Bound":
                    algorithm = algorithms.BranchAndBound
                case "Brute Force":
                    algorithm = algorithms.BruteForce
                case _:
                    raise Exception("Can not find the algorithm!")

            t1 = time()
            indexes = algorithm.findSolution(C, W, P)
            t2 = time()

            self.addDataToOutputTable({
                "table": {
                    "Weight": [W[x] for x in indexes],
                    "Price": [P[x] for x in indexes],
                    "Quantity": [1] * len(indexes)
                }
            })

            self.lb_time.setText("Time: {} s".format(t2 - t1))
            self.lb_status.setText("Status: completed!")
        except Exception as e:
            self.lb_status.setText("Status: error!")
            self.showMessageBox("Error", QMessageBox.critical, str(e))

    # Add new row to input table and focus last row
    def btn_addInput_clicked(self, checked) -> None:
        self.tb_input.insertRow(self.tb_input.rowCount())
        self.tb_input.clearSelection()
        self.tb_input.selectRow(self.tb_input.rowCount()-1)
        self.tb_input.setFocus()

    # Delete selected rows in input table in descent order
    def btn_deleteInput_clicked(self, checked) -> None:
        rows = list(set([index.row()
                    for index in self.tb_input.selectedIndexes()]))
        rows.reverse()
        for index in rows:
            self.tb_input.removeRow(index)

    # Convert input data to JSON then save to file
    def btn_exportInput_clicked(self, checked) -> None:
        fileName = self.saveFileDialog()
        if fileName:
            try:
                jsonData = self.exportInputToJson()
                self.saveData(fileName, jsonData)
                self.showMessageBox(
                    message="Export input data successfully!", boxType=QMessageBox.information)
            except:
                self.showMessageBox(
                    message="Error when export input data!", boxType=QMessageBox.critical)

    def btn_randomInput_clicked(self, checked) -> None:
        max_weights = self.spb_maximumWeight.value()
        weights = [int(random() * max_weights + 1) for i in range(max_weights)]
        price = [int(random() * max_weights + 1) for i in range(max_weights)]
        quantities = [1] * max_weights
        self.addDataToInputTable({
            "table": {
                "Weight": weights,
                "Price": price,
                "Quantity": quantities
            }
        })

    '''
    ---- Actions in File Menu ----
    '''

    # Close window
    def actionExit_triggered(self, checked) -> None:
        if self.showConfirmBox(message="Do you sure to exit?") == QMessageBox.Yes:
            self.mainwindow.close()

    # Read and import data to input table
    def actionImportDataToExist_triggered(self, checked) -> None:
        fileName = self.openFileNameDialog()
        if fileName:
            try:
                data = self.readData(fileName)
                self.addDataToInputTable(data)
            except:
                self.showMessageBox(
                    message="Error when import data!", boxType=QMessageBox.critical)

    # Read data, then clear table and import data to input table
    def actionImportDataToNew_triggered(self, checked) -> None:
        fileName = self.openFileNameDialog()
        if fileName:
            try:
                self.tb_input.setRowCount(0)
                data = self.readData(fileName)
                self.addDataToInputTable(data)
            except:
                self.showMessageBox(
                    message="Error when import data!", boxType=QMessageBox.critical)

    '''
    Actions in Edit Menu
    '''

    # Focus to SpinBox Maximum Weight
    def actionChangeMaximumWeight_triggered(self, checked) -> None:
        self.spb_maximumWeight.setFocus()

    # Show combobox Algorithm and focus it
    def actionChangeAlgorithm_triggered(self, checked) -> None:
        self.cbb_algorithm.showPopup()
        self.cbb_algorithm.setFocus()

    '''
    ---- Utilities functions ----
    '''

    # Get column index from column name
    def getColumnIndex(self) -> dict:
        result = dict()
        for i in range(self.tb_input.columnCount()):
            result[self.tb_input.horizontalHeaderItem(i).text()] = i
        return result

    # Show open file dialog and return full path of selected file
    def openFileNameDialog(self) -> str:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.modalWidget(
        ), "Import Data", "", "JSON Files (*.json);;Input Files (*.inp);;All Files (*)", options=options)
        return fileName

    # Show save file dialog and return full path of saved file
    def saveFileDialog(self) -> str:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self.modalWidget(
        ), "Export Data", "", "JSON Files (*.json);;Input Files (*.inp);;All Files (*)", options=options)
        return fileName

    # Read JSON Data
    def readData(self, fileName: str) -> dict:
        import json
        with open(fileName, "r") as f:
            data: dict = json.load(f)

        if data:
            return data
        return dict()

    # Save data to fileName
    def saveData(self, fileName: str, jsonData: str) -> None:
        with open(fileName, 'w') as f:
            json.dump(jsonData, f)

    # Convert data from combobox algorithm, spinbox maximum weight and input table to JSON string
    def exportInputToJson(self) -> dict:
        columns = self.getColumnIndex()
        jsonData = dict()
        jsonData["algorithm"] = self.cbb_algorithm.currentText()
        jsonData["maximum weight"] = self.spb_maximumWeight.value()
        for key in columns:
            columns[key] = [int(self.tb_input.item(i, columns[key]).text())
                            for i in range(self.tb_input.rowCount())]
        jsonData["table"] = columns
        return jsonData

    # Add data to combobox algorithm, spinbox maximum weight and input table
    def addDataToInputTable(self, jsonData: dict) -> None:
        algorithm = jsonData.get("algorithm", self.cbb_algorithm.currentText())
        self.cbb_algorithm.setCurrentText(algorithm)
        maxWeight = jsonData.get(
            "maximum weight", self.spb_maximumWeight.value())
        self.spb_maximumWeight.setValue(maxWeight)
        table: dict = jsonData.get("table", {})
        weights: list = table.get("Weight", [])
        values: list = table.get("Price", [])
        quantities: list = table.get("Quantity", [])
        columns: dict = self.getColumnIndex()
        tableRow = self.tb_input.rowCount()
        self.tb_input.setRowCount(
            tableRow + max(len(weights), max(len(values), len(quantities))))
        for i in range(len(weights)):
            self.tb_input.setItem(
                tableRow + i, columns["Weight"], QtWidgets.QTableWidgetItem(str(weights[i])))
        for i in range(len(values)):
            self.tb_input.setItem(
                tableRow + i, columns["Price"], QtWidgets.QTableWidgetItem(str(values[i])))
        for i in range(len(quantities)):
            self.tb_input.setItem(
                tableRow + i, columns["Quantity"], QtWidgets.QTableWidgetItem(str(quantities[i])))

    # Add data to combobox algorithm, spinbox maximum weight and input table
    def addDataToOutputTable(self, jsonData: dict) -> None:
        table: dict = jsonData.get("table", {})
        weights: list = table.get("Weight", [])
        values: list = table.get("Price", [])
        quantities: list = table.get("Quantity", [])
        columns: dict = self.getColumnIndex()

        self.tb_output.setRowCount(
            max(len(weights), max(len(values), len(quantities))) + 1)
        for i in range(len(weights)):
            self.tb_output.setItem(
                i, columns["Weight"], QtWidgets.QTableWidgetItem(str(weights[i])))
        for i in range(len(values)):
            self.tb_output.setItem(
                i, columns["Price"], QtWidgets.QTableWidgetItem(str(values[i])))
        for i in range(len(quantities)):
            self.tb_output.setItem(
                i, columns["Quantity"], QtWidgets.QTableWidgetItem(str(quantities[i])))

        self.tb_output.setVerticalHeaderLabels(
            [str(x + 1) for x in range(self.tb_output.rowCount())])
        self.tb_output.setVerticalHeaderItem(
            self.tb_output.rowCount() - 1, QtWidgets.QTableWidgetItem("Total"))
        self.tb_output.setItem(self.tb_output.rowCount(
        ) - 1, columns["Weight"], QtWidgets.QTableWidgetItem(str(sum(weights))))
        self.tb_output.setItem(self.tb_output.rowCount(
        ) - 1, columns["Price"], QtWidgets.QTableWidgetItem(str(sum(values))))
        self.tb_output.setItem(self.tb_output.rowCount(
        ) - 1, columns["Quantity"], QtWidgets.QTableWidgetItem(str(sum(quantities))))

    # Create dialog or message Widget
    def modalWidget(self, width: int = 400, height: int = 100) -> QWidget:
        wget = QWidget()
        wget.setFixedSize(width, height)
        wget.move(self.mainwindow.x() + int(self.mainwindow.width() / 2) - int(wget.width() / 2),
                  self.mainwindow.y() + int(self.mainwindow.height() / 2) - int(wget.height() / 2))

    # Show messagebox that only display message and OK button
    def showMessageBox(self, title: str = "Notification", boxType: QMessageBox.StandardButton = QMessageBox.information, message: str = "") -> None:
        boxType(self.modalWidget(), title, message, QMessageBox.Ok)

    # Show confirm box that return Yes or No
    def showConfirmBox(self, title: str = "Confirm", message: str = "") -> QMessageBox.StandardButton:
        reply = QMessageBox.question(
            self.modalWidget(), title, message, QMessageBox.No | QMessageBox.Yes)
        return reply


# Run GUI app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = GUI()
    ui.show()
    app.exec_()
