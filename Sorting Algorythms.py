# A few different basic sorting methods for integer lists - intro to python
# Import time and measure the different sorting methods?
# Bubble sort
def bubble_sort(int_list):
    i = 0   
    while i + 1 < len(int_list):
        if int_list[i] > int_list[i+1]:
            temp = 0
            temp = int_list[i+1]
            int_list[i+1] = int_list[i]
            int_list[i] = temp
            i = 0
        else:
            i+=1
    return int_list

#Comb Sort
def comb_sort(int_list):
    shrink = 1.25
    distance = int(len(int_list) / shrink)
    sort_complete = 0
    temp = 0
    while sort_complete == 0:
        for i in range(0,len(int_list)-distance):
            if int_list[i] > int_list[i+distance]:
                temp = int_list[i]
                int_list[i] = int_list[i+distance]
                int_list[i+distance] = temp
            i += 1
        if distance < 2:
            distance -= 1
        else :
            distance = int(distance / shrink)
        if distance == 0:
            sort_complete = 1
    return int_list

# Insertion Sort
def insertion_sort(int_list):
    i = 0
    k = 0
    while i < len(int_list)-1:
        
        if int_list[i+1] < int_list[i]:
            int_list[i+1], int_list[i] = int_list[i], int_list[i+1]
            if i != 0:
                i -= 1
        else:
            k += 1
            i = k
            
    return int_list

# Merge Sort
def merge_sort(int_list):

    if len(int_list) > 1:
        split = (len(int_list)//2)
        left = int_list[:split]
        right = int_list[split:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                int_list[k] = left[i]
                i += 1
                k += 1               

            else:
                int_list[k] = right[j]
                j += 1
                k += 1                   

        while i < len(left):
            int_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            int_list[k] = right[j]
            j += 1
            k += 1

    return int_list   

def main():
    test_list = [6,4,3,5,8,1,2,7,9,10]
    print(test_list)
    print("Sorted list")
    print(merge_sort(test_list))
    return

main()
