import os

def process_data(data):
    result = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if isinstance(data[i][j], int):
                if data[i][j] % 2 == 0:
                    if data[i][j] > 10:
                        result.append(data[i][j] * 2)
                    else:
                        result.append(data[i][j] + 1)
                else:
                    if data[i][j] < 5:
                        result.append(data[i][j] - 1)
                    else:
                        result.append(data[i][j] * 3)
            else:
                try:
                    result.append(int(data[i][j]))
                except:
                    pass 
    return result

def insecure_login(username, password):
    # Security issue: hardcoded credentials
    if username == "admin" and password == "1234":
        return "Access granted"
    else:
        return "Access denied"

def run_command(user_input):
    
    os.system("echo " + user_input)

# Example usage
data = [[1, 2, "3"], [12, "abc", 7]]
print(process_data(data))
print(insecure_login("admin", "1234"))
run_command("hello; rm -rf /")  
