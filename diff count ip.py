"""
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
ips_between("10.0.0.0", "10.0.0.50")  ==   50
ips_between("10.0.0.0", "10.0.1.0")   ==  256
ips_between("20.0.0.10", "20.0.1.0")  ==  246

"""

"""
def ips_between(start, end):
    return sum((int(b) - int(a)) * 256 ** i for i, (b, a) in enumerate(reversed(zip(end.split('.'), start.split('.')))))
    
from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))
"""

def ips_between(start, end):

    start_ip = start.split(".")
    end_ip = end.split(".")
    diff_ip = [(int(end_ip[_]) - int(start_ip[_])) for _ in range(4)]
    cell_value = 0
    for o in diff_ip[:-1]:
        if o != 0:
            cell_value += o*256
    cell_value += diff_ip[-1]

    return cell_value


print(ips_between("10.0.0.0", "10.0.0.50"))
print(ips_between("10.0.0.0", "10.0.0.50")  ==   50)
print(ips_between("10.0.0.0", "10.0.1.0")   ==  256)
print(ips_between("20.0.0.10", "20.0.1.0")  ==  246)

print(ips_between("52.6.58.150", "52.14.115.176") ==

"""
Testing 129.54.81.147 and 129.197.175.107, Expecting: 9395672
60632 should equal 9395672
Completed in 0.01ms
Testing 154.175.108.245 and 154.227.60.203, Expecting: 3395542
982 should equal 3395542
Completed in 0.02ms
Testing 36.69.34.215 and 36.78.121.215, Expecting: 612096
24576 should equal 612096
Completed in 0.02ms
Testing 31.10.55.85 and 180.218.133.71, Expecting: 2513456626
111346 should equal 2513456626
"""
