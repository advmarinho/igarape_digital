from sqlalchemy import create_engine, text

# URL de conexão com o banco de dados
db_url = 'mysql+pymysql://andersons:rootroot2@gerenciamentolivros.cxboev8t3ieu.us-east-1.rds.amazonaws.com:3306/gerenciamento_livros'

def test_db_connection():
    try:
        # Cria um engine para testar a conexão
        engine = create_engine(db_url)
        with engine.connect() as connection:
            # Executa uma consulta simples para testar a conexão
            result = connection.execute(text('SELECT VERSION()'))
            for row in result:
                print(f"Conexão bem-sucedida! Versão do MariaDB: {row[0]}")
    except Exception as e:
        print(f"Falha na conexão com o banco de dados: {e}")

if __name__ == "__main__":
    test_db_connection()
