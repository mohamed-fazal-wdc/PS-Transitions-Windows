import os
import fnmatch
import re
import subprocess
from typing import List
import logging
import json
import io

WDCKIT_LOG_FILE = 'runtime_logs.txt'

# Turns a dictionary into a class
class Dict2Class(object):
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])


class WDCKitNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class WDCKit:
    def __init__(self, accept_terms: bool = True, retain_logs: bool = False) -> None:
        self.exec_path = self.__find_wdckit()
        self.retain_logs = retain_logs
        self.version = "1.0.1"
        if accept_terms:
            self.__accept_terms()

    def log(self, log_text):
        with io.open(WDCKIT_LOG_FILE, 'a') as file:
            file.write(log_text)

    def __execute(self, command):
        logging.debug(f'Executing: {command}')
        out, err = subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=1
        ).communicate()
        try:
            for line in out.decode('unicode_escape').replace('\r\n\r\n', '\r\n').replace('\r\n', '\n').strip().split('\n'):
                logging.debug(line)
        except:
            for line in out.decode().replace('\r\n\r\n', '\r\n').replace('\r\n', '\n').strip().split('\n'):
                logging.debug(line)
        return out

    def __find_wdckit(self) -> str:
        matches = []
        for root, dirnames, filenames in os.walk("."):
            for filename in fnmatch.filter(filenames, 'wdckit.exe'):
                matches.append(os.path.join(root, filename))

        if len(matches) > 0:
            return matches[0]
        raise WDCKitNotFound('Unable to find path to wdckit.exe')

    def __accept_terms(self):
        self.exec_path
        # return True if file exists
        self.license_file_path = os.path.join(
            "\\".join(self.exec_path.split('\\')[:-1]), ".wdckit_lic")
        if os.path.exists(self.license_file_path):
            logging.info("WDCKit licenses already accepted! ")
        else:
            logging.info("WDCKit licenses doesn't exist! Accepting licenses.")
            with io.open(self.license_file_path, 'w') as stream:
                stream.write('1\n')
            return True

    def __parse_results(self, output: bytes) -> dict:
        try:
            op = json.loads("".join(output.decode().replace("\\","/").replace("//","/").strip().replace(" ", "").split('\r\n')[5:]))['wdckit']['results']
        except:
            op = json.loads("".join(output.decode('unicode_escape').replace("\\","/").replace("//","/").strip().replace(" ", "").split('\r\n')[5:]))['wdckit']['results']
        return op

    def get_duts(self):
        command = f'{self.exec_path} s --output json'
        self.log(f"Executing command: {command}")
        output = self.__execute(command)
        _duts = self.__parse_results(output)
        duts = []
        for dut in _duts:
            duts.append(Dict2Class(dut))
        return duts

    def get_smart(self, device: str):
        command = f'{self.exec_path} getsmart {device} --output json'
        self.log(f"Executing command: {command}")
        output = self.__execute(command)
        return self.__parse_results(output)

    def get_power_state(self, device: str) -> int:
        command = f'{self.exec_path} getfeature {device} -f 2'
        self.log(f"Executing command: {command}")
        output = self.__execute(command)
        self.log(output.decode())
        return int(re.findall('Power State\s*([0-9])', output.decode(), re.MULTILINE)[0])
    
    def set_power_state(self, device: str, power_state: int) -> bool:
        command = f'{self.exec_path} setfeature {device} -f 2 -v {power_state} -m'
        self.log(f"Executing command: {command}")
        output = self.__execute(command)
        self.log(output.decode())
        return True if "Success" in output.decode() else False


if __name__ == "__main__":
    import logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s | %(levelname)s | %(message)s',
        # datefmt='%d-%b-%y %H:%M:%S'
        datefmt='%H:%M:%S'
    )
    wdckit = WDCKit()
    try:
        logging.info(f'Found wdckit.exe at {wdckit.exec_path}')
    except WDCKitNotFound as e:
        logging.error(e)
    # print(wdckit.get_duts())
