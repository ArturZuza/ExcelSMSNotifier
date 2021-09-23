import pandas as pd
from twilio.rest import Client

# meu SID
account_sid = "AC6e2dce106df3fe3cbb8efdbaf0c1fd11"
# meu token
auth_token = "2a4eee7ead89ad02b0a9a6029ffc8d25"
client = Client(account_sid, auth_token)

# abrir o arquivo
# ver se algum aluno (1 a 20) tirou menos menos que 5 no resultado final (coluna S)
# se for menor do que 5 -> envia um SMS com o nome e a nota do aluno
lista_notas = ['notas']
for notas in lista_notas:
    tabela_notas = pd.read_excel(f'{notas}.xlsx')
    if (tabela_notas['RESULTADO FINAL'] < 5).any():
        aluno = tabela_notas.loc[tabela_notas['RESULTADO FINAL'] < 5, 'ALUNO'].values[0]
        nota = tabela_notas.loc[tabela_notas['RESULTADO FINAL'] < 5, 'RESULTADO FINAL'].values[0]
        print(f'alguem ficou com nota abaixo da media. Aluno: {aluno}, Nota: {nota}')
        message = client.messages.create(
            to="+5584991294012",
            from_="+16509841547",
            body=f'alguem ficou com nota abaixo da media. Aluno: {aluno}, Nota: {nota}')
        print(message.sid)
