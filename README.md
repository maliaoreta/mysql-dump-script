# mysql-dump-script
A script to import mysql dump files from a dump.tar.gz into an AWS RDS mysql instance within a private subnet.

### Setting up in dump.py
Edit ssh tunnel configuration:
```subprocess.Popen("ssh -N -L 1234:example.us-west-1.compute.amazonaws.com:3306 bastion", shell=True)```
where
1234 is the local port,
example.us-west-1.compute.amazonaws.com is the db host
3306 is the port the db is listening on
bastion is the ssh host (must be set up in ssh/config)

Edit path to tar in dump.py:
```tar = subprocess.check_output("tar -xvf ./path/to/dump.tar.gz", shell=True)```

Edit path to unzipped dump dir, db username, local db port, and db name in dump.py:
```db = subprocess.Popen("cat ./path/to/unzipped_dump/*.sql | mysql -u db_user
-p -h 127.0.0.1 -P 1234 db_name", shell=True, stdout=PIPE, stderr=PIPE)```

### Run
```python3 dump.py```
Enter db password when prompted
