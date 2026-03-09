from .models import Categoria

# Mapeamento de palavras-chave para categorias
# Formato: {'palavra_chave': 'nome_categoria'}
REGRAS_CATEGORIAS = {
    # Transporte
    'uber': 'Transporte',
    '99': 'Transporte',
    'taxi': 'Transporte',
    'cabify': 'Transporte',
    'combustivel': 'Transporte',
    'combustível': 'Transporte',
    'gasolina': 'Transporte',
    'estacionamento': 'Transporte',
    'pedagio': 'Transporte',
    'pedágio': 'Transporte',
    'onibus': 'Transporte',
    'ônibus': 'Transporte',
    'metro': 'Transporte',
    'metrô': 'Transporte',

    # Alimentação
    'mercado': 'Alimentação',
    'supermercado': 'Alimentação',
    'ifood': 'Alimentação',
    'restaurante': 'Alimentação',
    'lanchonete': 'Alimentação',
    'padaria': 'Alimentação',
    'açougue': 'Alimentação',
    'hortifruti': 'Alimentação',
    'pizza': 'Alimentação',
    'burger': 'Alimentação',
    'hamburguer': 'Alimentação',
    'café': 'Alimentação',
    'cafe': 'Alimentação',
    'almoço': 'Alimentação',
    'almoco': 'Alimentação',
    'jantar': 'Alimentação',
    'rappi': 'Alimentação',

    # Moradia
    'aluguel': 'Moradia',
    'condominio': 'Moradia',
    'condomínio': 'Moradia',
    'iptu': 'Moradia',
    'luz': 'Moradia',
    'energia': 'Moradia',
    'agua': 'Moradia',
    'água': 'Moradia',
    'gas': 'Moradia',
    'gás': 'Moradia',
    'internet': 'Moradia',
    'telefone': 'Moradia',
    'celular': 'Moradia',

    # Saúde
    'farmacia': 'Saúde',
    'farmácia': 'Saúde',
    'medico': 'Saúde',
    'médico': 'Saúde',
    'hospital': 'Saúde',
    'consulta': 'Saúde',
    'exame': 'Saúde',
    'remedio': 'Saúde',
    'remédio': 'Saúde',
    'dentista': 'Saúde',
    'plano de saude': 'Saúde',
    'plano de saúde': 'Saúde',

    # Lazer
    'cinema': 'Lazer',
    'netflix': 'Lazer',
    'spotify': 'Lazer',
    'teatro': 'Lazer',
    'show': 'Lazer',
    'festa': 'Lazer',
    'bar': 'Lazer',
    'viagem': 'Lazer',
    'hotel': 'Lazer',
    'passeio': 'Lazer',
    'parque': 'Lazer',
    'game': 'Lazer',
    'jogo': 'Lazer',
    'streaming': 'Lazer',

    # Educação
    'escola': 'Educação',
    'faculdade': 'Educação',
    'curso': 'Educação',
    'livro': 'Educação',
    'mensalidade': 'Educação',
    'material escolar': 'Educação',
    'udemy': 'Educação',
    'alura': 'Educação',

    # Salário
    'salario': 'Salário',
    'salário': 'Salário',
    'pagamento': 'Salário',
    'freelance': 'Salário',
    'freela': 'Salário',
    'pix recebido': 'Salário',
}


def sugerir_categoria(descricao):
    """
    Analisa a descrição e sugere uma categoria com base nas regras definidas.
    Retorna um dicionário com id e nome da categoria sugerida, ou None.
    """
    if not descricao:
        return None

    descricao_lower = descricao.lower().strip()

    # Verificar correspondências (prioridade para frases mais longas)
    regras_ordenadas = sorted(REGRAS_CATEGORIAS.items(), key=lambda x: len(x[0]), reverse=True)

    for palavra, nome_categoria in regras_ordenadas:
        if palavra in descricao_lower:
            try:
                categoria = Categoria.objects.filter(categoria__icontains=nome_categoria).first()
                if categoria:
                    return {
                        'id': categoria.id,
                        'nome': categoria.categoria,
                        'confianca': 95,
                        'motivo': f'Detectado "{palavra}" na descrição',
                    }
            except Exception:
                pass

    return None
