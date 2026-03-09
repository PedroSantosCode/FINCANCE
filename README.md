# 💰 FINANCE.BANK

> **Plataforma de Gestão Financeira Pessoal** — uma aplicação web full-stack para controle de entradas, saídas, contas bancárias, planejamento orçamentário e metas financeiras, com design premium dark-mode.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=flat&logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-CDN-06B6D4?style=flat&logo=tailwindcss&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)

---

## 📋 Sobre o Projeto

O **FINANCE.BANK** é uma aplicação de gestão financeira pessoal construída com Django. Permite ao usuário gerenciar contas bancárias, registrar entradas e saídas, definir planejamento por categoria, acompanhar metas financeiras, visualizar análises gráficas e exportar extratos em PDF.

A interface foi projetada com estética institucional dark-mode, utilizando glassmorphism, micro-animações e uma paleta de cores profissional voltada para wealth management.

---

## 🧱 Arquitetura

O projeto segue a arquitetura MVT (Model-View-Template) do Django, dividido em 4 apps independentes:

```
FINCANCE_PSW/
├── core/               # Configurações do projeto (settings, urls, wsgi)
├── perfil/             # Contas bancárias, categorias, dashboard analytics
├── extrato/            # Transações (entradas/saídas), exportação de extrato PDF
├── contas/             # Contas a pagar mensais e recorrentes
├── planejamento/       # Planejamento por categoria e metas financeiras
├── templates/          # Templates globais (base.html, gerenciar.html)
│   ├── bases/          # Template base com sidebar e header
│   ├── partials/       # Template HTML para geração de PDF
│   └── static/         # CSS estáticos
└── media/              # Uploads (ícones das contas bancárias, logo)
```

---

## ⚙️ Tecnologias Utilizadas

### Backend
| Tecnologia | Versão | Finalidade |
|---|---|---|
| **Python** | 3.11+ | Linguagem principal |
| **Django** | 6.0 | Framework web (MVT) |
| **WeasyPrint** | 68.1 | Geração de PDF do extrato |
| **python-dateutil** | 2.9 | Cálculo de meses anteriores no analytics |
| **Pillow** | 12.1 | Upload e processamento de imagens |
| **SQLite** | built-in | Banco de dados (desenvolvimento) |

### Frontend
| Tecnologia | Finalidade |
|---|---|
| **Tailwind CSS** (CDN) | Estilização utilitária |
| **Chart.js** (CDN) | Gráficos de analytics (barras, linhas) |
| **Vanilla JavaScript** | Interações, fetch API para sugestão de categoria via IA |
| **HTML5 / SVG** | Estrutura e ícones inline |

---

## 🧩 Funcionalidades

### 🏠 Dashboard (Home)
- Saldo total consolidado das contas cadastradas
- Totais de entradas e saídas do mês atual
- Gauge visual de equilíbrio financeiro (essenciais vs não essenciais)
- Alertas automáticos de orçamento ultrapassado por categoria

### 📊 Analytics (Dashboard)
- Gráfico de barras: gastos por categoria no mês atual
- Gráfico de linha: evolução mensal de entradas/saídas (últimos 6 meses)
- Gráfico de área: evolução do saldo patrimonial acumulado

### 📥 Extrato
- Listagem de transações filtradas por conta e categoria
- Exportação de extrato mensal em **PDF** via WeasyPrint

### ➕ Novo Valor
- Registro de entradas e saídas com conta, categoria, data e descrição
- **Sugestão automática de categoria via IA** baseada em palavras-chave da descrição (regras definidas em `perfil/categoria_rules.py`)
- Alerta imediato ao ultrapassar o orçamento de uma categoria

### ⚙️ Gerenciar
- Cadastro de contas bancárias (Nubank, Itaú, Bradesco, etc.) com ícone personalizado
- Cadastro e gerenciamento de categorias (essencial / não essencial)
- Saldo total consolidado das contas

### 📋 Contas a Pagar
- Cadastro de contas mensais recorrentes
- Agrupamento automático: **vencidas**, **próximas do vencimento** (5 dias) e **restantes**
- Management command (`processar_recorrencias`) para processar débitos recorrentes automaticamente

