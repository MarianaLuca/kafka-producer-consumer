# kafka-producer-consumer
## Este repositório contém código e instruções para configurar uma fila producer-consumer baseada em Kafka usando Docker Compose.

## Índice
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)
- [Agradecimentos](#agradecimentos)


# Requisitos:
- VS Code
- Docker desktop
- node js
- python

# Instalação
- Faça um clone do repositório atual:
 ```bash
https://github.com/MarianaLuca/kafka-producer-consumer.git
```
- Abra o projeto no vscode (ou editor de código de sua preferencia)
- Abra um terminal
- Faça a instalação das dependencias
 ```bash
npm install
```

# Uso
## Após os passos acima, faça o seguinte:

- Abra o Docker desktop (somente para realizar a conexão)
- Verifique se as portas utilizadas  no código estão livres (se não, faça a alteração das mesmas)
- Abra um novo terminal
- De o comando para inicializar a fila:
 ```bash
docker-compose up
```
- Em terminais diferentes, você pode visualizar os logs do PRODUCER e do CONSUMER:
```bash
docker-compose logs -f producer
docker-compose logs -f consumer
```
Com esses passos, a fila deve funcionar :)

# Contribuição
Contribuições são bem-vindas! Por favor, envie um pull request ou abra uma issue para discutir suas mudanças.

# Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](link para o arquivo) para detalhes.

# Contato
Mariana Luca Rocha - mluca2564@gmail.com

LinkedIn - https://www.linkedin.com/in/mariana-luca-rocha-157a90219/

# Agradecimentos
Pedro Matias de Araujo - pela sujestão do trabalho 

ChatGPT - pela ajuda com os erros sem solução rsrs 


