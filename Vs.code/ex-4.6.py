# Computation function...
def computepay(h,r):
    if h>40:
        exh = h - 40
        expay= exh * r * 1.5
        pay = 40 * r + expay
    else:
        pay = h*r
    return pay
# Input and output...
ntry = 3
while ntry > 0:
    hrs = input("Enter Hours:")
    rate = input("Enter rate:")
    ntry =ntry -1
    try:
        hrs = float(hrs)
        rate = float(rate)
        break
    except:
        print("Error please put valid number....", ntry, "try left..")


p = computepay(float(hrs),float(rate))
print("Pay",p)
