import argparse
import math
import sys

from pythonosc import dispatcher
from pythonosc import osc_server

def changeSignal(tmp) : 
	f = open("Dats.txt", 'w')
	f.write(str(tmp))
	f.close()

def eeg_handler1(unused_addr, args, ch1):
	print("Blink: ", ch1)
	changeSignal("a")

def eeg_handler2(unused_addr, args, ch1):
	print("Jaw Clench: ", ch1)
	changeSignal("b")

def eeg_handler3(unused_addr, args, ch1):
	print("Alpha: ", ch1 * 100)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="192.168.0.223", help="The ip to listen on")
    parser.add_argument("--port", type=int, default=5000, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    dispatcher.map("/muse/elements/blink", eeg_handler1, "Blink")
    dispatcher.map("/muse/elements/jaw_clench", eeg_handler2,"Jaw")
    dispatcher.map("/muse/elements/alpha_absolute", eeg_handler3, "Alpha")

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()