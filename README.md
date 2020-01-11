# RAK811_Utils
## utilities for RAK811
Simple Python Script to quickly configure RAK811 Lora Module in windows.

Usage: You only have to specify two arguments:
  - Serial port for module communication in format <COMX> where x is serial port number.
  - File with lora configurations
Example: ./rak811Configure.py COM2 configurations.txt
### The configuration file has the following format:
dev_eui=xxxxxxxxxxxxxxxx

app_eui=xxxxxxxxxxxxxxxx

app_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

### Notes:
Requirements: PySerial module

the script uses the new RUI Firmware AT Commands
