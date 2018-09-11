import threading


class Thread(threading.Thread):
    def __init__(self, t_id, name, counter,func,args=None):
        threading.Thread.__init__(self)
        self.t_ID = t_id
        self.name = name
        self.counter = counter
        self.x=func
        self.args=args
    def run(self):
        if self.args:
            self.x(self.args)
        else:
            self.x()




