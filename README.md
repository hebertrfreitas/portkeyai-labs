# Análise da ferramenta AI GTW PortkeyAI.


Este repositorio foi criado com o intuito de realizar uma análise da ferramenta [Portkey AI Gateway](https://github.com/Portkey-AI/gateway)


A ferramenta portkey é um AI GTW que tem por principal objetivo abstrair as chamadas realizadas da sua infraestrutura para diferentes provedores e modelos de LLMs como OpenAI, AzureOpenAI, AWS bedrock, Anthropic, entre outros.

Ao abstrair estas chamadas a ferramenta disponibiliza um único contrato independente de provedor de LLM, tal contrato é baseado na especificação de openapi da OpenAI, facilitando assim o trabalho do desenvolvedor para suportar novos provedores sem ter que fazer alterações massivas no seu código.

Neste repositorio testamos a versão opensource da ferramenta que pode ser provisionada na sua infraestrutura cloud.

## Como executar os testes.

1. Execute o docker-compose para subir localmente o portkey
```sh
docker-compose up -d
```
2. Execute os testes via python ou via bash

Os testes foram realizados com os provedores OpenAI(modelo gpt-3.5-turbo-16k) e AWS bedrock (modelo amazon.titan-text-express-v1) portanto é necessário ter credencias para ambas os provedores.

Antes de começar a execução copie o arquivo `.env.test` para `.env` e preencha as variáveis necessárias.

O portkey permite iteração via python usando a lib da OpenAI (como modelo para qualquer provedor), usando a lib nodejs da OpenAI ou ainda via request http diretamente.

Abaixo o tutorial de execução de testes via python ou via arquivo .sh contendo scripts curl para demonstrar a diferença de ambas as formas de iteração.

**Para executar os testes via python**

```bash
#este projeto foi testado com python 3.11.7
#crie um virtual environment
python -m venv .venv
#ative o virtual environment
source .venv/bin/activate
#instale as dependências
pip install -r requirements.txt
#execute o teste
python src/main.py
```

**para executar os testes via bash**

```bash
#conceda permissão de execução no script
chmod +x requests.sh
#carrege as variáveis de ambiente previamente preenchidas
source .env
#execute o script
./requests.sh
```