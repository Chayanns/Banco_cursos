import sys
 
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QVBoxLayout, QPushButton
import mysql.connector as mc
 
con = mc.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="tbcursos"
)
 
cursor = con.cursor()
 
class CadCursos(QWidget):
     def __init__(self):
        super().__init__()
     
        self.setGeometry(300,400,450,300)
        self.setWindowTitle("Cadastro dos cursos")
 
        labelCurs = QLabel("Nome do curso: ")
        self.editCurs = QLineEdit()
       
        labelChor = QLabel("Carga Horaria: ")
        self.editChor = QLineEdit()
       
        psbCadastro = QPushButton("Cadastrar")
        self.labelMsg =QLabel("|")
        layout = QVBoxLayout()
 
        layout.addWidget(labelCurs)
        layout.addWidget(self.editCurs)
       
        layout.addWidget(labelChor)
        layout.addWidget(self.editChor)
       
        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.Cadcurs)
     
        layout.addWidget(self.labelMsg)
       
        self.setLayout(layout)          
       
     def Cadcurs(self):
        cursor.execute("insert into registrodecursos(nome_cursos,cargahoraria)values(%s,%s)",
                       (self.editCurs.text(),self.editChor.text()))
        con.commit()
        self.labelMsg.setText("Curso cadastrado")
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = CadCursos()
    tela.show()
    sys.exit(app.exec_())
 
   
   