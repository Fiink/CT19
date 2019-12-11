SETUP:
Connect two computers, each equipped with the Intel I210 network card.
Ensure the gPTP is running correctly, and is transmitted as priority 7.

STEPS:
1. On the transmitter-computer, run the following command to initialise the test:
	sudo python3 TAS_qdisc_reconfiguration.py
2. In two new terminals, prepare (but do not run) the following commands to run the transmitter-program
   provided by IoTG:
   Terminal 1:
	sudo ./sample-app-taprio -i enp1s0 -c 169.254.0.2 -x 1 -w tsn_prio6_med.cfg
   Terminal 2: 
	sudo ./sample-app-taprio -i enp1s0 -c 169.254.0.2 -x 1 -w tsn_prio5_med.cfg 
   This will start two transmitters of 10Mbit/s and 5Mbit/s traffic, respectively.
   To transmit with 1 Gbit/s and 500 Mbit/s traffic, use the following commands:
	sudo ./sample-app-taprio -i enp1s0 -c 169.254.0.2 -x 1 -w tsn_prio6_high.cfg 
	sudo ./sample-app-taprio -i enp1s0 -c 169.254.0.2 -x 1 -w tsn_prio5_high.cfg
3. On the receiver-computer, start tcpdump using the following command:
	sudo tcpdump -i enp1s0 -w <FILEPATH>.pcap port 4800
   where <filename> is the path to the file which contains all traffic received.
   The frames will be transmitted using port 4800, and is thus used as a filter. 
4. Run the two transmitters (sample-app-taprio).
5. Press enter on the terminal with the python script.
6. After the desired amount of samples has been acquired, close the python script using ctrl+c. 
   Then the remaining programs (tcpdump and sample-app-taprio) may be closed in a similar manner.
7. Copy and save the timestamps from the terminal with the python script. 