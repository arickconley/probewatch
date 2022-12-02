# ProbeWatch

Quick and easy Python script to monitor for WiFi probe request frames. It attempts to look up the manufacturer of the device by the MAC address.

![image](https://user-images.githubusercontent.com/2053328/205366842-7125c85f-ddcc-4733-b152-d86c068316d9.png)


## CLI

#### First run
Update the MAC address database by running:
```
python probewatch.py -u
```

#### Help
Run with:
```
python probewatch.py -h
	usage: probewatch.py [-h] [-u] [-i INTERFACE]

	options:
  	-h, --help            show this help message and exit
  	-u, --update          Update MAC address database
  	-i INTERFACE, --interface INTERFACE
                        Interface to use. Must be in monitor mode

```
