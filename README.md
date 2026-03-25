# 🤖 AI Chat Application – LangChain + Streamlit

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55%2B-FF4B4B?style=flat-square&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green?style=flat-square)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=flat-square&logo=openai)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

## 📚 Contexto Académico

Projeto prático desenvolvido como parte da **Formação em Inteligência Artificial**, oferecida pelo **Instituto ECOA PUC-Rio** em parceria com o **Serratec**. Integra-se ao **Módulo 3: Introdução a Large Language Models (LLMs)**, onde aplicamos conceitos fundamentais de prompt engineering, integração de APIs de IA e desenvolvimento de interfaces interativas.

---

## 📖 Resumo Executivo

Esta aplicação demonstra a implementação completa de um **chatbot inteligente** capaz de processar perguntas em linguagem natural e gerar respostas contextualizadas utilizando modelos de linguagem de ponta. O projeto valida competências em:

- **Engenharia de IA**: Integração de LangChain com modelos OpenAI
- **Full-Stack Python**: Arquitetura limpa, tratamento de erros, gestão de estado
- **UX/UI**: Interface responsiva e intuitiva com Streamlit
- **DevOps**: Isolamento de ambiente, gestão de variáveis de ambiente, cache inteligente

---

## 🎯 Objetivos & Aprendizados

✅ Compreender e implementar orquestração de LLMs via LangChain  
✅ Desenvolver interface de usuário moderna com Streamlit  
✅ Aplicar padrões de validação, tratamento de erros e feedback do usuário  
✅ Demonstrar boas práticas: cache, segurança (dotenv), performance  
✅ Criar aplicação pronta para produção, não apenas para estudo

---

## 🛠️ Stack Tecnológico

| Categoria              | Tecnologia           | Versão   | Propósito                     |
| ---------------------- | -------------------- | -------- | ----------------------------- |
| **Runtime**            | Python               | 3.13+    | Linguagem principal           |
| **Framework Web**      | Streamlit            | 1.55+    | Interface de usuário          |
| **Orquestração de IA** | LangChain            | Latest   | Abstração e pipeline de LLM   |
| **Modelo LLM**         | OpenAI (GPT-4o-mini) | -        | Motor de inteligência         |
| **Gestão de Env**      | python-dotenv        | Latest   | Variáveis de ambiente seguras |
| **Segurança**          | getpass              | Built-in | Entrada segura de credenciais |

---

## ⚙️ Funcionalidades Implementadas

### Core Features

- 🎨 **Interface limpa**: Título, descrição e componentes bem organizados
- 💬 **Chat interativo**: Área de texto para perguntas com validação
- ⚡ **Processamento em tempo real**: Botão com feedback visual (spinner)
- 🔄 **Caching inteligente**: Reutilização de cliente LLM para performance
- ⚠️ **Tratamento robusto de erros**: Try-catch com mensagens claras
- 🔐 **Segurança**: Chave de API gerenciada via dotenv e prompt seguro

### Componentes Streamlit

```python
✓ st.title()          # Título da aplicação
✓ st.write()          # Exibição de texto e respostas
✓ st.text_area()      # Campo para entrada de pergunta
✓ st.button()         # Botão de envio
✓ st.spinner()        # Indicador de carregamento
✓ st.success()        # Feedback positivo
✓ st.warning()        # Validações
✓ st.error()          # Mensagens de erro
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.13+
- pip ou conda
- Chave de API OpenAI (ou endpoint OpenRouter configurado)

### 1. Clonar e configurar ambiente

```bash
# Clone o repositório
git clone https://github.com/Diogooliveira10/ai-chat-app-langchain-streamlit
cd ai-chat-app-langchain-streamlit

# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Ativar ambiente (macOS/Linux)
source .venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install streamlit langchain langchain-openai python-dotenv
```

### 3. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
OPENAI_API_KEY=sk-...
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1  # (opcional, se usar OpenRouter)
```

### 4. Executar a aplicação

```bash
# Com módulo
python -m streamlit run main.py

# Ou diretamente
streamlit run main.py
```

A aplicação abrirá em `http://localhost:8501`

---

## 📁 Estrutura do Projeto

```
.
├── main.py                # Aplicação principal
├── .env                   # Variáveis de ambiente (não commitar!)
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Este arquivo
Python
```

---

## 💡 Fluxo de Funcionamento

```mermaid
digraph {
  A[Usuario digita pergunta] → B[Validação de input]
  B → C{Input válido?}
  C →|Não| D[Exibir aviso]
  C →|Sim| E[Inicializar LLM (cached)]
  E → F[Spinner: "Processando..."]
  F → G[Invocar ChatOpenAI]
  G → H{Sucesso?}
  H →|Erro| I[Exibir erro]
  H →|Sucesso| J[Exibir resposta]
}
```

---

## 🎓 Competências Demonstradas

| Área                | Competência           | Evidência no código                     |
| ------------------- | --------------------- | --------------------------------------- |
| **AI/ML**           | Integração com LLM    | `ChatOpenAI()`, `llm.invoke()`          |
| **Python Avançado** | Cache e otimização    | `@st.cache_resource`                    |
| **Segurança**       | Gestão de credenciais | `dotenv`, `getpass`                     |
| **Frontend**        | UI/UX moderna         | Componentes Streamlit bem organizados   |
| **Engenharia**      | Tratamento de erros   | Try-catch, validações, mensagens claras |
| **DevOps**          | Ambiente isolado      | Virtualenv, requirements.txt            |

---

> Projeto desenvolvido durante o curso **Formação em IA** do Instituto **ECOA PUC-Rio** em parceria com o **Serratec**.
