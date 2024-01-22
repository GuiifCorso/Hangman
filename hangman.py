import random #Biblioteca random importada para usar as funções de aleatoriedade
words = ['caminhao', 'macaco', 'travesseiro', 'banana', 'teclado'] #Lista de palavras que serão sorteadas para a forca
empty = [] #Definindo uma lista vazia. Será útil para armazenar novos valores ao decorrer do código
secretWord = random.choice(words) #Buscando uma palavra aleatória (random.choice) da lista de palavras [words]
game_over = False #Como o jogo acabou de começar, game_over é falso
num = 5 #Num será a quantidade de tentativas que o jogador terá para advinhar a palavra
lettersGuessed = [] #Criação de uma lista vazia para inserir as letras que o jogador escolher como palpite
print(f'Você tem {num} chances!') 

for letter in secretWord: #Para cada letra na palavra aleatória escolhida em secretWord, irá repetir o código dentro do loop for
    empty += ('_') #Irá atribuir à lista [empty] uma quantidade de _ proporcional ao número de letras na palavra secreta. Exemplo: macaco -> _ _ _ _ _ _.
print(empty) #Irá imprimir a lista [empty]

while not game_over: #Enquanto não for game_over, irá repetir o código abaixo. (while not (game_over = True), como game_over = False, irá manter em loop)
    guess =  input('Advinhe uma letra: ').lower() #Palpite do jogador
    if guess in lettersGuessed: #Se o palpite já estiver na lista de letras escolhidas irá printar o comando abaixo
        print('Você já escolheu essa letra!')
    else:
        for position in range(len(secretWord)): #Para cada posição (index) no tamanho da string escolhida (secretWord), irá repetir o código abaixo
            letter = secretWord[position] #Atribui à letter a letra da palavra secreta em cada posição
            if letter == guess: #Se a letra em questão da palavra secreta for igual ao palpite
                empty[position] = letter #Irá substituir o '_' do empty pela letra na mesma posição da palavra secreta
                print(empty)
        if guess not in secretWord: #Se a letra em questão da palavra secreta não for igual ao palpite
            num -= 1 #Perde uma chance
            guesses_left = 0 + num #Nova variável de chances restantes
            print(f"Você tem mais {guesses_left} tentativas!")
            print(empty)
            if num == 0: #Se as chances forem 0
                print('Você perdeu!') #Você perde
                print('A palavra era', secretWord) #Mostra-se a palavra
                game_over = True #Atribui True para game_over, encerrando o loop

    
    if "_" not in empty: #Se não houver mais espaços vazios na lista [empty]
        print('Você venceu!') #O jogador ganha
        game_over = True #E o loop se encerra também

    lettersGuessed += guess #Adiciona o palpite à lista de letras escolhidas para evitar repetições
