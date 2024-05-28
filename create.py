class Create:

    def __init__(self, conn):
        self.cursor = conn.cursor
    
    def execute_query(self, query: str, values = []):
        try:
            self.cursor.execute(query, values)
        except Exception as e:
            print("Error: Can't execute query", e)
    
    def create_db(self):
        query_create = """CREATE SCHEMA IF NOT EXISTS loja;"""
        self.execute_query(query_create)
    
    def use_db(self):
        query = """USE loja;"""
        self.execute_query(query)

    def drop_db(self):
        query = """DROP SCHEMA loja;"""
        self.execute_query(query)
    
    def create_table_cliente(self):
        query = """CREATE TABLE IF NOT EXISTS loja.cliente(
                    id_cliente INT NOT NULL PRIMARY KEY,
                    nome_cliente VARCHAR(50) NOT NULL,
                    endereco VARCHAR(50) NOT NULL,
                    cidade VARCHAR(30) NOT NULL,
                    cep VARCHAR(6) NOT NULL,
                    UF VARCHAR(2) NOT NULL
        )"""
        self.execute_query(query)
    
    def create_table_vendedor(self):
        query = """CREATE TABLE IF NOT EXISTS loja.vendedor (
                    id_vendedor INT NOT NULL PRIMARY KEY,
                    nome_vendedor VARCHAR(50) NOT NULL,
                    salario_fixo INT NOT NULL,
                    faixa_comissao INT
        )"""
        self.execute_query(query)

    def create_table_pedido(self):
        query = """CREATE TABLE IF NOT EXISTS loja.pedido(
                    id_pedido INT NOT NULL PRIMARY KEY,
                    prazo_entrega DATE NOT NULL,
                    id_vendedor INT NOT NULL,
                    id_cliente INT NOT NULL,
                    FOREIGN KEY (id_vendedor) REFERENCES vendedor (id_vendedor),
                    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
        )"""
        self.execute_query(query)
    
    def create_table_produto(self):
        query = """CREATE TABLE IF NOT EXISTS loja.produto(
                    id_produto INT NOT NULL PRIMARY KEY,
                    unidade INT NOT NULL,
                    descricao VARCHAR(50),
                    valor FLOAT NOT NULL
        )"""
        self.execute_query(query)
    
    def create_table_item_pedido(self):
        query = """CREATE TABLE IF NOT EXISTS loja.item_pedido(
                    id_produto INT NOT NULL,
                    id_pedido INT NOT NULL,
                    quantidade INT NOT NULL,
                    PRIMARY KEY (id_produto, id_pedido)
        )"""
        self.execute_query(query)
        
    def create_tables(self):
        self.create_table_cliente()
        self.create_table_vendedor()
        self.create_table_produto()
        self.create_table_pedido()
        self.create_table_item_pedido()
        