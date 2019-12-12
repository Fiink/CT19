import time
import os

cmdDel = "sudo tc qdisc del dev enp1s0 root"
cmdSet_P6 = "sudo tc qdisc replace dev enp4s0 parent root handle 100 mqprio num_tc 3 map 0 2 2 2 2 2 1 2 2 2 2 2 2 2 2 2 queues 1@0 1@1 2@2 hw 0"
cmdSet_Qav1 = "sudo tc qdisc replace dev enp4s0 parent 100:1 cbs idleslope 7808 sendslope -992192 hicredit 12 locredit -97 offload 1"
cmdSet_Qav2 = "sudo tc qdisc replace dev enp4s0 parent 100:1 cbs idleslope 42762 sendslope -992192 hicredit 12 locredit -97 offload 1"

os.system(cmdSet_p6)
os.system(cmdSet_Qav2)
print("Start parameters already set by simple_talker, press (enter) to shaper")
input(" ")

print("\ttStart\t\t\ttMid\t\t\ttEnd")
while(1):
    tStart = time.time()
    os.system(cmdSet_Qav2)
    tEnd = time.time()
    print("P6->P5:\t%.9f\t%.9f" % (tStart, tEnd))
    
    time.sleep(10)

    tStart = time.time()
    os.system(cmdSet_Qav1)
    tEnd = time.time()
    print("P5->P6:\t%.9f\t%.9f" % (tStart, tEnd))

    time.sleep(10)
