from mega import Mega
import subprocess

def download_file(url,tmp_dir):
    mega = Mega()
    m = mega.login()
    m.download_url(url,tmp_dir)

def install(params,tmp_dir,disk):
    final_command=params.format(tmp_dir,disk)
    print(final_command)
    output=subprocess.getoutput(final_command)
    return output
    