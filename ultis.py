from models import Pessoas,  db_session, Usuario


def insere_pessoas():
    pessoa = Pessoas(nome='Joao', idade=72)
    pessoa.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Joao').first()
    
    

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Anselmo').first()
    pessoa.nome = 'Teste'
    db_session.add(pessoa)
    db_session.commit()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Joao').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuario(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuario():
    usuarios = Usuario.query.all()
    print(usuarios)



if __name__=='__main__':
    insere_usuario('Anselmo', '12345')
    insere_usuario('Prinscila', '12345')
    insere_usuario('teste', '12345')
    consulta_todos_usuario()