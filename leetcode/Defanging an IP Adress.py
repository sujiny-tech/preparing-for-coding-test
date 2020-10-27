address="1.1.1.1"

def defangIPaddr(address):
    return address.replace(".", "[.]")

print(defangIPaddr(address))