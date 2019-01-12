#! /usr/bin/python3
'''
    Client - calls server, opens file, sends server data line by line.
'''


import socket
import collections



def connect(host, port):
    bar = collections.deque([])

    with open('processes.txt', 'rt') as infile:
        lines = infile.read().split('\n')
        for x in range(len(lines)):
            bar.append(lines[x])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        print('Connected to %s:%s' % (host, port))

        while len(bar) > 0:

            tempSend = bar.popleft()
            print('\tSending:\t%s' % tempSend)
            sock.send(tempSend.encode('utf-8'))

            data = sock.recv(1024)
            tempRec = data.decode()
            tempD = tempRec.rsplit(',',6)
            temp1 = tempD[0]
            temp2 = tempD[1]
            temp6 = int(tempD[6])
            if temp6 > 0:
                print('\tReceived:\t%s' % tempRec)
                bar.append(tempRec)
            else:
                print('\t\tProcess %s, %s Completed.' % (temp2,temp1))

    print('Finished, connection closed.')


if __name__ == '__main__':

    host = '127.0.0.1'
    port = 9000

    connect(host, port)

