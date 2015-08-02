
#ThreadPool Component#
The ThreadPool is a component in which other components can get jobs executed.

The API has three important functions:

##ThreadPool(max_workers=5, kill_workers_after=3)##
Constructor function

max_workers is the maximum number of threads used in/by the pool.
kill_workers_after is the number of seconds a worker should wait for jobs before being killed

##add_job(function, args=None, return_callback=None)##
function is the callable that defines the job
args is a list of arguments to the function
return_callback is called when the function has been performed.


##shutdown(wait_for_workers_period = 1, clean_shutdown_reties = 5)##
Blocks so no more jobs are accepted. Waits for all workers to punch out. When a call to this function returns the program can be terminated.

wait_for_workers_period is the number of seconds to wait for workers to shutdown
clean_shutdown_reties how many times to retry the shutdown
the method returns True if the shutdown was succesfull.




Automatically exported from code.google.com/p/pythonthreadpool
