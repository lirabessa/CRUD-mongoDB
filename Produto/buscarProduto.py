def procurarProduto(meuBanquinho):
    minhaColuna = meuBanquinho.produtos
    minhaBusca = {'nomeProduto': 'gin'}
    x = minhaColuna.find(minhaBusca)

    for a in x:
        print(a)

def procurarTodesProduto (meuBanquinho):
    minhaColuna = meuBanquinho.produtos

    for x in minhaColuna.find():
        print(x)