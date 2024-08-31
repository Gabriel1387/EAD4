from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa = Pessoa("Carlos", "123456", "2024-01-01", True)
print('Instância da classe Pessoa:')
print(pessoa.imprimir())

pessoa_fisica = PessoaFisica("Ana", "654321", "2023-06-15", False, "1985-12-10", "123.456.789-00", "MG-12.345.678")
print('\nInstância da classe PessoaFisica:')
print(pessoa_fisica.imprimir())

pessoa_juridica = PessoaJuridica("Empresa X", "789123", "2023-04-20", True, "2010-09-15", "12.345.678/0001-95")
print('\nInstância da classe PessoaJuridica:')
print(pessoa_juridica.imprimir())

try:
    pessoa.cpf = "111.222.333-44"  
except ValueError as e:
    print(f"\nErro ao definir CPF: {e}")

try:
    pessoa_juridica.cnpj = "12.345.678/0001-9"  
except ValueError as e:
    print(f"\nErro ao definir CNPJ: {e}")

pessoa_fisica.cpf = "123.456.789-00"
pessoa_juridica.cnpj = "12.345.678/0001-95"

print('\nInstância da classe Pessoa após alteração:')
print(pessoa.imprimir())

print('\nInstância da classe PessoaFisica após alteração:')
print(pessoa_fisica.imprimir())

print('\nInstância da classe PessoaJuridica após alteração:')
print(pessoa_juridica.imprimir())
