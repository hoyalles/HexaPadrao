# CRUD de Usuários com Arquitetura Hexagonal

Este é o repositório oficial do projeto **fastapi_hex**, desenvolvido como parte da apresentação da disciplina **Qualidade de Software**, no curso de **Análise e Desenvolvimento de Sistemas** da **UFC**.

Este projeto é uma aplicação em **Python** utilizando **FastAPI**, que implementa um sistema de **CRUD de usuários** baseado na **arquitetura hexagonal**. O objetivo é aprofundar o entendimento prático sobre os conceitos de separação de responsabilidades e boas práticas de arquitetura de software.

🔗 Acesse o repositório completo: [https://github.com/kalil-camera/fastapi_hex.git](https://github.com/kalil-camera/fastapi_hex.git)



### Estrutura do Projeto

```
fastapi_hex/
├── app/                     
│   ├── main.py              # Ponto de entrada da aplicação FastAPI
│   ├── application/         # Camada de aplicação (casos de uso / serviços)
│   │   └── services.py
│   ├── domain/              # Camada de domínio 
│   │   ├── models.py
│   │   └── ports.py
│   ├── infrastructure/      # Implementações técnicas (ex: repositórios)
│   │   └── repositories.py
│   └── interfaces/          # Interfaces externas (ex: APIs)
│       └── api.py
├── requirements.txt         # Dependências do projeto
├── README.md                # Documentação do projeto
└── .gitignore              

```


## Iniciando

Siga estes passos para configurar e executar o projeto:

### Pré-requisitos

- Python 3.8 ou superior
- `pip` (gerenciador de pacotes do Python)

### Configuração

1. **Clone o repositório**  
    ```bash
    git clone <repository-url>
    cd user_crud_hex
    ```

2. **Crie o ambiente virtual**  
    ```bash
    python -m venv venv
    ```

3. **Ative o ambiente virtual**  
    - No Windows:
      ```bash
      venv\Scripts\activate
      ```
    - No macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Instale as dependências**  
    ```bash
    pip install -r requirements.txt
    ```

### Executando a Aplicação

1. **Inicie o FastAPI Server**  
    ```bash
    uvicorn app.main:app --reload
    ```

2. **Acesse a documentação da API**  
    Abra seu navegador e pesquise:  
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

##  Licença  
Este projeto está licenciado sob a MIT License. Veja [MIT License](LICENSE) para mais detalhes.

##  **Agradecimentos**
###
- **Anderson Goncalves Uchoa**: Orientador do projeto e professor da disciplina de Qualidade de Software na UFC Itapajé

###
- **Equipe do Projeto:** Carlos Kaique Rosa Silva ([Kaique Silva](https://github.com/hoyalles)) e Paulo Matheus Cardoso Viana ([Paulo Cardoso](https://github.com/Paulim18))
