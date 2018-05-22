from socket import *
import ssl
import base64

username = input("Enter your username: ")
password = input("Enter your password: ")
rcpt_to = input("SEND TO: ")
subject = input("Enter subject: ")
print("Enter your message (Finish message with blank line):")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
msg = "\r\n" + text


mail_server = 'smtp.gmail.com'
client_socket = socket(AF_INET, SOCK_STREAM) 

client_socket = ssl.wrap_socket(client_socket)
client_socket.connect((mail_server, 465))
recv = client_socket.recv(1024)
print (recv)

# Send HELO command and print server response.
hello_command = 'EHLO localhost\r\n'
client_socket.send(hello_command.encode())
recv1 = client_socket.recv(1024)
print (recv1)

# Authenticate.
username_b64 = base64.b64encode(bytes(username, 'utf-8'))
username_b64_str = username_b64.decode('utf-8')
usernameCommand = 'AUTH LOGIN {0}\r\n'.format(username_b64_str)
client_socket.send(usernameCommand.encode())
recv1 = client_socket.recv(1024)
print (recv1)

password_b64 = base64.b64encode(bytes(password, 'utf-8'))
password_b64_str = password_b64.decode('utf-8')
passCommand = password_b64_str + '\r\n'
client_socket.send(passCommand.encode())
recv1 = client_socket.recv(1024)
print (recv1)

# Send MAIL FROM command and print server response.
mailAdd = 'MAIL FROM: <{0}>\r\n'.format(username)
client_socket.send(mailAdd.encode())
recv1 = client_socket.recv(1024)
print(recv1)


# Send RCPT TO command and print server response.
rcptAdd = 'RCPT TO: <{0}> \r\n'.format(rcpt_to)
client_socket.send(rcptAdd.encode())
recv1 = client_socket.recv(1024)
print (recv1)


# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
client_socket.send(dataCommand.encode())
recv1 = client_socket.recv(1024)
print (recv1)


# Send subject data.
subject = "Subject:" + subject + "\r\n"
client_socket.send(subject.encode())
# Send message data.

client_socket.send(msg.encode())
# Message ends with a single period.
endmsg = "\r\n.\r\n"
client_socket.send(endmsg.encode())

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
client_socket.send(quitCommand.encode())
recv1 = client_socket.recv(1024)
print(recv1)

client_socket.close()
print("Complete!")