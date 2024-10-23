def rpsWinner(player1, player2):
  p1w = 'player one'
  p2w = 'player two'
  tie = 'tie'
  match (player1, player2):
    case ('rock','paper'): return p2w
    case ('rock','scissors'): return p1w
    case ('rock','rock'): return tie
    case('paper','rock'): return p1w
    case('paper','scissors'): return p2w
    case('paper', 'paper'): return tie
    case('scissors', 'rock'): return p2w
    case('scissors', 'paper'): return p1w
    case('scissors', 'scissors'): return tie
    
assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'