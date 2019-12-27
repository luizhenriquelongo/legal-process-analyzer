def analyze_case(soup):
    label_processo = soup.find("label", text="Processo:")
    label_classe = soup.find("label", text="Classe:")
    label_valor_da_causa = soup.find("label", text="Valor da ação:")
    label_juiz = soup.find("label", text="Juiz:")
    partes_do_processo = soup.find(id="tablePartesPrincipais")
    ultima_movimentacao = soup.find(id="tabelaUltimasMovimentacoes")

    numero_do_processo = label_processo.find_next('span').get_text().strip()
    classe = label_classe.find_next('span').get_text().strip()
    valor_da_causa = label_valor_da_causa.find_next('span').get_text().strip()
    juiz = label_juiz.find_next('span').get_text().strip()
    partes_do_processo = partes_do_processo.find_all('tr')
    ultima_movimentacao = ultima_movimentacao.find_next('span').get_text().strip()

    partes = []
    for parte in partes_do_processo:
        parte = ' '.join(parte.get_text().split())
        partes.append(parte)

    response = {
        "numeroDoProcesso": numero_do_processo,
        "valorDaCausa": valor_da_causa,
        "classe": classe,
        "juiz": juiz,
        "partesDoProcesso": partes,
        "ultimaMovimentacao": ultima_movimentacao,
    }

    return response