# Eprofiler

## Function and motivation

Eprofiler is a tool designed to easely and precisely time bloc of code rather than a function or a line. It's composed a small C library  providing a basic interface that product primitives outputs. This outputs are processed by eprof executable to produce kvhf files(https://github.com/crazyhouse33/kvhf). 

This design allow for the lib code to be the most simple, precise and efficient as possible. This also reduce greatly the effort to support another language. If you develop a library in another language you can reuse eprof executable and the generic library tests suits. Once integrated, this will also output metrics about the precision of your implementation.


## Install

The library is tested against latest Ubuntu, macOS and Windows.

```bash
# eprof executable
pip install --index-url https://test.pypi.org/simple/ eprof

# Building and installing C library 
git clone https://github.com/crazyhouse33/eprof
cd libs/C/build
cmake .. 
# Add -DCMAKE_INSTALL_PREFIX:PATH=/path/to/install to the last command to install in another directory than your default lib location (need root)
cmake --build . --target install
```

## Usage

```C

#include <eprof.h>
int main(int argc, char** argv) {
	
	Eprof *profiler = new_eprofiler("eprof_output_dir", false);  #If true append to an existing session. If false overwrite it.

	eprof_event_start(profiler, whole);
		for (int i = 0; i < 10 ; i++) {
			eprof_event_start(profiler, in_for);
			eprof_event_end(profiler, in_for);
		}
	eprof_event_end(profiler,whole);
	return 0;
}
```
The lib let you avoid a maximum of timing overhead by accepting many event per start/end call. If you start an event and finish another one at the same time, you can use take advantage of the fact that end/start return the time, and use the start\_nt/end\_nt functions:
```C
long t=eprof_event_end(profiler, event1, event2, event3);
eprof_event_start_nt(profiler, t, event4, event5);
```

Then run eprof on the produced session directory.
```bash
eprof eprof_output_dir -o result.kvhf
eprof -h # For help
```
This will produce an history key value file (https://github.com/crazyhouse33/kvhf) for further visualization of the result.


## Remarks on the lib:

Eprof support starting an event in a process and finishing it on another.    

Eprof includes a cross platform high precision timer for Windows, Mac and linux that you can use separatly for your softwares.

The library is immature and have some problems:


The library use macros and standard io to reduce the overhead to a timing + print. This simple behaviour dont allow for concurrency shemes. If you start two times the same events, the first end reached by any thread is always going to be affected to the first event. If you dont care for this problem you may output false information about minimum and maximum duration but wont impact means or standard deviation.

I suspect that using the functions of the library on different thread can impact the quality of the measures because of the lock of printf that may (I need to add a test for it) not preserve the order in which threads block on the lock. This would potentially lead again to bad max/min value.  

I am able to observe abnormally longs maximum values on runs even between two consecutives get\_time(). I must improve the benchmarking condition of the tests to be sure but this is probably just the sheduler that is interfering. 

This is your responsability to run the process on suitable environnement to get reproducible results (max and stddev are concerned, mean and min not so much). Check out https://github.com/parttimenerd/temci for Linux. By looking quickely this tool seem to ignore totally autogroup and chrt to achieve his goal while doing other questionable stuff. But it look like this is the only project that care about the problematic. 


## TODO

- Use thread pool unstead of raw (print) (print is unblocking until kernel buffer is full according to the experiments.) This mean that for now, if you output a lot of events in a short period of time, one event logging may block. If it's a start event, the logged time will include the time it took for the kernel to flush the buffer, the switch...

- The threadpool should improve precision (This is to be checked) while allowing to implement more complex logging  without impacting precision (support start and end concurrency?).

- Think of another api for the timer to stop paying the conversion to nano sec/long twice per block

