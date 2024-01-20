from models import Pessoas,  db_session


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



if __name__=='__main__':
    insere_pessoas()