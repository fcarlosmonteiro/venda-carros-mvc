from app import create_app, db
from app.models.carro import Carro

app = create_app()

carros = [
    {
        'marca': 'Volkswagen',
        'modelo': 'Fusca 1300',
        'ano': 1970,
        'preco': 35000.00,
        'quilometragem': 85000
    },
    {
        'marca': 'Volkswagen',
        'modelo': 'Fusca 1600',
        'ano': 1974,
        'preco': 42000.00,
        'quilometragem': 92000
    },
    {
        'marca': 'Chevrolet',
        'modelo': 'Opala SS',
        'ano': 1975,
        'preco': 85000.00,
        'quilometragem': 75000
    },
    {
        'marca': 'Chevrolet',
        'modelo': 'Opala Comodoro',
        'ano': 1979,
        'preco': 65000.00,
        'quilometragem': 88000
    },
    {
        'marca': 'Ford',
        'modelo': 'Maverick GT',
        'ano': 1974,
        'preco': 95000.00,
        'quilometragem': 65000
    },
    {
        'marca': 'Ford',
        'modelo': 'Maverick Super',
        'ano': 1976,
        'preco': 75000.00,
        'quilometragem': 78000
    },
    {
        'marca': 'Ford',
        'modelo': 'Corcel GT',
        'ano': 1975,
        'preco': 45000.00,
        'quilometragem': 95000
    },
    {
        'marca': 'Ford',
        'modelo': 'Corcel Luxo',
        'ano': 1973,
        'preco': 38000.00,
        'quilometragem': 102000
    },
    {
        'marca': 'Ford',
        'modelo': 'F-100',
        'ano': 1970,
        'preco': 58000.00,
        'quilometragem': 125000
    }
]

def seed_carros():
    with app.app_context():
        # Limpa todos os carros existentes
        Carro.query.delete()
        
        # Adiciona os novos carros
        for carro_data in carros:
            carro = Carro(**carro_data)
            db.session.add(carro)
        
        # Salva todas as mudanças
        db.session.commit()
        print("Carros cadastrados com sucesso!")

if __name__ == '__main__':
    seed_carros() 