import time
from datetime import datetime as dt
hosts_path=r"host/file/path"
redirect = "127.0.0.1"
website_list = ["blocking","list"]

while True:
    now = dt.now()
    hour = now.hour
    if hour < 9 or hour > 18 :
        with open(hosts_path, 'r+') as hf :
            content = hf.readlines()
            hf.seek(0)
            for line in content :
                flag = True
                for site in website_list :
                    if site in line :
                        flag = False
                        break
                if flag:
                    hf.write(line)
            hf.truncate() 
            hf.close()
                            
        print('Unlocked, and have fun :)')
    else :
        with open(hosts_path, 'r+') as hf :
            content = hf.read()
            for site in website_list:
                if site not in content:
                    hf.write(redirect + '  ' + site + '\n')
                else :
                    pass
            hf.close()
        print('Locked, hard work! :)')

    time.sleep(600)

    