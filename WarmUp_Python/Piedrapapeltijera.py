def eleccion(player1, player2):
    if player1 == player2: 
        print('Es un empate, juguemos de nuevo')
        return 0
    
    elif player1 == 1 and player2 == 3 or player1 == 2 and player2 == 1 or player1 == 3 and player2 == 2: 
        print('El ganador es el Jugador 1')
        return 1
    
    elif player2 == 1 and player1 == 3 or player2 == 2 and player1 == 1 or player2 == 3 and player1 == 2: 
        print('El ganador es el Jugador 2')
        return 2

def run():
    intentos = 1
    scoreplayer1 = 0
    scoreplayer2 = 0
         
    while intentos <=3:
        print(f'************* PARTIDA N {intentos} ***************')
        print('Juguemos al Piedra - Papel - Tijera')
        print(f'Player1: {scoreplayer1} puntos / Player2: {scoreplayer2} puntos')
        print('\n')
        
        player1 = int(input('Jugador 1 >> Ingresa 1. Para Piedra, 2. Para papel o 3. para tijera: '))
        player2 = int(input('Jugador 2 >> Ingresa 1. Para Piedra, 2. Para papel o 3. para tijera: '))
        
        scoregeneral = eleccion(player1, player2)
        
        if scoregeneral == 1: 
            scoreplayer1 +=1
            intentos +=1
        elif scoregeneral == 2:
            scoreplayer2 +=1
            intentos +=1
        else:
            intentos +=1
    
    print(f'el marcador quedó player1: {scoreplayer1} / player2: {scoreplayer2}')

if __name__ == "__main__":
    run()



