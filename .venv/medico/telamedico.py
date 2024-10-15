from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout
import sys 
import mysql.connector

class TelaMedico(QWidget):
    def __init__(self):
        super().__init__()

        # Tamanho e posição da janela
        self.setGeometry(50,50,600,600)
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        self.setWindowTitle("Tela de Cadastro do Médico")

        # Criação das Labels para a Janela Paciente
        self.label_nome = QLabel("Nome Completo:")
        self.label_nome.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_crm = QLabel("CRM:")
        self.label_crm.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_telefone = QLabel("Telefone:")
        self.label_telefone.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_endereco = QLabel("Endereco:")
        self.label_endereco.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_especialidade = QLabel("Especialidade:")
        self.label_especialidade.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_confirmacao = QLabel("")
              
        # Criação das line edits para os dados do paciente
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.edit_crm = QLineEdit()
        self.edit_crm.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.edit_telefone = QLineEdit()
        self.edit_telefone.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.edit_endereco = QLineEdit()
        self.edit_endereco.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.edit_especialidade = QLineEdit()
        self.edit_especialidade.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")


        self.combo_especialidade = QComboBox()
        self.combo_especialidade.setStyleSheet("QComboBox{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        especialidade =["Pediatra", "Ginecologista", "Psicologo", "Cardiologista", "Psiquiatra"]

        # Adicionar a lista a combo_especialidade
        self.combo_especialidade.addItems(especialidade)

        # Criação do layout vertical 
        self.layout_vertical = QVBoxLayout()
        self.layout_vertical.addWidget(self.label_nome)
        self.layout_vertical.addWidget(self.edit_nome)

        self.layout_vertical.addWidget(self.label_crm)
        self.layout_vertical.addWidget(self.edit_crm)

        self.layout_vertical.addWidget(self.label_telefone)
        self.layout_vertical.addWidget(self.edit_telefone)

        self.layout_vertical.addWidget(self.label_endereco)
        self.layout_vertical.addWidget(self.edit_endereco)

        self.layout_vertical.addWidget(self.label_especialidade)
        self.layout_vertical.addWidget(self.combo_especialidade)

        # Criar o botão de Cadastro
        self.button_cadastrar = QPushButton("Cadastrar")
        self.button_cadastrar.setStyleSheet("QPushButton{background-color:#2979ff; color:#fafafa; border-radius:5px; padding: 5px; font-weight:bold}")

        # Chamar uma função vinculada ao botão cadastrar
        self.button_cadastrar.clicked.connect(self.cadastrar)
       
        # Adicionar o botão ao layout
        self.layout_vertical.addWidget(self.button_cadastrar)

        # Adicionar a label de confirmação abaixo do botão cadastrar
        self.layout_vertical.addWidget(self.label_confirmacao)

        self.setLayout(self.layout_vertical)

     # Criar a função Cadastrar que será acionada pelo botão 
    # button cadastrar. Esta função cadastra os dados do formulario no banco de dados clinicadb,
    # dentro da tabela paciente
    def cadastrar(self):
        # Para estabelecer a conexao com o banco de dados mysql
        # Iremos usar um módulo chamado mysql-connector-python
        # a instalação é:
        # python -m pip install mysql-connector-phython
        conexao = mysql.connector.connect (
            host="127.0.0.1",
            user="root",
            password="",
            database="clinicadb",
            port="3307"
        )

        # Configurar um cursor para navegar na tabela
        cursor = conexao.cursor()

        # Capturar os dados do formulário para efetuar o cadastro
        nome = self.edit_nome.text()
        crm = self.edit_crm.text()        
        telefone = self.edit_telefone.text()
        endereco = self.edit_endereco.text()
        especialidade = self.combo_especialidade.currentText()

        sqlCommand = f"INSERT INTO medico(nomemedico,crm,telefone,endereco,especialidade)VALUES('{nome}','{crm}','{telefone}','{endereco}','{especialidade}')"

        # Vamos executar o comando de INSERT para cadastrar os dados do formulário na tabela paciente. 
        # Utilizaremos o comando execute
        cursor.execute(sqlCommand)

        # Para confirmar a inserção de dados na tabela paciente
        # Iremos usar o comando commit
        conexao.commit()

        # Exibir mensagem de confirmacao apos clicar no botão cadastrar
        self.label_confirmacao.setText("Médico Cadastrado com Sucesso!")

        # Limpar as caixas de texto
        self.edit_nome.setText("")
        self.edit_crm.setText("")
        self.edit_telefone.setText("")
        self.edit_endereco.setText("")

        cursor.close()
        conexao.close()

app = QApplication(sys.argv)
tela = TelaMedico()
tela.show()
app.exec_()