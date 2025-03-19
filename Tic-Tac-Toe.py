# # expecting number seperated by ',' input here

# user_input = input("Enter the numbers :")
# # we can use map(int, user_input.split(','))
# number = user_input.split(",") 
# processing_list = list(map(int, number))

# # print(lists)    

# # single value input
# target = int(input("Enter target value :"))

# for num in processing_list :        
#     remaining_number = target - num 
#     if remaining_number in processing_list :
#         if remaining_number != num or processing_list.count(remaining_number) >1 :

#             a = num
#             b = target - num
#             print(a, b)

    

# user_input = input("Enter array of numbers :")

# if user_input.startswith('[') and user_input.endswith(']'):
#     needed_list = user_input[1:len(user_input)-1]
# else :
#     needed_list = user_input

# list1 = list(map(int ,needed_list.split(',')))

# target = int(input("Enter target value :"))

# for num in list1 :
#     remain = target - num 
#     if remain in list1 and (remain != num or list1.count(remain)>1) :
#         a = num 
#         b = remain
#         print(f'[{a},{b}]')




# class Solution:
#     def twoSum(self, nums, target) :
#         return_array = {}
#         for i, num in enumerate(nums):
#             remain = target - num 
#             if remain in return_array :
#                 return [return_array[remain] , i]
#             return_array[num] = i
#         return []
    
# def test():
#     para1 = [1,2,3,4,5,6]
#     para2 = 4
#     ret  = Solution().twoSum(para1, para2)
#     print(ret)

# test()           




class Solution:
    def twoSum(self, nums, target) :
        return_array = {}
        pairs = []
        for i, num in enumerate(nums):
            remain = target - num 
            if remain in return_array :
                pairs.append([return_array[remain] , i])
            return_array[num] = i
        return pairs
    
def test():
    para1 = [1,2,3,4,5,6,7,8,9]
    para2 = 6
    ret  = Solution().twoSum(para1, para2)
    print(ret)

test()           