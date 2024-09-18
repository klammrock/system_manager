import subprocess

def get_os_version():
  return subprocess.run(['uname', '-o'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

def get_kernel_version():
  return subprocess.run(['uname', '-r'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
