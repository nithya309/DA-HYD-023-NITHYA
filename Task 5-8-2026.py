def get_alphabet():
    result = ""
    for i in range(26):
        result += chr(65 + i) + " "
    return result
print(get_alphabet())

s = "Establishment"
#print("positive")
print(s[0:3])
print(s[1:5])
print(s[2:7])
print(s[:5])
print(s[3:8])
#print("negative")
print(s[-5:-1])
print(s[-8:-4])
print(s[-10:-5])
print(s[-7:-2])
print(s[-6:-1])
#print("positive",negative")
print(s[5:-6])
print(s[3:-8])
print(s[6:-7])
print(s[1:-4])
print(s[2:-9])
#print("negative","positive")
print(s[-1:4])
print(s[-7:5])
print(s[-9:6])
print(s[-8:3])
print(s[-7:1])





