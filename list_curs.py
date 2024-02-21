import sys
 
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget,QTableWidgetItem, QVBoxLayout
import mysql.connector as mycon
 
cx = mycon.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="tbcursos"
)
 
cursor = cx.cursor()
 
class ExibirCursos(QWidget):
     def __init__(self):
        super().__init__()
     
        self.setGeometry(300,400,450,300)
        self.setWindowTitle("Cadastro dos cursos")
        
        tbcurso = QTableWidget(self)
        tbcurso.setColumnCount(3)
        tbcurso.setRowCount(10)
 
        headerLine=["Id","Curso","Carga horaria"]
        
        tbcurso.setHorizontalHeaderLabels(headerLine)
        cursor.execute("Select * from tbcursos.registrodecursos")
        lintb = 0
        
        for linha in cursor:
            tbcurso.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbcurso.setItem(lintb,1,QTableWidgetItem(linha[1]))
            tbcurso.setItem(lintb,2,QTableWidgetItem(linha[2]))
            tbcurso.setItem(lintb,2,QTableWidgetItem(linha[2]))
            lintb+=1
            
        layout= QVBoxLayout()
        layout.addWidget(tbcurso)
        self.setLayout(layout)          
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = ExibirCursos()
    tela.show()
    sys.exit(app.exec_())
 
   
   