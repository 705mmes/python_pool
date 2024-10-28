import time

print("Seconds since January 1, 1970: ", time.mktime(time.gmtime()), " or ",
    "{:e}".format(time.mktime(time.gmtime())), " in scientific notation")
print(time.strftime("%b %d %Y", time.localtime()))