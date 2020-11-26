import ftplib


def download_file(ftp=None, filename='TestToLabPPR.xlsx'):
    with open(filename, 'wb') as file:
        ftp.retrbinary('RETR %s' % filename, file.write)
    ftp.quit()


def connect(host="ftp.dlptest.com", user="dlpuser@dlptest.com", password="eUj8GeW55SvYaswqUyDSm5v6N"):
    """
    connect to an ftp server
    :param host:
    :param user:
    :param password:
    :return:
    """
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, password)
        print(ftp.dir())
        download_file(ftp=ftp)
        print(ftp.dir())
        ftp.quit()
        return True
    except:
        return False


def main():
    # Variables
    targetHostAddress = "ftp.dlptest.com"
    userName = "dlpuser@dlptest.com"
    password = "eUj8GeW55SvYaswqUyDSm5v6N"

    print('[+] Using anonymous credentials for ' + targetHostAddress)
    if connect(targetHostAddress, 'anonymous', 'test@test.com'):
        print('[*] FTP Anonymous log on succeeded on host '.format(targetHostAddress))
    else:
        print('[*] FTP Anonymous log on failed on host '.format(targetHostAddress))

        if connect(targetHostAddress, userName, password):
            # Password Found
            print("[*] FTP Logon succeeded on host " + targetHostAddress + " UserName:"
                  + userName + " Password:" + password)
            exit(0)
        else:
            # Password Not Found
            print("[*] FTP Logon failed on host " + targetHostAddress + " UserName:"
                  + userName + " Password:" + password)


if __name__ == "__main__":
    main()