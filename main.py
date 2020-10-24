from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, QSemaphore
import sys
from window import Ui_MainWindow
import queue
from producer import Producer
from consumer import Consumer

class Window(QMainWindow):
    # семафор для работы потока
    sem = QSemaphore()

    sem_forBuffer = QSemaphore()
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # буфер для отправленных, но еще не обработанных сообщений
        self.buffer = queue.Queue()
        # потоки для обработки информации
        self.sentThread = QThread()
        self.sentObj = Producer(self.sem, self.buffer)
        self.sentObj.moveToThread(self.sentThread)

        self.n = 1
        self.getThreadsPool = [QThread()]
        self.getObjs = [Consumer(self.sem, self.sem_forBuffer, 1, self.buffer)]
        self.getObjs[0].moveToThread(self.getThreadsPool[0])



        self.ui.sendBt.clicked.connect(self.sentObj.run)
        self.ui.sendBt.clicked.connect(self.check)
        self.sentObj.message_sented.connect(self.getObjs[0].run)
        self.sentObj.message_sented.connect(self.addSendedMessage)
        self.getObjs[0].message_getted.connect(self.addGettedMessage)
        self.ui.okBt.clicked.connect(self.change_threadNumber)


        self.sem_forBuffer.release()
        self.sentThread.start()
        self.getThreadsPool[0].start()

    def check(self):
        print('check', self.sem_forBuffer.available())

    def change_threadNumber(self):
        n_new = self.ui.threadNumberSBox.value()
        if self.n < n_new:
            print(list(range(self.n, n_new)))
            for i in range(self.n, n_new):
                self.getThreadsPool.append(QThread())
                self.getObjs.append(Consumer(self.sem, self.sem_forBuffer, i+1, self.buffer))
                self.getObjs[i].moveToThread(self.getThreadsPool[i])
                self.sentObj.message_sented.connect(self.getObjs[i].run)
                self.getObjs[i].message_getted.connect(self.addGettedMessage)
                self.getThreadsPool[i].start()
        elif self.n > n_new:
            for i in range(n_new, self.n):
                self.getThreadsPool[i].terminate()
                self.getThreadsPool[i].wait()
            self.getThreadsPool = self.getThreadsPool[:n_new]
            self.getObjs = self.getObjs[:n_new]
        self.n = n_new


    def addSendedMessage(self, message):
        self.ui.sendedText.append(message)
        # print('1')

    def addGettedMessage(self, message):
        print('add', self.sem_forBuffer.available())
        self.sem_forBuffer.acquire(1)
        self.ui.gettedText.append(message)
        self.sem_forBuffer.release(1)
        # print('1')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
