from lib_wdckit import WDCKit
from terminaltables import SingleTable
import sys

wdckit = WDCKit()

duts = wdckit.get_duts()

def select_dut():
    print("Following DUTs are detected:")
    data = [["DUT", "Device", "Model Number", "Serial Number", "Boot Device"]]
    for dut in duts:
        data.append([dut.DUT, dut.Device, dut.ModelNumber, dut.SerialNumber, dut.BootDevice])
    table = SingleTable(data)
    print(table.table)
    return input("Select the DUT (disk0/disk1): ")

selected_dut = select_dut()
number_of_cycles = int(input("Enter the number of cycles: "))

for cycle in range(number_of_cycles):
    print(f"Cycle: {cycle}")
    result = True
    for ps in range(1,6):
        print(f"Setting Power State: PS{ps}")
        set_status = wdckit.set_power_state(selected_dut, ps)
        if not set_status:
            raise Exception("Unable to change Power State using SetFeature")
        power_state = wdckit.get_power_state(selected_dut)
        result = True if power_state == ps else False
        print(f"Current Power State: PS{power_state}\tTest Status: {'Pass' if result == True else 'Fail'}")
        if result == False:
            break
    if not result:
        break

sys.exit()

