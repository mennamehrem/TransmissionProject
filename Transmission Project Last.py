from scipy.stats import erlang


Area_city=250
no_of_users_km=4000
avg_nocalls_day=10/(60*24)
avg_call_duration=1
max_channels_cell=25
prob_drop=0.02

i=0

sectoring_array=[10,120,180,360]


total_no_users=Area_city*no_of_users_km



full_duplex=8/2

a_user=avg_nocalls_day*avg_call_duration

CarrierToInt=6.25
ResuseFactorWithoutSectoring=(CarrierToInt*6)/3



from scipy.optimize import brentq
import math


def erlang_b_formula(load, trunks):
    return (load ** trunks / math.factorial(trunks)) / sum([(load ** i) / math.factorial(i) for i in range(trunks + 1)])

def find_offered_load(pdrop, trunks, initial_load, tolerance, max_iterations):
    load = initial_load
    difference = erlang_b_formula(load, trunks) - pdrop
    iteration = 0

    while abs(difference) > tolerance and iteration < max_iterations:
        load =load-( difference )  
        #print(load)
        difference = erlang_b_formula(load, trunks) - pdrop
        iteration += 1
    #print(iteration)
    if iteration == max_iterations:
        print("Maximum iterations reached and the offered load wasn't calculated")

    return load

length=len(sectoring_array)

for i in range (length):
    no_of_sectors=360/sectoring_array[i]
    print(no_of_sectors)
    no_of_trunks=(int) ((max_channels_cell*full_duplex)/no_of_sectors)
    OfferedLoad = find_offered_load( prob_drop,no_of_trunks,0,1e-6,10000000)
    no_users=(OfferedLoad*no_of_sectors)/a_user
    no_cells=total_no_users/no_users
    print("Number of Cells:")
    print(no_cells)
    




