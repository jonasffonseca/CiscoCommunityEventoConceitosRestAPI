# Conceitos de Rest API usando o Sandbox Cisco

Este projeto tem objetivo exclusivamente didático e foi utilizado no **[primeiro evento da Cisco Community em Português](https://www.linkedin.com/posts/jonas-fragaf_developer-devnet-devops-activity-6759217193625382913-fz1P)** onde abordamos conceitos de Rest API usando a documentação e o SandBox do Cisco Meraki.

:exclamation: É importante alertar que este repositório tem uso exclusivamente didático e não recomendamos utilizá-lo para soluções de produção ou em ambientes críticos. Para isto existem outros métodos como o [SDK do Meraki](https://developer.cisco.com/meraki/api-v1/#python).

#### Para executar este projeto os seguintes itens são necessários:

- [Python 3.8](https://www.python.org/downloads/) ou superior
- pip3 20.1 ou superior (Já vem instalado junto com o Python)
- virtualenv 16.7 ou superior
  - Para instalar o virtualenv execute o comando abaixo:
    ```sh
    pip install virtualenv
    ```
- Biblioteca Requests 2.25 ou superior (Explicamos como instalar a biblioteca dentro de um Environment abaixo)

### Recomendamos a criação de um Virtual Environment para segregar as bibliotecas e versões do servidor/computador

Para criar seu Environment:

```sh
python3 -m venv <nome_do_ambiente>
```

Para começar a utilizar o Environment (ingressar no Environment):

```sh
source <nome_do_ambiente>/bin/activate
```

Para instalar a biblioteca Requests dentro do Environment (depois de ingressar pela etapa acima):

```sh
pip3 install requests
```

### Para organizar o seu código de uma forma mais limpa no Visual Studio Code recomendamos o uso do [PEP8](https://code.visualstudio.com/docs/python/editing)

## Os seguintes arquivos foram criados para a didática do evento:

- getIds.py: Possui as funções que executam a busca e manipulação de informações dentro da nuvem Cisco Meraki
- networks.py: Arquivo que recebe a APIKEY e o Body de requisições para enviar como parâmetro às funções do arquivo getIds.py
