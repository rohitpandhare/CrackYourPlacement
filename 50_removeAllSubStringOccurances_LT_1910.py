class Solution(object):
    def removeOccurrences(self, s, part):
        while True:  # Keep looping until no occurrences of `part` are left
            # Check if `part` exists in the string `s`
            if part not in s:
                # If `part` is no longer in `s`, return the final string
                return s
            else:
                # If `part` is found, remove the first occurrence by replacing it with an empty string
                s = s.replace(part, "", 1)  # The `1` ensures only the first occurrence is removed
