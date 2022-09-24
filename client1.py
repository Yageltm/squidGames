import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
c.connect(('127.0.0.1', port))
game_is_on = True
while game_is_on:
    guess = input("Enter your guess: ")
    c.send(guess.encode())
    answer = c.recv(1024).decode()
    print(answer)
    if answer == 'You won!' or answer == 'You lost..':
        c.close()
        game_is_on = False