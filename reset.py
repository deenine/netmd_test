#!/usr/bin/python
from __future__ import print_function
from builtins import input
import usb1
import libnetmd
import time


def main(bus=None, device_address=None, show_uuids=False):
    context = usb1.LibUSBContext()
    netmd_devs = list(libnetmd.iterdevices(context, bus=bus, device_address=device_address))
    if len(netmd_devs):
        print('Found %d netmd_devs' % (len(netmd_devs)))
        for md in netmd_devs:
            testMD(md, show_uuids)
    else:
        count = 0
        devs = list(context.getDeviceList())
        print("No Known NetMD Devices Found. Currently connected USB Devices:")
        while count < len(devs):
            print ("%d: %s" % (count, devs[count]))
            count += 1
        print("Enter device number to attempt netmd test, any other key to terminate")
        try:
            selection = eval(input())
            if type(selection) == type(int()):
                if selection < len(devs):
                    print("attempting to test %s" % devs[selection])
                    for md in libnetmd.iterdevices(context, bus=devs[selection].getBusNumber(), device_address=devs[selection].getDeviceAddress(), jfdi=True):
                        testMD(md, show_uuids)
        except:
            exit(0)

def testMD(md, show_uuids):
    def reprDiscFlags(flags):
        result = []
        if flags & libnetmd.DISC_FLAG_WRITABLE:
            result.append('writable media')
        if flags & libnetmd.DISC_FLAG_WRITE_PROTECTED:
            result.append('write-protected')
        return result

    def timeToFrames(time_tuple):
        assert len(time_tuple) == 4
        return (((time_tuple[0] * 60) + time_tuple[1]) * 60 + time_tuple[2]) \
            * 512 + time_tuple[3]

    md_iface = libnetmd.NetMDInterface(md)


    try:
        print('Leave Secure Session', end=' ')
        md_iface.leaveSecureSession()
        print('....OK')
    except Exception as err:
        print('....FAIL')
        print('Error: {0}'.format(err))

    try:
        print('Release Device', end=' ')
        md_iface.release()
        print('....OK')
    except Exception as err:
        print('....FAIL')
        print('Error: {0}'.format(err))












#    print('syncTOC')
#    md_iface.syncTOC()
#    print('cacheTOC')
#    md_iface.cacheTOC()

    # print('erase track')
    # md_iface.eraseTrack(0)
    # print 'eraseDisc'
    # md_iface.eraseDisc()





#    print('set disc title')
#    md_iface.setDiscTitle('Test 780 - by python')


    # requires handshake:
    # md_iface.getOperatingStatus()
    # md_iface.setDiscTitle("Test 780")


def ls_usb ():
#            return (device.getVendorID(), device.getProductID()) in filter_set
    context = usb1.LibUSBContext()
    for device in context.getDeviceList():
            print(device)





if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-b', '--bus')
    parser.add_option('-d', '--device')
    parser.add_option('-u', '--uuids', action="store_true")
    (options, args) = parser.parse_args()
    assert len(args) == 0

    main(bus=options.bus, device_address=options.device,
         show_uuids=options.uuids)
