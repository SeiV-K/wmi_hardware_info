import wmi

print("++++++++++++ WMI BASIC SYSTEM INFORMATION ++++++++++++\n")

try:
    cpu_name = wmi.WMI().win32_Processor()[0].name
    cpu_serial = wmi.WMI().win32_Processor()[0].processorid
    print("---- CPU ----")
    print("CPU Name: %s\nCPU Serial: %s\n\n" % (cpu_name, cpu_serial))
except:
    print("---- CPU ----")
    print("CPU Exception Raised\n")

try:
    mobo_name = str(wmi.WMI().win32_BaseBoard()[0].manufacturer + " " + wmi.WMI().win32_BaseBoard()[0].product)
    mobo_serial = wmi.WMI().win32_BaseBoard()[0].serialnumber
    print("---- MotherBoard----")
    print("MOBO Name: %s\nMOBO Serial: %s\n\n" % (mobo_name, mobo_serial))
except:
    print("---- MotherBoard----")
    print("MotherBoard Exception Raised\n")

try:
    rams = wmi.WMI().win32_PhysicalMemory()
    print("---- RAM ----")
    for ram in rams:
        print("RAM Name: %s\nRAM Serial: %s\nDIMM: %s\n" % (ram.manufacturer, ram.partnumber, ram.DeviceLocator))
except:
    print("---- RAM ----")
    print("RAM Exception Raised\n")

try:
    mac = wmi.WMI().win32_NetworkAdapter()[1].macaddress
    print("\n---- MAC ----")
    print("MAC: %s\n\n" % mac)
except:
    print("\n---- MAC ----")
    print("MAC Exception Raised\n")

try:
    disks = wmi.WMI().win32_DiskDrive()
    print("---- DISK ----")
    for disk in disks:
        print("DISK Name: %s\nDISK Serial: %s\n" % (disk.caption, disk.serialnumber.strip()))
except:
    print("---- DISK ----")
    print("DISK Exception Raised\n")

try:
    gpu = wmi.WMI().win32_VideoController()[0]
    print("\n---- GPU ----")
    print("GPU Name: %s\nGPU PNP: %s" % (gpu.caption, gpu.PNPDeviceID))
except:
    print("\n---- GPU ----")
    print("GPU Exception Raised\n")

input()
