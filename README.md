<div align="center">

  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/WeasyPrint-68.1-FF6B6B?style=for-the-badge" alt="WeasyPrint">
  <img src="https://img.shields.io/badge/Chart.js-CDN-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white" alt="Chart.js">
  <img src="https://img.shields.io/badge/Tailwind_CSS-CDN-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind">

  <br/><br/>

  <h1>💳 FINANCE.BANK</h1>
  <p><strong>Gestão Financeira Pessoal com estética institucional dark-mode</strong></p>

  <img src="https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=1200&h=400&fit=crop&q=80" alt="Finance Dashboard Banner" width="100%" style="border-radius:12px; margin: 20px 0;"/>

</div>

---

## 📋 Sobre o Projeto

**FINANCE.BANK** é uma aplicação web completa de **gestão financeira pessoal**, construída com Django. Ela permite ao usuário controlar suas finanças com uma interface premium no estilo *wealth management* — dark mode, glassmorphism e micro-animações.

> 🎯 **Para que serve?** Acompanhar saldo de contas bancárias, registrar entradas e saídas, definir metas e orçamentos por categoria, visualizar analytics com gráficos e exportar extratos em PDF.

---

## ✨ Funcionalidades

| Módulo | Funcionalidades |
|--------|----------------|
| 🏠 **Dashboard** | Saldo total, entradas/saídas do mês, gauge de equilíbrio financeiro, alertas de orçamento |
| 📊 **Analytics** | Gráfico de barras (gastos/categoria), linha (evolução 6 meses), área (patrimônio acumulado) |
| 📄 **Extrato** | Listagem filtrada por conta/categoria, exportação em **PDF** via WeasyPrint |
| ➕ **Novo Valor** | Registro de transações com **sugestão automática de categoria via IA** por palavras-chave |
| ⚙️ **Gerenciar** | Cadastro de contas bancárias (com ícone), categorias (essencial/não essencial) |
| 💰 **Contas a Pagar** | Contas mensais recorrentes agrupadas: vencidas, próximas (5 dias), restantes |
| 🎯 **Planejamento** | Orçamento por categoria com barra de progresso (verde/amarelo/vermelho) + metas financeiras |
| ✍️ **Blog** | Blog integrado para dicas e conteúdo financeiro |

---

## 🛠️ Stack Tecnológica

### 🐍 Backend
| Tecnologia | Versão | Uso |
|---|---|---|
| **Python** | 3.11+ | Linguagem principal |
| **Django** | 6.0 | Framework MVT |
| **WeasyPrint** | 68.1 | Geração de PDFs |
| **Pillow** | 12.1 | Upload/processamento de imagens |
| **python-dateutil** | 2.9 | Cálculo de datas para analytics |
| **SQLite** | built-in | Banco de dados (desenvolvimento) |

### 🎨 Frontend
| Tecnologia | Uso |
|---|---|
| **Tailwind CSS** (CDN) | Estilização utilitária |
| **Chart.js** (CDN) | Gráficos de analytics |
| **Vanilla JavaScript** | Fetch API, sugestão de categoria |
| **HTML5 / SVG** | Estrutura e ícones inline |

---

## 🚀 Como Rodar o Projeto

### ✅ Pré-requisitos

