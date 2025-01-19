class Solution(object):
    def reverse(self, x):
        # Define 32-bit integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Reverse the string representation
        if x < 0:
            reversed_x = int('-' + str(-x)[::-1])  # Handle negative
        else:
            reversed_x = int(str(x)[::-1])  # Handle positive
        
        # Check 32-bit integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x

# Testing the function
solution = Solution()
s = 120
reverse_integer = solution.reverse(s)
print(reverse_integer)  # Output: 21


solution = Solution()
s = 120
reverse_integer = solution.reverse(s)
print(reverse_integer)