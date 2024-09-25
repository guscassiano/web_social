#🌐 Tuwit (Web Social) - Sua Rede Social Personalizada 🐦
##Bem-vindo ao Tuwit!
O Tuwit (ou Web Social) é uma aplicação de microblogging inspirada no Twitter, onde os usuários podem postar atualizações curtas e seguir outros perfis. Construído com as mais modernas tecnologias, o Tuwit oferece uma experiência rápida e interativa para todos os usuários.

##🚀 Principais Tecnologias Utilizadas
Linguagem: Python 3.10 🐍
Framework: Django (para o back-end escalável e robusto) 🌱
APIs RESTful: Django Rest Framework (DRF) para construção das APIs 💻
Dinâmicas de Front: jQuery com AJAX para funcionalidades em tempo real 🎨
Banco de Dados: PostgreSQL (no Docker, mas em desenvolvimento local utiliza SQLite) 🗄️
Docker & Docker-compose: Containers separados para o app e banco de dados facilitam o deploy e a escalabilidade 🐳
Arquivos Estáticos: Utilização do staticfiles para centralizar CSS e outros recursos 📂
🛠️ Rodando o Projeto Localmente
Siga estas instruções para configurar e rodar o projeto na sua máquina local:

##Pré-requisitos:
Python 3.10 instalado
Docker e Docker Compose configurados corretamente
Passo a Passo:
Clone o repositório:

bash
Copiar código
git clone https://github.com/guscassiano/web_social.git
Navegue até o diretório do projeto:

bash
Copiar código
cd web_social
Build dos containers com Docker:

bash
Copiar código
docker-compose up --build
Acesse o Tuwit no navegador: O projeto estará disponível em: http://localhost:8000/

📂 Estrutura do Projeto
bash
Copiar código
web_social/
│
├── env/                         # Ambiente virtual
├── feed/                        # Funcionalidades relacionadas ao feed
├── media/                       # Armazenamento de uploads de mídia (como imagens de perfil)
├── register/                    # Módulo de registro e autenticação
├── social_web_page/             # Páginas web da aplicação
├── static/                      # Arquivos estáticos
├── staticfiles/                 # Configuração de staticfiles
├── .env                         # Variáveis de ambiente
├── docker-compose.yml           # Configuração do Docker Compose
├── Dockerfile                   # Configuração do Docker para o app
├── manage.py                    # Gerenciador do Django
├── README.md                    # Documentação do projeto
├── requirements.txt             # Dependências do projeto
└── db.sqlite3                   # Banco de dados SQLite (para desenvolvimento)
📡 APIs Disponíveis
As APIs do Tuwit são construídas usando Django Rest Framework. Abaixo estão algumas das principais rotas disponíveis no projeto:

Admin:

GET /admin/: Acesso ao painel de administração do Django.
Autenticação e Registro:

POST /api/v1/register/: Criar um novo registro de usuário via API.
POST /api/v1/login/: Obter token JWT para login.
POST /api/v1/refresh/: Atualizar o token JWT.
Perfis:

GET /perfil/<int:pk>/: Ver perfil de um usuário.
PUT /perfil/<int:pk>/update/: Atualizar informações de perfil.
Feed e Posts:

GET /feed/: Exibir a lista de tuwits (postagens).
POST /like/<int:post_id>/: Dar "like" em um tuwit.
DELETE /post/<int:post_id>/delete/: Excluir um tuwit.
Seguir Usuário:

POST /seguir/<int:user_id>/: Seguir ou deixar de seguir um usuário.
🎨 Funcionalidades Futuras
Comentários em Tuwits: Adicionar um sistema de comentários.
Mensagens Diretas: Enviar mensagens privadas entre usuários.
Notificações em Tempo Real: Implementar WebSockets para alertas instantâneos.
Retuwit: Repostar tuwits de outros usuários.
⚠️ Nota: A funcionalidade de dar "like" em um tuwit já está implementada.

🐳 Dockerizando o Tuwit
O projeto está configurado para rodar em containers Docker. Aqui estão os dois containers principais:

App: Container que executa a aplicação Django.
Banco de Dados: Container PostgreSQL (em desenvolvimento local, utilizamos SQLite).
Comandos Docker
Para rodar o projeto:

bash
Copiar código
docker-compose up
Para criar um build completo do Docker:

bash```
Copiar código
docker-compose up --build
🤝 Contribuindo
Quer contribuir com o Tuwit? Aqui está o processo básico:

Faça um fork do projeto.
Crie uma branch para a sua feature (git checkout -b feature/nova-feature).
Faça commit das suas alterações (git commit -m 'Adiciona nova feature').
Faça push para a branch (git push origin feature/nova-feature).
Crie um Pull Request.
📜 Licença
Este projeto está licenciado sob a MIT License.

🦸 Autor
Criado com 💻 e ☕ por Seu Nome.
