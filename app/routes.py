from flask import Blueprint, render_template
from app.controllers.carros_controller import CarrosController

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/carros')
def listar_carros():
    return CarrosController.listar_carros()

@main_bp.route('/carros/novo', methods=['GET', 'POST'])
def criar_carro():
    return CarrosController.criar_carro()

@main_bp.route('/carros/<int:id>/editar', methods=['GET', 'POST'])
def editar_carro(id):
    return CarrosController.editar_carro(id)

@main_bp.route('/carros/<int:id>/deletar', methods=['POST'])
def deletar_carro(id):
    return CarrosController.deletar_carro(id) 