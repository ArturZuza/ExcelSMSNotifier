# ExcelSMSNotifier

O **ExcelSMSNotifier** é um script em Python que analisa uma planilha Excel com nomes de alunos e suas notas finais. Caso algum aluno tenha uma nota abaixo de 5, o sistema envia um SMS para o professor com as informações do aluno e da nota usando a API Twilio.

## Funcionalidades

- Leitura de uma planilha Excel contendo nomes de alunos e suas notas finais.
- Identificação automática de alunos com notas abaixo de 5.
- Envio de SMS ao professor com o nome do aluno e a nota usando Twilio.

## Instalação

### Requisitos

- Python 3.5 ou Superior
- Bibliotecas:
  - `pandas`
  - `openpyxl` (para manipulação de arquivos Excel)
  - API Twilio

### Como instalar

1. Clone este repositório:
    ```bash
    git clone https://github.com/ArturZuza/ExcelSMSNotifier.git
    ```

2. Navegue até a pasta do projeto:
    ```bash
    cd ExcelSMSNotifier
    ```

3. Instale as dependências:
    ```bash
    pip install pandas openpyxl twilio
    ```

4. Adicione suas credenciais da Twilio (Account SID e Auth Token) diretamente no código, substituindo os valores em `account_sid` e `auth_token`.

5. Certifique-se de configurar o número de telefone de envio e recepção no campo `to` e `from_` da função `client.messages.create()`.

## Uso

1. Coloque a planilha Excel com os dados dos alunos e notas no diretório do projeto. O nome do arquivo Excel deve ser `notas.xlsx`.
   
2. Execute o script:
    ```bash
    python nome_do_arquivo.py
    ```

3. Se algum aluno tiver uma nota abaixo de 5 na coluna **RESULTADO FINAL**, será enviado um SMS ao número configurado no script com a seguinte mensagem:
    ```
    Alguém ficou com nota abaixo da média. Aluno: {aluno}, Nota: {nota}
    ```

### Exemplo de Planilha

A planilha Excel deve seguir este formato:

| ALUNO           | RESULTADO FINAL |
|-----------------|-----------------|
| Abel Ferreira   | 4.8             |
| Marcos Assunção | 6.0             |
| Jorge Valdivia  | 3.5             |

## Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie um branch com sua nova feature: `git checkout -b minha-nova-feature`.
3. Faça commit das suas mudanças: `git commit -m 'Adicionada nova feature'`.
4. Envie suas mudanças para o branch: `git push origin minha-nova-feature`.
5. Crie um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
