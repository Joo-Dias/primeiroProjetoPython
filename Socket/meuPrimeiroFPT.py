from ftplib import *

# Passando como parametro um protocolo (FTP) e um dominio
ftp = FTP("ftp.ibiblio.org")

print(ftp.getwelcome())

ftp.quit()