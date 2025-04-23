from flask import render_template, redirect, url_for, flash, request
from app.models.carro import Carro
from app import db

class CarrosController:
    @staticmethod
    def listar_carros():
        carros = Carro.query.all()
        return render_template('carros.html', carros=carros)
    
    @staticmethod
    def criar_carro():
        if request.method == 'POST':
            marca = request.form['marca']
            modelo = request.form['modelo']
            ano = int(request.form['ano'])
            preco = float(request.form['preco'])
            
            novo_carro = Carro(marca=marca, modelo=modelo, ano=ano, preco=preco)
            db.session.add(novo_carro)
            db.session.commit()
            
            flash('Carro adicionado com sucesso!', 'success')
            return redirect(url_for('main.listar_carros'))
        
        return render_template('novo_carro.html')
    
    @staticmethod
    def editar_carro(id):
        carro = Carro.query.get_or_404(id)
        
        if request.method == 'POST':
            carro.marca = request.form['marca']
            carro.modelo = request.form['modelo']
            carro.ano = int(request.form['ano'])
            carro.preco = float(request.form['preco'])
            
            db.session.commit()
            flash('Carro atualizado com sucesso!', 'success')
            return redirect(url_for('main.listar_carros'))
        
        return render_template('editar_carro.html', carro=carro)
    
    @staticmethod
    def deletar_carro(id):
        carro = Carro.query.get_or_404(id)
        db.session.delete(carro)
        db.session.commit()
        flash('Carro deletado com sucesso!', 'success')
        return redirect(url_for('main.listar_carros')) 