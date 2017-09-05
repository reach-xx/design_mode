class manager():
    successer = ''
    name = ''

    def __init__(self, name):
        self.name = name

    def set_successer(self, successer):
        self.successer = successer

    def handle_request(self, request):
        pass


class request():
    requestType = ''
    requestNum = 0
    requestContent = ''


class LineManage(manager):
    def handle_request(self, request):
        if request.requestType == 'Dayoff' and request.requestNum <= 3:
            print('Line Manage request %d days Over' % request.requestNum)
        else:
            print('Line Manage request continue!')
            self.successer.handle_request(request)

class DepartManage(manager):
    def handle_request(self, request):
        if request.requestType == 'Dayoff' and  request.requestNum <= 7:
            print('Depart Manage request %d days Over' % request.requestNum)
        else:
            print('Depart Manage request continue!')
            self.successer.handle_request(request)


class GeneralManage(manager):
    def handle_request(self, request):
        if request.requestType == 'Dayoff':
            print('General Manage request Over!')


if __name__ == '__main__':
    Lmanage = LineManage("Line Manage")
    Dmanage = DepartManage('Depart Manage')
    Gmanage = GeneralManage('General Manage')

    Lmanage.set_successer(Dmanage)
    Dmanage.set_successer(Gmanage)

    req = request()
    req.requestNum = 8
    req.requestType = 'Dayoff'
    req.requestContent = 'Ask 8 days off'
    Lmanage.handle_request(req)





