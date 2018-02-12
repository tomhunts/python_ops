#!coding:utf-8
import paramiko  
import threading

def check_disk(host):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='192.168.3.%s'%(str(host)), port=22, username='btmon', password='btmon2015!@#')
        stdin, stdout, stderr = ssh.exec_command("df -h |grep /opt$ | awk '{print $4}' |cut -d '%' -f 1")
        str_out = stdout.read().decode()
        str_err = stderr.read().decode()
        if str_err != "":
            print(str_err)
        str_out = int(str_out)
        if str_out > 80:
            print ("192.168.3.%s"%(str(host)), ":" ," ",str_out)
        ssh.close()
    except:
        pass


def thread_check():
    for host in range(1,254):
        t = threading.Thread(target=check_disk,args=(host,))
        t.start()

if __name__ == '__main__':
    thread_check()
