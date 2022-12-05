addnomecompleto = input(str('Adicione o nome completo: '))
ddd = int(input('Digite o DDD: ' ))
telefone = int(input('Digite o telefone: ' ))
addemail = input(str('Adicione o email: '))

def numConcat(ddd, telefone):
    ddd = str(ddd)
    telefone = str(telefone)

    ddd += telefone
    return int(ddd)

addtelefone = (numConcat(ddd, telefone))



