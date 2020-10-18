# NetMD Tester

This is an app to test a series of commands against a NetMD device. In the event of a failure, debug information is output.

DO NOT RUN TEST ON IMPORTANT MINIDISCS. This app does not test destructive functions, like erase tracks or discs, or setting titles, but it does test moving tracks. It is suggested that you create a test disc by entering a blank disc, press record, then creating some track marks by pressing record or trackmark, then stop and eject the disc to write the TOC.

useage: `python netmd_test.py`

This is only compatible with python2, so if python2 is not your default python, you may need to specify the version with `python2 netmd_test.py` or `C:\<path to python2>\Python.exe`

Succesful run:
```
$ python netmd_test.py 
Found NetMD: Bus 020 Device 022: ID 054c:0081 Sony Net MD
Found 1 netmd_devs
Acquire Device ....OK
Get Status ....OK
Get Disc Flags ....OK
Get Disc Title ....OK
Test Disc

...etc...
```

If no known netmd devices are found, this tool will display a list of netmd devices and prompt the user to select a device:
```
$ python netmd_test.py
No Known NetMD Devices Found. Currently connected USB Devices:
0: Bus 020 Device 013: ID 054c:0081 Sony Net MD
1: Bus 020 Device 012: ID 0781:5567 SanDisk Cruzer Blade
Enter device number to attempt netmd test, any other key to terminate
0
attempting to test Bus 020 Device 013: ID 054c:0081 Sony Net MD
Acquire Device ....OK
Get Status ....OK
Get Disc Flags ....OK
Get Disc Title ....OK

...etc...
```

If a test fails, it will display the usb command and the response from the device:
```
Found NetMD: Bus 020 Device 011: ID 054c:0081 Sony Net MD
Found 1 netmd_devs
Acquire Device ....OK
Get Status ....FAIL
Error: Rejected
out -> 18 09 80 01 02 30 88 00 00 30 88 04 00 ff 00 00 00 00 00
in <- 18 09 80 01 02 30 88 00 00 30 88 04 00 ff 00 00 00 00 00
netmd status: 0A

Get Disc Flags ....OK
Get Disc Title ....OK
Test Disc
Get Disc Capacity ....FAIL
Error: Rejected
out -> 18 06 02 10 10 00 30 80 03 00 ff 00 00 00 00 00
in <- 18 06 02 10 10 00 30 80 03 00 ff 00 00 00 00 00
netmd status: 0A
```

In the event that a test fails, try unplugging the device, turning it off and on again, then replugging it and re-run the test. If it is a bookshelf or deck, remember to put it into netmd mode, and if it is a Hi-MD device, make sure the disk is formatted as MD not Hi-MD. 

If the test fails again, please open an issue on this repository and post the output of the tool, along with the model of the device.


# Install

Make sure you have git installed: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Open a terminal.

Clone this repo:
`git clone https://github.com/deenine/netmd_test`

## OSX

Change into cloned directory:
`cd netmd_test`

Run the test tool:
`python2 netmd_test.py`


## Windows

Windows install sucks, sorry.

Install python2: https://www.python.org/downloads/release/python-2718/

If you are using 64-bit Windows, copy `libusb-1.0.dll` from the directory where the tool was cloned, to the python2 install directory (e.g. `C:\Python27`), or if you are using 32-bit Windows copy `libusb-1.0-32.dll` instead and rename it to `libusb-1.0.dll`

Open the windows system environment settings and make sure that the python directory above is on the system PATH (not the user path).

Open a terminal in the directory you cloned the tool to, and run the tool:
`python2 netmd_test.py`