- **Python 3.11+** instalado → [python.org](https://www.python.org/downloads/)
- **pip** (geralmente já incluso com Python)
- Terminal: PowerShell (Windows) ou Bash (Linux/macOS)

---

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/FINANCE.git
cd FINANCE
```

---

### 2️⃣ Criar e Ativar o Ambiente Virtual

```bash
# 🪟 Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# 🐧 Linux / 🍎 macOS
python -m venv .venv
source .venv/bin/activate
```

> ✅ O terminal deve mostrar `(.venv)` no início da linha quando o ambiente estiver ativo.

---

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

> ⚠️ **WeasyPrint no Windows** pode exigir o [GTK Runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer). Veja a [documentação oficial](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows).

---

### 4️⃣ Aplicar as Migrações

```bash
python manage.py migrate
```

---

### 5️⃣ Criar Superusuário *(necessário para acessar o sistema)*

```bash
python manage.py createsuperuser
```

Siga as instruções no terminal (username, email, senha).

---

### 6️⃣ Rodar o Servidor

```bash
python manage.py runserver
```

Acesse: **[http://localhost:8000](http://localhost:8000)**

> 🔁 A rota `/` redireciona automaticamente para `/perfil/home/`.

---

### 🔄 Processar Contas Recorrentes *(opcional)*

Para lançar automaticamente débitos recorrentes no extrato do mês atual:

```bash
python manage.py processar_recorrencias
```

---

## 🗺️ Mapa de URLs

| URL | Descrição |
|-----|-----------|
| `/perfil/home/` | 🏠 Dashboard principal |
| `/perfil/gerenciar/` | ⚙️ Gerenciar contas e categorias |
| `/perfil/dashboard/` | 📊 Analytics com gráficos |
| `/extrato/novo_valor/` | ➕ Registrar transação |
| `/extrato/view_extrato/` | 📄 Visualizar extrato |
| `/extrato/exportar_pdf/` | 📥 Exportar extrato em PDF |
| `/contas/definir_contas/` | 💳 Cadastrar conta mensal |
| `/contas/ver_contas/` | 💰 Ver contas a pagar |
| `/planejamento/definir_planejamento/` | 📝 Definir orçamento por categoria |
| `/planejamento/ver_planejamento/` | 📈 Ver progresso do planejamento |
| `/planejamento/metas/` | 🎯 Metas financeiras |
| `/perfil/api/sugerir_categoria/` | 🤖 API de sugestão de categoria |
| `/admin/` | 🔧 Django Admin |

---

## 🤖 API de Sugestão de Categoria

O endpoint analisa a descrição de uma transação e retorna a categoria sugerida automaticamente.

**Endpoint:** `GET /perfil/api/sugerir_categoria/?descricao=<texto>`

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

> As regras estão em `perfil/categoria_rules.py` e cobrem: **Transporte, Alimentação, Moradia, Saúde, Lazer, Educação e Salário**.

---

## 🏗️ Arquitetura do Projeto

```
FINANCE/
├── core/               # Settings, URLs raiz, WSGI, middleware
├── perfil/             # Dashboard, contas bancárias, analytics, API de categoria
├── extrato/            # Transações (entradas/saídas), exportação PDF
├── contas/             # Contas a pagar mensais e recorrentes
├── planejamento/       # Planejamento por categoria e metas financeiras
├── blog/               # Blog de conteúdo financeiro
├── templates/
│   ├── bases/          # Template base com sidebar e header
│   ├── partials/       # Templates para geração de PDF
│   └── static/         # CSS globais
├── media/              # Uploads (ícones das contas bancárias)
├── svg/                # Ícones SVG inline
├── manage.py
└── requirements.txt
```

---

## 🗃️ Modelos de Dados

```
Categoria         → categoria, essencial (bool), valor_planejamento
Conta             → apelido, banco, tipo, valor, icone
Valores           → valor, categoria, descrição, data, conta, tipo (E/S)
ContaPagar        → título, categoria, valor, dia_pagamento, recorrente (bool)
ContaPaga         → conta, data_pagamento
MetaFinanceira    → título, tipo, valor, categoria (opcional)
```

---

## ⚙️ Variáveis de Configuração

Configure em `core/settings.py`:

| Variável | Padrão | Descrição |
|---|---|---|
| `SECRET_KEY` | insecure-key | 🔴 **Alterar em produção** |
| `DEBUG` | `True` | 🔴 **Definir `False` em produção** |
| `ALLOWED_HOSTS` | `[]` | Hosts permitidos em produção |
| `DATABASES` | SQLite | Banco de dados |
| `MEDIA_ROOT` | `./media` | Diretório de uploads |

> 🔐 **Para produção:** troque `SECRET_KEY`, configure `ALLOWED_HOSTS`, defina `DEBUG=False` e use **PostgreSQL**.

---

## 📸 Screenshots

<div align="center">

| Dashboard | Extrato | Planejamento |
|:---------:|:-------:|:------------:|
| <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=250&fit=crop" width="260"/> | <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400&h=250&fit=crop" width="260"/> | <img src="https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=400&h=250&fit=crop" width="260"/> |

</div>

---

## 📄 Licença

Este projeto foi desenvolvido para fins **educacionais e pessoais**.

---

<div align="center">
  <sub>Feito com ❤️ usando Django · Python · Tailwind CSS · Chart.js</sub>
</div>
