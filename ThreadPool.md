# ThreadPool Component #
The ThreadPool is a component in which other components can get jobs executed.

The API has three important functions:

### ThreadPool(max\_workers=5, kill\_workers\_after=3) ###
Constructor function
  * max\_workers is the maximum number of threads used in/by the pool.
  * kill\_workers\_after is the number of seconds a worker should wait for jobs before being killed


### add\_job(function, args=None, return\_callback=None) ###
  * function is the callable that defines the job
  * args is a list of arguments to the function
  * return\_callback is called when the function has been performed.

### shutdown(wait\_for\_workers\_period = 1, clean\_shutdown\_reties = 5) ###
Blocks so no more jobs are accepted. Waits for all workers to punch out. When a call to this function returns the program can be terminated.
  * wait\_for\_workers\_period is the number of seconds to wait for workers to shutdown
  * clean\_shutdown\_reties how many times to retry the shutdown

the method returns True if the shutdown was succesfull.