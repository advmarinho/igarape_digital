from app import db

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    exemplares = db.Column(db.Integer, nullable=False)
    fotoCapa = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'autor': self.autor,
            'ano': self.ano,
            'exemplares': self.exemplares,
            'fotoCapa': self.fotoCapa
        }
