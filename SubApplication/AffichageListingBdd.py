import sys
import sqlite3
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from package import requetesql

class AffichagelistingBdd(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listing des plantes de la base de données")
        loadUi("SubApplication/AffichagePlantesBdd.ui",self)
        self.loaddata()
        self.show()

    def loaddata(self):
        connection = sqlite3.connect('plantes.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM plantes LIMIT 40'

        tablerow = 0
        results = cur.execute(sqlstr)
        self.tableWidget.setRowCount(40)
        for row in results:
            for colonnes in range(12):
                self.tableWidget.setItem(tablerow, colonnes, QtWidgets.QTableWidgetItem(str(row[colonnes])))
            tablerow += 1