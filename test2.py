import time


def main():
    print("Calculating time in minutes")
    print(2 + 3)
    print(2 + 3)
    print(2 + 3)
    print(2 + 3)
    print(2 + 3)
    print(2 + 3)
    print(2 + 3)



start = time.time()
main()
end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))