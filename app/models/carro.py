from app import db

class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quilometragem = db.Column(db.Integer, nullable=False, default=0, server_default='0')
    
    def __repr__(self):
        return f'<Carro {self.marca} {self.modelo}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'modelo': self.modelo,
            'ano': self.ano,
            'preco': self.preco,
            'quilometragem': self.quilometragem
        } 