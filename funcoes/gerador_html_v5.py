

bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def filtrar_atrs(informados, suportados):
    # ''.join para concatenar /
    # k.split("_")[-1] para acessar somente a ultima parte da chave ->
    # accesskey
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(
        conteudo) else conteudo(*args, **novos_atrs)
    atributos = filtrar_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos}  class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    lista = ''.join((f'<li>{item}</li>' for item in itens))  # generator
    return f'<ul> {filtrar_atrs(novos_atrs, ul_atrs)}{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(classe='letras', conteudo='inline', inline=False))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('item 1', 'item 2'), classe='info'))
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo', classe='info',
                    inline=True))
    print(tag_bloco(tag_lista, 'item 1', 'item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista'))
