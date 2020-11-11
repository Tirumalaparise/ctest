'''import subprocess as sp
import xml.etree.ElementTree as et

print("WELCOME".center(60,'*'))
print("menu is \
	1.date \
	2.cal \
	3.configure and start datanode \
	4.configure ,start namenode \
	5.start webserver \
        6.start and launch docker container")
n=int(input("Enter which option you want"))
n1=input("Choose local or remote execution(l/r)")

dl={1:date,2:cal,3:dataname,4:dataname,5:webserver,6:docker}
if(n1=='r'):
    ip=input("Enter ip address of remote machine")
    x=sp.getstatusoutput('ssh '+ip+' python3 /root/menu.py')
    if(x):
        sp.getoutput('scp menu.py '+ip+':/root')
    x=sp.getstatusoutput('ssh '+ip+' python3 /root/menu.py'+n)
elif(n1=='l'):
    result=dl[n]
    result()'''

def date():
    sp.getoutput('date')

def cal():
    sp.getoutput('cal')

def dataname():
    if(n==3):
        string="data"
    else:
        string="name"
    out=sp.getoutput('jps')
    out=out.split()
    ip=input("Enter namenode ip")
    folder=input("Enter distributed folder")
    core=et.parse('/etc/hadoop/core-site.xml')
    hdfs=et.parse('/etc/hadoop/hdfs-site.xml')
    croot=core.getroot()
    hroot=hdfs.getroot()
    if(len(croot)>=1 and len(hroot)>=1):
        if(croot[0][1]=='hdfs://'+ip+':9001' and hroot[0][1]==folder and hroot[0            ][0]=='dfs.'+string+'.dir'):

            if(('DataNode' in out) or ('NameNode' in out)):
                print(string+"node is already running")
            else:
                sp.getoutput("hadoop-daemon.sh start "+string+"node")
        else:
            sp.getstatusoutput('hadoop-daemon.sh stop datanode')
            sp.getstatusoutput('hadoop-daemon.sh stop namenode')
            croot[0][1]=='hdfs://'+ip+':9001'
            hroot[0][1]==folder
            hroot[0][0]=='dfs.'+string+'.dir'
            core.write('/etc/hadoop/core-site.xml')
            hdfs.write("/etc/hadoop/hdfs-site.xml")
            sp.getoutput("hadoop-daemon.sh start "+string+"node")
    else:
        prop=et.Element("property")
        name=et.Element("name")
        value=et.Element("value")
        name.text="fs.default.name"
        value.text='hdfs://'+ip+':9001'
        prop.append(name)
        prop.append(value)
        croot.append(prop)
        core.write('/etc/hadoop/core-site.xml')
        name.text="dfs."+string+'.dir'
        value.text=folder
        hdfs.write('/etc/hadoop/hdfs-site.xml')
        sp.getoutput("hadoop-daemon.sh start "+string+"node")
    print(string+"node is running")
    sp.getoutput('jps')
def docker():
    sp.getoutput("systemctl start docker")
    print("1.pull an image\n \
            2.start a new container\n \
            3.start a stopped container\n \
            4.delete a container\n \
            5.delete an image\n \
            6.delete all containers\n \
            7.copy files between  base os and conatiner")
    n=int(input("choose which u want : "))
    if(n==1):
        image=input('Enter image name with version : ')
        sp.getoutput('docker pull '+image)
    elif(n==2):
        print(sp.getoutput("docker images"))
        container=input("Enter image to launch with name optionally as 'image n                          ame_to_container': ")
        container=container.split()
        print(container)
        x=sp.getstatusoutput('docker run -it --name '+container[1]+" "+container[0])
        print(x)
    elif(n==3):
        print(sp.getoutput("docker ps -a"))
        s=input("[better to enter the container name]")
        sp.getoutput("docker start "+s)
        sp.getoutput("docker attach "+s)
    elif(n==4):
        c=input("Enter which container to delete : ")
        sp.getoutput("docker rm -f "+c)
    elif(n==5):
        c=input("Enter which to delete to delete")
        sp.getoutput("docker rmi -f "+c)
    elif(n==7):
        print("Enter the container file location like <container_name/ID:file_path>")
        src=input("Enter source file location/path: ")
        dest=input("Enter destination file location/path: ")
        sp.getoutput("docker cp "+src+" "+dest)
    elif(n==6):
        sp.getoutput("docker rm `docker ps -a -q`")
        sp.getoutput("docker ps -a")
        print("containers were deleted")
def webserver():
    sp.getoutput('syatemctl start httpd')
    print("web server started")
def aws():
    print("aws ")
def partitions():
    print("welcome to ")

if(__name__=='__main__'):
    import subprocess as sp
    import xml.etree.ElementTree as et
  
    print("WELCOME".center(60,'*'))
    print("menu is \n \
        1.date \n \
        2.cal \
        3.configure and start datanode \
        4.configure ,start namenode \
        5.start webserver \
        6.start and launch docker container\
        7.make partitions\
        8.create and start aws instances")
    n=int(input("Enter which option you want"))
    n1=input("Choose local or remote execution(l/r)")

    dl={1:date,2:cal,3:dataname,4:dataname,5:webserver,6:docker,7:partitions,8:aws}
    if(n1=='r'):
        ip=input("Enter ip address of remote machine")
        x=sp.getstatusoutput('ssh '+ip+' python3 /root/menu.py')
        if(x):
            sp.getoutput('scp menu.py '+ip+':/root')
            x=sp.getstatusoutput('ssh '+ip+' python3 /root/menu.py'+n)
    elif(n1=='l'):
        result=dl[n]()

