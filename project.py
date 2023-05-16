import os,random

def main():
    exit=True
    while exit is True:
        os.system('cls')
        print("\n")
        print("Algorithms\n".center(50))
        print("\n\nChoose an Algorithm:\n")
        print("  1  Bubble Sort")
        print("  2  Insertion Sort")
        print("  3  Selection Sort")
        print("  4  Linear Search")
        print("  5  Binary Search\n")
        print("  0  exit\n")

        try:
            choice=int(input("Enter your choice: "))
        except ValueError:
            input("Has to be an integer between 0 and 5\nPress Enter to try again ")
            continue
        match choice:
            case 0:
                exit=False
            case 1:
                BubbleSort(RandomList())
            case 2:
                InsertionSort(RandomList())
            case 3:
                SelectionSort(RandomList())
            case 4:
                LinearSearch(RandomList(1,15),random.randint(1,15))
            case 5:
                BinarySearch(sorted(RandomList(1,20,10)),random.randint(1,20))
            case _:
                input("Not an integer between 0 and 5. \nPress Enter to try again ")
    
    os.system('cls')

def RandomList(start=1,end=99,length=5):
    randomList=[random.randint(start,end) for _ in range(length)]
    return randomList

def BubbleSort(randomList):
    os.system('cls')
    print("\n")
    print("Bubble Sort\n".center(50))
    print(f"We have our unsorted list of elements: {randomList}\n")
    s=input("During each step for proceeding forward, press enter\nOr to return to the main menu, enter 0\nPress Enter to start\n")   
    if s=='0':
        return randomList
    print("\n")
    count=0
    n=len(randomList)
    for i in range(n):
        for j in range(0,n-i-1):
            count+=1
            print(f"{count}".center(50))
            print(f"We compare the elements on the index-{j+1} and index-{j+2}\n")
            print("              ",end="")
            for k in range(n):
                if k==j or k==(j+1):
                    print(f"({randomList[k]})",end=" ")
                else:
                    print(f"{randomList[k]}",end=" ")
            print("\n")
            if randomList[j]>randomList[j+1]:
                print(f"Since the element on the index-{j+1} is greater than the element on the index-{j+2}, we swap them. ")
                randomList[j],randomList[j+1]=randomList[j+1],randomList[j]
            else:
                print(f"Since the element on the index-{j+1} is not greater than the element on the index-{j+2}, we don't swap them.")
            print("\n              ",end="")
            for k in range(n):
                print(randomList[k],end=" ")
            print("\n\n\n")
            s=input("\n")
            if s=="0":
                return randomList
            

    print("The list has been sorted.")
    print(f"Sorted List: {randomList}")
    print("\n\n")
    input("Press Enter to go back to the main menu ")
    return randomList

def InsertionSort(randomList):
    os.system('cls')
    print("\n")
    print("Insertion Sort\n".center(50))
    print(f"We have our unsorted list of elements: {randomList}\n")
    s=input("During each step for proceeding forward, press enter\nOr to return to the main menu, enter 0\nPress Enter to start\n")   
    if s=='0':
        return randomList
    print("\n")
    newList=randomList
    count=0
    n=len(randomList)
    for i in range(1,n):   
        count+=1
        print(f"{count}".center(50))
        print("\n")
        print(f"Let our element-{i+1}: {randomList[i]}, be our key.")
        for k in range(n):
            if k==(i):
                print(f"({randomList[k]})",end=" ")
            else:
                print(f"{randomList[k]}",end=" ")

        print(f"\nWe traverse the list from its left until we find the element less than our key\n")
        key=randomList[i]
        j=i-1
        while j>=0 and key<newList[j]: 
            for k in range(n):
                if k==j or k==(i):
                    print(f"({randomList[k]})",end=" ")
                else:
                    print(f"{randomList[k]}",end=" ")
            print("\n")
            newList[j+1]=newList[j]
            j-=1
        
        newList[j+1]=key
        randomList=newList
        print("We have found the right spot for our key. The current list is:\n")
        for k in range(n):
            if k==j+1:
                print(f"({randomList[k]})",end=" ")
            else:
                print(randomList[k],end=" ")
        print("\n\n\n")
        s=input()
        if s=="0":
            return randomList

    print("The list has been sorted.")
    print(f"Sorted List: {randomList}")
    print("\n\n")
    input("Press Enter to go back to the main menu ")
    return randomList

