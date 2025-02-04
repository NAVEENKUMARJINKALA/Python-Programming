input_list=list(map(int,input("Enter the numbers:").split()))
target=int(input("Enter the target:"))
subarrays=[]
for i in range(len(input_list)-2):
    subarray=input_list[i:i+3]
    if sum(subarray)==target:
        subarrays.append(subarray)
print("Valid subarrays of length 3 with the target sum:", subarrays)