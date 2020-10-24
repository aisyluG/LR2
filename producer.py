from PyQt5.QtCore import QObject, QThread, pyqtSignal

class Producer(QObject):
    message_sented = pyqtSignal(str)
    def __init__(self, semaphore, buffer, parent=None):
        super().__init__(parent)
        self.semaphore = semaphore
        self.message_count = 0
        self.messages = buffer

    def run(self):
        self.messages.put(f'Сообщение {self.message_count}')
        self.semaphore.release(1)
        # уведомление о том, что сообщение отправлено
        self.message_sented.emit(f'Сообщение {self.message_count}')
        self.message_count += 1
        # print('Сообщение', self.message)