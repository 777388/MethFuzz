import sys
import os


print("Usage: python methfuzz.py path/to/iplist.txt output.txt")
input1 = sys.argv[1]
output1 = open(sys.argv[2], 'w')
method = "C:/Users/chris/SecLists/Fuzzing/http-request-methods.txt"
with open(input1, 'r') as filer:
    for line in filer:
        with open(method, 'r') as filee:
            for methodline in filee:
                if (len(line.rstrip()) and len(methodline.rstrip())):
                    process = os.popen("curl -m 3.3 -so /dev/null https://"+line.rstrip()+"/"+" -X "+methodline.rstrip()+" -w %{http_code}").read()
                    if process == '200':
                        print("https://"+line.rstrip()+"/"+"  "+methodline.rstrip()+"  "+process+"\r")
                        print("https://"+line.rstrip()+"/"+"  "+methodline.rstrip()+"  "+process+"\r", file=output1)
                    if process == '403':
                        process = os.popen("curl -m 3.3 -so /dev/null https://"+line.rstrip()+"/"+" -X "+methodline.rstrip()+" --header 'Host: 127.0.0.1' -w %{http_code}").read()
                        if process =='200':
                            print("https://"+line.rstrip()+"/"+" -X "+methodline.rstrip()+" --header 'Host: 127.0.0.1'"+process+"\r")
                            print("https://"+line.rstrip()+"/"+" -X "+methodline.rstrip()+" --header 'Host: 127.0.0.1'"+process+"\r", file=output1)
                    process = os.popen("curl -m 3.3 -so /dev/null http://"+line.rstrip()+"/"+" -X "+methodline.rstrip()+" -w %{http_code}").read()
                    if process == '200':
                        print("http://"+line.rstrip()+"/"+"  "+methodline.rstrip()+"   "+process+"\r")
                        print("http://"+line.rstrip()+"/"+"  "+methodline.rstrip()+"   "+process+"\r", file=output1)
                    if process == '403':
                        process = os.popen("curl -m 3.3 -so /dev/null http://"+line.rstrip()+"/"+" -X "+methodline.rstrip()+" --header 'Host: 127.0.0.1' -w %{http_code}").read()
                        if process =='200':
                            print("http://"+line.rstrip()+"/"+" -X "+methodline.rstrip()+" --header 'Host: 127.0.0.1'"+process+"\r")
                            print("http://"+line.rstrip()+"/"+" -X "+methodline.rstrip()+" --header 'Host: 127.0.0.1'"+process+"\r", file=output1)
                else:
                    break
                print("https://"+line.rstrip()+"/"+"  "+methodline.rstrip()+"\r", end="\r", flush=True)                  

                
