"""
###                         设计模式之策略模式
###     举例： 客户消息通知
###     策略： 针对客户以短信还是Email
###
"""
class Customer:
    customer_name = ''
    phone_num = ''
    snd_way = ''
    email_addr = ''
    info = ''

    def set_name(self, name):
        self.customer_name = name

    def get_name(self):
        return self.customer_name

    def set_phone(self, phone):
        self.phone_num = phone

    def get_phone(self):
        return self.phone_num

    def set_email(self, email):
        self.email_addr = email

    def get_email(self):
        return self.email_addr

    def set_brdway(self, way):
        self.snd_way = way

    def set_info(self, info):
        self.info = info
    def snd_msg(self):
        self.snd_way.send(self.info)


class SendMessage:
    dst_code = ''
    def set_code(self, code):
        self.dst_code = code

    def send(self):
        pass


class EmailSender(SendMessage):
    def send(self, info):
        print('Email Address: %s  Info: %s' % (self.dst_code, info))


class PhoneSender(SendMessage):
    def send(self, info):
        print('Phone Number: %s  Info: %s' % (self.dst_code, info))


if __name__ == '__main__':
    customer_x = Customer()
    customer_x.set_name('Custom A')
    customer_x.set_phone('18629162828')
    customer_x.set_email('517970464@qq.com')
    customer_x.set_info('Welcome to China!')
    email_x = EmailSender()
    email_x.set_code(customer_x.get_email())
    customer_x.set_brdway(email_x)
    customer_x.snd_msg()

    phone_x = PhoneSender()
    phone_x.set_code(customer_x.get_phone())
    customer_x.set_brdway(phone_x)
    customer_x.snd_msg()


