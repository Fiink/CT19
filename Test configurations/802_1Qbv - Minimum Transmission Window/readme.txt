SETUP:
Connect two computers, each equipped with the Intel I210 network card.
Ensure the gPTP is running correctly, and is transmitted as priority 7.

STEPS:
1. Configure the gates.sched file to match the desired configuration. For this test, the second window was configured
	S 0x3 <time_in_ns>
2. Run the following command on the receiver-computer:
	sudo tcpdump -i enp1s0 -w <FILEPATH>.pcap port 4800
   where <filename> is the path to the file which contains all traffic received.
   The frames will be transmitted using port 4800, and is thus used as a filter.
3. Run the following command on the transmitter-computer:
	sudo python scheduler.py -i enp1s0 -q queue.cfg -e 30 -g gates.sched
   This will configure the TAS using the scheduler provided by IoTG.
4. After the TAS is configured, run the transmitter-program:
	sudo ./sample-app-taprio -i enp1s0 -c 169.254.0.2 -x 1 -w txconfig.cfg -B base_time
   The transmitter will send frames 30 seconds after the specified base_time,
   which is set by the scheduler.py script.
   The sample-app-taprio program is provided by IoTG.
5. After 60 seconds of active transmissions, stop the tcpdump on the receiver.