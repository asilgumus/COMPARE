import numpy as np
#import matplotlib.pyplot as plt

def listDiff(list1, list2):
    diff_list = []
    if len(list1) != len(list2):
        lenDiff = abs(len(list1) - len(list2))
        for i, k in zip(list1, list2):
            diff = abs(i - k)
            diff_list.append(diff)
        diff_list.extend([None] * lenDiff)
        return diff_list   
    else:
        for i, k in zip(list1, list2):
            diff = abs(i - k)
            diff_list.append(diff)
        return diff_list

def isListEqual(list1, list2):
    if list1 == list2:
        return True
    else:
        return False
    
def whichDiff(list1,list2):
    index = 0
    diff_list = []
    if len(list1) != len(list2):
        lenDiff = abs(len(list1) - len(list2))
        
        for i, k in zip(list1, list2):
            diff = abs(i - k)
            if diff != 0:
                diff_list.append(index)
            index += 1
        diff_list.extend([None] * lenDiff)
        return diff_list   
    else:
        for i, k in zip(list1, list2):
            diff = abs(i - k)
            if diff != 0:
                diff_list.append(index)
            index += 1
        return diff_list
    
def missingElements(list1, list2):
    if len(list1) != len(list2):
        return [x for x in list2 if x not in list1]
    else:
        return False
    
def extraElements(list1, list2):
    if len(list1) != len(list2):
        return [x for x in list1 if x not in list2]
    else:
        return False
    
def duplicates(list):
    list.sort()
    list_dup = []
    for i in range(len(list) - 1):
        if list[i] == list[i+1]:
            list_dup.append(list[i])
    return list_dup

def isListEqualUNO(list1, list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
    
def meanDifference(list1,list2):
    mean1 = np.mean(list1)
    mean2 = np.mean(list2)
    meanDiff = mean1-mean2
    return meanDiff

def maxDifference(list1, list2):
    if not list1 or not list2:
        return None 
    max = np.max(list1)
    min = np.min(list2)
    diff = max-min
    return diff

def mean_percentage_deviation(list1, list2):
    a, b = np.array(list1), np.array(list2)
    min_len = min(len(a), len(b)) 
    diffs = np.abs(a[:min_len] - b[:min_len])
    return np.mean(diffs / np.abs(b[:min_len])) * 100

        
list1 = [1,-2,3,4,5,6,6,2,3,4,7,7]
list2 = [1,2,3,4,5]
list3 = [1,2,3,5,4]
print(maxDifference(list3,list1))