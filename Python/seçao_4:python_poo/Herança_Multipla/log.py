class LogMixin:
    @staticmethod
    # Esse decorador indica que o método não irá utilizar nem a class nem o objeto, mas que no fim será usado!
    def write(msg):
        with open('log.log', 'a+') as file:
            file.write(msg)
            file.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')
