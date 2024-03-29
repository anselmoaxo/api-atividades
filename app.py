from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuario
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)





@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuario.query.filter_by(login=login, senha=senha).first()


class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa nao encontrada'
            }
        return response
    
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
            }
        return response
    
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = f'Pessoa Excluida com sucesso {pessoa.nome}'
        pessoa.delete()
        return { 'status': 'Sucesso', 'mensagem': mensagem}
    
    
class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade } for i in pessoas]
        return response
    
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
              
            }
        return response
    

class ListaAtividade(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = []

        for i in atividades:
            # Verifica se i.pessoa não é None antes de acessar o atributo nome
            pessoa_nome = i.pessoa.nome if i.pessoa else None

            response.append({
                'id': i.id,
                'nome': i.nome,
                'pessoa': pessoa_nome
            })

        return response

    def post(self):
        dados = request.json

        # Certifique-se de que a classe Pessoas e Atividades estejam corretamente definidas no seu código
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()

        # Certifique-se de que a classe Atividades tenha um método 'save()' definido
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()

        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response

# rotas dos endpoints
api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividade, '/atividade/')


if __name__=='__main__':
    app.run(debug=True)