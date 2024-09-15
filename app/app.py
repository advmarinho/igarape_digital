from app import create_app

# Inicializar a aplicação com a função create_app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)  # Ajuste a porta se necessário
