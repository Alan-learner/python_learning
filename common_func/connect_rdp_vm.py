from pyRDP.rdp import RDPClient

def execute_command(rdp_client, command):
    # 连接到RDP服务器
    rdp_client.connect()
    # 执行命令
    rdp_client.send_command(command)
    # 获取命令执行结果
    result = rdp_client.get_output()
    # 断开RDP连接
    rdp_client.disconnect()
    return result

def main():
    # RDP服务器的主机名或IP地址
    hostname = 'your_hostname'
    # RDP服务器的用户名和密码
    username = 'your_username'
    password = 'your_password'
    # 要执行的CMD命令
    command = 'dir'
    
    # 创建RDP客户端对象
    rdp_client = RDPClient(hostname, username, password)
    # 执行命令并获取结果
    result = execute_command(rdp_client, command)
    
    # 打印结果
    print(result)

if __name__ == '__main__':
    main()
