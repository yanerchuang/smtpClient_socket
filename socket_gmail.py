from socket import *
import ssl
import base64

# Email message.
subject = "Subject: Gmail SMTP Test\r\n"
# Subject and message cách nhau bởi \r\n\r\n
msg = "\r\n Test gửi mail bằng SMTP."
endmsg = '\r\n.\r\n'
rcpt_to = input("Nhập địa chỉ người nhận: ")


mail_server = 'smtp.gmail.com' # Dung mail server la gmail
client_socket = socket(AF_INET, SOCK_STREAM) 
# Tao 1 doi tuong socket,  
#tham số AF_INET cho biết chúng ta sử dụng IP v4, SOCK_TREAM là dùng giao thức TCP.

# Client socket.
# Establish TCP connection with mail server
client_socket = ssl.wrap_socket(client_socket)
client_socket.connect((mail_server, 465))
recv = client_socket.recv(1024)
print("Mã trả về từ connect: ", end=" ")
print (recv)
if recv[:3] != b'220':
	print ('220 reply not received from server.')

# Send HELO command and print server response.
hello_command = 'EHLO localhost\r\n'
# Server chi nhan bytes object -> encode()
client_socket.send(hello_command.encode())
recv1 = client_socket.recv(1024)
print("Mã trả về từ EHLO: ", end=" ")
print (recv1)
if recv1[:3] != b'250':
	print ('250 reply not received from server.')

# Authenticate.
# The hashcode is Username and password of your email. Hash it by b64encode
usernameCommand = 'AUTH LOGIN cXV5LmRjOThAZ21haWwuY29t\r\n'
client_socket.send(usernameCommand.encode())
recv1 = client_socket.recv(1024)
print("Mã trả về từ AUTH LOGIN: ", end=" ")
print (recv1)
passCommand = 'UXV5X0NWUDk4\r\n'
client_socket.send(passCommand.encode())
recv1 = client_socket.recv(1024)
print("Mã trả về sau khi đã nhập email và password: ", end=" ")
print (recv1)
# Return: b'334 UGFzc3dvcmQ6\r\n'
# A 334 reply code is sent in response to the AUTH command when the requested security mechanism is accepted

# Send MAIL FROM command and print server response.
mailAdd = 'MAIL FROM: <quy.dc98@gmail.com>\r\n'
client_socket.send(mailAdd.encode())
recv1 = client_socket.recv(1024)
print("Mã trả về từ MAIL FROM: ", end=" ")
print (recv1)
if recv1[:3] != b'250': #if the data is not received
	print ('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptAdd = 'RCPT TO: <{0}> \r\n'.format(rcpt_to)
client_socket.send(rcptAdd.encode())
recv1 = client_socket.recv(1024)
print("Mã trả về từ RCPT TO: ", end=" ")
print (recv1)
if recv1[:3] != b'250':
	print ('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
client_socket.send(dataCommand.encode())
recv1 = client_socket.recv(1024)
print("Mã trả về từ DATA: ", end=" ")
print (recv1)
if recv1[:3] != b'354':
	print ('250 reply not received from server.')


client_socket.send(subject.encode())
# Send message data.
client_socket.send(msg.encode())

# Message ends with a single period.
client_socket.send(endmsg.encode())
recv1 = client_socket.recv(1024)
print("Mã trả về từ send message: ", end=" ")
print (recv1)
if recv1[:3] != b'250':
	print ('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
client_socket.send(quitCommand.encode())
recv1 = client_socket.recv(1024)
print("Mã trả về từ QUIT: ", end=" ")
print(recv1)
if recv1[:3] != b'221':
	print('221 reply not received from server.')
client_socket.close()
