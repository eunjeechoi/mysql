import sys
import pymysql
from PyQt5.QtWidgets import *

def connectDB():
    host = "localhost"
    user = "root"
    pw = "0000"
    db = "world"
    conn = pymysql.connect(host=host, user=user, password=pw, db=db)
    return (conn)

def disconnectDB(conn):
    conn.close()
    
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1 = QLabel('Country name')
        label2 = QLabel('Continent')
        label3 = QLabel('Population')
        label4 = QLabel('GNP')
        label5 = QLabel('Capital city')
        label6 = QLabel('Language')
        
        self.text_name = QTextEdit()
        self.text_name.setFixedWidth(200)
        self.text_name.setFixedHeight(30)
        btn_1 = QPushButton('Query')
        btn_1.clicked.connect(self.btn_1_clicked)
        self.text_continent = QTextEdit()
        self.text_continent.setFixedWidth(200)
        self.text_continent.setFixedHeight(30)
        self.text_population = QTextEdit()
        self.text_population.setFixedWidth(200)
        self.text_population.setFixedHeight(30)
        self.text_gnp = QTextEdit()
        self.text_gnp.setFixedWidth(200)
        self.text_gnp.setFixedHeight(30)  
        self.text_capital = QTextEdit()
        self.text_capital.setFixedWidth(200)
        self.text_capital.setFixedHeight(30)  
        self.text_lang = QTextEdit()
        self.text_lang.setFixedWidth(200)
        self.text_lang.setFixedHeight(30)
        
        gbox = QGridLayout()
        gbox.addWidget(label1, 0, 0)
        gbox.addWidget(self.text_name, 0, 1)
        gbox.addWidget(btn_1, 0, 2)
        gbox.addWidget(label2, 1, 0)
        gbox.addWidget(self.text_continent, 1, 1)
        gbox.addWidget(label3, 2, 0)
        gbox.addWidget(self.text_population, 2, 1)
        gbox.addWidget(label4, 3, 0)
        gbox.addWidget(self.text_gnp, 3, 1)
        gbox.addWidget(label5, 4, 0)
        gbox.addWidget(self.text_capital, 4, 1)
        gbox.addWidget(label6, 5, 0)
        gbox.addWidget(self.text_lang, 5, 1)
        
        self.setLayout(gbox)
        self.setWindowTitle('My Program')
        self.setGeometry(300, 300, 480, 250)
        self.show()
    def btn_1_clicked(self):
         name = self.text_name.toPlainText()
 
         # sql쿼리 문
         sql = "SELECT continent, country.population, gnp, city.name, language\
             FROM country , countrylanguage, city\
             where country.code = countrylanguage.countrycode\
             and city.countrycode=country.code\
             and city.id = country.capital\
             and countrylanguage.percentage =\
            (select max(percentage) from countrylanguage\
            where countrycode = country.code)\
            and country.name = '%s'" %name
 
         conn = connectDB()
         curs = conn.cursor()
         curs.execute(sql)
            
         result = curs.fetchone()
    
         if result:    
            self.text_continent.setText(str(result[0]))
            self.text_population.setText(str(result[1]))
            self.text_gnp.setText(str(result[2]))
            self.text_capital.setText(str(result[3]))
            self.text_lang.setText(str(result[4]))
         else:
            self.text_continent.setText("")
            self.text_population.setText("")
            self.text_gnp.setText("")
            self.text_capital.setText("")
            self.text_lang.setText("")
         curs.close()
         disconnectDB(conn)
        
if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        