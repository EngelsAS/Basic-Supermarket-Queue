from fila import Fila
 
#Itens existentes que podem ser adicionados aos carrinhos de compras dos clientes
frango = 21
arroz = 4
feijao = 11
acucar = 4
 
fila = Fila() #Aqui é onde a fila é inicializada
print("Quantos clientes tem na fila?")
quantclientes = int(input())
atual = 1 #Variavel que mostra para o usuario o atual cliente que ele está atendendo
total = 0
 
#Laço for para inserir clientes na fila
#Nesse caso, para simplificação, cada cliente equivale a um número na fila
 
for i in range(quantclientes):
    fila.insere(i)
 
print("Inicio do atendimento aos clientes\nInsira os itens existenstes no carrinho de compras do 1º cliente")
 
#Laço while para atender todos os clientes existentes na fila
 
while(quantclientes != 0):
    print("1 - Frango\n2 - Arroz\n3 - Feijao\n4 - Açucar ")
    x = int(input())
    if(x == 1):
        print("Quantas unidades de frango existem no carrinho?")
        quantidade = int(input())
        total = total + frango*quantidade
    elif(x == 2):
        print("Quantas unidades de arroz existem no carrinho?")
        quantidade = int(input())
        total = total + arroz*quantidade
    elif(x == 3):
        print("Quantas unidades de feijao existem no carrinho?")
        quantidade = int(input())
        total = total + feijao*quantidade
    else:
        print("Quantas unidades de açucar existem no carrinho?")
        quantidade = int(input())
        total = total + acucar*quantidade
   
    print("Existem mais itens no carrinho do cliente?(sim/nao)") #Condição para saber se finaliza o carrinho de compras do cliente
                                                                 #atual e passa para o proximo cliente
    resp = input()
 
    if(resp == "nao"):
        print("O valor total da compra desse cliente deu "+str(total)+"R$\nOs itens no carrinho desse cliente acabaram") #Printa o valor total depois da conta finalizada
        fila.remove() #Remove o cliente da fila
        if(quantclientes > 1):
            print("Insira os itens existentes no carrinho do "+str((atual +                     1))+"º cliente")
        atual += 1 #Soma 1 a mais na variavel atual para representar o proximo cliente
        quantclientes -= 1
        total = 0 #Iguala novamente o total a 0 para começar com um novo cliente
 
print("Não tem mais nenhum cliente na fila")
