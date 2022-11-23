def procurarUsuario (meuBanquinho ) :
    minhaColuna = meuBanquinho.Usuario
    minhaBusca = {'nome': 'Lira'}
    x = minhaColuna.find(minhaBusca)

    for a in x :
        print(a)

def procurarTodesUsuario (meuBanquinho):
    minhaColuna = meuBanquinho.Usuario

    for x in minhaColuna.find ():
        print(x)