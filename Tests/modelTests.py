from Model import player as p


#Player Model Test
def playerModelTest():
    testPlayer = p.player()
    print('Games Won: ' + str(testPlayer.gamesWon))
    print('Games Played: ' + str(testPlayer.gamesPlayed))
    testPlayer.gamesWon = 1
    testPlayer.gamesPlayed = 2
    print('Games Won: ' + str(testPlayer.gamesWon))
    print('Games Played: ' + str(testPlayer.gamesPlayed))

#Custom Player Model Test
def customPlayerModelTest():
    testPlayer = p.customPlayer('Abraham')
    print('Player Name: ' + testPlayer.name)
    print('Games Won: ' + str(testPlayer.gamesWon))
    print('Games Played: ' + str(testPlayer.gamesPlayed))
    testPlayer.gamesWon = 1
    testPlayer.gamesPlayed = 2
    print('Games Won: ' + str(testPlayer.gamesWon))
    print('Games Played: ' + str(testPlayer.gamesPlayed))