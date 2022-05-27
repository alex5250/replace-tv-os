import eel
import os 
import sys
import psutil
import easygui
from download import download_file,install
from config_parse import read_config
from utils import remove_pathernesses
eel.init('web')


@eel.expose
def my_python_function(a, b):
    print(a, b, a + b)


@eel.expose
def exit_from_app(a, b):
    os.system("launcher")
    sys.exit(0)

@eel.expose
def install_os():
    eel.show('install_os.html')


@eel.expose
def clone_install_os(disk):
    disk_final=disk.split(",")[0].split(":")[1]
    url,checksum,tmp_dir,command=read_config()
    print(remove_pathernesses(url),remove_pathernesses(tmp_dir))
    download_file(remove_pathernesses(url),remove_pathernesses(tmp_dir))
    install(command,tmp_dir,disk_final)
    easygui.msgbox("Установка завершена! Перезагрузитесь")
    


@eel.expose
def scan_for_drives():
    disks_data=[]
    print(psutil.disk_partitions())
    print('Calling from JS...')

    for a in psutil.disk_partitions():
        disk_stirng="Device:{}, Filesystem:{}".format(a.device,a.fstype)
        print(len(disk_stirng))
        disks_data.append(disk_stirng)
           
    return disks_data







eel.start('main.html')


