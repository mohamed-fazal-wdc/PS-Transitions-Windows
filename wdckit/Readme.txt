//=============================================================================
// Copyright (C) 2019-2023 Western Digital Technologies, Inc.
//
// This code is CONFIDENTIAL and a TRADE SECRET of Western Digital
// Technologies, Inc. ('WD'). This code is protected
// under copyright laws as an unpublished work of WD. Notice is
// for informational purposes only and does not imply publication.
//
// The receipt or possession of this code does not convey any rights to
// reproduce or disclose its contents, or to manufacture, use, or sell
// anything that it may describe, in whole or in part, without the
// specific written consent of WD. Any reproduction or distribution
// of this code without the express written consent of WD is strictly
// prohibited, is a violation of the copyright laws, and may subject you
// to criminal prosecution.
//=============================================================================

Name
  wdckit 

Copyright
  Copyright (C) 2019-2023 Western Digital Technologies, Inc. 

Description
  wdckit is a command line utility to perform various operations on one or 
  more supported devices. 
  Any of the wdckit commands may be executed as a one time command from the 
  terminal or from within the interactive session. From the interactive 
  sessions, enter 'h' for help or 'q' to quit. 
  Windows: Administrative privilege is required to execute the tool. 
  Linux: Root authority is required to execute the tool. 

Linux Install Instructions:
  RPM
      rpm -Uvh wdckit-<version>.<arch>.rpm 
  Debian
      sudo dpkg -i wdckit_<version>_<arch>.deb 
  Local
      tar xzvf wdckit-<version>-<arch>.tar.gz 

Windows Install Instructions
  Run the wdckit-<version>.win<32|64>.exe installer. From the installed 
  directory, run wdckit.exe with Administrator privileges. 

Usage
  description
      wdckit is a command line utility to perform various operations on one 
      or more supported devices. 
      Any of the wdckit commands may be executed as a one time command from 
      the terminal or from within the interactive session. From the 
      interactive sessions, enter 'h' for help or 'q' to quit. 
      Windows: Administrative privilege is required to execute the tool. 
      Linux: Root authority is required to execute the tool. 
  options
      wdckit [ahci|aop|assert|atasecurity|debug|do-not-operate|erase|e| 
      errors|eula|format|fsflush|getdui|geteyediagram|getfeature|getlog| 
      getpe|getpersistentevent|getsmart|getsmr|h|help|hmb|i|idd|l|logdump| 
      ns-attach|ns-create|ns-delete|ns-detach|nsze|power|q|quit|rdp|reset| 
      sasphypower|scsipt|security|securityprofile|selftest|serverconfig| 
      setfeature|sethctmtemps|setthrottlingtemp|s|show|standby|u|update|v| 
      version|vuc|writelog|zns|zone] 

