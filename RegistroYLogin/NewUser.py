import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class RegistroUsuario(QWidget):

    def __init__(self):
        super(RegistroUsuario, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100,100,400,410)
        self.setWindowTitle("Registro de Usuario")
        self.display_widgets()

    def display_widgets(self):
        user_image = "nuevo_usuario.png"
        try:
            with open(user_image):
                label_image = QLabel(self)
                pixmap = QPixmap(user_image)
                label_image.setPixmap(pixmap)
                label_image.move(175,80)
        except FileNotFoundError:
            print("No se encontró el archivo")

        label_titulo = QLabel("Crear nueva cuenta", self)
        label_titulo.move(0,20)
        label_titulo.setFont(QFont("Arial",20))
        label_titulo.resize(400,40)
        label_titulo.setAlignment(Qt.AlignCenter)

        self.label_nombre = QLabel("Nombre completo", self)
        self.label_nombre.move(30,170)

        self.entrada_nombre = QLineEdit(self)
        self.entrada_nombre.move(150,170)
        self.entrada_nombre.resize(200,20)

        self.label_usuario = QLabel("Nombre de usuario", self)
        self.label_usuario.move(30, 210)

        self.entrada_usuario = QLineEdit(self)
        self.entrada_usuario.move(150,210)
        self.entrada_usuario.resize(200,20)

        self.label_password = QLabel("Contraseña", self)
        self.label_password.move(30,250)

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(150,250)
        self.password.resize(200,20)

        self.label_confirmar = QLabel("Confirmar", self)
        self.label_confirmar.move(30, 290)

        self.confirmar = QLineEdit(self)
        self.confirmar.setEchoMode(QLineEdit.Password)
        self.confirmar.move(150, 290)
        self.confirmar.resize(200, 20)

        #Boton de registro
        self.boton = QPushButton("Registrarse", self)
        self.boton.resize(130,40)
        self.boton.move(140,340)
        #Señal del boton
        self.boton.clicked.connect(self.registro)

    def registro(self):
        texto_password = self.password.text()
        texto_confirmar = self.confirmar.text()

        if texto_password != texto_confirmar:
            QMessageBox.warning(self, "Mensaje de error", "Las contraseñas ingresadas no coinciden, intente de nuevo", QMessageBox.Ok, QMessageBox.Ok)
        else:
            with open("usuarios.txt", "a+") as f:
                f.write(self.entrada_usuario.text() + " ")
                f.write(texto_password + "\n")
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistroUsuario()
    window.show()
    sys.exit(app.exec_())