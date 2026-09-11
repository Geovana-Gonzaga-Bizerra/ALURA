🤖 Assistente Inteligente de Documentos — IA com RAG🤖
Projeto desenvolvido para o Challenge Alura, com o objetivo de criar um agente de IA capaz de responder dúvidas de colaboradores com base em documentos internos da empresa.

A aplicação utiliza a técnica de RAG (Retrieval-Augmented Generation), que combina busca semântica em documentos com geração de respostas por modelos de linguagem, garantindo informações contextualizadas e confiáveis.

🎯 Objetivo do Projeto
O agente foi desenvolvido para apoiar colaboradores em dúvidas relacionadas a:

Políticas de RH

Regras de Reembolso

Benefícios corporativos

Normas internas

Cada resposta inclui a fonte consultada, permitindo validação direta no documento original.

🏗️ Arquitetura da Solução
📂 Ingestão de documentos: PDFs adicionados à pasta ./docs são carregados com PyPDFLoader.

✂️ Segmentação (chunking): os textos são divididos em blocos menores para melhorar a precisão da busca.

🧠 Embeddings: cada trecho é convertido em vetor semântico com o modelo da Google.

🔎 Recuperação: o ChromaDB identifica os trechos mais relevantes e envia ao modelo Gemini.

💬 Resposta: o agente gera a resposta contextualizada e apresenta as fontes consultadas.

🌐 Interface: interação via Streamlit, em formato de chat simples e funcional.

🛠️ Tecnologias Utilizadas
Tecnologia	Função
Python 3.10+	Linguagem principal
LangChain	Pipeline RAG
Google Gemini API	Embeddings e geração de texto
ChromaDB	Banco vetorial
Streamlit	Interface web
PyPDFLoader	Extração de texto de PDFs
OCI	Deploy em nuvem


📂 Estrutura do Projeto

Código
Assistente-RAG/
│
├── docs/              # PDFs internos da empresa
│   └── exemplo.pdf
│
├── chroma_storage/    # Base vetorial persistida
├── src/
│   └── app.py         # Código principal
├── requirements.txt   # Dependências
├── .env               # Chave da API
└── README.md

📋 requirements.txt
streamlit
langchain
chromadb
google-generativeai
pypdf

🚀 Como rodar
Instale dependências: pip install -r requirements.txt
Configure sua chave no .env: GOOGLE_API_KEY=sua_chave_aqui
Adicione PDFs na pasta docs/.
Execute:streamlit run src/app.py

Código
GOOGLE_API_KEY=sua_chave_aqui
Adicione documentos na pasta docs/.

Execute a aplicação:

bas
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
