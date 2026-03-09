from django.core.management.base import BaseCommand
from blog.models import BlogPost


class Command(BaseCommand):
    help = 'Seed the database with sample blog posts'

    def handle(self, *args, **options):
        if BlogPost.objects.exists():
            self.stdout.write(self.style.WARNING('Blog posts already exist. Skipping seed.'))
            return

        posts = [
            {
                'title': '5 Passos para Organizar suas Finanças Pessoais em 2026',
                'summary': 'Descubra as melhores estratégias para colocar sua vida financeira em ordem e começar o ano com o pé direito.',
                'content': (
                    'Organizar as finanças pessoais é o primeiro passo para conquistar a liberdade financeira. '
                    'Neste artigo, apresentamos cinco passos práticos que você pode começar a aplicar hoje mesmo.\n\n'
                    '1. **Faça um diagnóstico financeiro** — Antes de qualquer coisa, é preciso saber para onde seu dinheiro está indo. '
                    'Use o Finance.Bank para categorizar todas as suas despesas do último mês.\n\n'
                    '2. **Defina metas claras** — Estabeleça objetivos de curto, médio e longo prazo. '
                    'O módulo de Metas do Finance.Bank permite acompanhar o progresso em tempo real.\n\n'
                    '3. **Crie um orçamento mensal** — Distribua sua renda entre categorias essenciais e não essenciais. '
                    'A regra 50-30-20 é um ótimo ponto de partida.\n\n'
                    '4. **Automatize suas economias** — Configure transferências automáticas para sua conta de investimentos '
                    'logo após receber o salário.\n\n'
                    '5. **Revise mensalmente** — Use o Dashboard de Analytics para identificar padrões e ajustar seu planejamento.'
                ),
                'category': 'planejamento',
            },
            {
                'title': 'Como a Inteligência Artificial está Transformando o Mercado Financeiro',
                'summary': 'Entenda como algoritmos e IA estão mudando a forma como investimos e gerenciamos dinheiro.',
                'content': (
                    'A inteligência artificial já não é ficção científica — ela está presente no dia a dia do mercado financeiro. '
                    'De robôs advisors a análise preditiva, a tecnologia tem democratizado o acesso a estratégias que antes eram '
                    'exclusivas de grandes investidores.\n\n'
                    'Os principais bancos e fintechs brasileiras já utilizam IA para:\n\n'
                    '• **Análise de crédito** — Modelos de machine learning avaliam milhares de variáveis para aprovar empréstimos.\n\n'
                    '• **Detecção de fraudes** — Algoritmos identificam transações suspeitas em tempo real.\n\n'
                    '• **Gestão de investimentos** — Robôs advisors montam carteiras personalizadas com base no perfil de risco.\n\n'
                    '• **Atendimento ao cliente** — Chatbots financeiros resolvem dúvidas e executam operações 24/7.\n\n'
                    'O Finance.Bank utiliza categorização inteligente para ajudar você a entender melhor seus padrões de gastos '
                    'e oferecer sugestões personalizadas.'
                ),
                'category': 'mercado',
            },
            {
                'title': 'Investimentos para Iniciantes: Por Onde Começar?',
                'summary': 'Um guia completo para quem nunca investiu e quer dar os primeiros passos com segurança.',
                'content': (
                    'Investir pode parecer intimidador no início, mas com o conhecimento certo, qualquer pessoa pode fazer '
                    'seu dinheiro trabalhar para ela. Vamos desmistificar o mundo dos investimentos.\n\n'
                    '**Renda Fixa vs Renda Variável**\n\n'
                    'Renda fixa é ideal para iniciantes: CDBs, Tesouro Direto e LCIs oferecem segurança e previsibilidade. '
                    'Já a renda variável (ações, FIIs) oferece maior potencial de retorno, mas com mais risco.\n\n'
                    '**Quanto investir?**\n\n'
                    'Comece com o que puder, mesmo que seja R$ 30 por mês no Tesouro Direto. O importante é criar o hábito. '
                    'Use o planejamento do Finance.Bank para definir quanto separar por mês para investimentos.\n\n'
                    '**Diversificação**\n\n'
                    'Nunca coloque todos os ovos na mesma cesta. Distribua seus investimentos entre diferentes classes de ativos.\n\n'
                    '**Reserva de emergência**\n\n'
                    'Antes de investir em renda variável, monte uma reserva de emergência equivalente a 6 meses de despesas '
                    'em aplicações de alta liquidez.'
                ),
                'category': 'investimentos',
            },
            {
                'title': '7 Dicas para Economizar no Dia a Dia sem Perder Qualidade de Vida',
                'summary': 'Pequenas mudanças de hábito que podem gerar uma economia significativa ao longo do ano.',
                'content': (
                    'Economizar não significa viver uma vida de privações. Com pequenos ajustes no dia a dia, é possível '
                    'guardar uma quantia significativa sem abrir mão do que é importante.\n\n'
                    '1. **Leve marmita** — Comer fora todos os dias pode custar mais de R$ 1.500 por mês. Preparar refeições '
                    'em casa reduz esse valor pela metade.\n\n'
                    '2. **Revise suas assinaturas** — Quantos serviços de streaming você realmente usa? Cancele os que não assiste.\n\n'
                    '3. **Compare preços antes de comprar** — Use aplicativos de comparação e aguarde promoções para compras maiores.\n\n'
                    '4. **Negocie suas contas fixas** — Ligue para sua operadora de telefone e internet e peça desconto. Funciona!\n\n'
                    '5. **Use transporte público ou caronas** — O custo do carro vai muito além do combustível.\n\n'
                    '6. **Faça lista de compras** — Ir ao mercado sem lista é receita para gastar mais do que precisa.\n\n'
                    '7. **Defina um "dia sem gastar"** — Uma vez por semana, não gaste nada. Leve café de casa, caminhe ao invés '
                    'de usar app de transporte.\n\n'
                    'Use o Finance.Bank para acompanhar o impacto dessas mudanças no seu orçamento mensal!'
                ),
                'category': 'dicas',
            },
            {
                'title': 'Cenário Econômico Brasileiro: O que Esperar para o Segundo Semestre',
                'summary': 'Análise das perspectivas econômicas e como elas impactam suas finanças pessoais.',
                'content': (
                    'O primeiro semestre de 2026 foi marcado por movimentos importantes na economia brasileira. '
                    'A taxa Selic, inflação e mercado de trabalho seguem como fatores-chave para planejamento financeiro.\n\n'
                    '**Selic e Renda Fixa**\n\n'
                    'Com as expectativas de manutenção da taxa Selic, investimentos em renda fixa continuam atrativos. '
                    'CDBs de bancos digitais e Tesouro Selic são boas opções para a reserva de emergência.\n\n'
                    '**Inflação**\n\n'
                    'A inflação controlada traz alívio ao consumidor, mas é fundamental manter o poder de compra. '
                    'Investimentos que rendem acima da inflação são essenciais.\n\n'
                    '**Mercado de Trabalho**\n\n'
                    'O mercado de tecnologia continua aquecido, e a tendência de trabalho remoto impacta os padrões de gastos. '
                    'Profissionais devem aproveitar para investir na qualificação.\n\n'
                    '**O que fazer?**\n\n'
                    'Mantenha sua reserva de emergência em dia, diversifique investimentos e use ferramentas como '
                    'o Finance.Bank para acompanhar seu progresso financeiro em tempo real.'
                ),
                'category': 'economia',
            },
            {
                'title': 'Finance.Bank Lança Novas Funcionalidades de Planejamento',
                'summary': 'Conheça as novidades da plataforma: metas financeiras, analytics avançado e muito mais.',
                'content': (
                    'Temos o prazer de anunciar novas funcionalidades que vão transformar a maneira como você '
                    'gerencia suas finanças no Finance.Bank!\n\n'
                    '**Metas Financeiras**\n\n'
                    'Agora você pode criar metas personalizadas de economia mensal e limites de gasto por categoria. '
                    'Acompanhe o progresso com barras visuais e receba alertas automáticos.\n\n'
                    '**Dashboard de Analytics**\n\n'
                    'O novo painel de analytics oferece gráficos interativos de evolução mensal, gastos por categoria '
                    'e saldo acumulado. Filtre por período e tenha insights poderosos.\n\n'
                    '**Calculadora Financeira**\n\n'
                    'Uma calculadora integrada para simulações rápidas de investimentos, empréstimos e financiamentos.\n\n'
                    '**Contas a Pagar**\n\n'
                    'Gerencie suas contas a pagar com datas de vencimento, categorização e geração automática de boletos.\n\n'
                    'Todas as funcionalidades estão disponíveis gratuitamente. Acesse o Finance.Bank e experimente agora!'
                ),
                'category': 'noticias',
            },
        ]

        for post_data in posts:
            BlogPost.objects.create(**post_data)
            self.stdout.write(self.style.SUCCESS(f'  Created: {post_data["title"][:50]}...'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully seeded {len(posts)} blog posts!'))
