# 🌐 **Tuwit** - Sua Rede Social Personalizada 🐦

### **Bem-vindo ao Tuwit!**
O Tuwit (ou Web Social) é uma aplicação de microblogging inspirada no Twitter, onde os usuários podem postar atualizações curtas, curtí-las e seguir outros perfis. Construído com as mais modernas tecnologias, o Tuwit oferece uma experiência rápida e interativa para todos os usuários.

---

## 🚀 **Principais Tecnologias Utilizadas**

- **Linguagem**: Python 3.10 🐍
- **Framework**: Django (para o back-end escalável e robusto) 🌱
- **APIs RESTful**: Django Rest Framework (DRF) para construção das APIs 💻
- **Dinâmicas de Front**: jQuery com AJAX para funcionalidades em tempo real 🎨
- **Banco de Dados**: PostgreSQL (no Docker, mas em desenvolvimento local utiliza SQLite) 🗄️
- **Docker & Docker-compose**: Containers separados para o app e banco de dados facilitam o deploy e a escalabilidade 🐳
- **Arquivos Estáticos**: Utilização do `staticfiles` para centralizar os arquivos CSS e outros recursos 📂

---

## 🛠️ **Rodando o Projeto Localmente**

Siga estas instruções para configurar e rodar o projeto na sua máquina local:

### Pré-requisitos:

- **Python 3.10** instalado.
- **Docker** e **Docker Compose** instalados e configurados corretamente.

### Passo a Passo:

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/guscassiano/web_social.git
    ```

2. **Navegue até o diretório do projeto**:
    ```bash
    cd web_social
    ```

3. **Build dos containers com Docker**:
    ```bash
    docker-compose up --build
    ```

4. **Acesse o Tuwit no navegador**:
    O projeto estará disponível em: `http://localhost:8000/`

---

## 📂 **Estrutura do Projeto**

```bash
web_social/
│
├── env/                         # Ambiente virtual
├── feed/                        # Funcionalidades relacionadas ao feed
├── media/                       # Armazenamento de uploads de mídia (como imagens de perfil)
├── register/                    # Módulo de registro e autenticação de usuários
├── social_web_page/             # Pasta principal do projeto
├── static/                      # Arquivos estáticos
├── staticfiles/                 # Configuração de staticfiles
├── .env                         # Variáveis de ambiente
├── docker-compose.yml           # Configuração do Docker Compose
├── Dockerfile                   # Configuração do Docker para o app
├── manage.py                    # Gerenciador do Django
├── README.md                    # Documentação do projeto
├── requirements.txt             # Dependências do projeto
└── db.sqlite3                   # Banco de dados SQLite (para desenvolvimento)
```

---

## 📡 **APIs Disponíveis**

As APIs do Tuwit são construídas usando Django Rest Framework. Abaixo estão as rotas que pertencem à API (URLs que começam com /api/v1/):

### **APIs (RESTful)**
- Autenticação e Registro:
  - POST `/api/v1/register/`: Criar um novo registro de usuário via API.
  - POST `/api/v1/login/`: Obter token JWT para login.
  - POST `/api/v1/refresh/`: Atualizar o token JWT.
      
Nota: Essas APIs podem ser usadas para integração com clientes front-end ou outros serviços que precisem se comunicar diretamente com o back-end.

### **Endpoints do Front-end**
Além das APIs, o Tuwit também possui diversos endpoints voltados para o front-end, ou seja, aqueles que renderizam páginas e funcionam diretamente com o navegador. Estes endpoints são acessados por URLs que não começam com `/api/v1/`. Abaixo estão os principais:

- Admin:
  - `GET` `/admin/`: Acesso ao painel de administração do Django.
- Perfis:

  - `GET` `/perfil/<int:pk>/`: Ver perfil de um usuário.
  - `PUT` `/perfil/<int:pk>/update/`: Atualizar informações de perfil.
- Feed e Posts:

  - `GET` `/feed/`: Exibir a lista de tuwits (postagens).
  - `POST` `/like/<int:post_id>/`: Dar "like" em um tuwit.
  - `DELETE` `/post/<int:post_id>/delete/`: Excluir um tuwit.
- Seguir Usuário:

  - `POST` `/seguir/<int:user_id>/`: Seguir ou deixar de seguir um usuário.
Nota: Esses endpoints são voltados para a navegação web, retornando páginas HTML ou redirecionando os usuários dentro do site.

---

## 🎨 **Funcionalidades Futuras**
- Comentários em Tuwits: Adicionar um sistema de comentários.
- Mensagens Diretas: Enviar mensagens privadas entre usuários.
- Notificações em Tempo Real: Implementar WebSockets para alertas instantâneos nos E-mails dos usuários.
- Retuwit: Repostar tuwits de outros usuários.

---

## 🐳 **Dockerizando o Tuwit**
O projeto está configurado para rodar em containers Docker. Aqui estão os dois containers principais:

- Web: Container que executa a aplicação Django.
- db: Container PostgreSQL V16 (em desenvolvimento local, utilizamos SQLite).

### **Comandos Docker**
- Para rodar o projeto:
```bash
docker-compose up
```
- Para criar um build completo do Docker:
```bash
docker-compose up --build
```

---

## 🤝 **Contribuindo**
Quer contribuir com o Tuwit? Aqui está o processo básico:

1. Faça um fork do projeto.
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Crie um Pull Request.

---

## 🦸 **Autor**
Criado com 💻 e ☕ por Gustavo Cassiano Pinto.
