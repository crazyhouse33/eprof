# Eprofiler

## Function and motivation

Eprofiler is a tool designed to easely and precisely time bloc of code rather than a function of a line. This is also done to work across many process. It's composed a small C library  providing a really basic interface that product primitives outputs. This outputs are processed by eprof executable to produce kvhf files(https://github.com/crazyhouse33/kvhf). 

This design allow for the lib code to be the most simple, precise and efficient as possible. This also reduce greatly the effort to support another language. If you develop a library in another language you can reuse eprof executable and the generic library tests suits. Once integrated, this will also output metrics about the precision of your implementation.


## Install

```bash
# eprof executable
pip install --index-url https://test.pypi.org/simple/ eprof

# Building and installing C library 
git clone url
cd libs/C/build
cmake .. 
# Add -DCMAKE_INSTALL_PREFIX:PATH=/path/to/install to the last command to install in another directory than your default lib location (need root)
cmake --build . --target install
```

## Usage
Once installed link your code, wich would look like:

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

Then run eprof on the produced directory.
```bash
eprof eprof_output_dir -o result.kvhf
eprof -h # For help
```
This will produce an history key value file (https://github.com/crazyhouse33/kvhf) for further visualization of the result.


## Remarks on the lib:

The library aim to be cross platform. It includes a cross platform high precision timer for Windows, Mac and linux that you can use separatly for your softwares.

The library use macros and standard io to reduce the overhead to a timing + print. This simple behaviour dont allow for concurrency shemes. If you start two times the same events, the first end reached is always going to be affected to the first event. This will render false information about minimum and maximum duration, without impacting means or standard deviation.


The basic io approach also introduce an abnormal long event duration if you fill up the kernel buffer.


Boths theses limitations will disapear when a thread pool will be used unstead.



## TODO

- Test on windows an Mac with git workflow

- Use thread pool unstead of raw (print) (print is unblocking until kernel buffer is full according to the experiments.) This mean that for now, if you output a lot of events in a short period of time, one event logging may block. If it's a start event, the logged time will include the time it took for the kernel to flush the buffer, the switch...

- The threadpool should improve precision (This is to be checked) while allowing to implement more complex logging  without impacting precision (support start and end concurrency?).

