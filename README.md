# redes_servidor_web

## Servidor TCP

Olá! Neste trabalho, nós aprendemos os fundamentos da programação de soquetes para conexões TCP em Python 🐍. <br>
Descobrimos:

- Como criar um soquete
- Vinculá-lo a um endereço e porta específicos
- Enviar e receber um pacote HTTP 🌐.

Além disso, aprendemos alguns fundamentos do formato de cabeçalho HTTP 📑.

Durante este projeto, desenvolvemos um servidor da Web 🔧 que lida com uma solicitação HTTP por vez. <br>
Nosso servidor é capaz de:

- aceitar e analisar a solicitação HTTP
- obter o arquivo solicitado do sistema de arquivos do servidor
- criar uma mensagem de resposta HTTP consistindo no arquivo solicitado precedido por linhas de cabeçalho
- enviar a resposta diretamente ao cliente 👤.

Caso o arquivo não estivesse presente no servidor, nosso servidor envia automaticamente uma mensagem HTTP "404 Not Found" de volta ao cliente ❌.

## Servidor UDP

Este programa cliente tem como objetivo enviar 10 pings para o servidor, utilizando o protocolo UDP. Como este protocolo não é confiável, pode ocorrer perda de pacotes durante a transmissão entre o cliente e o servidor.

Para contornar esse problema, neste programa cliente, foi definido um tempo limite (timeout) de um segundo para cada ping enviado ao servidor. Caso uma resposta não seja recebida dentro desse intervalo de tempo, o cliente assume que o pacote foi perdido na rede.

O programa cliente foi implementado em Python e utiliza a biblioteca socket para criar um socket de datagrama. Para configurar o tempo limite no socket criado, é necessário consultar a documentação do Python, visto que cada sistema operacional pode ter sua própria forma de definir essa configuração.

Este programa cliente é uma solução simples para enviar pings ao servidor usando o protocolo UDP, mas não é adequado para ambientes de rede complexos ou de alta disponibilidade. É importante lembrar que há outras formas de garantir a entrega de pacotes, como a utilização de protocolos mais robustos, como o TCP.

## Como executar o projeto?

Utilize a sequência de comandos abaixo para executar o projeto:

```bash
# Clone este repositório
$ git clone

# Acesse a pasta do projeto no terminal/cmd
$ cd redes_servidor_web
```
