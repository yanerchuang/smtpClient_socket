from socket import *
import ssl

# Email message.
msg = '\r\n Xin Chao!'
endmsg = '\r\n.\r\n'

mail_server = 'smtp.gmail.com'
client_socket = socket(AF_INET, SOCK_STREAM)

# Client socket.
# Establish TCP connection with mail server
client_socket = ssl.wrap_socket(client_socket)
client_socket.connect((mail_server, 465))
recv = client_socket.recv(1024)
print (recv)
if recv[:3] != '220':
	print ('220 reply not received from server.')

# Send HELO command and print server response.
hello_command = 'EHLO localhost\r\n'
client_socket.send(hello_command.encode())
recv1 = client_socket.recv(1024)
print (recv1)
if recv1[:3] != '250':
	print ('250 reply not received from server.')

# Authenticate.

# The hashcode is Username and password of your email. Hash it by b64encode

authCommand = 'AUTH LOGIN cXV5LmRjOThAZ21haWwuY29t\r\n'
client_socket.send(authCommand.encode())
recv1 = client_socket.recv(1024)
print (recv1)
appCommand = 'MDIxMTE5OTg=\r\n'
client_socket.send(appCommand.encode())
recv1 = client_socket.recv(1024)
print (recv1)

# Send MAIL FROM command and print server response.
mailAdd = 'MAIL FROM: <quy.dc98@gmail.com>\r\n'
client_socket.send(mailAdd.encode())
recv1 = client_socket.recv(1024)
print (recv1)
if recv1[:3] != '250': #if the data is not received
	print ('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptAdd = 'RCPT TO: <skyvp98@gmail.com> \r\n'
client_socket.send(rcptAdd.encode())
recv1 = client_socket.recv(1024)
print (recv1)
if recv1[:3] != '250':
	print ('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
client_socket.send(dataCommand.encode())
recv1 = client_socket.recv(1024)
print (recv1)
if recv1[:3] != '354':
	print ('250 reply not received from server.')

# Send message data.
client_socket.send(msg.encode())

# Message ends with a single period.
client_socket.send(endmsg.encode())
recv1 = client_socket.recv(1024)
print (recv1)
if recv1[:3] != '250':
	print ('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
client_socket.send(quitCommand.encode())
client_socket.close()