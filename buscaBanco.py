import redis
import pymongo


cliente =  pymongo.MongoClient('mongodb+srv://Lirabessa11:abcd0102@meubanquinho.qppkdbq.mongodb.net/?retryWrites=true&w=majority')
clienteRedis = redis.Redis(host='redis-12898.c60.us-west-1-2.ec2.cloud.redislabs.com',
                    port=12898,
                    password = 'abcd0102')

meuBanquinho = cliente.MercadoLivre
minhaColuna = meuBanquinho.Usuario
minhaBusca = {'nome': 'NATY REDIS'}
x = minhaColuna.find_one(minhaBusca)

clienteRedis.set('user:name', x['nome'])

print(clienteRedis.get('user:name'))
print('Sua informação no MONGO', x)