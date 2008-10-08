import logging
from ThreadPool import ThreadPool
from time import sleep

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(levelname)-8s thread: %(thread)d %(name)-16s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S'
)


class testJobClass():
    def __init__(self, id, x):
        self.x = x
        self.id = id
        logging.info( "init %s %i" %(id, self.x) )
        
    def countUp(self):
        self.x +=1
        logging.info("cup %s %i"%(self.id, self.x))

def job1(msg, tp = None, spawn = False, sleepTime = 0):
    logging.info("job start %s"%msg)
    
    if (spawn):
        tp.add_job(job1, [msg + ".1"])
        tp.add_job(job1, [msg + ".2"])
        tp.add_job(job2)
    sleep(sleepTime)
        
    logging.info("job end %s"%msg)
    return ("Yihaa!", 124)

def job2():
    logging.info("II job start")
    sleep(2)
    logging.info("II job end")
    return 42

def result(val):
    logging.info("result : %s"%str(val))

tp = ThreadPool()

t1 = testJobClass("t1", 42)
t2 = testJobClass("t2", 1)


tp.add_job(job1, ["1", tp, True, 4], result)
tp.add_job(t1.countUp, None)
tp.add_job(t2.countUp, return_callback=result)
tp.add_job(t1.countUp)
tp.add_job(t2.countUp)
