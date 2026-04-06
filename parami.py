import paramiko

username = "winteck"
password = "winteck@2026"
hostname = "192.168.0.143"
port = 22


# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to server
ssh.connect(hostname=hostname, port=port, username=username, password=password)

# Execute command
stdin, stdout, stderr = ssh.exec_command("lsblk")#ls -l #uptime #uname -a #cat /etc/os-release #cat /etc/resolv.conf #date #ifconfig
#cat /proc/cpuinfo #cat /proc/meminfo #lspci -k #ps -eaf #du #df -h #lsblk #ls -alrt#lshw #lsusb #lspci #lspci -k #cat /etc/fstab

# Read output
print(stdout.read().decode())

# Close connection
ssh.close()