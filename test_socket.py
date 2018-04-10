import base64, getpass, socket, ssl, sys

# Global variables
mailserv = ''
mailport = -1
mailfrom = ''
mailrcpt = ''
mailmess = ''
username = ''
password = ''
cryptmethod = 'none'

# Derpy hooves ascii art for maximum swag
derpyAscii = """                                                                                
              .,:ccoolc:;'.                                                     
          .cxKNNNWWNNNWNNNXOd,                                                  
        ,xXNWWWWWWWWWWWWWWWNNNKd,.cxl.                                          
       cdxXNNNWWWWWWWWWWWWWWWNNX00000d.                                         
        ;0NWNWWWWWWWWWWWNNNNNNKO000000c                                         
      .xNNNWWWWWWWWNNNNXKKKK00000000O0x.                                        
     .OKXNNNWWWWWNNNXK00Okkxk0OO000Ok0O.                                        
     .dONWWWWNNNNNXK0OdldkxlloxO000kk0o                                         
  ..:dXNNNNNNXOKNK00k:dXMMMMKxxO00Ok0O,                                         
  :dOOOOOkoxNNkX000Oc0W0KWMMMX0000O00c                                          
           ;NWOx000c,NN:oWMMMX0000O0x                                           
           ,KMWK000, ..:KWMWX00000kKK.                                          
           .OKX0000o'  'OXXK000000KXNl                                          
          .dkkO000000Ok0000000000KNNNO.                                         
          .oOO00O000000000000000KNNNNX'              .;ldOO000Oko:.             
           'xOkkO000000000000000XNNNNW,            'xXNNNNWWNWNWNNNOl.          
         ,xXKKXX0OOOOOOOOOOO0000NNNNWN;          .xNNWWWWWWWWWWWWWNNNNO;        
       ;OWMMMMMMMNO:,,.'dOO0000KNXXNNXxo;..',''',kNWWWWWWWWWWWWWWWWNNNNNO,      
     .xWMMWXXWMMMWO;   :0000000KNx0NNXkxkOOOOOOOOOXWWWNNWWWWWWWWWWWWNNNNKXo     
   .dNMMWXKXNMMKo'    ,O0000000Kk,ONNNK0OOOOOOOOOkk;,,ckNNWWNWWWWWWWWWNNx'do    
  ;OXMMN0OXNWXl       o00000000Kc.xNNNX00000OOOOOKk.    lNNWWWWWWWWWWWWNN' ''   
 ,KOXMMMWNWNd.       .x00000000O;.:XNNNK000OkOO0KK0,    'NNWWWWWWWWWWWWNW,      
  :ONMMMMWO'          o00000000x'..oNKKX0Okdlx0KKK0c    lNNWWWWWWWWWWWWNW,      
   .;kNMNo            ,O0000000o...'ko,okc''.o0XXK0,  .dNNWWWWWWWWWWWWWNN,      
      .:;              ;O000000l....,;..',..'d00KKOddONNNNWWWWWWWWWWWWWNNl      
                     .':xkO0000l............,k0000kXNNNNNWWWWWWWWWWWWWWNNk      
                   ;dxkxkxxkkO0d.ldc....:lc'c0000O'...lXNNWWWWWWWWWWWWWWNX'     
                  .kkkkxxkdl,.';::c;....;c:;x0000Oxl..KNWWWWWWWWWWWWWWWWWNk     
                  .dkkkkxxc.    cc:olll:'.:xxk000000kxNNNNNWWWWWWWWWWWWNWNNd    
                   'xkkkkkkxo'  'O00000x'.dxkxkO00000OXNXXNNNWWWWWWWWNNNNNNNx.  
                    ;xkkkkkkkx, '0000000d.lxkkxk0000000K,cNNWWWWWWWWWWNNKcoOXXo.
                     :xkkkkkkkc 'O000000O,lkkkkxO00000O: .0NNWWWWWWWWWWNNO. ....
                      ,dkkkkkkc ;O000000OllkkkkxO000000o  .0NNNWWWWWWWNNNN0;    
                       .cxkkkx' o00000000kxkkkkxO000000O.  .oXNNWWWWNNNNNNNNx.  
                         .,c:. 'O00000000xxkkkxk0000000O,    .ckXNNNNNNXxodk00d;
                               o000000000kkkkkxO0000000O;       .,codk0KKkc.  ..
                              :O000000000kkkkxk00000000O;                       
                             'k000000000Od;:cdO00000000k.                       
                             .lkOOOOOOOko'   .coxxxxol,.                        """


# Function - getServerAddr
# Description - asks the user to input the mail server's address
def getServAddr():
    global mailserv
    mailserv = input('Enter the address of the mail server: ')

# Function - getServerPort
# Description - asks the user to input the mail server's port number
def getServPort():
    global mailport
    while True:
        p = int(input('Enter the port number to connect to: '))
        if not (p < 0 or p > 65535):
            mailport = p
            return
        else:
            print('Invalid entry. Port number must be between 0 and 65,535.')

# Function - getFromAddr
# Description - asks the user to input the email address they're sending from
def getFromAddr():
    global mailfrom
    mailfrom = input('Enter the email address you\'re sending from: ')

# Function - getRcptAddr
# Description - asks the user to input the email address they're sending to
def getRcptAddr():
    global mailrcpt
    mailrcpt = input('Enter the email address you\'re sending to: ')

