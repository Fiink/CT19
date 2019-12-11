SETUP:
Connect two computers, each equipped with the Intel I210 network card.

STEPS:
1. Ensure the gPTP is working as intended, and that ptp4l and phc2sys is running correctly using the
   setup_sync.sh script provided by IoTG. 
2. On the receiver-computer, prepare the receiver using the sample-app-taprio program provided by IoTG:
	sudo ./sample-app-taprio -i enp1s0 -x 2 -q "7 3 0" -y 1 > <FILEPATH>.txt
   replace <FILEPATH> with the path to the output file. This will contain all the desired data.
3. Prepare the transmitters using the program sample-app-taprio provided by IoTG. 
   To do so, open three terminals on the transmitter, and enter (but do not execute) the following:
   Terminal 1:
	sudo ./sample-app-taprio -i enp1s0 -c 169.254.0.2 -x 1 -w tsn_prio6.cfg -B base_time
   Terminal 2: 
	sudo ./sample-app-taprio -i enp1s0 -c 169.254.0.2 -x 1 -w tsn_prio3.cfg -B base_time
   Terminal 3: 
	sudo ./sample-app-taprio -i enp1s0 -c 169.254.0.2 -x 1 -w tsn_prio0.cfg -B base_time
4. Run the following command in a new terminal on the transmitter to configure the TAS:
	sudo python scheduler.py -i enp1s0 -q queue.cfg -e 30 -g gates.sched
5. Execute the commands prepared in step 2.
6. After sufficient data has been gathered, close the receiver-program using CTRL+C.
   Afterwards, close the transmitters in the same manner.