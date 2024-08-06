import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from design import  Ui_MainWindow

class BookApp(QtWidgets.QMainWindow, Ui_MainWindow):
      # display screen
      def __init__(self):
        super().__init__()
        self.setupUi(self)

      # Table Create
      def create_table(self):   
            connection = sqlite3.connect('booklist.db')    
            cursor = connection.cursor()        
            cursor.execute('''CREATE TABLE IF NOT EXISTS book2    
                          (bookID INTEGER PRIMARY KEY AUTOINCREMENT, 
                           title TEXT, 
                           price REAL)''')      
            connection.commit()     
            connection.close()    

      # Insert record
      def insert_data(self):  
            title = self.title.text()     
            price = float(self.price.text())   
            connection = sqlite3.connect('booklist.db')   
            cursor = connection.cursor()              
            cursor.execute("INSERT INTO book2 (title, price) VALUES (?, ?)", (title, price))    
            connection.commit()   
            connection.close()      
            QtWidgets.QMessageBox.information(self.centralwidget, "Success", "Book inserted successfully!")
            self.select_data()      

      # Display record
      def select_data(self):
            connection = sqlite3.connect('booklist.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM book2")
            rows = cursor.fetchall()
            self.tableWidget.setRowCount(len(rows))
            # self.tableWidget.setColumnCount(3)  # Assuming you have 3 columns: bookID, title, price
            for row_index, row_data in enumerate(rows):
                  for col_index, item in enumerate(row_data):
                        self.tableWidget.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(item)))
            connection.close()

      # Update record
      def update_data(self):
            # current_row = self.tableWidget.currentRow()
            # if current_row > -1:
            # bookID = int(self.tableWidget.item(current_row, 0).text())
            bookID=int(self.bookID.text())
            title = self.title.text()
            price = float(self.price.text())
            connection = sqlite3.connect('booklist.db')
            cursor = connection.cursor()
            cursor.execute("UPDATE book2 SET title = ?, price = ? WHERE bookID = ?", (title, price, bookID))
            connection.commit()
            connection.close()
            QtWidgets.QMessageBox.information(self.centralwidget, "Success", "Book Updated successfully!")
            self.select_data()

      # delete record
      def delete_data(self):
            # current_row = self.tableWidget.currentRow()
            # if current_row > -1:
            # bookID = int(self.tableWidget.item(current_row, 0).text())
            bookID=int(self.bookID.text())
            connection = sqlite3.connect('booklist.db')
            cursor = connection.cursor()
            cursor.execute("DELETE FROM book2 WHERE bookID = ?", (bookID,))
            connection.commit()
            connection.close()
            QtWidgets.QMessageBox.information(self.centralwidget, "Success", "Book Deleted successfully!")
            self.select_data()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = BookApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()