from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n Hello world!"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

   # Create socket called clientSocket and establish a TCP connection with mailserver and port

   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver, port))
   recv = clientSocket.recv(1024)
 # print(recv)
   if recv[:3] != '220':
       print('220 reply not received from server.')

   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024)
 # print(recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   mailFrom = "MAIL FROM: <source@gmail.com> \r\n"
   clientSocket.send(mailFrom.encode())
   recv2 = clientSocket.recv(1024)
 # print(recv2)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Send RCPT TO command and print server response.
   rcptTo = "RCPT TO: <destination@gmail.com> \r\n"
   clientSocket.send(rcptTo.encode())
   recv3 = clientSocket.recv(1024)
 # print(recv3)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Send DATA command and print server response.
   data = "DATA\r\n"
   clientSocket.send(data.encode())
   recv4 = clientSocket.recv(1024)
 # print(recv4)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Send message data.
   subject = "Subject: Test \r\n\r\n"
   clientSocket.send(subject.encode())
   clientSocket.send(msg.encode())
   clientSocket.send(endmsg.encode())
   recv5 = clientSocket.recv(1024)
 # print(recv5)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Message ends with a single period.
   clientSocket.send(endmsg.encode())
   recv6 = clientSocket.recv(1024)
 # print(recv6)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Send QUIT command and get server response.
   clientSocket.send("QUIT\r\n".encode())
   recv7 = clientSocket.recv(1024)
  # print(recv7)
   clientSocket.close()

if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
