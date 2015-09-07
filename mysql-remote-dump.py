import paramiko
import time

class downloadDB(object):
    """
    This class is to
    - connect to remote server with ssh
    - dump an sql file into  ~ folder
    - download the sql file into local
    - delete the remote sql file
    """

    def __init__(self, sshServer, sshUser, sshPassword, mysqlDB, mysqlUser, mysqlPassword):
        self.sshServer = sshServer
        self.sshUser = sshUser
        self.sshPassword = sshPassword
        self.mysqlUser = mysqlUser
        self.mysqlPassword = mysqlPassword
        self.dbName = mysqlDB

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.fileName = str(int(time.time())) + '_auto_download.sql.gz'

    def connectSSH(self):
        try:
            self.ssh.connect(self.sshServer, username=self.sshUser, password=self.sshPassword)
        except:
            print 'Could not connect to server.'
            exit()

    def close(self):
        self.ssh.close()

    def runCommand(self,cmd):
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(cmd)
        print ssh_stdout.readlines()
        print ssh_stderr.readlines()

    def createDump(self):
        dumpCommand = 'mysqldump -u %s -p%s %s| zip > %s' % (self.mysqlUser, self.mysqlPassword, self.dbName, self.fileName)
        self.connectSSH()
        self.runCommand(dumpCommand)

    def downloadSql(self):
        port = 22
        transport = paramiko.Transport((self.sshServer, port))
        transport.connect(username = self.sshUser, password = self.sshPassword)

        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get(self.fileName, self.dbName + '.sql.gz')
        sftp.close()
        transport.close()

    def deleteBuckup(self):
        delCommand = 'rm ' + self.fileName
        self.runCommand(delCommand)
        self.close()

    def run(self):
        self.createDump()
        self.downloadSql()
        self.deleteBuckup()


if __name__ == '__main__':
    server = raw_input('Host name: ')
    username = raw_input('Server user name: ')
    password = raw_input('Server password: ')
    dbName = raw_input('Database Name: ')
    dbUser = raw_input('Database user name: ')
    dbPass = raw_input('Database password: ')

    dump = downloadDB(server, username, password, dbName, dbUser, dbPass)
    dump.run()