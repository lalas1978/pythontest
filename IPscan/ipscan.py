import socket
from contextlib import closing
from itertools import islice



#TODO: IF Webinterface exists, try to find out what type it is




def DoesWebinterfaceExist(ipaddress, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ipaddress, port))
        s.close()
    except:
        return False

    return True



def main():
   list = []
   for ip in range(1, 10):
      addr = "192.168.178." + str(ip)
      check = DoesWebinterfaceExist(addr, 80)
      if check == True:
         print(addr, "web interface EXISTS")
         list.append(addr)
      elif check == False:
         print(addr, "NO web interface")
      else:
         print("ERROR")

   print(list)


if __name__ == "__main__":
   main()
