import xmlrpc.client

PORT = 8080

proxy = xmlrpc.client.ServerProxy(f"http://localhost:{PORT}/")
print(f"Type 1 for Addition\n"
      f"Type 2 for Subtraction\n"
      f"Type 3 for DISCONNECTING")

call = xmlrpc.client.MultiCall(proxy)
while True:
    task = int(input(f"Enter no. to perform task -"))
    if task == 3:
        print("DISCONNECTING...")
        break

    if task == 1:
        a = int(input("Value of A = "))
        b = int(input("Value of B = "))
        call.add(a, b)
        print(a, "+", b, "=", end=" ")
        result = call()
        print(result[-1])
    elif task == 2:
        a = int(input("Value of A = "))
        b = int(input("Value of B = "))
        call.sub(a, b)
        print(a, "-", b, "=", end=" ")
        result = call()
        print(result[-1])

    else:
        print("Wrong Call")
