from flask import request, jsonify, render_template
from app.models import Livro
from app import db

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')  # Renderiza o arquivo HTML da página inicial

    @app.route('/api/livros', methods=['GET'])
    def listar_livros():
        livros = Livro.query.all()
        return jsonify([livro.to_dict() for livro in livros])

    @app.route('/api/livros', methods=['POST'])
    def criar_livro():
        data = request.json
        livro = Livro(
            nome=data.get('nome'),
            autor=data.get('autor'),
            ano=data.get('ano'),
            exemplares=data.get('exemplares'),
            fotoCapa=data.get('fotoCapa')
        )
        db.session.add(livro)
        db.session.commit()
        return jsonify(livro.to_dict()), 201

    @app.route('/api/livros/<int:livro_id>', methods=['GET'])
    def consultar_livro(livro_id):
        livro = Livro.query.get_or_404(livro_id)
        return jsonify(livro.to_dict())

    @app.route('/api/livros/<int:livro_id>', methods=['PUT'])
    def editar_livro(livro_id):
        livro = Livro.query.get_or_404(livro_id)
        data = request.json
        livro.nome = data.get('nome', livro.nome)
        livro.autor = data.get('autor', livro.autor)
        livro.ano = data.get('ano', livro.ano)
        livro.exemplares = data.get('exemplares', livro.exemplares)
        livro.fotoCapa = data.get('fotoCapa', livro.fotoCapa)

        db.session.commit()
        return jsonify(livro.to_dict())

    @app.route('/api/livros/<int:livro_id>', methods=['DELETE'])
    def excluir_livro(livro_id):
        livro = Livro.query.get_or_404(livro_id)
        db.session.delete(livro)
        db.session.commit()
        return jsonify({'message': 'Livro excluído com sucesso'}), 204
