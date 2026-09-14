PROTÓTIPO DE SISTEMA DE GESTÃO DE PRODUTOS/ CLIENTES - CRUD

Aplicação web full-stack desenvolvida para gerenciamento, cadastro e vinculação relacional de clientes e produtos, implementando as operações de leitura, escrita e exclusão de dados.

Metodologia de Desenvolvimento

1 - levantamento de requisitos e modelagem relacional:  Identificação das entidades de domínio e necessidade de relacionamentos. Modelagem em esquema SQLite com integridade referencial( chave estrangeira com exclusão em cascata)
vinculando produtos aos seus respectivos clientes cadastrados.
2 - Estrutura e inicialização da Base de Banco de Dados: Script criado para inicializar o banco de dados (banco.py), implementando verificação condicional de existência com resolução de caminhos para evitar inconsistências.
3 - Backend e controle de rotas: Gestão de ciclo de vida de das conexões SQLite, definição de rotas HTTP com GET e POST para renderização, processamento de formulários e persistência/exclusão.
4 - Camada de Apresentação e integração: Utilização de frontend com Jinja2, templates em HTML estruturado com endpoints do backend, renderização dinâmica.

Tecnologias utilizadas
- Python 3/Flask: Servidor web, roteamento e lógica backend.
- SQLite3: Banco de dados relacional.
- HTML5/Jinja2: Estruturação semântica e motor de templates dinâmico.

  A ideia foi treinar fundamentos e forcar uma nova descoberta de stacks.
