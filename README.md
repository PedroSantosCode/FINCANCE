<div align="center">

  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/WeasyPrint-68.1-FF6B6B?style=for-the-badge" alt="WeasyPrint">
  <img src="https://img.shields.io/badge/Chart.js-CDN-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white" alt="Chart.js">
  <img src="https://img.shields.io/badge/Tailwind_CSS-CDN-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind">

  <br/><br/>

  <h1>FINANCE.BANK</h1>
  <p><strong>Gestão Financeira Pessoal com Estética Institucional Dark-Mode</strong></p>

  <img src="imgsource/BankSlip.png" alt="Finance Dashboard Banner" width="100%" style="border-radius:12px; margin: 20px 0;"/>

</div>

---

## Sobre o Projeto

**FINANCE.BANK** é uma aplicação web de gestão financeira pessoal construída com o ecossistema Python e Django. O objetivo do sistema é permitir o controle de finanças utilizando uma interface moderna com estética corporativa institucional e design em _glassmorphism_. Serve para registro de contas, fluxos de caixa e geração de relatórios tabulares em PDF gerados on-the-fly, acompanhados de dashboard gerencial.

---

## Telas do Sistema

### 1. Dashboard Principal
<img src="imgsource/Dashboard.png" width="100%" alt="Visão Geral do Dashboard" style="border-radius:8px; margin-bottom: 20px;">

### 2. Extrato e Movimentações
<img src="imgsource/Extract.png" width="100%" alt="Visualização do Extrato" style="border-radius:8px; margin-bottom: 20px;">

### 3. Orçamento e Planejamento
<img src="imgsource/Planning.png" width="100%" alt="Visualização do Planejamento" style="border-radius:8px; margin-bottom: 20px;">

### 4. Blog & News
<img src="imgsource/BlogNews.png" width="100%" alt="Visualização do Planejamento" style="border-radius:8px; margin-bottom: 20px;">

---

## Stack Tecnológica

| Componente | Ferramenta / Linguagem | Descrição |
|-----------|------------------------|-----------|
| **Backend Core** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white) | Lógica de servidor, roteamento e gerenciamento ORM interno. |
| **Banco de Dados** | ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white) | Banco relacional rápido para arquivos persistentes em disco. |
| **Geração de PDF** | ![WeasyPrint](https://img.shields.io/badge/WeasyPrint-FF6B6B?style=flat) | Engine binário de interpretação de estilos para documentos portáteis PDF de alta fidelidade. |
| **Interface de Usuário** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) ![VanillaJS](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) | Código padrão de interação visual, DOM manipulado diretamente no navegador. |
| **Gráficos** | ![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat&logo=chartdotjs&logoColor=white) | Analytics implementados via _canvas_, gerando áreas poligonais e gauges de saúde orçamentária. |
| **Estilo e Layout** | ![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat&logo=tailwindcss&logoColor=white) | Configuração de variáveis unitárias importadas e mapeadas em CDN externo para UI. |

---

## Funcionalidades e Módulos Estruturais

| Módulo de Lógica | Descrição da Funcionalidade Injetada |
|------------------|---------------------------------------|
| ![Perfil e Dashboard](https://img.shields.io/badge/Módulo-Dashboard-5865F2?style=flat) | Consolidador universal de saldos e medidor de equilíbrio econômico global do usuário. |
| ![Módulo Extrato](https://img.shields.io/badge/Módulo-Extrato_PDF-E34F26?style=flat) | Camada em lista interativa para pagamentos retroativos. Renderiza saídas HTML customizadas para matriz de WeasyPrint. |
| ![Bot de Categoria](https://img.shields.io/badge/Recurso-Classificador_Contextual-10B981?style=flat) | IA básica baseada em array contextual: Escaneia strings na origem e preenche o form dinamicamente no _frontend_ antes de salvar (API REST Local). |
| ![Agendamento Mensal](https://img.shields.io/badge/Módulo-Contas_Recorrentes-F59E0B?style=flat) | Listagem inteligente programática; segrega as cobranças em vetores de: _Vencidas_, _Prioritárias (5d)_ e _Status Ok_. |
| ![Indicador de Metas](https://img.shields.io/badge/Módulo-Planejamento_Budge-6366F1?style=flat) | Monitoramento teto-limite de carteira injetada _per_ tag baseada em calculo volumétrico predefinido ou flexível. |

---

## Rotas de Acesso Mapeadas (Tabela de URLs)

| Endpoints de Rota Mapeada | Aplicação Responsável | Fluxo do Usuário / Contexto de Acionamento |
|--------------|-----------|------------------------|
| `/perfil/home/` | app: Perfil | Apresentação universal consolidada e alertas de risco |
| `/perfil/dashboard/` | app: Perfil | Analytics estendido carregando a matriz de Chart.js |
| `/perfil/gerenciar/` | app: Perfil | Gerenciar cadastros de cartões lógicos da plataforma |
| `/extrato/novo_valor/` | app: Extrato | Formulário de transação monetária principal e entrada |
| `/extrato/view_extrato/` | app: Extrato | Grid detalhado de logs da movimentação passiva e ativa |
| `/extrato/exportar_pdf/` | app: Extrato | Engine de compressão binária, retorna cabeçalho de tipo _application/pdf_ |
| `/contas/ver_contas/` | app: Contas | Viewer do escopo passional listado de faturamento a pagar agendado |
| `/planejamento/ver_planejamento/` | app: Planejamento | Barra analítica colorada (Safe Zone e Alert Zone) ativamente traqueada |
| `/perfil/api/sugerir_categoria/` | app: Perfil | Receptor micro-serviço (API Local) do escopo JS para parsear categorizações automáticas |

---

## Deploy e Setup em Ambiente Local

**1. Clone o repositório raiz na sua rede ou terminal:**
```bash
$ git clone https://github.com/PedroSantosCode/FINCANCE.git
$ cd FINCANCE
```

**2. Provisionamento seguro de sub-rede Python:**
```bash
# Ambiente Microsoft Windows (Cmd/Powershell)
$ python -m venv .venv
$ .venv\Scripts\activate

# Ambiente Linux / Darwin (MacOS) Baseados em Bash ou Zsh
$ python3 -m venv .venv
$ source .venv/bin/activate
```

**3. Instalação e Montagem do Build Dependencies:**
```bash
$ pip install -r requirements.txt
```

**4. Rotina Inicial de Migrações do ORM (Estruturação Relacional Sqlite3):**
```bash
$ python manage.py migrate
```

**5. Setup da Secret e Run Server TCP (Virtualização no Navegador):**
*OBS: Verifique configurações de variáveis `.env` na montagem local se baseadas no escopo do repositório em modo debug global.*
```bash
$ python manage.py runserver
```

Acompanhe através da URL interna disparada na _network_ isolada:
`http://localhost:8000`

---

### Módulos Estendidos

Para sincronizar o script assíncrono programado a debitar laços da fatura recorrente do respectivo ciclo e período:

```bash
$ python manage.py processar_recorrencias
```

---
<div align="center">
  Desenvolvido sob Arquitetura e Engenharia de Software no Ecossistema da Linguagem Python &bull; 2026
</div>