# Function - getMailMsg
# Description - asks the user to input a message terminated with an EOF to send
def getMailMess():
    global mailmess
    print('--------------------------------------------------------------------------------')
    print('|               Enter your message below. Terminate with an EOF.               |')
    print('--------------------------------------------------------------------------------')
    mailmess = sys.stdin.read(-1)

# Function - getUserName
# Description - asks the user to input their username to authenticate
def getUserName():
    global username
    username = input('Enter your username: ')

# Function - getPassword
# Description - asks the user to input their password to authenticate
def getPassword():
    global password
    password = getpass.getpass('Enter your password: ')

# Function - getCryptoOpt
# Description - asks the user to select their method of encryption
def getCryptoOpt():
    global cryptmethod
    while True:
        c = input('Choose an encryption protocol (TLS, SSL, or none): ')
        if (c == 'TLS') or (c == 'SSL') or (c == 'none'):
            cryptmethod = c
            return
        else:
            print("Invalid choice!")
        

# Function - dispMenu
# Description - displays the program's main menu
def dispMenu():
    print(derpyAscii)
    print("--------------------------------------------------------------------------------")
    print("| Welcome to Derpy Mailer! | Ver. 0.01 | Edit parameters below and enter send! |")
    print("--------------------------------------------------------------------------------")
    print("1) SMTP Server: " + mailserv)
    if mailport == -1:
        print("2) Port: ")
    else:
        print("2) Port: " + str(mailport))
    print("3) From: " + mailfrom)
    print("4) To: " + mailrcpt)
    print("5) Username: " + username)
    print("6) Password: <not displayed>")
    print("7) Crypto: " + cryptmethod)

# Function - mainLoop
# Description - handles the main loop of the program
def mainLoop():
    useropt = 'derp'
    while useropt != 'send':
        dispMenu()
        useropt = input()
        if useropt == '1':
            getServAddr()
        elif useropt == '2':
            getServPort()
        elif useropt == '3':
            getFromAddr()
        elif useropt == '4':
            getRcptAddr()
        elif useropt == '5':
            getUserName()
        elif useropt == '6':
            getPassword()
        elif useropt == '7':
            getCryptoOpt()
        elif useropt == 'send':
            getMailMess()
            smtpSession()
        else:
            print('Invalid choice. Please enter again.')

# Function - getSSLSocket
# Description - creates a new socket, wraps it in an SSL context, and returns it
def getSSLSocket():
    return ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), ssl_version=ssl.PROTOCOL_SSLv23)

# Function - getTLSSocket
# Description - creates a new socket, wraps it in a TLS context, and returns it
def getTLSSocket():
    return ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), ssl_version=ssl.PROTOCOL_TLSv1)

# Function - getPlainSocket
# Description - creates a new vanilla socket and returns it
def getPlainSocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function - smtpSession
# Description - handles sending the message
def smtpSession():
    # Get the socket
    if cryptmethod == 'SSL':
        sock = getSSLSocket()
    elif cryptmethod == 'TLS':
        sock = getTLSSocket()
    else:
        sock = getPlainSocket()
    # Attempt to connect to the SMTP server
    sock.connect((mailserv, mailport))
    # Receive response from server and print it
    respon = sock.recv(2048)
    print(str(respon, 'utf-8'))
    # Say HELO and print response
    heloMesg = 'HELO Derpy\r\n'
    print(heloMesg)
    sock.send(heloMesg.encode('utf-8'))
    respon = sock.recv(2048)
    print(str(respon, 'utf-8'))
    # Authenticate with the server
    authMesg = 'AUTH LOGIN\r\n'
    crlfMesg = '\r\n'
    print(authMesg)
    sock.send(authMesg.encode('utf-8'))
    respon = sock.recv(2048)
    print(str(respon, 'utf-8'))
    user64 = base64.b64encode(username.encode('utf-8'))
    pass64 = base64.b64encode(password.encode('utf-8'))
    print(user64)
    sock.send(user64)
    sock.send(crlfMesg.encode('utf-8'))
    respon = sock.recv(2048)
    print(str(respon, 'utf-8'))
    print(pass64)
    sock.send(pass64)
    sock.send(crlfMesg.encode('utf-8'))
    respon = sock.recv(2048)
    print(str(respon, 'utf-8'))
    # Tell server the message's sender
    fromMesg = 'MAIL FROM: <' + mailfrom + '>\r\n'
    print(fromMesg)
    sock.send(fromMesg.encode('utf-8'))
    respon = sock.recv(2048)
    print(str(respon, 'utf-8'))
    # Tell server the message's recipient
    rcptMesg = 'RCPT TO: <' + mailrcpt + '>\r\n'
    print(rcptMesg)
    sock.send(rcptMesg.encode('utf-8'))
    respon = sock.recv(2048)
    print(str(respon, 'utf-8'))
    # Give server the message
    dataMesg = 'DATA\r\n'
    print(dataMesg)
    sock.send(dataMesg.encode('utf-8'))
    respon = sock.recv(2048)
    print(str(respon, 'utf-8'))
    mailbody = mailmess + '\r\n'
    print(mailbody)
    sock.send(mailbody.encode('utf-8'))
    fullStop = '\r\n.\r\n'
    print(fullStop)
    sock.send(fullStop.encode('utf-8'))
    respon = sock.recv(2048)
    print(str(respon, 'utf-8'))
    # Signal the server to quit
    quitMesg = 'QUIT\r\n'
    print(quitMesg)
    sock.send(quitMesg.encode('utf-8'))
    respon = sock.recv(2048)
    print(str(respon, 'utf-8'))
    # Close the socket to finish
    sock.close()

# mainLoop()