import pytest


class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__que = []

    def put(self, param):
        self.__que.insert(0,param)
        print(self.__que)
        pass

    def get(self):
        if self.is_empty():
            raise QueueError()
        item = self.__que[-1]
        del self.__que[-1]
        return item

    def is_empty(self):
        if len(self.__que) == 0:
            return True
        else:
            return False


def test_queue():
    que = Queue()

    assert que.is_empty() == True
    try:
        que.get()
        assert False
    except QueueError:
        pass

    que.put(1)
    que.put("dog")
    que.put(False)

    try:
        assert que.get() == 1
        assert que.get() == "dog"
        assert que.get() == False
        assert que.is_empty()
    except:
        print("Queue error")
        assert False

