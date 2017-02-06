import subprocess
from subprocess import Popen, PIPE

print("Opening ssh tunnel")
subprocess.Popen("ssh -N -L 1234:example.us-west-1.compute.amazonaws.com:3306 bastion", shell=True)

print("Unzipping corpwatch dump tar..")
tar = subprocess.check_output("tar -xvf ./path/to/dump.tar.gz", shell=True)
print(tar)

print("Connecting to mysql")
db = subprocess.Popen("cat ./path/to/unzipped_dump/*.sql | mysql -u db_user -p -h 127.0.0.1 -P 1234 db_name", shell=True, stdout=PIPE, stderr=PIPE)
ouptut, err = db.communicate();