ahci usage:
  restrictions
      This task is only valid in Linux.
      This task is only valid for SATA targets.
      This task is only valid for WDC targets.
       
  description
      Gets contents of AHCI Configuration Registers. 
      wdckit ahci [<devList> ...|--model <model number> ...|--serial <serial 
      number> ...] [--trace|--trace-with-scan|--no-trace] [-R <filename>] 
      [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          Device name(s) to execute ahci command. Use 'all' to select all 
          devices. For example, in Windows, it will be shown in Disk 
          Management as Disk0, Disk1, etc. In Linux it will be /dev/nvme0, 
          /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices can be 
          repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

aop usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for WDC targets.
      This task is only valid for SATA targets.
      This task is only valid for ATA devices that support 48-bit LBAs.
       
  description
      Adjust OverProvisioning (AOP) of the device. Supported sub-cmds: get, 
      set and reset. NOTE: Per the ATA specification, a power cycle shall be 
      required between each AOP change. 
      wdckit aop <<devList> ...|--model <model number> ...|--serial <serial 
      number> ...> <-g|-s <new max lba>|-r> [--trace|--trace-with-scan| 
      --no-trace] [-f] [-R <filename>] [--no-win-disk] [--no-win-ctrl-hdc] 
      [--no-win-ctrl-scsi] [--no-win-csmi] [--no-win-rste] 
      [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] [--no-linux-nvme] 
      [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] 
      [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level <silent|error| 
      info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute aop command. Use 'all' to 
          select all devices. For example, in Windows, it will be shown in 
          Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -g,  --get
          (OR required)  Gets the actual user addressable max LBA. 
      -s <new max lba>,  --set <new max lba>
          (OR required)  Sets the user addressable max LBA to a new 
          supported. 
      -r,  --reset
          (OR required)  Resets the user addressable max LBA to actual 
          value. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -f,  --force
          Force the overprovisioning without asking for user confirmation. 
          Valid for only the set or reset option. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

assert usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for NVMe targets.
      This task is only valid for WD or HGST targets.
       
  description
      Check, clear or force a device asserts. 
      wdckit assert <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> <-g|-c> [--trace|--trace-with-scan|--no-trace] 
      [-f] [-m] [--nsid <value>] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute assert command. Use 'all' 
          to select all devices. For example, in Windows, it will be shown 
          in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -g,  --get
          (OR required)  Check for device asserts. 
      -c,  --clear
          (OR required)  Clear device assert. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -f,  --force
          Send a clear device assert command even if an assert is not 
          present. 
      -m,  --mirror
          Uses the NVMe mirror command instead of the NVMe standard command. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

atasecurity usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for SATA targets.
      This task is only valid for WDC targets.
       
  description
      This command is used to set, disable, freeze or unlock ATA security 
      using User or Master password with High or Maximum security for ATA 
      devices. NOTE: Many modern BIOSes will issue an ATA security freeze 
      lock which blocks all subsequent ATA security commands until the next 
      power cycle. Use 'idd' to confirm. The security frozen is reported at 
      word 128, bit 3. 
      wdckit atasecurity <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> <-s|-d|-f|-U> [-u|-m] [-H|-M] [--trace| 
      --trace-with-scan|--no-trace] [-P <password>] [-R <filename>] 
      [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute atasecurity command. Use 
          'all' to select all devices. For example, in Windows, it will be 
          shown in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -s,  --set
          (OR required)  This option is used to enable ATA security by 
          setting the User password or Master password. 
      -d,  --disable
          (OR required)  This option is used to disable ATA security by 
          using the User or Master password. 
      -f,  --freeze
          (OR required)  This option is used to freeze all changes to ATA 
          security options on the drive. 
      -U,  --unlock
          (OR required)  This option is used to unlock a security locked 
          drive on which ATA security is enabled. 
      -u,  --userpassword
          This option is used if User Password is provided in the --password 
          option to set, disable or unlock ATA security. 
      -m,  --masterpassword
          This option is used if Master Password is provided in the 
          --password option to set, disable or unlock ATA security. 
      -H,  --high
          This option is used to set Security Mode to High when setting the 
          User password. 
      -M,  --maximum
          This option is used to set Security Mode to Maximum when setting 
          the User password. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -P <password>,  --password <password>
          This option is used for providing the password string. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

debug usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for NVMe targets.
      This task is only valid for SanDisk targets.
       
  description
      Send vendor unique command for debugging operations for supported NVMe 
      devices. 
      wdckit debug <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> <-k <value>|-p <file>> [--trace|--trace-with-scan| 
      --no-trace] -f <value> [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute debug command. Use 'all' 
          to select all devices. For example, in Windows, it will be shown 
          in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -k <value>,  --key <value>
          (OR required)  Private key code required for FW to accept this 
          command. 
      -p <file>,  --payload <file>
          (OR required)  Private file containing 4-byte aligned data 
          (maximum of 512 bytes). 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -f <value>,  --flag <value>
          (required) Value for the general flag. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

do-not-operate usage:
  description
      Add a device to the list of do not operate devices. Operations shall 
      ignore for each device found in the do not operate list. 
      wdckit do-not-operate <-s <serial number> ...|-d|-c> [--trace| 
      --trace-with-scan|--no-trace] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      -s <serial number>,  --serial <serial number>  (accepted multiple times)
          (OR required)  Add this device to the Do Not Operate list. 
      -d,  --display
          (OR required)  Print a list of all devices from the Do Not Operate 
          list. 
      -c,  --clear
          (OR required)  Clear all devices from the Do Not Operate list. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

erase usage:
  restrictions
      This task is only valid for an actual target.
      This task is not allowed on a boot device.
      This task is only valid for non-RAID devices.
      This task is only valid for WDC targets.
       
  description
      This issues a secure erases, a trim of all user data or a sanitize 
      command the device. Since this is a destructive operation, by default, 
      this tool prompts for user confirmation before execution of this 
      operation. To force the operation, use -f (--force). Note: For Windows 
      with the NVMe inbox driver, erase via Sanitize must be run from 
      Windows PE. The erase command can not be issued to the boot drive. If 
      no sub-option is specified, by default all sub-options (except -o 
      (--overwrite)) will be executed until the device is successfully 
      erased, trimmed or sanitized. 
      wdckit erase <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> [-n|-e|-t|-B|-o <pattern>|-F <filename>|-c|-x| 
      --table|-p|-s] [--progress-bar|--simple-progress|--no-progress] 
      [--trace|--trace-with-scan|--no-trace] [-b] [-l <1|2|3|4>] [-C <1-31>] 
      [-i] [--nsid <value>] [-f] [--no-sanitize-status] [-R <filename>] 
      [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute erase command. Use 'all' 
          to select all devices. For example, in Windows, it will be shown 
          in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -n,  --normal
          Performs a normal Security Erase operation on the device list. 
          Supported on only ATA devices. 
      -e,  --enhanced
          Performs an enhanced Security Erase operation on the device list. 
          Supported on only ATA devices. 
      -t,  --trim
          Performs a trim operation from LBA 0 to the Maximum User 
          Addressable LBA on the device list. 
      -B,  --blockerase
          Performs a Sanitize Block Erase operation on the device list. 
      -o <pattern>,  --overwrite <pattern>
          Performs a Sanitize Overwrite operation on the device list. The 
          pattern is this 32-bit value. To specify length of pattern in 
          bytes, use -l|--length. 
      -F <filename>,  --file <filename>
          Performs a Sanitize Overwrite operation on the device list. The 
          pattern source is from this file. 
      -c,  --crypto
          Performs a Sanitize Crypto Scramble operation on the device list. 
      -x,  --exit-failure-mode
          Performs a Sanitize Exit Failure Mode operation on the device list 
          (NVMe & SCSI only) or clear sanitize errors (ATA only). 
      --table
          Erase the device partition table. 
      -p,  --progress
          Query the progress of an erase operation. 
      -s,  --show-support
          Show the erase methods that are supported on the device. No erase 
          shall be performed. 
      --progress-bar
          Display a full screen progress bar screen. 
      --simple-progress
          Prevent the display of the progress bar screen, useful when 
          running commands from a script. 
      --no-progress
          No progress display. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -b,  --blocked
          For a Sanitize operation, waits for the operation to complete. 
      -l <1|2|3|4>,  --length <1|2|3|4>
          Specify the length of the pattern (1-4) in bytes. This argument is 
          only valid for -o|--overwrite. If not specified, default is 4. 
      -C <1-31>,  --overwrite-count <1-31>
          Specify the number of Sanitize Overwrite passes to be perform. 
          This argument is only valid with -o|--overwrite or -F|--file. 
      -i,  --invert
          Specify that the pattern shall be inverted after every pass. This 
          argument is only valid with -o|--overwrite or -F|--file. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -f,  --force
          Force the erase operation without asking for user confirmation. 
      --no-sanitize-status
          Do not check ATA sanitize status, which on some systems, may not 
          operate correctly. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

errors usage:
  description
      List some or all application status codes and messages. 
      wdckit errors [<error-code> ...] [-n|-s|-c|-r <error,exit> ...] 
      [--trace|--trace-with-scan|--no-trace] [-e <exit code>] [-S] [-R 
      <filename>] [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <error-code>  (accepted multiple times)
          Show message for this error code. 
      -n,  --nvme
          Show an NVMe status command type/status command code. This 
          error-code is a 12-bit value, where SCT = bits 11:8 and SC = bits 
          7:0. 
      -s,  --status-field
          Show value as NVMe status field (SF). This error-code is expected 
          to be a 16-bit value. 
      -c,  --clear
          Clear all exit codes overrides  (IE reset to default). 
      -r <error,exit>,  --replace <error,exit>  (accepted multiple times)
          Replace the exit code for the given error code. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -e <exit code>,  --exit-code <exit code>
          Filter error codes to only this exit code. 
      -S,  --sort-exit-code
          Show all application errors, and sort then by the exit code value. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

eula usage:
  description
      Show the End User License Agreement (EULA). 
      wdckit eula [-a|-3] [-h] 
       
  options:
      -a,  --exhibit-a
          Show EULA Exhibit A 
      -3,  --third-party
          Show third party notices. 
      -h,  --help
          Display help and exit. 

format usage:
  restrictions
      This task is only valid for an actual target.
      This task is not allowed on a boot device.
      This task is only valid for WDC targets.
      This task is only valid in Windows PE with NVMe devices when connected via the inbox or Intel RST driver.
      This task requires the device to be ready.
       
  description
      Performs a format on a SCSI/ATA or NVMe device. Notes: NVMe format is 
      supported in only Linux or Windows PE with the inbox driver. ATA 
      format is only supported on L-H and L-W products. 
      wdckit format <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> <-l <lba format>|-b <bytes>> [--progress-bar| 
      --simple-progress] [--trace|--trace-with-scan|--no-trace] [-s <0-7>] 
      [--nsid <value>] [-n <number of blocks>] [--merge] [--fastformat] [-c] 
      [-p <protection type>] [--danger-zone] [--timeout-seconds <seconds>] 
      [--no-sanitize-status] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute format command. Use 'all' 
          to select all devices. For example, in Windows, it will be shown 
          in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -l <lba format>,  --lbaformat <lba format>
          (OR required)  Specify the LBA format number for an NVMe device. 
          Not applicable for SCSI/ATA devices. 
      -b <bytes>,  --blocksize <bytes>
          (OR required)  Specify the block size, in bytes. Valid values for 
          ATA devices: 512, 4096. Valid values for SCSI devices: 512, 520, 
          528, 4096, 4112, 4160, 4224. Valid values for NVMe devices are 
          reported in identify namespace data. 
      --progress-bar
          Display a full screen progress bar screen. 
      --simple-progress
          Prevent the display of the progress bar screen, useful when 
          running commands from a script. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -s <0-7>,  --ses <0-7>
          Specify the Secure Erase Settings (SES) value for an NVMe device. 
          Defaults to 1 (0 = no secure erasure; 1 = user data erasure; 2 = 
          cryptographic erasure; 3-7 = reserved). Not applicable for 
          SCSI/ATA devices. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -n <number of blocks>,  --numblocks <number of blocks>
          Specify number of blocks to format for SCSI/ATA devices. Not 
          applicable for NVMe devices. Default: will format to maximum 
          number of blocks supported by the device. 
      --merge
          Merge G-List and P-List for SCSI/ATA devices. Not applicable for 
          NVMe devices. 
      --fastformat
          Set Fast Format for SCSI/ATA devices. Not applicable for NVMe 
          devices. 
      -c,  --media-compatibility-check
          Perform media compatibility check for SCSI/ATA devices. Not 
          applicable for NVMe devices. 
      -p <protection type>,  --protection <protection type>
          Specify a type of Protection Information (0|1|2|3) for SCSI/ATA 
          devices. Not applicable for NVMe devices. 
      --danger-zone
          Flag tells the application that you know you are going to destroy 
          your data with this command and will not prompt the user. 
      --timeout-seconds <seconds>
          Timeout value, in seconds. Allowed range is 30 seconds to 604800 
          (1 week). 
      --no-sanitize-status
          Do not check ATA sanitize status, which on some systems, may not 
          operate correctly. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

fsflush usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for WDC targets.
       
  description
      Performs a file system flush on device. 
      wdckit fsflush <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> [--trace|--trace-with-scan|--no-trace] [-R 
      <filename>] [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute fsflush command. Use 
          'all' to select all devices. For example, in Windows, it will be 
          shown in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

getdui usage:
  restrictions
      This task is only valid for an actual NVMe device or file target.
      This task is only valid for SanDisk targets.
       
  description
      Retrieves the vendor specific DUI (Device Unit Information) log from 
      supported WDC devices. The log is saved in a file named {serial 
      number}_{DDMMYYYY_HHMMSS}_dui_2.17.0.0.bin. 
      wdckit getdui <<devList|filename> ...|--model <model number> ...| 
      --serial <serial number> ...> [--progress-bar|--simple-progress| 
      --no-progress] [--trace|--trace-with-scan|--no-trace] [-S] [-g <type[, 
      max size]> ...] [-e <type[,max size]> ...] [-d <1|2|3|4>] [-x 
      <transfer size>] [-s <path>] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList|filename>  (accepted multiple times)
          (OR required)  Device or file name(s) to execute getdui command. 
          Use 'all' to select all devices. For example, in Windows, it will 
          be shown in Disk Management as Disk0, Disk1, etc. In Linux it will 
          be /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple 
          devices can be repeated by separating each device with a space. 
          See also do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --progress-bar
          Display a full screen progress bar screen. 
      --simple-progress
          Prevent the display of the progress bar screen, useful when 
          running commands from a script. 
      --no-progress
          No progress display. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -S,  --show-header
          Show header - will not collect DUI log. 
      -g <type[,max size]>,  --get-type <type[,max size]>  (accepted multiple times)
          Specify section type to extract, with an optional maximum size 
          limit in bytes. 
      -e <type[,max size]>,  --exclude-type <type[,max size]>  (accepted multiple times)
          Specify section type to exclude. If an optional maximum size limit, 
          in bytes, is specified, then this section type will be read up to 
          the specified limit. 
      -d <1|2|3|4>,  --data-area <1|2|3|4>
          Data area to retrieve up to. 
      -x <transfer size>,  --xfer <transfer size>
          Specify the maximum size, in bytes, to transfer per command. This 
          value must be a multiple of 512. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

geteyediagram usage:
  restrictions
      This task is only valid for an actual NVMe device, an actual HGST device or file target.
      This task is only valid for WDC targets.
       
  description
      Retrieves the vendor specific Eye Diagram (Eye Surf) log from 
      supported devices. If saving the raw data, the filename shall be 
      {serial number}_{DDMMYYYY_HHMMSS}_eye_2.17.0.0.bin. 
      wdckit geteyediagram <<devList|filename> ...|--model <model number> 
      ...|--serial <serial number> ...> [-r|-s <path>|-f <filename>] 
      [--trace|--trace-with-scan|--no-trace] [-m] [--nsid <value>] [--phy-id 
      <0|1>] [--bit-depth <value>] [--phase-low <phase value>] [--phase-high 
      <phase value>] [--phase-step <positive value>] [--voltage-low <voltage 
      value>] [--voltage-high <voltage value>] [--voltage-step <positive 
      value>] [--snapshot] [-x <bytes>] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList|filename>  (accepted multiple times)
          (OR required)  Device or file name(s) to execute geteyediagram 
          command. Use 'all' to select all devices. For example, in Windows, 
          it will be shown in Disk Management as Disk0, Disk1, etc. In Linux 
          it will be /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. 
          Multiple devices can be repeated by separating each device with a 
          space. See also do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -r,  --raw
          Dump the raw buffer. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      -f <filename>,  --file <filename>
          Saves the device output to the file specified. Can only be used 
          with a single device. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -m,  --mirror
          Uses the NVMe mirror command instead of the NVMe standard command. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      --phy-id <0|1>
          Specify the port number (0 or 1) on SAS drives. Only used with L-H 
          devices. 
      --bit-depth <value>
          Bit depth (default = 100000). Only used with L-H devices. 
      --phase-low <phase value>
          Phase low value (default = 0). Only used with L-H devices. 
      --phase-high <phase value>
          Phase high value (default = 31). Only used with L-H devices. 
      --phase-step <positive value>
          Phase step (default = 1). Only used with L-H devices. 
      --voltage-low <voltage value>
          Low voltage value (default = -31). Only used with L-H devices. 
      --voltage-high <voltage value>
          High voltage value (default = 31). Only used with L-H devices. 
      --voltage-step <positive value>
          Voltage value (default = 1). Only used with L-H devices. 
      --snapshot
          Specify a snap shot eye diagram. This option is only used with L-H 
          NVMe devices. 
      -x <bytes>,  --xfer <bytes>
          Specify maximum size, in bytes, to transfer per command. This 
          value must be a multiple of 4096. Only applicable for NVMe 
          devices. Default values is 4096 for NVMeoF or 64KB for PCI NVMe. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

getfeature usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for WDC targets.
      This task is only valid for NVMe or SATA targets.
       
  description
      Gets the various fields along with their values related to features on 
      the device. If saving the raw data, the filename shall be {serial 
      number}_{DDMMYYYY_HHMMSS}_feature-{feature-id}[-{select-value}]_2.17.0 
      .0.bin. 
      wdckit getfeature <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> <-f <feature-id>|-l|-p <alias> ...> [-S 
      <select-value>|--current|--default|--saved|--supported-capabilities] 
      [-r|--raw-limit <bytes>|-s <path>|--set-feature-xml <filename>] 
      [--trace|--trace-with-scan|--no-trace] [-v <dw11 value>] 
      [--payload-size <bytes>] [--xml-decoder <filename>] [-m] [--nsid 
      <value>] [-u <uuid index>] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute getfeature command. Use 
          'all' to select all devices. For example, in Windows, it will be 
          shown in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -f <feature-id>,  --feature <feature-id>
          (OR required)  NVMe devices only. Feature id to be retrieved. 
      -l,  --list
          (OR required)  Prints the list of supported features. 
      -p <alias>,  --parameterlist <alias>  (accepted multiple times)
          (OR required)  ATA devices only. Name of the operational 
          parameters whose values need to be retrieved. Use 'all' to 
          retrieve all operational parameter values. 
      -S <select-value>,  --select <select-value>
          NVMe devices only. Option for the select field. 
      --current
          NVMe devices only. Select current feature setting. 
      --default
          NVMe devices only. Select default feature setting. 
      --saved
          NVMe devices only. Select saved feature setting. 
      --supported-capabilities
          NVMe devices only. Select supported capabilities feature setting. 
      -r,  --raw
          Dump the raw buffer. 
      --raw-limit <bytes>
          Dump the raw buffer, with at most, this many bytes. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      --set-feature-xml <filename>
          Save NVMe set feature response buffer in an XML format suitable 
          for setfeatures. Only applies to feature IDs: 3h, Ch, Eh, 13h, 16h, 
          7Dh, 7Eh, 7Fh and 81h. <filename> will be used if and only if one 
          target device is specified. When multiple targets are specified, 
          the XML filename will be 
          <sn>_<timestamp>_feature-<id>_<version>.xml. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -v <dw11 value>,  --value <dw11 value>
          NVMe devices only. Dw11 value (only some feature ids use it). 
      --payload-size <bytes>
          NVMe devices only. Override default payload data size, in bytes 
          (only some feature ids use it). 
      --xml-decoder <filename>
          Decode additional data as described by this xml file. Please refer 
          to the user guide appendix for the XML schema. 
      -m,  --mirror
          Uses the NVMe mirror command instead of the NVMe standard command. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -u <uuid index>,  --uuid-index <uuid index>
          Specify the NVMe UUID Index (0-7fh). This field is only valid for 
          NVMe devices. It will be ignored for ATA/SCSI devices. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

getlog usage:
  restrictions
      This task is only valid for an actual device or file target.
      This task is only valid for WDC targets.
       
  description
      This command retrieves logs from ATA, NVMe and SCSI devices. Log 
      events for various factors, such as error handling, status handling, 
      statistics, accounting, and so forth. This will decode and show the 
      log contents in human readable text. If saving the raw data, the 
      filename shall be {serial 
      number}_{DDMMYYYY_HHMMSS}_{log-name}_2.17.0.0.bin. 
      wdckit getlog <<devList|filename> ...|--model <model number> ...| 
      --serial <serial number> ...> [--smartlog|-g|-G] [--ata|--nvme|--scsi] 
      [-r|--raw-limit <bytes>|-s <path>] [--data-area <1|2|3|4>|-t <type[, 
      max size]> ...|-e <type[,max size]]> ...|--show-dui-header] 
      [--no-progress|--progress-bar|--simple-progress] [--trace| 
      --trace-with-scan|--no-trace] [-l <log number>] [--lsp <log specific 
      number>] [--lpo <log page offset>] [-u <uuid index>] [--rae] [-f 
      <value>] [-p <page list>] [--ignore-directory] [-S <bytes>] [-b 
      <blocks>] [--lsi <value>] [--csi <value>] [--force] [-m] [--nsid 
      <value>] [-x <transfer size>] [--xml-decoder <filename>] [--output 
      <text|json|xml|csv|csv-no-header>] [--timeout <seconds>] [-R 
      <filename>] [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList|filename>  (accepted multiple times)
          (OR required)  Device or file name(s) to execute getlog command. 
          Use 'all' to select all devices. For example, in Windows, it will 
          be shown in Disk Management as Disk0, Disk1, etc. In Linux it will 
          be /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple 
          devices can be repeated by separating each device with a space. 
          See also do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --smartlog
          Use ATA SMART read log command to access the data. 
      -g,  --gpl
          Use ATA GPL read log command to access the data. 
      -G,  --gpl-dma
          Use ATA GPL read log DMA command to access the data. 
      --ata
          Specify that the binary file was retreived from an ATA device. 
      --nvme
          Specify that the binary file was retreived from an NVMe device. 
      --scsi
          Specify that the binary file was retreived from a SCSI device. 
      -r,  --raw
          Dump the raw buffer. 
      --raw-limit <bytes>
          Dump the raw buffer, with at most, this many bytes. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      --data-area <1|2|3|4>
          Specify the highest NVMe telemetry data area to retrieve. The 
          default value is 3. 
      -t <type[,max size]>,  --get-type <type[,max size]>  (accepted multiple times)
          Specify NVMe telemetry section type to extract, with an optional 
          maximum size limit in bytes. Note, may not be supported for all 
          WDC NVMe devices. 
      -e <type[,max size]]>,  --exclude-type <type[,max size]]>  (accepted multiple times)
          Specify NVMe telemetry section type to exclude. If an optional 
          maximum size limit, in bytes, is specified, then this section type 
          will be read up to the specified limit. Note, may not be supported 
          for all WDC NVMe devices. 
      --show-dui-header
          Show NVMe telemetry log (log 7h) header - will not collect 
          telemetry log. Note, may not be supported for all WDC NVMe 
          devices. 
      --no-progress
          No progress display. 
      --progress-bar
          Display a full screen progress bar screen. 
      --simple-progress
          Prevent the display of the progress bar screen, useful when 
          running commands from a script. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -l <log number>,  --log <log number>
          Specify the NVMe log page id (LID) to be retrieved or the ATA log 
          address to be retreived or the SCSI page code to be retrieved. 
          Refer to the appendix of the user guide for a list of log numbers 
          and names. 
      --lsp <log specific number>
          Specify the NVMe log specific field (LSP) value. 
      --lpo <log page offset>
          Specify the log page offset for an NVMe device. Ignore for 
          non-NVMe devices. 
      -u <uuid index>,  --uuid-index <uuid index>
          Specify the NVMe UUID Index (0-7fh). This field is only valid for 
          NVMe devices. It will be ignored for ATA/SCSI devices. 
      --rae
          Specify the NVMe Retain Asyncrhonous Event (rae) flag. It will be 
          ignored for ATA/SCSI devices. 
      -f <value>,  --features <value>
          Specify the ATA General Purpose Log address FEATURE value. Used 
          only on some GPL addresses. 
      -p <page list>,  --pages <page list>
          Pages from the ATA log address or SCSI subpage code to be 
          retrieved. If not specified, all the pages are displayed. The 
          following notations are supported for pageList: x|x..y|x..+y[,x| 
          x..y|x..+y]. 
      --ignore-directory
          Skips the check if the log exists and tries the command. 
      -S <bytes>,  --size <bytes>
          Specify the number of bytes to read for NVMe devices. 
      -b <blocks>,  --block-count <blocks>
          Specify the maximum number of blocks to transfer per ATA command. 
      --lsi <value>
          Specify the log specific identifier (0-FFFFh) for NVMe devices. 
      --csi <value>
          Specify the command set identifier (0-FFh) for NVMe devices. 
      --force
          Force reading an empty NVMe telemetry-controller intiated log 
          (lid=8h). 
      -m,  --mirror
          Uses the NVMe mirror command instead of the NVMe standard command. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -x <transfer size>,  --xfer <transfer size>
          Specify the maximum size, in 4096 byte (4 KiB) units, to transfer 
          per command. This is only used for NVMe devices. Default is 1. 
      --xml-decoder <filename>
          Decode additional data as described by this xml file. Please refer 
          to the user guide appendix for the XML schema. 
      --output <text|json|xml|csv|csv-no-header>
          Specify output format. 
      --timeout <seconds>
          Timeout value, in seconds. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

getpe usage:
  restrictions
      This task is only valid for an actual NVMe device or file target.
      This task is only valid for devices with a unique customer firmware.
      This task is only valid for WDC targets.
       
  description
      Retrieves the vendor specific PE (Program Erase) log from supported 
      NVMe devices. If saving the raw data, the filename shall be {serial 
      number}-_{DDMMYYYY_HHMMSS}_pelog_2.17.0.0.bin. 
      wdckit getpe <<devList|filename> ...|--model <model number> ...| 
      --serial <serial number> ...> [-r|--raw-limit <bytes>|-s <path>] 
      [--trace|--trace-with-scan|--no-trace] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList|filename>  (accepted multiple times)
          (OR required)  Device or file name(s) to execute getpe command. 
          Use 'all' to select all devices. For example, in Windows, it will 
          be shown in Disk Management as Disk0, Disk1, etc. In Linux it will 
          be /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple 
          devices can be repeated by separating each device with a space. 
          See also do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -r,  --raw
          Dump the raw buffer. 
      --raw-limit <bytes>
          Dump the raw buffer, with at most, this many bytes. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

getpersistentevent usage:
  restrictions
      This task is only valid for an actual NVMe device or file target.
      This task is only valid for WDC targets.
       
  description
      Retrieves and parses the Persistent Event Log (dh) from supported NVMe 
      devices. If saving the raw data, the filename shall be {serial 
      number}_{DDMMYYYY_HHMMSS}_persistentevent_2.17.0.0.bin. 
      wdckit getpersistentevent <<devList|filename> ...|--model <model 
      number> ...|--serial <serial number> ...> [-r|--raw-limit <bytes>|-s 
      <path>] [--trace|--trace-with-scan|--no-trace] [-m] [--nsid <value>] 
      [-R <path>] [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList|filename>  (accepted multiple times)
          (OR required)  Device or file name(s) to execute 
          getpersistentevent command. Use 'all' to select all devices. For 
          example, in Windows, it will be shown in Disk Management as Disk0, 
          Disk1, etc. In Linux it will be /dev/nvme0, /dev/nvme1, /dev/sda, 
          /dev/sdb etc. Multiple devices can be repeated by separating each 
          device with a space. See also do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -r,  --raw
          Dump the raw buffer. 
      --raw-limit <bytes>
          Dump the raw buffer, with at most, this many bytes. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -m,  --mirror
          Uses the NVMe mirror command instead of the NVMe standard command. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -R <path>,  --redirect <path>
          Redirects the screen output to the path specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

getsmart usage:
  restrictions
      This task is only valid for an actual device or file target.
      This task is only valid for WDC targets.
       
  description
      Retrieves the SMART data and the SMART status with SMART trip 
      parameter, if any, from the device. If saving the raw data, the 
      filename shall be {serial 
      number}_{DDMMYYYY_HHMMSS}_smart_2.17.0.0.bin. 
      wdckit getsmart <<devList|filename> ...|--model <model number> ...| 
      --serial <serial number> ...> [-a|-r|--raw-limit <bytes>|-S|-s <path>] 
      [--trace|--trace-with-scan|--no-trace] [--output <text|json|xml|csv| 
      csv-no-header>] [--nsid <value>] [-f] [-n <filename>] [-R <filename>] 
      [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList|filename>  (accepted multiple times)
          (OR required)  Device or file name(s) to execute getsmart command. 
          Use 'all' to select all devices. For example, in Windows, it will 
          be shown in Disk Management as Disk0, Disk1, etc. In Linux it will 
          be /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple 
          devices can be repeated by separating each device with a space. 
          See also do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -a,  --attributes
          Retrieves the SMART attributes of the device. 
      -r,  --raw
          Dump the raw buffer. 
      --raw-limit <bytes>
          Dump the raw buffer, with at most, this many bytes. 
      -S,  --status
          Retrieves the SMART status of the device. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      --output <text|json|xml|csv|csv-no-header>
          Specify output format. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -f,  --fail
          Retrieves the SMART failed attributes of the device. 
      -n <filename>,  --namesub <filename>
          Takes xml filename as input for name substitution of attributes. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

getsmr usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for WDC targets.
      This task is only valid for SATA targets.
       
  description
      Retrieves the vendor specific SMR data from supported WDC devices. The 
      log is saved in a file named {serial 
      number}_{DDMMYYYY_HHMMSS}_smrbin_2.17.0.0.bin. 
      wdckit getsmr <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> [--progress-bar|--simple-progress|--no-progress] 
      [--trace|--trace-with-scan|--no-trace] [-s <path>] [-a] [--xfer 
      <bytes>] [-R <filename>] [--no-win-disk] [--no-win-ctrl-hdc] 
      [--no-win-ctrl-scsi] [--no-win-csmi] [--no-win-rste] 
      [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] [--no-linux-nvme] 
      [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] 
      [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level <silent|error| 
      info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute getsmr command. Use 'all' 
          to select all devices. For example, in Windows, it will be shown 
          in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --progress-bar
          Display a full screen progress bar screen. 
      --simple-progress
          Prevent the display of the progress bar screen, useful when 
          running commands from a script. 
      --no-progress
          No progress display. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      -a,  --collect-all
          Collects all conditional data. 
      --xfer <bytes>
          Specify maximum number of bytes to transfer per command for L-H 
          devices. Must be a multiple of 512. Default values is 64KB. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

help usage:
  description
      Displays help information about wdckit commands. 
      wdckit help [<command name>] [-n|-d|-e|-s|-r] [--cssd-sata|--cssd-nvme| 
      --chdd|--essd-sata|--essd-nvme|--ehdd|--ssd-sata|--ssd-nvme|--hdd|-a] 
      [--trace|--trace-with-scan|--no-trace] [-o <w|l|f|windows|linux| 
      freebsd>] [-t <label>] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <command name>
          Any wdckit command for which help information is required. Always 
          a particular command at once. 
      -n,  --syntax
          Displays syntax for command. 
      -d,  --description
          Displays description for command. 
      -e,  --examples
          Displays examples for command. 
      -s,  --shortdescription
          Displays short description for command. 
      -r,  --restriction
          Displays restriction(s) for command. 
      --cssd-sata
          Filter help to include functions that support client SSD SATA 
          devices. 
      --cssd-nvme
          Filter help to include functions that support client SSD NVMe 
          devices. 
      --chdd
          Filter help to include functions that support client HDD devices. 
      --essd-sata
          Filter help to include functions that support enterprise SSD SATA 
          devices. 
      --essd-nvme
          Filter help to include functions that support enterprise SSD NVMe 
          devices. 
      --ehdd
          Filter help to include functions that support enterprise HDD 
          devices. 
      --ssd-sata
          Filter help to include functions that support SSD SATA devices. 
      --ssd-nvme
          Filter help to include functions that support SSD NVMe devices. 
      --hdd
          Filter help to include functions that support HDD devices. 
      -a,  --all
          Show help for every function. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -o <w|l|f|windows|linux|freebsd>,  --operatingsystem <w|l|f|windows|linux|freebsd>
          Displays examples for specified operating system. Use 'w' for 
          Windows and 'l' for Linux. 
      -t <label>,  --table <label>
          Save table of command line args to 'label-flag.csv' and 
          'label-desc.csv'. Best case usage is all commands, eg: 'wdckit 
          help "*" -t label' 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

hmb usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for NVMe targets.
      This task is only valid for WDC targets.
       
  description
      Display Host Memory Buffer support for an NVMe device. If saving the 
      raw data, the filename shall be {serial 
      number}-_{DDMMYYYY_HHMMSS}_hmb_2.17.0.0.bin. 
      wdckit hmb <<devList> ...|--model <model number> ...|--serial <serial 
      number> ...> [-r|--raw-limit <bytes>|-s <path>] [--trace| 
      --trace-with-scan|--no-trace] [-u <uuid index>] [-R <filename>] 
      [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute hmb command. Use 'all' to 
          select all devices. For example, in Windows, it will be shown in 
          Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -r,  --raw
          Dump the raw buffer. 
      --raw-limit <bytes>
          Dump the raw buffer, with at most, this many bytes. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -u <uuid index>,  --uuid-index <uuid index>
          Specify the NVMe UUID Index (0-7fh). This field is only valid for 
          NVMe devices. It will be ignored for ATA/SCSI devices. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

idd usage:
  restrictions
      This task is only valid for an actual device or file target.
       
  description
      Retrieves the Identify data of the ATA or NVMe device or Inquiry data 
      for SCSI devices. For ATA devices, the Identify Device data is 
      reported. For NVMe devcies, the Identify Controller or Identify 
      Namespace data is reported. For SCSI devices, the Inquiry data is 
      reported. Note, in Windows, attempting to list NVMe namespaces (idd 
      disk0 --namespace --list) for devices using the Microsoft inbox NVMe 
      driver, --nsid <value> will not work as expected. Instead, use diskX 
      that Windows assigns to the namespace. 
       
      Filename when saving (where {base} will be {serial 
      number}_{DDMMYYYY_HHMMSS}). 
      Device  Argument         Filename                                
      ------  ---------------  -------------------------------------   
      Any                      {base}_idd_2.17.0.0.bin               
      NVMe    -n | --cns 0     {base}_idd_ns_2.17.0.0.bin            
      NVMe    -n -l | --cns 2  {base}_idd_ns_list_2.17.0.0.bin       
      NVMe    --cns 3          {base}_idd_nsid_list_2.17.0.0.bin     
      NVMe    --cns 4          {base}_idd_nvmset_list_2.17.0.0.bin   
      NVMe    --cns 5 --csi 0  {base}_iocs_ns_2.17.0.0.bin           
      NVMe    --cns 5 --csi 2  {base}_zns_ns_2.17.0.0.bin            
      NVMe    --cns 6 --csi 0  {base}_iocs_ctrl_2.17.0.0.bin         
      NVMe    --cns 6 --csi 2  {base}_zns_ctrl_2.17.0.0.bin          
      NVMe    --cns 7 --csi 0  {base}_iocs_ns_list_2.17.0.0.bin      
      NVMe    --cns 7 --csi 2  {base}_zns_ns_list_2.17.0.0.bin       
      NVMe    --cns 8          {base}_iocs_ind_ns_2.17.0.0.bin       
      NVMe    --cns 10h        {base}_alloc_ns_2.17.0.0.bin          
      NVMe    --cns 11h        {base}_idd_ns_alloc_2.17.0.0.bin      
      NVMe    --cns 12h        {base}_idd_ns_ctrl_list_2.17.0.0.bin  
      NVMe    --cns 13h        {base}_idd_ctrl_list_2.17.0.0.bin     
      NVMe    --cns 14h        {base}_idd_pri_ctrl_cap_2.17.0.0.bin  
      NVMe    --cns 15h        {base}_idd_sec_ctrl_list_2.17.0.0.bin 
      NVMe    --cns 16h        {base}_idd_ns_gran_2.17.0.0.bin       
      NVMe    --cns 17h        {base}_idd_uuid_2.17.0.0.bin          
      NVMe    --cns 18h        {base}_idd_domain_2.17.0.0.bin        
      NVMe    --cns 19h        {base}_idd_end_grp_2.17.0.0.bin       
      NVMe    --cns 1Ah        {base}_iocs_alloc_ns_2.17.0.0.bin     
      NVMe    --cns 1Bh        {base}_iocs_alloc_id_ns_2.17.0.0.bin  
      NVMe    --cns 1Ch        {base}_iocs_cmd_set_2.17.0.0.bin      
      SCSI    -v XXh           {base}_inq_vpd_XXh_2.17.0.0.bin.      
       
      wdckit idd [<devList|filename> ...|--model <model number> ...|--serial 
      <serial number> ...] [-r|--raw-limit <bytes>|-s <path>] [-c|-n|-d] 
      [--trace|--trace-with-scan|--no-trace] [-l] [--zns] [--cns <cns 
      value>] [--nsid <value>] [-u <uuid index>] [--csi <csi value>] 
      [--cntid <cntid value>] [--cnssi <cnssi value>] [-v <page code>] 
      [--xml-decoder <filename>] [--output <text|json|xml|csv| 
      csv-no-header>] [-R <filename>] [--no-win-disk] [--no-win-ctrl-hdc] 
      [--no-win-ctrl-scsi] [--no-win-csmi] [--no-win-rste] 
      [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] [--no-linux-nvme] 
      [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] 
      [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level <silent|error| 
      info|debug|cmd-debug>] [-h] 
       
  options:
      <devList|filename>  (accepted multiple times)
          Device or file name(s) to execute idd command. Use 'all' to select 
          all devices. For example, in Windows, it will be shown in Disk 
          Management as Disk0, Disk1, etc. In Linux it will be /dev/nvme0, 
          /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices can be 
          repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          Filter devices that only match this serial number. 
      -r,  --raw
          Dump the raw buffer. 
      --raw-limit <bytes>
          Dump the raw buffer, with at most, this many bytes. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      -c,  --controller
          Displays the Identify Controller Data for an NVMe device 
          (CNS=01h). Displays the Identify Device Data for an ATA device. 
          SCSI devices are not valid. 
      -n,  --namespace
          Displays the Identify Namespace Data of the NVMe device (CNS=00h). 
          ATA and SCSI devices are not valid. 
      -d,  --desc
          Displays the Namespace Identification Descriptor list (CNS=03h). 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -l,  --list
          Displays the controller list (CNS=13h), when used with -c| 
          --controller or displays the active Namespace ID list (CNS=02h) 
          when used with -n|--namespace of the NVMe device. ATA and SCSI 
          devices are not valid. 
      --zns
          Display the identify controller ZNS specific data (CNS=06h), when 
          used with -c|--controller or display the identify namespace ZNS 
          specific data (CNS=05h), when used with -n|--namespace of the NVMe 
          device. ATA and SCSI devices are not valid. 
      --cns <cns value>
          NVMe controller or namespace structure. Mutually exclusive with -c| 
          --controller, -n|--namespace, -l|--list, --zns. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -u <uuid index>,  --uuid-index <uuid index>
          Specify the NVMe UUID Index (0-7fh). This field is only valid for 
          NVMe devices. It will be ignored for ATA/SCSI devices. 
      --csi <csi value>
          NVMe Command Set Identifier value. Used for ZNS commands. 
      --cntid <cntid value>
          NVMe Controller Identifier value. 
      --cnssi <cnssi value>
          NVMe CNS Specific Identifier value. 
      -v <page code>,  --vpd <page code>
          Display inquiry vital product data for a SCSI device. NVMe and ATA 
          devices are not valid. 
      --xml-decoder <filename>
          Decode additional data as described by this xml file. Please refer 
          to the user guide appendix for the XML schema. 
      --output <text|json|xml|csv|csv-no-header>
          Specify output format. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

logdump usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for WDC targets.
      This task requires the device to be ready.
       
  description
      Dump logs from specified devices. Collects an E6 log from L-H devices. 
      Collects a DRM Super Binary log from L-W devices. Use 'getdui' to 
      collect a DUI log from most L-S devices. Collects a log dump from some 
      recent L-S devices. 
      wdckit logdump [<devList> ...|--model <model number> ...|--serial 
      <serial number> ...] [--inc-start|--inc-update|--inc-max|--inc-min-io] 
      [--progress-bar|--simple-progress|--no-progress] [--trace| 
      --trace-with-scan|--no-trace] [-s <path>] [--default] [--short] 
      [--south-dump] [--ati] [--p-list] [--fly-height] [--partial-context] 
      [--metadata] [--fly-height2] [--snr-ow] [--servo] [--erp] [--cpu] 
      [--rw-incr] [--partial-context2] [--nand-smart] [--excursion] 
      [--latency] [--workload-tracking] [--workload-tracking-0] 
      [--workload-tracking-1] [--workload-tracking-2] 
      [--workload-tracking-3] [--all-modes] [--mode <mode byte> ...] [-t 
      <bytes>] [-2] [--no-sanitize-status] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          Device name(s) to execute logdump command. Use 'all' to select all 
          devices. For example, in Windows, it will be shown in Disk 
          Management as Disk0, Disk1, etc. In Linux it will be /dev/nvme0, 
          /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices can be 
          repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          Filter devices that only match this serial number. 
      --inc-start
          Collects incremental starting log (mode 0x80). This in only used 
          with L-H devices. 
      --inc-update
          Collects incremental update log (mode 0x81). This in only used 
          with L-H devices. 
      --inc-max
          Collects incremental log with maximum log entries (specified in 
          mode page 0x1C, sub-page 0xE5) (mode 0x82). This in only used with 
          L-H devices. 
      --inc-min-io
          Collects incremental log minimizing host IO (mode 0x83). This in 
          only used with L-H devices. 
      --progress-bar
          Display a full screen progress bar screen. 
      --simple-progress
          Prevent the display of the progress bar screen, useful when 
          running commands from a script. 
      --no-progress
          No progress display. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      --default
          Collects default modes (normal 0x10, latest snapshot 0x11, older 
          snapshot 0x21 and oldest snapshot 0x31). This in only used with 
          L-H devices. If no mode is specified, this is the default logdump 
          collection method. 
      --short
          A small log for data-collection purposes (mode 0x00). This in only 
          used with L-H devices. 
      --south-dump
          Collects debug information for SSDs only (mode 0x03). This in only 
          used with L-H devices. 
      --ati
          Collects device Adjacent Track Interference (ATI) data (mode 
          0x12). This in only used with L-H devices. 
      --p-list
          Collects device P-List data (mode 0x13). This in only used with 
          L-H devices. 
      --fly-height
          Collects device Fly-height data (mode 0x14). This in only used 
          with L-H devices. 
      --partial-context
          Collects device partial context data (mode 0x15). This in only 
          used with L-H devices. 
      --metadata
          Collects the flash stored metadata (mode 0x16). This in only used 
          with L-H devices. 
      --fly-height2
          Collects device Fly-height 2 data (mode 0x17). This in only used 
          with L-H devices. 
      --snr-ow
          Collects the SNR/OW data (mode 0x18). This in only used with L-H 
          devices. 
      --servo
          Collects the servo error log data (mode 0x19). This in only used 
          with L-H devices. 
      --erp
          Collects the ERP historgram data (mode 0x1A). This in only used 
          with L-H devices. 
      --cpu
          Collects the CPU performance data (mode 0x1B). This in only used 
          with L-H devices. 
      --rw-incr
          Collects the RW incremental log data (mode 0x1C). This in only 
          used with L-H devices. 
      --partial-context2
          Collects device partial context 2 data (mode 0x1D). This in only 
          used with L-H devices. 
      --nand-smart
          Collects device Nand SMART data (mode 0x1E). This in only used 
          with L-H devices. 
      --excursion
          Collects device excursion log data (mode 0x20). This in only used 
          with L-H devices. 
      --latency
          Collects device latency monitor data (mode 0x22). This in only 
          used with L-H devices. 
      --workload-tracking
          Collects the working tracking data (mode 0xA0). This in only used 
          with L-H devices. 
      --workload-tracking-0
          Collects the working tracking data (mode 0xA0). This in only used 
          with L-H devices. 
      --workload-tracking-1
          Collects the working tracking data (mode 0xA1). This in only used 
          with L-H devices. 
      --workload-tracking-2
          Collects the working tracking data (mode 0xA2). This in only used 
          with L-H devices. 
      --workload-tracking-3
          Collects the working tracking data (mode 0xA3). This in only used 
          with L-H devices. 
      --all-modes
          Collects all available logs. This in only used with L-H devices. 
      --mode <mode byte>  (accepted multiple times)
          Collect this E6 mode. This in only used with L-H devices. 
      -t <bytes>,  --transfer-size <bytes>
          Specify maximum number of bytes to transfer per command. Default 
          values is 64KB. 
      -2,  --two-ports
          Collects 2 logs, one for each port of a SAS device. 
      --no-sanitize-status
          Do not check ATA sanitize status, which on some systems, may not 
          operate correctly. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

ns-attach usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for NVMe targets.
      This task is only valid for WDC targets.
      This task is only valid in Windows PE with NVMe devices when connected via the inbox driver.
       
  description
      Send a namespace attachment command to attach a namepace to a 
      controller identifier(s). Note: For Windows with the inbox driver, 
      this command must be run from Windows PE. 
      wdckit ns-attach <<device name>|--model <model number> ...|--serial 
      <serial number> ...> [--trace|--trace-with-scan|--no-trace] -n <value> 
      -c <value> ... [-R <filename>] [--no-win-disk] [--no-win-ctrl-hdc] 
      [--no-win-ctrl-scsi] [--no-win-csmi] [--no-win-rste] 
      [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] [--no-linux-nvme] 
      [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] 
      [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level <silent|error| 
      info|debug|cmd-debug>] [-h] 
       
  options:
      <device name>
          (OR required)  Device name to execute ns-attach command. For 
          example, in Windows, it will be shown in Disk Management as Disk0, 
          Disk1, etc. In Linux it will be /dev/nvme0, /dev/nvme1, /dev/sda, 
          /dev/sdb etc. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -n <value>,  --nsid <value>
          (required) Specify the namespace ID value. 
      -c <value>,  --controller <value>  (accepted multiple times)
          (required) The controller identifier to attach. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

ns-create usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for NVMe targets.
      This task is only valid for WDC targets.
      This task is only valid in Windows PE with NVMe devices when connected via the inbox driver.
       
  description
      Send a namespace management command to create a namespace for an NVMe 
      device. Note: For Windows with the inbox driver, this command must be 
      run from Windows PE. 
      wdckit ns-create <<device name>|--model <model number> ...|--serial 
      <serial number> ...> <-f <0-Fh>|-b <1|2|4|8|16|32|64|128|256|512|1024| 
      2048|4096|8192|16384|32768>> [--trace|--trace-with-scan|--no-trace] 
      [--csi <0-FFh>] [-s <blocks>] [-c <blocks>] [-d <0-FFh>] [-m <0-FFh>] 
      [-a <0-FFFFFFFFh>] [-i <0-FFFFh>] [-e <0-FFFFh>] [-l <value>] [-t 
      <seconds>] [-R <filename>] [--no-win-disk] [--no-win-ctrl-hdc] 
      [--no-win-ctrl-scsi] [--no-win-csmi] [--no-win-rste] 
      [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] [--no-linux-nvme] 
      [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] 
      [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level <silent|error| 
      info|debug|cmd-debug>] [-h] 
       
  options:
      <device name>
          (OR required)  Device name to execute ns-create command. For 
          example, in Windows, it will be shown in Disk Management as Disk0, 
          Disk1, etc. In Linux it will be /dev/nvme0, /dev/nvme1, /dev/sda, 
          /dev/sdb etc. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -f <0-Fh>,  --flbas <0-Fh>
          (OR required)  LBA format index, as shown by idd -n. 
      -b <1|2|4|8|16|32|64|128|256|512|1024|2048|4096|8192|16384|32768>,  --block-size <1|2|4|8|16|32|64|128|256|512|1024|2048|4096|8192|16384|32768>
          (OR required)  LBA format in bytes (1-32768, in power of 2 
          increments). 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      --csi <0-FFh>
          The command set identifier. Default is 0. Use 2 for ZNS. 
      -s <blocks>,  --nsze <blocks>
          The namespace size, in logical blocks. 
      -c <blocks>,  --ncap <blocks>
          The namespace capacity, in logical blocks. 
      -d <0-FFh>,  --dps <0-FFh>
          End-to-end data protection type setting. 
      -m <0-FFh>,  --nmic <0-FFh>
          Namespace Multi-path I/O and Namespace Sharing Capabilities. 
      -a <0-FFFFFFFFh>,  --anagrpid <0-FFFFFFFFh>
          ANA Group Identifier. 
      -i <0-FFFFh>,  --nvmsetid <0-FFFFh>
          NVM Set Identifier. 
      -e <0-FFFFh>,  --endgid <0-FFFFh>
          Endurance Group Identifier. 
      -l <value>,  --lbstm <value>
          Logical Block Storage Tag Mask. 
      -t <seconds>,  --timeout <seconds>
          Timeout value, in seconds. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

ns-delete usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for NVMe targets.
      This task is only valid for WDC targets.
      This task is only valid in Windows PE with NVMe devices when connected via the inbox driver.
       
  description
      Send a namespace management command to delete a namespace for an NVMe 
      device. Note: For Windows with the inbox driver, this command must be 
      run from Windows PE. 
      wdckit ns-delete <<device name>|--model <model number> ...|--serial 
      <serial number> ...> [--trace|--trace-with-scan|--no-trace] -n <value> 
      [-R <filename>] [--no-win-disk] [--no-win-ctrl-hdc] 
      [--no-win-ctrl-scsi] [--no-win-csmi] [--no-win-rste] 
      [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] [--no-linux-nvme] 
      [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] 
      [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level <silent|error| 
      info|debug|cmd-debug>] [-h] 
       
  options:
      <device name>
          (OR required)  Device name to execute ns-delete command. For 
          example, in Windows, it will be shown in Disk Management as Disk0, 
          Disk1, etc. In Linux it will be /dev/nvme0, /dev/nvme1, /dev/sda, 
          /dev/sdb etc. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -n <value>,  --nsid <value>
          (required) Specify the namespace ID value to delete. Use FFFFFFFFh 
          to delete all namespaces in the NVM subsystem. If the value of 
          FFFFFFFFh is specified and there are zero valid namespaces, the 
          command completes successfully. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

ns-detach usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for NVMe targets.
      This task is only valid for WDC targets.
      This task is only valid in Windows PE with NVMe devices when connected via the inbox driver.
       
  description
      Send a namespace attachment command to detach a namepace from a 
      controller identifier(s). Note: For Windows with the inbox driver, 
      this command must be run from Windows PE. 
      wdckit ns-detach <<device name>|--model <model number> ...|--serial 
      <serial number> ...> [--trace|--trace-with-scan|--no-trace] -n <value> 
      -c <value> ... [-R <filename>] [--no-win-disk] [--no-win-ctrl-hdc] 
      [--no-win-ctrl-scsi] [--no-win-csmi] [--no-win-rste] 
      [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] [--no-linux-nvme] 
      [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] 
      [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level <silent|error| 
      info|debug|cmd-debug>] [-h] 
       
  options:
      <device name>
          (OR required)  Device name to execute ns-detach command. For 
          example, in Windows, it will be shown in Disk Management as Disk0, 
          Disk1, etc. In Linux it will be /dev/nvme0, /dev/nvme1, /dev/sda, 
          /dev/sdb etc. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -n <value>,  --nsid <value>
          (required) Specify the namespace ID value. 
      -c <value>,  --controller <value>  (accepted multiple times)
          (required) The controller identifier to detach. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

nsze usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for NVMe targets.
      This task is only valid for SanDisk targets.
      This task is only valid for devices with a unique customer firmware.
       
  description
      Send vendor unique command to modify namespace size for NVMe devices. 
      wdckit nsze <<devList> ...|--model <model number> ...|--serial <serial 
      number> ...> [--trace|--trace-with-scan|--no-trace] -o <value> [-R 
      <filename>] [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute nsze command. Use 'all' 
          to select all devices. For example, in Windows, it will be shown 
          in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -o <value>,  --option <value>
          (required) Value for the required option. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

power usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for NVMe targets.
      This task is only valid for devices with a unique customer firmware.
      This task is only valid for WDC targets.
       
  description
      Displays or sets power management APST state (PMAS) for NVMe devices. 
      wdckit power <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> [-s <value>|-c] [--trace|--trace-with-scan| 
      --no-trace] [-R <filename>] [--no-win-disk] [--no-win-ctrl-hdc] 
      [--no-win-ctrl-scsi] [--no-win-csmi] [--no-win-rste] 
      [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] [--no-linux-nvme] 
      [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] 
      [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level <silent|error| 
      info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute power command. Use 'all' 
          to select all devices. For example, in Windows, it will be shown 
          in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -s <value>,  --set <value>
          Enable Power Management APST State. 
      -c,  --clear
          Disable Power Management APST State. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

quit usage:
  description
      Exit the CLI. 
       
      wdckit quit 
       
  options:

rdp usage:
  restrictions
      This task is only valid for an actual ATA/SCSI device or file target.
      This task is not allowed on a boot device.
      This task is only valid for WDC targets.
      RDP support was not detected.
       
  description
      Performs RDP (repurpose depopulation) on a SCSI or ATA device. RDP is 
      also known as the storage element feature set. 
      wdckit rdp <<device name|filename>|--model <model number> ...|--serial 
      <serial number> ...> <-g|-r <head>|--repop-all> [--raw|--raw-limit 
      <bytes>|-s <path>] [--no-progress|--progress-bar|--simple-progress] 
      [--trace|--trace-with-scan|--no-trace] [-H <head>] [-t <type>] [-f 
      <filter>] [-m <LBA>] [--retry-limit <count>] [-b <bytes>] 
      [--danger-zone] [-R <filename>] [--no-win-disk] [--no-win-ctrl-hdc] 
      [--no-win-ctrl-scsi] [--no-win-csmi] [--no-win-rste] 
      [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] [--no-linux-nvme] 
      [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] 
      [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level <silent|error| 
      info|debug|cmd-debug>] [-h] 
       
  options:
      <device name|filename>
          (OR required)  Device or file name toexecute rdp command. For 
          example, in Windows, it will be shown in Disk Management as Disk0, 
          Disk1, etc. In Linux it will be /dev/nvme0, /dev/nvme1, /dev/sda, 
          /dev/sdb etc. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -g,  --gpes
          (OR required)  Get physical element status. 
      -r <head>,  --ret <head>
          (OR required)  Remove element and truncate. Specified the element 
          to remove. 
      --repop-all
          (OR required)  Revert all removed elements with a restore elements 
          and rebuild command. 
      --raw
          Dump the raw buffer. 
      --raw-limit <bytes>
          Dump the raw buffer, with at most, this many bytes. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      --no-progress
          No progress display. 
      --progress-bar
          Display a full screen progress bar screen. 
      --simple-progress
          Prevent the display of the progress bar screen, useful when 
          running commands from a script. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -H <head>,  --head <head>
          Specify the starting element field for the get physical element 
          status operation. 
      -t <type>,  --report-type <type>
          Specify the report type field for the get physical element status 
          operation. Value must be from 0 to 15, inclusive. 
      -f <filter>,  --filter <filter>
          Specify the filter field for the get physical element status 
          operation. Value must be from 0 to 3, inclusive. 
      -m <LBA>,  --max-lba <LBA>
          Specify the requested maximum LBA for the remove element and 
          truncate operation. Defaults to 0  which allows the device to 
          specify the maximum LBA after successful command completion. 
      --retry-limit <count>
          Specify a retry limit. Value must be between 0 and 15. Used for 
          only -r (--ret) or (--repop-all). 
      -b <bytes>,  --blocksize <bytes>
          Specify the block size, in bytes when decoding a filename. Valid 
          values for ATA sourced binary files: 512, 4096. Valid values for 
          SCSI sourced binary files: 512, 520, 528, 4096, 4112, 4160, 4224.  
      --danger-zone
          Flag tells the application that you know you are going to destroy 
          your data with this command and will not prompt the user. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

reset usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for WDC targets.
       
  description
      Perform a reset for supported devices and OS drivers. Beware - this 
      operation may be dangerous. Note, some OSes / drivers do not allow a 
      reset. Only supported in Linux and Windows. 
      wdckit reset <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> [--trace|--trace-with-scan|--no-trace] [-f] [-R 
      <filename>] [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute reset command. Use 'all' 
          to select all devices. For example, in Windows, it will be shown 
          in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -f,  --force
          Force the reset operation without asking for user confirmation. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

sasphypower usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for SAS targets.
      This task is only valid for WDC targets.
       
  description
      Show, enable or disable SAS PHY power management (partial & slumber). 
      wdckit sasphypower <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> [--trace|--trace-with-scan|--no-trace] [-p 
      <boolean>] [-s <boolean>] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute sasphypower command. Use 
          'all' to select all devices. For example, in Windows, it will be 
          shown in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -p <boolean>,  --partial <boolean>
          Specify partial value (0-1). 
      -s <boolean>,  --slumber <boolean>
          Specify slumber value (0-1). 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

security usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for WDC targets.
      This task is only valid in Linux when /sys/module/libata/parameters/allow_tpm=1.
       
  description
      Performs the various security related features on the device. WARNING: 
      TCG operations may erase user data - use with caution! 
      wdckit security <<device name>|--model <model number> ...|--serial 
      <serial number> ...> <-g|-a|-i|-s|-e|-d|-l|--unlock|-c|-v| 
      --erase-locking|--msid-activate|--msid-revert|-p <psid>|--stack-reset| 
      -L <sid password>> [-A <Admin password>|-B <BandMaster password>|-E 
      <EraseMaster password>|-S <SID password>] [--admin|-u <1|2>|--sid|-b 
      <-1|0-1023> ...|--erasemaster] [--raw|--raw-limit <bytes>] 
      [--progress-bar|--simple-progress|--no-progress] [--trace| 
      --trace-with-scan|--no-trace] [--skip-status] [--show-enabled-bands] 
      [-U <user password>] [-o <old password>] [-n <new password>] 
      [--range-start <lba>] [--range-length <blocks>] [-r <true|false>] [-w 
      <true|false>] [--lock-on-reset <true|false>] [-t <seconds>] [-R 
      <filename>] [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <device name>
          (OR required)  Device name to execute security command. For 
          example, in Windows, it will be shown in Disk Management as Disk0, 
          Disk1, etc. In Linux it will be /dev/nvme0, /dev/nvme1, /dev/sda, 
          /dev/sdb etc. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -g,  --get
          (OR required)  This option gets the security information from the 
          device. 
      -a,  --activate
          (OR required)  For TCG Enterprise devices that support BDE/TCG 
          firmware, will activate TCG. Not applicable for TCG Opal. 
      -i,  --inactivate
          (OR required)  For TCG Enterprise devices that support BDE/TCG 
          firmware, will de-activate TCG. 
      -s,  --setadminpassword
          (OR required)  This option sets a new admin/bandmaster/erasemaster 
          password on device. For TCG Opal, it must be executed with -A| 
          --Adminpassword option. For TCG Enterprise it must be executed 
          with -B|--bandmasterpassword, -E|--erasemasterpassword or -S| 
          --sidpassword option. This option may also activate TCG. 
      -e,  --enable
          (OR required)  This option enables the new user along with its 
          password. For TCG Opal, it must be executed with -u|--user, -U| 
          --Userpassword and -A|--Adminpassword options. Not applicable for 
          TCG Enterprise. 
      -d,  --disable
          (OR required)  This option disables the given user. For TCG Opal, 
          it must be executed with -u|--user and -A|--Adminpassword options. 
          Not applicable for TCG Enterprise. 
      -l,  --lock
          (OR required)  This option enables read/write locking and 
          locks/unlocks read/write operations on the device. It must be 
          executed with -r|--readlock, -w|--writelock and an appropriate 
          password (-A|--Adminpassword, -u|--user (and -U|--Userpassword) or 
          -B|--bandmasterpassword (and -b|--bandmaster)) option. Bracketed 
          option selection depends on who is issuing lock operation. For TCG 
          Opal, use with -A|--Adminpassword or -u|--user. For TCG Enterprise, 
          use with -B|--bandmasterpassword. 
      --unlock
          (OR required)  This options disables read/write locking operations 
          on the device. It must be executed with an appropriate password 
          (-A|--Adminpassword, -u|--user (and -U|--Userpassword) or -B| 
          --bandmasterpassword (and -b|--bandmaster)) option. Bracketed 
          option selection depends on who is issuing lock operation. For TCG 
          Opal, use with -A|--Adminpassword or -u|--user. For TCG Enterprise, 
          use with -B|--bandmasterpassword. 
      -c,  --changepassword
          (OR required)  This option changes 
          Admin/User/BandMaster/EraseMaster password on the device. It must 
          be executed with -o|--oldpassword, -n|--newpassword. For TCG Opal 
          and if issued by User1 or User2, also use -u|--user option. For 
          TCG Enterprise, use -B|--bandmasterpassword, -E| 
          --erasemasterpassword or -S|--sidpassword option. 
      -v,  --revert
          (OR required)  This option reverts the entire security 
          configuration to defaults. For TCG Opal, it must be executed with 
          -A|--Adminpassword option. Not applicable for TCG Enterprise, use 
          --erase-locking instead. 
      --erase-locking
          (OR required)  This option shall crytographically erase user data. 
          For TCG Enterprise, it must be executed with -B| 
          --bandmasterpassword or -E|--erasemasterpassword option. Not 
          applicable for TCG Opal, use -v|--revert instead. 
      --msid-activate
          (OR required)  This option activates security configuration using 
          MSID. 
      --msid-revert
          (OR required)  This option reverts the entire security 
          configuration to defaults using MSID. 
      -p <psid>,  --psidrevert <psid>
          (OR required)  This option reverts the entire security 
          configuration to defaults using PSID. Use optional -t|--timewait 
          to specify the maximum time to wait. The default wait time is 30 
          seconds. The PSID argument is a 20 or 32 character value printed 
          on the label. 
      --stack-reset
          (OR required)  This option performs a TCG stack reset operation. 
      -L <sid password>,  --list-locking-ranges <sid password>
          (OR required)  This option lists all locking ranges. Not 
          applicable for TCG Opal. 
      -A <Admin password>,  --Adminpassword <Admin password>
          For TCG Opal, this option is used for taking Admin Password as 
          input. It should be used with either -s (--setadminpassword), -l 
          (--lock), (--unlock), -v (--revert), -e (--enable) or -d 
          (--disable) options. Not applicable for TCG Enterprise. 
      -B <BandMaster password>,  --bandmasterpassword <BandMaster password>
          This option is used for taking BandMaster Password as input. It 
          should be used with either -s (--setadminpassword), -l (--lock), 
          (--unlock) or (--erase-locking) options. Not applicable for TCG 
          Opal. 
      -E <EraseMaster password>,  --erasemasterpassword <EraseMaster password>
          This option is used for taking EraseMaster Password as input. It 
          should be used with either -s (--setadminpassword), -l (--lock), 
          (--unlock), (--erase-locking) options. Not applicable for TCG 
          Opal. 
      -S <SID password>,  --sidpassword <SID password>
          This option is used for taking SID Password as input. It should be 
          used with either -s (--setadminpassword), -l (--lock), (--unlock), 
          options. Not applicable for TCG Opal. 
      --admin
          This option will change the Admin password. It should be used with 
          -c (--changepassword). Not applicable for TCG Enterprise. 
      -u <1|2>,  --user <1|2>
          For TCG Opal, this option is used for taking User number as input. 
          It should be used with either of -c (--changepassword), -l 
          (--lock), -e (--enable) or -d (--disable) options. Not applicable 
          for TCG Enterprise. 
      --sid
          This option will change the SID password. It should be used with 
          -c (--changepassword). Not applicable for TCG Opal. 
      -b <-1|0-1023>,  --bandmaster <-1|0-1023>  (accepted multiple times)
          This option specifies the BandMaster value. It is required when -B| 
          --bandmasterpassword is used. A value of -1 will use all 
          BandMaster values. Not applicable for TCG Opal. 
      --erasemaster
          This option will change the EraseMaster password. It should be 
          used with -c (--changepassword). Not applicable for TCG Opal. 
      --raw
          Dump the raw buffer. 
      --raw-limit <bytes>
          Dump the raw buffer, with at most, this many bytes. 
      --progress-bar
          Display a full screen progress bar screen. 
      --simple-progress
          Prevent the display of the progress bar screen, useful when 
          running commands from a script. 
      --no-progress
          No progress display. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      --skip-status
          Pass the PSID regardless of the state of the device. 
      --show-enabled-bands
          List only enabled locking ranges. Optional when -L 
          (--list-locking-ranges) is present. Not applicable for TCG Opal. 
      -U <user password>,  --Userpassword <user password>
          For TCG Opal, this option is used for taking User Password as 
          input. It should be used with either -l (--lock) or -e (--enable) 
          options. Not applicable for TCG Enterprise. 
      -o <old password>,  --oldpassword <old password>
          This option is used for taking the old password as input while 
          changing the password of Admin/User/BandMaster/EraseMaster. 
      -n <new password>,  --newpassword <new password>
          This option is used for taking new old password as input while 
          changing the password of Admin/User/BandMaster/EraseMaster. 
      --range-start <lba>
          This option specifies the range start LBA. Not applicable for TCG 
          Opal. 
      --range-length <blocks>
          This option specifies the range length. Not applicable for TCG 
          Opal. 
      -r <true|false>,  --readlock <true|false>
          This option is used for taking Lock/Unlock value for read 
          operation as input. The default value is false. It should be used 
          with -l (--lock) option. 
      -w <true|false>,  --writelock <true|false>
          This option is used for taking Lock/Unlock value for write 
          operation as input. The default value is false. It should be used 
          with -l (--lock) option. 
      --lock-on-reset <true|false>
          This option is used for setting the lock on reset value. The 
          default value is false. This is used only with -l (--lock). Not 
          applicable for TCG Opal. 
      -t <seconds>,  --timewait <seconds>
          Specify timeout in seconds (15 to 3600). The default value is 30 
          seconds. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

securityprofile usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for SATA targets.
      This task is only valid for WDC targets.
      This task is only valid in Linux when /sys/module/libata/parameters/allow_tpm=1.
       
  description
      Performs the various security profile related features on the ATA 
      device. 
      wdckit securityprofile <<devList> ...|--model <model number> ...| 
      --serial <serial number> ...> <-g|-c|-s <security-profile>> [--trace| 
      --trace-with-scan|--no-trace] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute securityprofile command. 
          Use 'all' to select all devices. For example, in Windows, it will 
          be shown in Disk Management as Disk0, Disk1, etc. In Linux it will 
          be /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple 
          devices can be repeated by separating each device with a space. 
          See also do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -g,  --get
          (OR required)  This option is used to get all the supported 
          Security Profiles of the Device. 
      -c,  --current
          (OR required)  This option is used to get the current Security 
          Profile of the Device. 
      -s <security-profile>,  --set <security-profile>
          (OR required)  This option is used to set the new Security profile 
          on the device. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

selftest usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for WDC targets.
      This task requires the device to be ready.
       
  description
      Runs the short or extended test on the device(s) specified by the 
      user. Note, Windows 20H1 and later may impose a self test time 
      restriction of 10 minutes between self tests to the same NVMe device. 
      wdckit selftest <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> <-s|-e|-a|-p> [--progress-bar|--simple-progress| 
      --no-progress] [--trace|--trace-with-scan|--no-trace] [--nsid <value>] 
      [-b] [-r] [-m] [--no-sanitize-status] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute selftest command. Use 
          'all' to select all devices. For example, in Windows, it will be 
          shown in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -s,  --short
          (OR required)  This option initiates the short Self Test on the 
          device. 
      -e,  --extended
          (OR required)  This option initiates the extended Self Test on the 
          device. 
      -a,  --abort
          (OR required)  This option aborts the running Self Test on the 
          device. 
      -p,  --progress
          (OR required)  Query the self test progress. 
      --progress-bar
          Display a full screen progress bar screen. 
      --simple-progress
          Prevent the display of the progress bar screen, useful when 
          running commands from a script. 
      --no-progress
          No progress display. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -b,  --blocked
          Perform the self test operation as a blocking operation. 
      -r,  --result
          Shows result of the last Extended test execution from ATA log. 
          Valid only with -e option. No result is available for non-ATA 
          devices. 
      -m,  --mirror
          Uses the NVMe mirror command instead of the NVMe standard command. 
      --no-sanitize-status
          Do not check ATA sanitize status, which on some systems, may not 
          operate correctly. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

serverconfig usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for NVMe targets.
      This task is only valid for SanDisk targets.
      This task is only valid for devices with a unique customer firmware.
       
  description
      Send vendor unique command to modify the resource server configuration 
      on supported NVMe devices. 
      wdckit serverconfig <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> [--trace|--trace-with-scan|--no-trace] -p <1|2> 
      [-s <value>] [-R <filename>] [--no-win-disk] [--no-win-ctrl-hdc] 
      [--no-win-ctrl-scsi] [--no-win-csmi] [--no-win-rste] 
      [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] [--no-linux-nvme] 
      [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] 
      [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level <silent|error| 
      info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute serverconfig command. Use 
          'all' to select all devices. For example, in Windows, it will be 
          shown in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -p <1|2>,  --power <1|2>
          (required) Power type configuration. 
      -s <value>,  --set <value>
          Set to a new configuration value (0-100). 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

setfeature usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for WDC targets.
      This task is only valid for NVMe or SATA targets.
       
  description
      Sets the specified feature value for NVMe devices. Sets the given 
      input operational Parameters with input Values for ATA devices. 
      wdckit setfeature <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> [-f <feature-id>|-l] [-b <buffer-file>| 
      --xml-encoder <filename>] [--trace|--trace-with-scan|--no-trace] [-v 
      <dw11 value>] [-d <data-length>] [-s] [--nsid <value>] [-u <uuid 
      index>] [-m] [--dipm <enable|disable>] [--apm <value|disable>] [--hwc 
      <enable|disable>] [--aptst <enable|disable>] [--stimeout <value| 
      default>] [--apst <value|default>] [--sscshift <value|default>] 
      [--esspectrum <enable|disable|default>] [--ssrange <0|1|2|3|default>] 
      [--gen1pemphasis <value|default>] [--gen2pemphasis <value|default>] 
      [--gen3pemphasis <value|default>] [--gen1amplitude <value|default>] 
      [--gen2amplitude <value|default>] [--gen3amplitude <value|default>] 
      [--spspeed <0|1|2|default>] [--devslp <enable|disable>] [-R 
      <filename>] [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute setfeature command. Use 
          'all' to select all devices. For example, in Windows, it will be 
          shown in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -f <feature-id>,  --feature <feature-id>
          Feature id to be modified. This is for NVMe devices only. 
      -l,  --list
          Prints the list of supported features. 
      -b <buffer-file>,  --bufferfile <buffer-file>
          File name of file containing the data that will be transferred. 
          This is for NVMe devices only. 
      --xml-encoder <filename>
          Encode payload data as described by this xml file. Please refer to 
          the user guide appendix for the XML schema. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -v <dw11 value>,  --value <dw11 value>
          Dw11 value (only some feature ids use it). This is for NVMe 
          devices only. 
      -d <data-length>,  --data-len <data-length>
          Data transfer length, amount of data in the buffer file. This is 
          for NVMe devices only. 
      -s,  --save
          Save settings permanently. This is for NVMe devices only. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -u <uuid index>,  --uuid-index <uuid index>
          Specify the NVMe UUID Index (0-7fh). This field is only valid for 
          NVMe devices. It will be ignored for ATA/SCSI devices. 
      -m,  --mirror
          Uses the NVMe mirror command instead of the NVMe standard command. 
      --dipm <enable|disable>
          Device Initiated Power Management. This is for ATA devices only. 
      --apm <value|disable>
          Advanced Power Management. This is for ATA devices only. 
      --hwc <enable|disable>
          Host Write Cache. This is for ATA devices only. 
      --aptst <enable|disable>
          Auto Partial To Slumber Transition. This is for ATA devices only. 
      --stimeout <value|default>
          Slumber Timeout. This is for ATA devices only. 
      --apst <value|default>
          Auto Partial Slumber Timeout. This is for ATA devices only. 
      --sscshift <value|default>
          Spread Spectrum Clock Shift. This is for ATA devices only. 
      --esspectrum <enable|disable|default>
          Enable Spread Spectrum. This is for ATA devices only. 
      --ssrange <0|1|2|3|default>
          Spread Spectrum Range. This is for ATA devices only. 
      --gen1pemphasis <value|default>
          Gen1 Pre Emphasis. This is for ATA devices only. 
      --gen2pemphasis <value|default>
          Gen2 Pre Emphasis. This is for ATA devices only. 
      --gen3pemphasis <value|default>
          Gen3 Pre Emphasis. This is for ATA devices only. 
      --gen1amplitude <value|default>
          Gen1 Amplitude. This is for ATA devices only. 
      --gen2amplitude <value|default>
          Gen3 Amplitude. This is for ATA devices only. 
      --gen3amplitude <value|default>
          Gen3 Amplitude. This is for ATA devices only. 
      --spspeed <0|1|2|default>
          SATA PHY Speed. This is for ATA devices only. 
      --devslp <enable|disable>
          Device Sleep. This is for ATA devices only. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

sethctmtemps usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for WDC targets.
      This task is only valid for NVMe targets.
       
  description
      Configures the settings for the host controlled thermal management 
      feature on the NVMe device. 
      wdckit sethctmtemps <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> [--trace|--trace-with-scan|--no-trace] [-1 
      <temperature>] [-2 <temperature>] [-d] [-s] [--nsid <value>] [-m] [-R 
      <filename>] [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute sethctmtemps command. Use 
          'all' to select all devices. For example, in Windows, it will be 
          shown in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -1 <temperature>,  --tmt1 <temperature>
          Specify the thermal management temperature 1 (Celcuis or Kelvin 
          acceptable). Use 0 to disable TMT1. 
      -2 <temperature>,  --tmt2 <temperature>
          Specify the thermal management temperature 2 (Celcuis or Kelvin 
          acceptable). Use 0 to disable TMT2. 
      -d,  --disable
          Disable both thermal management temperatures. 
      -s,  --save
          Save settings permanently. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -m,  --mirror
          Uses the NVMe mirror command instead of the NVMe standard command. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

setthrottlingtemp usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for SanDisk targets.
      This task is only valid for NVMe targets.
       
  description
      Sets the Light and Heavy Throttling Temperature on the NVMe device. 
      wdckit setthrottlingtemp <<devList> ...|--model <model number> ...| 
      --serial <serial number> ...> [--trace|--trace-with-scan|--no-trace] 
      [-l <temperature>] [-H <temperature>] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute setthrottlingtemp 
          command. Use 'all' to select all devices. For example, in Windows, 
          it will be shown in Disk Management as Disk0, Disk1, etc. In Linux 
          it will be /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. 
          Multiple devices can be repeated by separating each device with a 
          space. See also do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -l <temperature>,  --light <temperature>
          Specify the light throttling temperature value. 
      -H <temperature>,  --heavy <temperature>
          Specify the heavy throttling temperature value. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

show usage:
  restrictions
      This task is only valid for an actual target.
       
  description
      List the details like serial number, capacity, state, geometry 
      information, protection information, progress information, version, 
      statistics, etc. of the devices. 
      wdckit show [<devList> ...|--model <model number> ...|--serial <serial 
      number> ...] [-a|-g|-s|-d|-f|-t] [-p|-l] [--trace|--trace-with-scan| 
      --no-trace] [--output <text|json|xml|csv|csv-no-header>] 
      [--show-duplicates] [--block-device] [--customer-id] [-L] 
      [--capacity-no-decimal] [--no-sanitize-status] [--no-usb] 
      [--no-multiple-ns] [--rdp-status] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          Device name(s) to execute show command. Use 'all' to select all 
          devices. For example, in Windows, it will be shown in Disk 
          Management as Disk0, Disk1, etc. In Linux it will be /dev/nvme0, 
          /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices can be 
          repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          Filter devices that only match this serial number. 
      -a,  --asset
          Show only asset information, such as drive name, serial number, 
          revision level, etc. 
      -g,  --geometry
          Show only device geometry information, such as capacity, etc. 
      -s,  --state
          Show device state information with an appropriate description of 
          reason(s) why the device is in that state. 
      -d,  --dco
          Shows DCO Identify Data details. 
      -f,  --features
          Shows the list of features supported by device. 
      -t,  --standards
          Shows the details of standards followed by device. 
      -p,  --physical
          Show only physical devices (no logical devices). 
      -l,  --logical
          Show only logical devices (no physical devices). 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      --output <text|json|xml|csv|csv-no-header>
          Specify output format. 
      --show-duplicates
          Show duplicate device paths. 
      --block-device
          Show only block devices (no SES devices). 
      --customer-id
          Show the customer ID and HGST internal firmware. 
      -L,  --locked
          Show reason devices are locked. 
      --capacity-no-decimal
          Show capacity without decimal point. 
      --no-sanitize-status
          Do not check ATA sanitize status, which on some systems, may not 
          operate correctly. 
      --no-usb
          Do not show USB devices. 
      --no-multiple-ns
          Do not show NVMe drives with multiple namespaces (Linux/FreeBSD). 
      --rdp-status
          Check ATA RDP (repurposing depopulation) state, which on some 
          systems, may not operate correctly. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

standby usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for SATA targets.
      This task is only valid for WDC targets.
       
  description
      Puts the ATA device in standby mode. 
      wdckit standby <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> [--trace|--trace-with-scan|--no-trace] [-R 
      <filename>] [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute standby command. Use 
          'all' to select all devices. For example, in Windows, it will be 
          shown in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

update usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for WDC targets.
       
  description
      Updates the device firmware with new firmware on the specified device. 
      wdckit update [<devList> ...|--model <model number> ...|--serial 
      <serial number> ...] <-f <firmware>|-a|-g|--xml <xml filename>| 
      --reset> [--progress-bar|--simple-progress|--no-progress] [--trace| 
      --trace-with-scan|--no-trace] [-x <transfer size>] [-d] [-s <slot 
      value>] [-c <ca value>] [-b <0|1>] [-v] [-r <seconds>] [--pause-apst] 
      [--fast] [--no-sanitize-status] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          Device name(s) to execute update command. Use 'all' to select all 
          devices. For example, in Windows, it will be shown in Disk 
          Management as Disk0, Disk1, etc. In Linux it will be /dev/nvme0, 
          /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices can be 
          repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          Filter devices that only match this serial number. 
      -f <firmware>,  --firmware <firmware>
          (OR required)  The filename of the firmware binary. 
      -a,  --activate
          (OR required)  Perform a firmware commit (aka activate) action. 
          For an NVMe device, this option requires --slot. Activation is 
          usually preceeded by a --firmware command. 
      -g,  --getfwinfo
          (OR required)  Get FW slot information from log id 3h. 
      --xml <xml filename>
          (OR required)  The filename of an XML file with firmware update 
          directives. Please refer to the end of the user guide for the XML 
          schema. 
      --reset
          (OR required)  Perform a controller reset (NVMe only). This may 
          not be supported with all Windows NVMe drivers. Not supported in 
          FreeBSD. 
      --progress-bar
          Display a full screen progress bar screen. 
      --simple-progress
          Prevent the display of the progress bar screen, useful when 
          running commands from a script. 
      --no-progress
          No progress display. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -x <transfer size>,  --xfer <transfer size>
          Specify the maximum size, in bytes, to transfer the firmware 
          image. The firmware image will be sent to the device via multilple 
          commands when the image is larger than this value. Use -1 to 
          specify a large transfer size determined programatically. This can 
          only be used with -f|--firmware or --xml. 
      -d,  --defer
          Download and save the firmware image to the device and update it 
          only after a system power cycle (non NVMe devices) or activate 
          action. 
      -s <slot value>,  --slot <slot value>
          Specify the firmware slot that shall be used for the activate 
          action for an NVMe device. This can only be used with -a| 
          --activate. 
      -c <ca value>,  --commit-action <ca value>
          NVMe activate commit action value (0-7). This can only be used 
          with -a|--activate. Note: this option is not accepted by the 
          Windows inbox driver. 
      -b <0|1>,  --bpid <0|1>
          Specify the boot partition ID. This can only be used with -a| 
          --activate. Note: this option is not accepted by the Windows inbox 
          driver. 
      -v,  --validate
          Validate the firmware image with the specified device(s). If used 
          with --xml it will check if any device(s) needs an update. 
      -r <seconds>,  --rescan-control <seconds>
          Set the delay in seconds between firmware update and the device 
          re-scan. Zero is no delay and negative numbers skip the re-scan. 
      --pause-apst
          Save and disable Autonomous Power State Transition (APST) before 
          update and restore afterwards. 
      --fast
          Skip non-essential commands to speed up performance. 
      --no-sanitize-status
          Do not check ATA sanitize status, which on some systems, may not 
          operate correctly. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

version usage:
  description
      Displays version information. 
       
      wdckit version 
       
  options:

writelog usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for SATA targets.
      This task is only valid for WDC targets.
       
  description
      This command is used to write a log page to the ATA device. The data 
      will be read from a binary file. The method shall be either the SMART 
      or the general purpose logging (GPL) interface. 
      wdckit writelog <<devList> ...|--model <model number> ...|--serial 
      <serial number> ...> [-s|-g|-G] <-d <dataFile>|--xml-encoder 
      <filename>> [--trace|--trace-with-scan|--no-trace] -l <value> [-f 
      <value>] [-b <blocks>] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute writelog command. Use 
          'all' to select all devices. For example, in Windows, it will be 
          shown in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      -s,  --smart
          Use SMART write log command to access the data. 
      -g,  --gpl
          Use GPL write log command to access the data. 
      -G,  --gpl-dma
          Use GPL write log DMA command to access the data. 
      -d <dataFile>,  --data <dataFile>
          (OR required)  The binary filename to send to the device. 
      --xml-encoder <filename>
          (OR required)  Encode payload data as described by this xml file. 
          Please refer to the user guide appendix for the XML schema. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -l <value>,  --logaddress <value>
          (required) The log address to access. 
      -f <value>,  --features <value>
          Value for the FEATURES field. 
      -b <blocks>,  --block-count <blocks>
          Specify the maximum number of blocks to transfer per command. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

zns usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for NVMe targets.
      This task is only valid for WDC targets.
       
  description
      Perform various ZNS operations and show ZNS reports. Supported 
      operations: open zone, close zone, finish zone, offline zone, set zone 
      desc. This can also report parital and extended zone info. 
      wdckit zns [<devList> ...|--model <model number> ...|--serial <serial 
      number> ...] <--open|--close|--finish|--reset|--offline| 
      --set-zone-desc <filename>|--report <max-value>|--extended-report 
      <max-value>> [-r|--raw-limit <bytes>|--save <path>] [--start-lba <lba>| 
      --all-zones] [--trace|--trace-with-scan|--no-trace] [--data-lifetime 
      <lifetime>] [-s <all|empty|implicitly-opened|explicitly-opened|closed| 
      full|read-only|offline>] [-p] [--nsid <value>] [-u <uuid index>] [-R 
      <filename>] [--no-win-disk] [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] 
      [--no-win-csmi] [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] 
      [--no-linux-scsi] [--no-linux-nvme] [--no-linux-wd-nvme] 
      [--no-bsd-cam] [--no-bsd-nvme] [--no-ad] [--no-mr] [--probe-flag <flag 
      bits>] [-z] [--log-level <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          Device name(s) to execute zns command. Use 'all' to select all 
          devices. For example, in Windows, it will be shown in Disk 
          Management as Disk0, Disk1, etc. In Linux it will be /dev/nvme0, 
          /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices can be 
          repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          Filter devices that only match this serial number. 
      --open
          (OR required)  Open one or more zones. NOTE: In Linux, the device 
          name MUST be a namespace name (eg /dev/nvme0n1). 
      --close
          (OR required)  Close one or more zones. NOTE: In Linux, the device 
          name MUST be a namespace name (eg /dev/nvme0n1). 
      --finish
          (OR required)  Finish one or more zones. NOTE: In Linux, the 
          device name MUST be a namespace name (eg /dev/nvme0n1). 
      --reset
          (OR required)  Reset one or more zones. NOTE: In Linux, the device 
          name MUST be a namespace name (eg /dev/nvme0n1). 
      --offline
          (OR required)  Offline one or more zones. NOTE: In Linux, the 
          device name MUST be a namespace name (eg /dev/nvme0n1). 
      --set-zone-desc <filename>
          (OR required)  Attach Zone Descriptor Extension data to a zone. 
          NOTE: In Linux, the device name MUST be a namespace name (eg 
          /dev/nvme0n1). 
      --report <max-value>
          (OR required)  Reports zone descriptor entries through the Report 
          Zones data structure. Use -1 to report all entries. NOTE: In Linux, 
          the device name MUST be a namespace name (eg /dev/nvme0n1). 
      --extended-report <max-value>
          (OR required)  Reports zone descriptor entries through the 
          Extended Report Zones data structure. Use -1 to report all 
          entries. NOTE: In Linux, the device name MUST be a namespace name 
          (eg /dev/nvme0n1). 
      -r,  --raw
          Dump the raw buffer. 
      --raw-limit <bytes>
          Dump the raw buffer, with at most, this many bytes. 
      --save <path>
          Saves the device output to the path specified. 
      --start-lba <lba>
          Specify the zone starting LBA. Used with open, close, finish, 
          reset, offline, report, extended-report or set zone desc options. 
      --all-zones
          Select all zones. Used with open, close, finish, reset, offline or 
          set zone desc options. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      --data-lifetime <lifetime>
          Specify the zone data lifetime. Used with open zone. Valid values 
          range from 0 to 3Fh. 
      -s <all|empty|implicitly-opened|explicitly-opened|closed|full|read-only|offline>,  --state <all|empty|implicitly-opened|explicitly-opened|closed|full|read-only|offline>
          Filter report/extended report to only this state. 
      -p,  --partial
          Show a parital report/extended report. 
      --nsid <value>
          Specify the NVMe namespace ID value. 
      -u <uuid index>,  --uuid-index <uuid index>
          Specify the NVMe UUID Index (0-7fh). This field is only valid for 
          NVMe devices. It will be ignored for ATA/SCSI devices. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 

zone usage:
  restrictions
      This task is only valid for an actual target.
      This task is only valid for ZAC/ZBC device.
      This task is only valid for WDC targets.
      This task requires the device to be ready.
       
  description
      Perform various Zoned ATA/Block Commands (ZAC/ZBC). Supported 
      commands: close zone, finish zone, open zone, report zones and reset 
      write pointer. 
      wdckit zone <<devList> ...|--model <model number> ...|--serial <serial 
      number> ...> <--report-zones|--close|--finish|--open|--reset> [-r| 
      --raw-limit <bytes>|-s <path>] [--trace|--trace-with-scan|--no-trace] 
      [-a] [--start-lba <lba>] [-p <count>] [-o <all|empty|implicitly-opened| 
      explicitly-opened|closed|full|read-only|offline|inactive| 
      rwp-recommeded|non-seq-wr-res-active|zone-cond-not-write-ptr>] 
      [--no-sanitize-status] [-x <bytes>] [-R <filename>] [--no-win-disk] 
      [--no-win-ctrl-hdc] [--no-win-ctrl-scsi] [--no-win-csmi] 
      [--no-win-rste] [--no-win-amd-raid] [--no-win-ses] [--no-linux-scsi] 
      [--no-linux-nvme] [--no-linux-wd-nvme] [--no-bsd-cam] [--no-bsd-nvme] 
      [--no-ad] [--no-mr] [--probe-flag <flag bits>] [-z] [--log-level 
      <silent|error|info|debug|cmd-debug>] [-h] 
       
  options:
      <devList>  (accepted multiple times)
          (OR required)  Device name(s) to execute zone command. Use 'all' 
          to select all devices. For example, in Windows, it will be shown 
          in Disk Management as Disk0, Disk1, etc. In Linux it will be 
          /dev/nvme0, /dev/nvme1, /dev/sda, /dev/sdb etc. Multiple devices 
          can be repeated by separating each device with a space. See also 
          do-not-operate to exclude devices. 
      --model <model number>  (accepted multiple times)
          (OR required)  Filter devices that only match this model number. 
      --serial <serial number>  (accepted multiple times)
          (OR required)  Filter devices that only match this serial number. 
      --report-zones
          (OR required)  Report zones. 
      --close
          (OR required)  Close zone. 
      --finish
          (OR required)  Finish zone. 
      --open
          (OR required)  Open zone. 
      --reset
          (OR required)  Reset write pointer. 
      -r,  --raw
          Dump the raw buffer. 
      --raw-limit <bytes>
          Dump the raw buffer, with at most, this many bytes. 
      -s <path>,  --save <path>
          Saves the device output to the path specified. 
      --trace
          Save trace log for command operation upon success. Note, by 
          default, trace logging enabled upon error. The trace log filename 
          is wdckit-trace.txt. 
      --trace-with-scan
          Save trace log for command operation and include commands issued 
          while scanning for devices. 
      --no-trace
          Disable trace logging. 
      -a,  --all-zones
          Perform zone operation (open/close/finish/reset) on all zones. 
      --start-lba <lba>
          Specify the zone starting LBA. 
      -p <count>,  --partial <count>
          Show a partial zone report, with at least this many entries. Note: 
          The OS may prevent large values from succeeding. 
      -o <all|empty|implicitly-opened|explicitly-opened|closed|full|read-only|offline|inactive|rwp-recommeded|non-seq-wr-res-active|zone-cond-not-write-ptr>,  --reporting-option <all|empty|implicitly-opened|explicitly-opened|closed|full|read-only|offline|inactive|rwp-recommeded|non-seq-wr-res-active|zone-cond-not-write-ptr>
          Filter report with this reporting option. 
      --no-sanitize-status
          Do not check ATA sanitize status, which on some systems, may not 
          operate correctly. 
      -x <bytes>,  --xfer <bytes>
          Specify maximum number of bytes to transfer for --report-zones 
          option. Must be a multiple of 512. Default values is 64KB. 
      -R <filename>,  --redirect <filename>
          Redirects the screen output to the file specified. 
      --no-win-disk
          Do not interact with Windows disk devices (eg disk* and only 
          useful with the Windows version). 
      --no-win-ctrl-hdc
          Do not interact with Windows controller HDC devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-ctrl-scsi
          Do not interact with Windows controller SCSI devices (eg storage 
          space devices disk* or NVMe controllers without namespaces nvme* 
          and only useful with the Windows version). 
      --no-win-csmi
          Do not interact with Windows CSMI devices (eg csmi* and only 
          useful with the Windows version). 
      --no-win-rste
          Do not interact with Windows RSTe devices (eg rste* and only 
          useful with the Windows version). 
      --no-win-amd-raid
          Do not interact with Windows AMD raid devices (eg amdraid* and 
          only useful with the Windows version). 
      --no-win-ses
          Do not interact with Windows SCSI Enclosure Service (SES) devices 
          (eg SCSI*) 
      --no-linux-scsi
          Do not interact with Linux ATA/SCSI devices (eg /dev/sg* or 
          /dev/sd* and only useful with the Linux version). 
      --no-linux-nvme
          Do not interact with Linux NVMe devices (eg /dev/nvme* and only 
          useful with the Linux version). 
      --no-linux-wd-nvme
          Do not interact with Linux NVMe devices using the WD NVMe driver 
          (eg wdnvme_bdfs* and only useful with the Linux version). 
      --no-bsd-cam
          Do not interact with FreeBSD CAM devices (eg /dev/ada*  and only 
          useful with the FreeBSD version). 
      --no-bsd-nvme
          Do not interact with FreeBSD NVMe devices (eg /dev/nvme*  and only 
          useful with the FreeBSD version). 
      --no-ad
          Do not use the AD driver (only useful with the RAID version). 
      --no-mr
          Do not use the MR driver (only useful with the RAID version). 
      --probe-flag <flag bits>
          Specify probe flags (bit 0: Windows prefer SAT passthru over ATA 
          passthru). 
      -z,  --nobanner
          Suppresses the banner from printing, which includes information 
          such as copyright, license, etc. 
      --log-level <silent|error|info|debug|cmd-debug>
          Change log level. 
      -h,  --help
          Display help and exit. 


   

