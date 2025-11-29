

# This script is designed to be run from INSIDE the Mininet CLI.
# Usage: mininet> py exec(open('second_moment.py').read())

print("Starting OSPFv2 on router r4")

# In the Mininet CLI 'py' scope, r1, r2, etc. are available as global variables.

r4.cmd('/usr/lib/frr/ospfd -d -f /home/advnet/Desktop/lab4/configs/ospfd_r4.cfg -i /home/advnet/Desktop/lab4/run/ospfd_r4.pid -z /home/advnet/Desktop/lab4/run/frr_r4.api -u frr -g frr')

print("Starting OSPFv3 on router r4")

r4.cmd('/usr/lib/frr/ospf6d -d -f /home/advnet/Desktop/lab4/configs/ospf6d_r4.cfg -i /home/advnet/Desktop/lab4/run/ospf6d_r4.pid -z /home/advnet/Desktop/lab4/run/frr_r4.api -u frr -g frr')