def SelectionSort(randomList):
    os.system('cls')
    print("\n")
    print("Selection Sort\n".center(50))
    print(f"We have our unsorted list of elements: {randomList}\n")
    s=input("During each step for proceeding forward, press enter\nOr to return to the main menu, enter 0\nPress Enter to start\n")   
    if s=='0':
        return randomList
    print("\n")
    count=0
    n=len(randomList)
    for i in range(0,n-1):    
        count+=1
        print(f"{count}".center(50))
        print("\n")
        print(f"Let our element-{i+1}: {randomList[i]}, be our key.")
        for k in range(n):
            if k==(i):
                print(f"({randomList[k]})",end=" ")
            else:
                print(f"{randomList[k]}",end=" ")

        print(f"\nWe traverse the list from its right until we find the smallest element\n")
        key=randomList[i]
        idx=i
        j=i+1
        while j<n: 
            if randomList[j]<key:
                key=randomList[j]
                idx=j
            j+=1
                      
        print(f"The minimum element is on index {idx+1}: {randomList[idx]}. We swap the minimum element with our key\n")
        randomList[i],randomList[idx]=randomList[idx],randomList[i] 
        for k in range(n):
            if k==i or k==idx:
                print(f"({randomList[k]})",end=" ")
            else:
                print(randomList[k],end=" ")
        print("\n\n\n")   
        s=input()
        if s=="0":
            return randomList
        

    print("The list has been sorted.")
    print(f"Sorted List: {randomList}")
    print("\n\n")   
    input("Press Enter to go back to the main menu ")
    return randomList

def LinearSearch(randomList,key):
    os.system('cls')
    print("\n")
    print("Linear Search\n".center(50))
    print(f"Our given list is: {randomList}\nWe have to search for our key={key} in the list.\n")
    print("We go through the list from start to finish to find our key\n")
    n=len(randomList)
    for i in range(n):
        for k in range(n):
            if k==i:
                print(f"({randomList[i]})",end=" ")
            else:
                print(randomList[k],end=" ")
        print("\n")
        if randomList[i]==key:
            print(f"We have found our key on the index-{i+1}")
            print("\n\n")
            input("Press Enter to go back to the main menu\n ")
            return True
        else:
            print(f"{randomList[i]} is not our key\n\n")
    
    print("Our key isn't present on the list.")
    print("\n\n")
    input("Press Enter to go back to the main menu ")
    return False
  
def BinarySearch(randomList,key):
    os.system('cls')
    print("\n")
    print("Binary Search\n".center(50))
    print(f"For Binary Search, we need a sorted list\nOur given sorted list is: {randomList}\nWe have to search for our key={key} in the list.\n")
    n=len(randomList)
    s=input("During each step for proceeding forward, press enter\nOr to return to the main menu, enter 0\nPress Enter to start\n")   
    if s=='0':
        return randomList
    print("\n")
    start=0
    end=n-1
    count=0
    while start<=end:
        count+=1
        print(f"{count}".center(50))
        randomList=randomList[start:end+1]
        start=0
        end=len(randomList)-1
        print(f"Our current list is :{randomList}\n")
        mid=int((start+end)/2)
        print(f"Our middle value is {randomList[mid]}")
        for k in range(start,end+1):
            if k==mid:
                print(f"({randomList[k]})",end=" ")
            else:
                print(randomList[k],end=" ")
        print("\n")
        if randomList[mid]==key:
            print("We have found our key in the list")
            print("\n\n")
            input("Press Enter to go back to the main menu ")
            return True
        
        elif start==end:
            print(f"Since we have only one value left and it doesn't match our key, our key is not in the list")
            print("\n\n")
            input("Press Enter to go back to the main menu \n\n")
            return False
        
        elif randomList[mid]>key:
            print(f"Since our middle value is larger than our key. Our key must lie in the left half of the middle.")
            end=mid-1
        
        else:
            print(f"Since our middle value is smaller than our key. Our key must lie in the right half of the middle.")
            start=mid+1

        if start>end:
            print(f"Our key is not in the list")
            print("\n\n")
            input("Press Enter to go back to the main menu \n\n")
            return False

        print("\n\n")
        s=input("\n")
        if s=="0":
            return True

#-----------Test Functions-----------
def Bubble(randomList):
    n=len(randomList)
    for i in range(n):
        for j in range(0,n-i-1):
            if randomList[j]>randomList[j+1]:
                randomList[j],randomList[j+1]=randomList[j+1],randomList[j]
    return randomList

def Insertion(randomList):
    newList=randomList
    n=len(randomList)
    for i in range(1,n):
        key=randomList[i]
        j=i-1
        while j>=0 and key<newList[j]: 
            newList[j+1]=newList[j]
            j-=1
        
        newList[j+1]=key
        randomList=newList
        
    return randomList

def Selection(randomList):
    n=len(randomList)
    for i in range(0,n-1):    
        key=randomList[i]
        idx=i
        j=i+1
        while j<n: 
            if randomList[j]<key:
                key=randomList[j]
                idx=j
            j+=1
                      
        randomList[i],randomList[idx]=randomList[idx],randomList[i] 
        
    return randomList

def Linear(randomList,key):
    n=len(randomList)
    for i in range(n):
        if randomList[i]==key:
            return True
        
    return False

def Binary(randomList,key):
    n=len(randomList)
    start=0
    end=n-1
    while start<=end:
        randomList=randomList[start:end+1]
        start=0
        end=len(randomList)-1
        mid=int((start+end)/2)
        if randomList[mid]==key:
            return True
        elif start==end:
            return False
        
        elif randomList[mid]>key:
            end=mid-1
        
        else:
            start=mid+1

        if start>end:
            return False


if __name__ == "__main__":
    main()
    os.system('cls')