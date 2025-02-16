class Solution(object):
    def constructDistancedSequence(self, n):
        # Create an answer list of size (2*n - 1) filled with zeros.
        # This list will hold the final sequence.
        ans = [0] * (2 * n - 1)  # <sup data-citation="2" className="inline select-none [&>a]:rounded-2xl [&>a]:border [&>a]:px-1.5 [&>a]:py-0.5 [&>a]:transition-colors shadow [&>a]:bg-ds-bg-subtle [&>a]:text-xs [&>svg]:w-4 [&>svg]:h-4 relative -top-[2px] citation-shimmer"><a href="https://blog.heycoach.in/construct-the-lexicographically-largest-valid-sequence-solution-in-python/">2</a></sup>

        # "canput" is a list to keep track of available numbers.
        # canput[i] is 1 (available) if number (i+1) can be placed; once used, it is set to 0.
        canput = [1] * n  # <sup data-citation="2" className="inline select-none [&>a]:rounded-2xl [&>a]:border [&>a]:px-1.5 [&>a]:py-0.5 [&>a]:transition-colors shadow [&>a]:bg-ds-bg-subtle [&>a]:text-xs [&>svg]:w-4 [&>svg]:h-4 relative -top-[2px] citation-shimmer"><a href="https://blog.heycoach.in/construct-the-lexicographically-largest-valid-sequence-solution-in-python/">2</a></sup>

        # Define a helper function to try placing numbers starting from index 'idx'
        def find(idx):
            # Skip positions that have already been filled.
            while idx < (2 * n - 1) and ans[idx] != 0:
                idx += 1
            # If we have reached the end of the list, then we have a complete valid sequence.
            if idx == (2 * n - 1):
                return True  # <sup data-citation="2" className="inline select-none [&>a]:rounded-2xl [&>a]:border [&>a]:px-1.5 [&>a]:py-0.5 [&>a]:transition-colors shadow [&>a]:bg-ds-bg-subtle [&>a]:text-xs [&>svg]:w-4 [&>svg]:h-4 relative -top-[2px] citation-shimmer"><a href="https://blog.heycoach.in/construct-the-lexicographically-largest-valid-sequence-solution-in-python/">2</a></sup>

            # Try placing numbers in descending order (largest first for lexicographical order)
            for i in range(n - 1, -1, -1):
                # Proceed only if the number (i+1) is still available.
                if canput[i]:
                    # For numbers greater than 1, they must be placed twice with exactly (i) numbers in between.
                    # Check if there is enough space to place the second occurrence,
                    # and ensure that the target position is not already occupied.
                    if i != 0 and (idx + i + 1 >= (2 * n - 1) or ans[idx + i + 1] != 0):
                        continue  # Skip this number if it cannot be placed validly.

                    # Place the number (i+1) at the current free index.
                    ans[idx] = i + 1
                    # If the number is greater than 1, place its second occurrence at index (idx + i + 1).
                    if i != 0:
                        ans[idx + i + 1] = i + 1

                    # Mark this number as used so that it won't be placed again.
                    canput[i] = 0

                    # Recursively attempt to fill in the rest of the sequence.
                    if find(idx + 1):
                        return True  # A valid sequence has been found.
                    else:
                        # Backtracking step: if the placement didn't lead to a solution,
                        # reset the flags and clear the placements.
                        canput[i] = 1
                        ans[idx] = 0
                        if i != 0:
                            ans[idx + i + 1] = 0

            # If no number can be placed at the current index to form a valid sequence, return failure.
            return False

        # Begin the recursive search starting from index 0.
        find(0)
        # Once the sequence is complete, return it.
        return ans
