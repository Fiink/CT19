import time
import os

cmdDel = "sudo tc qdisc del dev enp1s0 root"
cmdSet_P6 = "sudo tc -d qdisc replace dev enp1s0 parent root handle 100 taprio num_tc 4 map 2 2 2 2 2 0 1 3 3 3 3 3 3 3 3 3 queues 1@0 1@1 1@2 1@3 sched-entry S 0xA 20000000  sched-entry S 0xA 5000000  clockid CLOCK_TAI"
cmdSet_P5 = "sudo tc -d qdisc replace dev enp1s0 parent root handle 100 taprio num_tc 4 map 2 2 2 2 2 0 1 3 3 3 3 3 3 3 3 3 queues 1@0 1@1 1@2 1@3 sched-entry S 0x9 20000000  sched-entry S 0x9 5000000  clockid CLOCK_TAI"

print("Setting initial prio 6...")
os.system(cmdDel)
os.system(cmdSet_P6)
print("Finished. Start transmitters, and press enter.")
input(" ")

print("\ttStart\t\t\ttMid\t\t\ttEnd")
while(1):
    tStart = time.time()
    os.system(cmdDel)
    tMid = time.time()
    os.system(cmdSet_P5)
    tEnd = time.time()
    print("P6->P5:\t%.9f\t%.9f\t%.9f" % (tStart, tMid, tEnd))
    
    time.sleep(2.5)

    tStart = time.time()
    os.system(cmdDel)
    tMid = time.time()
    os.system(cmdSet_P6)
    tEnd = time.time()
    print("P5->P6:\t%.9f\t%.9f\t%.9f" % (tStart, tMid, tEnd))

    time.sleep(2.5)