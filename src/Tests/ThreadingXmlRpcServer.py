from TestTiming import time_this
from SocketServer import ThreadingMixIn
from SimpleXMLRPCServer import SimpleXMLRPCServer
from threading import Thread
from thread import start_new_thread 
from xmlrpclib import ServerProxy
from ThreadPool import ThreadPoolMixIn
from time import sleep

PORT_NUMBER = 20392 

def test_method():
    return True

class XmlRpcServer(ThreadingMixIn, SimpleXMLRPCServer):
        
    def __init__(self):
        
        SimpleXMLRPCServer.__init__ (self, ('localhost', PORT_NUMBER), logRequests=False)
        self.register_function(test_method, "test")
        
        print "XmlRpcServer"

class XmlRpcServerThreadPool(ThreadPoolMixIn, SimpleXMLRPCServer):
        
    def __init__(self):
        SimpleXMLRPCServer.__init__ (self, ('localhost', PORT_NUMBER), logRequests=False)
        ThreadPoolMixIn.__init__(self)
        self.register_function(test_method, "test")
        print "XmlRpcServerThreadPool"


def setup():
    server = XmlRpcServerThreadPool()
    #server = XmlRpcServer()
    start_new_thread(server.serve_forever, ())

def call_test():
    client = ServerProxy('http://localhost:%i'%PORT_NUMBER)
    client.test()

def run_test():
    threads = []
    
    for _ in range(0,10):
        sleep(0.7)
        t = Thread(None, call_test)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

setup()
time_this(call_test)
time_this(call_test)
time_this(call_test)
time_this(call_test)
time_this(call_test)