def organizar(valor, conta):
    str_valor = str(valor)
    Numero_novo = ""
    if conta == 'A':
        if len(str_valor) >= 6:
            return False
        for N in range(len(str_valor)):
            if N == 3:
                Numero_novo += str_valor[N]+'.'
                continue
            Numero_novo += str_valor[N]
    if conta == 'C':
        if len(str_valor) < 7 or len(str_valor) > 7:
            return False
        for N in range(len(str_valor)):
            if N == 2:
                Numero_novo += str_valor[N]+'.'
                continue
            if N == 5:
                Numero_novo += str_valor[N]+'-'
                continue
            Numero_novo += str_valor[N]

    return Numero_novo