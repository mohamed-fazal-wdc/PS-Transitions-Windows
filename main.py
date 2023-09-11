from lib_wdckit import WDCKit
from terminaltables import SingleTable

wdckit = WDCKit()

duts = wdckit.get_duts()

def select_dut():
    print("Following DUTs are detected:")
    data = [["DUT", "Device", "Model Number", "Serial Number"]]
    for dut in duts:
        data.append([dut.DUT, dut.Device, dut.ModelNumber, dut.SerialNumber])
    table = SingleTable(data)
    print(table.table)
    return input("Select the DUT (disk0/disk1): ")

selected_dut = select_dut()
power_state = wdckit.get_power_state(selected_dut)
print(f"Current Power State: PS{power_state}")