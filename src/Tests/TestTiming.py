from time import time


def time_this( function_callable ):
    start_time = time()
    function_callable()
    print "time: ", time() - start_time
    