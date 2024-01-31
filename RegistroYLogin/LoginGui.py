import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QLabel, QLineEdit, QCheckBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from NewUser import RegistroUsuario

class Login(QWidget):

    def __init__(self):
        super(Login, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100,100,400,270)
        self.setWindowTitle("Login")
        self.login_usuario()

    def login_usuario(self):
        self.lbl_login = QLabel("Login", self)
        self.lbl_login.move(160,10)
        self.lbl_login.setFont(QFont("Arial", 20))

        self.lbl_usuario = QLabel("Usuario", self)
        self.lbl_usuario.move(30,60)

        self.lned_usuario = QLineEdit(self)
        self.lned_usuario.move(110,60)
        self.lned_usuario.resize(220,20)

        self.lbl_password = QLabel("Password", self)
        self.lbl_password.move(30,90)

        self.lned_password = QLineEdit(self)
        self.lned_password.setEchoMode(QLineEdit.Password)
        self.lned_password.move(110,90)
        self.lned_password.resize(220,20)

        self.btn_login = QPushButton("Login", self)
        self.btn_login.move(150,155)
        self.btn_login.resize(100,40)

        self.chbox_show_password = QCheckBox("Show password", self)
        self.chbox_show_password.move(110,120)
        self.chbox_show_password.setChecked(False)

        self.lbl_miembro = QLabel("Aun no estas registrado?", self)
        self.lbl_miembro.move(70,225)
        # self.lbl_miembro.setWordWrap(True)
        self.lbl_miembro.setFont(QFont("Arial",7))

        self.btn_registro = QPushButton("Registrarse", self)
        self.btn_registro.move(225,217)
        self.btn_registro.resize(100,30)

        self.btn_registro.clicked.connect(self.registro_usuario)

        self.chbox_show_password.stateChanged.connect(self.show_password)

        self.btn_login.clicked.connect(self.click_login)

    def click_login(self):
        usuarios = {}

        try:
            with open("usuarios.txt") as u:
                for line in u:
                    campo_usuarios = line.split(" ")
                    usuario = campo_usuarios[0]
                    password = campo_usuarios[1].rstrip("\n")
                    usuarios[usuario] = password
        except FileNotFoundError:
            u = ("usuarios.txt", "w")

        usuario = self.lned_usuario.text()
        password = self.lned_password.text()

        if(usuario, password) in usuarios.items():
            QMessageBox.information(self, "Inicio exitoso", "Inicio de sesión exitoso", QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.warning(self, "Error", "El nombre de usuario o la contraseña son incorrectos", QMessageBox.Close, QMessageBox.Close)

    def show_password(self, state):
        if state == Qt.Checked:
            self.lned_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lned_password.setEchoMode(QLineEdit.Password)

    def registro_usuario(self):
        self.create_new_user = RegistroUsuario()
        self.create_new_user.show()

    def closeEvent(self, event):
        msg_cerrar = QMessageBox.question(self, "Cerrar aplicacion?", "¿Está seguro que desea cerrar la aplicación?",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if msg_cerrar == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())