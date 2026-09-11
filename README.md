🤖Assistente Corporativo Inteligente — Projeto RAG🤖

Este projeto foi desenvolvido como parte do Challenge Alura, com foco em construir um agente de IA que responde perguntas de colaboradores usando documentos internos da empresa como base.

A aplicação combina busca semântica com geração de linguagem, garantindo respostas contextualizadas e sempre acompanhadas das fontes consultadas.

🎯 Finalidade
O agente foi criado para:

Apoiar colaboradores em dúvidas sobre políticas internas;

Facilitar acesso a informações de RH e benefícios;

Reduzir tempo gasto em consultas manuais;

Garantir transparência ao exibir a origem de cada resposta.

🔧 Como Funciona
Coleta de documentos: PDFs são adicionados à pasta ./base_docs.

Divisão em blocos (chunking): os textos são segmentados para melhorar a precisão da busca.

Criação de embeddings: cada trecho é convertido em vetor semântico.

Busca vetorial: o ChromaDB identifica os trechos mais relevantes.

Geração da resposta: o modelo Gemini utiliza os trechos recuperados para compor a resposta.

Interface de uso: interação via Streamlit, em formato de chat simples e direto.

🛠️ Stack Tecnológica
Ferramenta	Papel
Python	Linguagem principal
LangChain	Orquestração do pipeline RAG
Google Gemini API	Embeddings e geração de texto
ChromaDB	Armazenamento vetorial
Streamlit	Interface web
PyPDFLoader	Extração de texto de PDFs
OCI	Deploy em nuvem


📂 Estrutura
Código
Projeto-RAG/
base_docs/
arquivos.pdf
src/
 app.py
requirements.txt
.env
.gitignore
 README.md
🚀 Execução
Clone o repositório

bash
git clone https://github.com/seu-usuario/Projeto-RAG.git
cd Projeto-RAG
Crie o ambiente virtual

bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.\.venv\Scripts\activate    # Windows
Instale dependências

bash
pip install -r requirements.txt
Configure o .env com sua chave:

Código
GOOGLE_API_KEY=sua_chave_aqui
Adicione documentos na pasta base_docs/.

Execute a aplicação:

bash
streamlit run src/app.py
💡 Exemplos de Perguntas
"Quais são as regras para solicitar reembolso?"

"Quais benefícios estão disponíveis para os colaboradores?"

"Como funciona a política de férias?"

☁️ Deploy
O projeto pode ser hospedado em Oracle Cloud Infrastructure (OCI) ou outro provedor, permitindo acesso remoto e escalabilidade.

🔐 Segurança
Nunca exponha chaves de API no código.

Use variáveis de ambiente e mantenha .env no .gitignore.

📌 Sobre
Este projeto aplica conceitos de:

RAG

Embeddings

Busca semântica

Cloud Computing

👩‍💻 Autora: Geovana Gonzaga Bizerra
Projeto desenvolvido para aprendizado e portfólio.
