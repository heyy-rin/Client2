
import socket
import cv2
import numpy

#socket 수신 버퍼를 읽어서 반환하는 함수
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

#수신에 사용될 내 ip와 내 port번호
TCP_IP = ''
TCP_PORT = 5002
connect_list = []

if __name__ == '__main__':
    #TCP소켓 열고 수신 대기
    client2 = socket.socket()
    client2.bind((TCP_IP, TCP_PORT))

    print(TCP_IP)
    client2.listen(1)

    while True :

        print("waiting !")
        server, addr = client2.accept()  # socket과 client주소
        connect_list.append(server)
        print("connected 1 : "+str(connect_list ))

        if connect_list :

            print(" server -> success connection ! ")

            length = recvall(server, 16)
            # 길이 16의 데이터를 먼저 수신하는 것은 여기에 이미지의 길이를
            # 먼저 받아서 이미지를 받을 때 편리하려고 하는 것이다.
            stringData = recvall(server, int(length))
            print("string length", length.decode())  # 받은 이미지 크기를 출력
            data = numpy.fromstring(stringData, dtype='uint8')

            connect_list.remove(server)
            print("connected 2: " + str(connect_list))

            server.close()
            decimg = cv2.imdecode(data, 1)
            cv2.imshow('CLIENT2@recv', decimg)
            cv2.waitKey(1)  # 0 으로 무한대기 상태면 멈출 수 있음

