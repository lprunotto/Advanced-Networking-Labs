

# This script is designed to be run from INSIDE the Mininet CLI.
# Usage: mininet> py exec(open('second_moment.py').read())

print("Starting OSPFv3 on routers...")

# In the Mininet CLI 'py' scope, r1, r2, etc. are available as global variables.
routers = [r1, r2, r3, r4, r5]
index = 0

for router in routers:
    index += 1
    if index != 4:
        print("Starting ospf6d on r%s" % index)
        router.cmd('/usr/lib/frr/ospf6d -d -f /home/advnet/Desktop/lab4/configs/ospf6d_r%s.cfg -i /home/advnet/Desktop/lab4/run/ospf6d_r%s.pid -z /home/advnet/Desktop/lab4/run/frr_r%s.api -u frr -g frr' % (index, index, index))



