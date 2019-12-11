SETUP:
Connect two computers, each equipped with the Intel I210 network card.


STEPS:
1. Start the GM ptp using the script provided by IoTG.
2. Run the test_sync.sh script on the slave computer, using the following command:
	sudo bash ./test_sync.sh -i enp1s0 -b boardB -f <FILEPATH>.txt

Replace enp1s0 with the device name of the network card.
<FILEPATH> writes the output of ptp4l to a file at the specified path, which contains the desired information.