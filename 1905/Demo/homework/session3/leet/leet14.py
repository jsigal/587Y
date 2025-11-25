# # Leet Code Problem 14 Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string

def longestCommonPrefix(strs):
    prefix = strs[0]
    for item in strs[1:]:
        # look for common prefix
        while not item.startswith(prefix) and prefix:
            prefix = prefix[:-1]
        # deal with empty
        if not prefix:
            return ""
    return prefix


strs = ["flower","flow","flight"]
ret = longestCommonPrefix(strs)
print(f'the list {strs} has an LCP of "{ret}"')
strs = ["dog","racecar","car"]
ret = longestCommonPrefix(strs)
print(f'the list {strs} has an LCP of "{ret}"')
strs = ["texting","texted","texts"]
ret = longestCommonPrefix(strs)
print(f'the list {strs} has an LCP of "{ret}"')