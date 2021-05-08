import psycopg2


class Inserir():

    def start(self):
        con = psycopg2.connect(host='localhost', database='Teste',
                       user='postgres', password='kk93909979')
        return con

    def inseri_dados_estoque(self, produto, categoria, valor, quantidade, descricao, con):
        Cursor_inserir = con.cursor()
        Cursor_inserir.execute(
                "INSERT INTO Estoque (produto, categoria, valor, quantidade, descricao) VALUES (%s,%s,%s,%s,%s)",
                (produto, categoria, valor, quantidade, descricao))

        con.commit()
        con.close()
    
class Seleciona():

    def start(self):
        con = psycopg2.connect(host='localhost', database='Teste',
                       user='postgres', password='kk93909979')
        return con 

    def selec_estoque(self, con):
        dados=[]
        Cursor_seleciona = con.cursor()
        Cursor_seleciona.execute("SELECT * FROM Estoque")
        for item in Cursor_seleciona:
            dados.append(item)
        con.close()

        return dados