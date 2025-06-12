from mercado import app
from flask import render_template, redirect, url_for, flash
from mercado.models import Item, User
from mercado.forms import CadastroForm, LoginForm
from mercado import db
from flask_login import login_user, logout_user, login_required

@app.route('/')
def page_home():
    return render_template("home.html")

@app.route('/produtos')
@login_required
def page_produto():
    itens1 = Item.query.all()
    return render_template("produtos.html", itens=itens1)

@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
    forms = CadastroForm()
    if forms.validate_on_submit():
        usuario = User(
            usuario = forms.usuario.data,
            email = forms.email.data,
            senhacrip = forms.senha1.data
        )
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('page_produto'))
    if forms.errors != {}:
        for err in forms.errors.values():
            flash(f"Erro ao cadastrar usuário {err}", category="danger")
    return render_template("cadastro.html", form=forms)

@app.route('/login', methods=['GET','POST'])
def page_login():
    forms = LoginForm()
    if forms.validate_on_submit():
        usuario_logado = User.query.filter_by(usuario=forms.usuario.data).first()
        if usuario_logado and usuario_logado.converte_senha(senha_texto_claro = forms.senha.data):
            login_user(usuario_logado)
            flash(f'Sucesso! Seu login é : {usuario_logado.usuario}', category='success')
            return redirect(url_for('page_produto'))
        else:
            flash(f'Usuário ou senha estão incorretos! Tente novamente.', category='danger')
    return render_template('login.html', form = forms)

@app.route('/logout')
def page_logout():
    logout_user()
    flash("Você fez o logout", category="info")
    return redirect(url_for('page_home'))