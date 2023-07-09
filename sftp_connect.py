

def c_sftp(direction,log_name,file_name_ventas,file_name_locales,file_name_articulos,pag_name_ventas,pag_name_locales,pag_name_articulos):
    print('SFTP connect')

    import paramiko
    from paramiko import SSHClient
    from scp import SCPClient
    
    # Establecer la conexión SFTP
    host = 'host'
    port = 2393
    
    username = 'user'
    password = 'pass'
    
    
    # Crear una instancia de SSHClient
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    sftp = ssh.open_sftp()
    
    # Enviar un archivo al servidor SFTP    
    sftp.put(file_name_ventas, pag_name_ventas)
    sftp.put(file_name_locales, pag_name_locales)
    sftp.put(file_name_articulos, pag_name_articulos)
    
    
    # Cerrar la conexión SFTP
    sftp.close()
    ssh.close()
    
 
