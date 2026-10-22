from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Portaria Digital")
        self.resize(820,520)
        
        titulo = QLabel("Recepção: controle de visitantes")
        
        layout = QVBoxLayout()
        layout.addWidget(titulo)
        self.setLayout(layout)
        