"""
##          代理模式
##  将服务器收发显示与代理完全区分开来
##
##
"""


#服务器 收发 类
class Server(object):
    content = ''

    def recv(self, info):
        pass

    def send(self, info):
        pass

    def show(self):
        pass


#服务器   信息
class InfoServer(Server):
    def recv(self, info):
        self.content = info
        return 'recv OK'

    def send(self, info):
        pass

    def show(self):
        print('SHOW: ', self.content)


#服务器代理
class ServerProxy:
    pass


class infoServerProxy(ServerProxy):

    def __init__(self, server):
        self.server = server

    def recv(self, info):
        return self.server.recv(info)

    def show(self):
        self.server.show()


class WhiteInfoServerProxy(infoServerProxy):
    white_list = []

    def recv(self, info):
        try:
            assert type(info) == dict
        except:
            return 'type is not correct!'

        addr = info.get('addr', 0)
        if addr in self.white_list:
            content = info.get('content','')
            self.server.recv(content)
        else:
            print("Your Address isn't  in white list!!")

    def show(self):
        self.server.show()

    def addWhite(self, info):
        self.white_list.append(info)
        print(self.white_list)

    def rmvWhite(self, info):
        self.white_list.remove(info)
        print(self.white_list)

    def clearWhite(self):
        self.white_list.clear()
        print(self.white_list)

if __name__ == '__main__':
    info_list = dict()
    server = InfoServer()
    white_server = WhiteInfoServerProxy(server)
    info_list['addr'] = 10000
    info_list['content'] = 'Hello World'

    white_server.recv(info_list)
    white_server.show()

    white_server.addWhite(10000)
    white_server.addWhite(10001)
    white_server.addWhite(10002)
    white_server.addWhite(10003)
    white_server.addWhite(10004)
    white_server.addWhite(10005)
    white_server.addWhite(10006)
    white_server.recv(info_list)
    white_server.show()

    white_server.rmvWhite(10000)
    white_server.recv(info_list)
    white_server.show()

    info_list['addr'] = 10002
    info_list['content'] = 'Welcome China!'
    white_server.recv(info_list)
    white_server.show()










