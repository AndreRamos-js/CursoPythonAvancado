


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user


    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
'''    
c1 = Connection()
c1.set_user('André')
print(c1.user)
'''

c1 = Connection.create_with_auth('André', '12345')
print(c1.user)
print(c1.password)
