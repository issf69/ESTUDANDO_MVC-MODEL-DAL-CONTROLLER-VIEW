from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)
    @classmethod
    def ler(self):
        nome = 'Irene'
        idade = 54
        cpf = '12345678910'
        return Pessoa(nome, idade, cpf)


#p1 = Pessoa( 'Irene', 54, ' 12345678910 ')
#PessoaDal.salvar(p1)
#print(PessoaDal.ler())
#print(PessoaDal.ler().cpf)
#print(PessoaDal.ler().idade)
#print(PessoaDal.ler().nome)