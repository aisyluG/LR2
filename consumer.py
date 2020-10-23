from PyQt5.QtCore import QObject, pyqtSignal
import queue


class Consumer(QObject):
    message_getted = pyqtSignal(str)
    def __init__(self, semaphoreGet, semaphoreAddToWindow, name, buffer, parent=None):
        super().__init__(parent)
        self.semaphore = semaphoreGet
        self.semaphore2 = semaphoreAddToWindow
        self.buffer = buffer
        self.name = name

    def run(self, message=None):
        print('w')
        if message is not None and self.semaphore.tryAcquire(1)==True:
            print(f'consumer {self.name}', message)
            self.thread().sleep(2)
            self.semaphore2.acquire(1)
            self.buffer.put(f'Поток {self.name}. ' + message)
            self.semaphore2.release(1)
            self.message_getted.emit(self.buffer)
            print('getted')
        else:
            print('n')


