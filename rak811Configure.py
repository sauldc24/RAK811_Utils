import sys
import serial
import time

def main():
    if len(sys.argv) == 3:
        loraParams = {}

        with open(sys.argv[2], "r") as file:
            for line in file.readlines():
                line = line.strip()
                parameter = line.partition("=")
                loraParams[parameter[0]] = parameter[2]
            print(f"the LoRa parameters to be configured are: {loraParams}")

        with serial.Serial(sys.argv[1], 115200, timeout = 3) as mySerial:
            def sendcommand(command):
                mySerial.write(command.encode("utf-8"))
                time.sleep(.2)
                while mySerial.inWaiting() > 0:
                    time.sleep(.2)
                    print(mySerial.readline())
            command = "\r\n"
            sendcommand(command)
            for parameterKey, parameterValue in loraParams.items():
                command = f"at+set_config=lora:{parameterKey}:{parameterValue}\r\n"
                sendcommand(command)
            command = "at+join\r\n"
            sendcommand(command)
            command = "at+get_config=lora:status\r\n"
            sendcommand(command)

    elif len(sys.argv) == 2:
        with serial.Serial(sys.argv[1], 115200, timeout = 3) as mySerial:
            mySerial.write(b"at+get_config=lora:status\r\n")
            time.sleep(.2)
            while mySerial.inWaiting() > 0:
                time.sleep(.2)
                print(mySerial.readline())

    else:
        print("usage: rak811Configure port configurationFile")


if __name__ == "__main__":
    main()
