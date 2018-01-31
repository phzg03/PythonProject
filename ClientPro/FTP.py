import ftplib
import os
import socket

# HOST = '127.0.0.1'
# DIRN = 'file'
# FILE = 'ftp.txt'
HOST = 'ftp1.at.proftpd.org'
DIRN = 'pub/mozilla/'
FILE = 'README.MIRRORS'

def ftp():
    f = ftplib.FTP(HOST)
    print('Connected to HOST : "%s"' % HOST)
    try:
        f.login()
    except ftplib.error_perm:
        print('Cannot login "%s"' % HOST)
    # try:
    #     f.cwd(DIRN)
    # except ftplib.error_perm:
    #     print('Cannot CD to "%s"' % DIRN)
    #     f.quit()
    #     return
    # print('change to "%s"' % DIRN)
    f.pwd()
    try:
        loc = open(FILE, 'wb').write
        f.retrbinary('RETE %s' % FILE, loc)   # 报错，不能读取文件
    except ftplib.error_perm:
        print('error is : %s ' % ftplib.error_perm)
        print('cannot read file "%s"' % FILE)
        # os.unlink(FILE)
    else:
        print('downloaded "%s" to CWD' % FILE)
    f.quit()


def wirteFile(data):
    with open(FILE, 'wb') as fobj:
        fobj.write(data)


if __name__ == '__main__':
    ftp()
