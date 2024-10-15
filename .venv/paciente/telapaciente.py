from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout
import sys 
import mysql.connector

class TelaPaciente(QWidget):
    def __init__(self):
        super().__init__()

        # Tamanho e posição da janela
        self.setGeometry(50,50,600,600)
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        self.setWindowTitle("Tela de Cadastro")

        # Criação das Labels para a Janela Paciente
        self.label_nome = QLabel("Nome Completo:")
        self.label_nome.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_cpf = QLabel("CPF:")
        self.label_cpf.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_telefone = QLabel("Telefone:")
        self.label_telefone.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_endereco = QLabel("Endereço:")
        self.label_endereco.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_datanascimento = QLabel("Data de Nascimento:")
        self.label_datanascimento.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_dia = QLabel ("Dia:")
        self.label_dia.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_mes = QLabel ("Mês:")
        self.label_mes.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_ano = QLabel ("Ano:")
        self.label_ano.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_confirmacao = QLabel("")

        # Criação das line edits para os dados do paciente
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.edit_cpf = QLineEdit()
        self.edit_cpf.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.edit_telefone = QLineEdit()
        self.edit_telefone.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.edit_endereco = QLineEdit()
        self.edit_endereco.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")

        # Criação das combobox para dia, mês e ano
        self.combo_dia = QComboBox()
        self.combo_dia.setStyleSheet("QComboBox{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.combo_mes = QComboBox()
        self.combo_mes.setStyleSheet("QComboBox{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.combo_ano = QComboBox()
        self.combo_ano.setStyleSheet("QComboBox{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")

        # Criar uma estrutura de repetição que vai fazer uma contagem de 1 a 31 
        # e adicionar a caixa (combobox) do dia

        list_dia = []
        for i in range(1,32):
            list_dia.append(str(i))
        self.combo_dia.addItems(list_dia)

        lst_mes = []
        for i in range(1,13):
            lst_mes.append(str(i))
        self.combo_mes.addItems(lst_mes)

        lst_ano = []
        for i in range (1930,2025):
            lst_ano.append(str(i))
        self.combo_ano.addItems(lst_ano)

        # Criação do layout vertical 
        self.layout_vertical = QVBoxLayout()
        self.layout_vertical.addWidget(self.label_nome)
        self.layout_vertical.addWidget(self.edit_nome)

        self.layout_vertical.addWidget(self.label_cpf)
        self.layout_vertical.addWidget(self.edit_cpf)

        self.layout_vertical.addWidget(self.label_telefone)
        self.layout_vertical.addWidget(self.edit_telefone)

        self.layout_vertical.addWidget(self.label_endereco)
        self.layout_vertical.addWidget(self.edit_endereco)

        self.layout_vertical.addWidget(self.label_datanascimento)

        self.label_layout_horizontal = QLabel()
        self.layout_horizontal = QHBoxLayout()

        self.layout_horizontal.addWidget(self.label_dia)
        self.layout_horizontal.addWidget(self.combo_dia)

        self.layout_horizontal.addWidget(self.label_mes)
        self.layout_horizontal.addWidget(self.combo_mes)

        self.layout_horizontal.addWidget(self.label_ano)
        self.layout_horizontal.addWidget(self.combo_ano)
        
        self.layout_horizontal.addWidget(self.combo_dia)
        self.layout_horizontal.addWidget(self.combo_mes)
        self.layout_horizontal.addWidget(self.combo_ano) 

        self.label_layout_horizontal.setLayout(self.layout_horizontal)
        self.layout_vertical.addWidget(self.label_layout_horizontal)

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
        cpf = self.edit_cpf.text()
        telefone = self.edit_telefone.text()
        endereco = self.edit_endereco.text()
        datanascimento = f"{self.combo_ano.currentText()}-{self.combo_mes.currentText()}-{self.combo_dia.currentText()}"

        # Vamos criar uma variável que irá guardar o comando INSERT INTO
        # que insere os dados do formulário na tabela paciente

        sqlCommand = f"INSERT INTO paciente(nomepaciente,cpf,telefone,endereco,datanascimento)VALUES('{nome}','{cpf}','{telefone}','{endereco}','{datanascimento}')"

        # Vamos executar o comando de INSERT para cadastrar os dados do formulário na tabela paciente. 
        # Utilizaremos o comando execute
        cursor.execute(sqlCommand)

        # Para confirmar a inserção de dados na tabela paciente
        # Iremos usar o comando commit
        conexao.commit()

        # Exibir mensagem de confirmacao apos clicar no botão cadastrar
        self.label_confirmacao.setText("Paciente Cadastrado com Sucesso!")

        # Limpar as caixas de texto
        self.edit_nome.setText("")
        self.edit_cpf.setText("")
        self.edit_telefone.setText("")
        self.edit_endereco.setText("")
        

        cursor.close()
        conexao.close()

app = QApplication(sys.argv)
tela = TelaPaciente()
tela.show()
app.exec_()