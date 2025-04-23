# Fusca Preto Garage 🚗

Sistema para de catálogo de carros clássicos desenvolvido com Flask e arquitetura MVC.

## 📋 Sobre o Projeto

A Fusca Preto Garage é uma plataforma web para exposição e gerenciamento de carros clássicos. O sistema permite visualizar um catálogo de carros antigos com informações detalhadas sobre cada veículo, incluindo marca, modelo, ano, quilometragem e preço.

### 🎯 Objetivo

Criar uma plataforma moderna e intuitiva para apresentação de carros clássicos, facilitando a visualização e gerenciamento do catálogo de veículos.

## 🔧 Tecnologias Utilizadas

- **Python 3.13**
- **Flask 3.0.2**: Framework web
- **SQLAlchemy**: ORM para banco de dados
- **Flask-SQLAlchemy**: Integração Flask com SQLAlchemy
- **Flask-Migrate**: Gerenciamento de migrações do banco de dados
- **SQLite**: Banco de dados
- **Tailwind CSS**: Framework CSS para estilização
- **Jinja2**: Engine de templates

## 🏗️ Arquitetura MVC

O projeto segue o padrão arquitetural MVC (Model-View-Controller):

### Estrutura de Diretórios
```
venda-carros-mvc/
├── app/
│   ├── init.py
│   ├── models/         # Camada Model
│   │   └── carro.py
│   ├── controllers/    # Camada Controller
│   │   └── carros_controller.py
│   ├── views/          # Camada View
│   │   └── templates/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── carros.html
│   │       ├── novo_carro.html
│   │       └── editar_carro.html
│   └── routes.py       
├── instance/
│   └── database.db     
├── migrations/         
├── requirements.txt    
└── run.py              
```

### Componentes MVC

- **Model**: Responsável pela estrutura dos dados e regras de negócio
- **View**: Responsável pela apresentação dos dados ao usuário
- **Controller**: Gerencia as interações entre Model e View

## 💻 Requisitos do Sistema

### Funcionais
- Visualização do catálogo de carros
- Cadastro de novos carros
- Edição de informações dos carros
- Exclusão de carros do catálogo

### Não Funcionais
- Interface responsiva
- Design moderno e minimalista
- Persistência em banco de dados
- Arquitetura MVC

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)

### Configuração do Ambiente
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/venda-carros-mvc.git
cd venda-carros-mvc
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados:
```bash
flask db init
flask db migrate -m "Migracao inicial"
flask db upgrade
```

5. Popule o banco com dados iniciais:
```bash
python seed_carros.py
```

6. Execute a aplicação:
```bash
python run.py
```

A aplicação estará disponível em `http://localhost:5000`

## 📚 Endpoints da API

- `GET /`: Página inicial
- `GET /carros`: Lista todos os carros
- `GET /carros/novo`: Formulário para adicionar novo carro
- `POST /carros/novo`: Adiciona um novo carro
- `GET /carros/<id>/editar`: Formulário para editar carro
- `POST /carros/<id>/editar`: Atualiza um carro
- `POST /carros/<id>/deletar`: Remove um carro