### 🎯 Planejamento & Metas
- Definição de valor de planejamento mensal por categoria
- Visualização de progresso com barra de status (verde / amarelo / vermelho)
- Metas financeiras: economizar por mês ou limitar gasto por categoria

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Python 3.11 ou superior
- `pip` e `venv`

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/FINCANCE_PSW.git
cd FINCANCE_PSW
```

### 2. Criar e ativar o ambiente virtual
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Aplicar as migrações
```bash
python manage.py migrate
```

### 5. Criar superusuário (opcional, para o admin)
```bash
python manage.py createsuperuser
```

### 6. Rodar o servidor de desenvolvimento
```bash
python manage.py runserver
```

Acesse: [http://localhost:8000](http://localhost:8000)

> A rota raiz redireciona automaticamente para `/perfil/home/`.

---

## 📁 Estrutura de URLs

| URL | App | Descrição |
|---|---|---|
| `/perfil/home/` | perfil | Dashboard principal |
| `/perfil/gerenciar/` | perfil | Gerenciar contas e categorias |
| `/perfil/dashboard/` | perfil | Analytics com gráficos |
| `/extrato/novo_valor/` | extrato | Registrar transação |
| `/extrato/view_extrato/` | extrato | Visualizar extrato |
| `/extrato/exportar_pdf/` | extrato | Exportar extrato em PDF |
| `/contas/definir_contas/` | contas | Cadastrar conta mensal |
| `/contas/ver_contas/` | contas | Ver contas a pagar |
| `/planejamento/definir_planejamento/` | planejamento | Definir orçamento |
| `/planejamento/ver_planejamento/` | planejamento | Ver progresso |
| `/planejamento/metas/` | planejamento | Metas financeiras |
| `/perfil/api/sugerir_categoria/` | perfil | API de sugestão de categoria (IA) |
| `/admin/` | Django Admin | Administração |

---

## 🤖 API de Sugestão de Categoria

O endpoint `/perfil/api/sugerir_categoria/?descricao=<texto>` analisa o texto da descrição e retorna uma sugestão de categoria baseada em mapeamento de palavras-chave.

**Exemplo de resposta:**
```json
{
  "encontrado": true,
  "categoria_id": 3,
  "categoria_nome": "Alimentação",
  "confianca": 95,
  "motivo": "Detectado \"mercado\" na descrição"
}
```

As regras estão definidas em `perfil/categoria_rules.py` e cobrem categorias como Transporte, Alimentação, Moradia, Saúde, Lazer, Educação e Salário.

---

## 🛠️ Management Commands

### Processar recorrências
Cria automaticamente lançamentos no extrato para contas marcadas como recorrentes que ainda não foram pagas no mês atual:

```bash
python manage.py processar_recorrencias
```

---

## 📊 Modelos de Dados

```
Categoria          — categoria, essencial, valor_planejamento
Conta              — apelido, banco, tipo, valor, icone
Valores            — valor, categoria, descricao, data, conta, tipo (E/S)
ContaPagar         — titulo, categoria, descricao, valor, dia_pagamento, recorrente
ContaPaga          — conta, data_pagamento
MetaFinanceira     — titulo, tipo, valor, categoria (opcional)
```

---

## 🗂️ Variáveis de Configuração

Configure em `core/settings.py`:

| Variável | Padrão | Descrição |
|---|---|---|
| `SECRET_KEY` | insecure-key | Chave secreta do Django |
| `DEBUG` | `True` | Modo debug |
| `ALLOWED_HOSTS` | `[]` | Hosts permitidos em produção |
| `DATABASES` | SQLite | Banco de dados |
| `MEDIA_ROOT` | `./media` | Diretório de uploads |
| `STATICFILES_DIRS` | `./templates/static` | Diretório de arquivos estáticos |

> ⚠️ Para produção, altere `SECRET_KEY`, configure `ALLOWED_HOSTS`, defina `DEBUG=False` e use um banco de dados robusto (PostgreSQL recomendado).

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e pessoais.
