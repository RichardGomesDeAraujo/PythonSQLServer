import pyodbc

## Criar a conexão com os dados do banco de dados 
## Importante manter o sinal de = sem espaços
dadosconexao = (
    "Driver={SQL Server};"
    "Server=BOOK-JYYYYYYYYY;"
    "Database=DBBV;"
)

## Efetivar a conexão com o comando pyodbc
conexao = pyodbc.connect(dadosconexao)

## Imprimir uma mensagem caso a conexão seja bem sucedida
print("Conexão Bem Sucedida")

## Criar uma "Nova Consulta" para rodar comandos no SQL Server
cursor = conexao.cursor()

## Criando variáveis para inserir dados dinâmicos na tabela
NrPasta = 3002
NrRequisicao = 3002
DtRequisicao = "12/08/2023"
DtExecucao = "13/08/2023"
StRequisicao = "Concluída"
Login = "S"
PzSla = 2
PzExecucao = 1
FlConformidade = "S"
NmAssessoria = "Gary"

## Criar os comandos para rodar no SQL
comando = f"""
INSERT INTO TbJuridicoEncerramento
VALUES
(
{NrPasta},{NrRequisicao},'{DtRequisicao}','{DtExecucao}','{StRequisicao}','{Login}',{PzSla},{PzExecucao},'{FlConformidade}','{NmAssessoria}'
)
"""

## Criar Executável do comando
cursor.execute(comando)

## Se for executado algum comando de criação ou alteração do banco de dados
## será necessário o comando de commit abaixo:
cursor.commit()


