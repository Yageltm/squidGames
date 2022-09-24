import socket
from bull_cows import Play
s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
while True:
    c, addr = s.accept()
    num = Play()
    print(f'The digits are {num.number}, but don\'t tell the client')
    rounds = 0
    global result
    while rounds < 10:
        guess = c.recv(1024).decode()
        result = str(num.compare(guess))
        if result == "['B', 'B', 'B', 'B']":
            result = 'You won!'
            c.send(result.encode())
            s.close()
            break
        if rounds != 9:
            c.send(result.encode())
        rounds += 1
    if result != 'You won!':
        c.send('You lost..'.encode())
        s.close()

