class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        # First, build a list with the correct words, space-separated.
        retlist = [words[0]]
        for n in range(1, len(words)):
            curr_length = len(retlist[-1])
            n_length = len(words[n]) + 1  # Include at least 1 space before the word.
            if curr_length + n_length <= maxWidth:
                retlist[-1] = retlist[-1] + " " + words[n]
            else:
                retlist.append(words[n])
        # Now pad with spaces for all but the last line.
        for m in range(len(retlist) - 1):
            # Find all the indices with spaces
            indices = {idx: 1 for idx, char in enumerate(retlist[m]) if char == " "}
            # Find how much padding you need.
            padding = maxWidth - len(retlist[m])
            # If there are no spaces, add spaces to the end:
            if not indices:
                retlist[m] = retlist[m] + " " * padding
                continue
            # Split the padding across the indices.
            each, spread = divmod(padding, len(indices))
            left = 0
            newstr = ""
            for idx, cnt in indices.items():
                cnt = cnt + each
                cnt += 1 if spread > 0 else 0
                spread -= 1
                newstr = newstr + retlist[m][left:idx] + " " * cnt
                left = idx + 1
            newstr += retlist[m][left:]
            retlist[m] = newstr
        # Now pad the last line:
        retlist[-1] = retlist[-1] + " " * (maxWidth - len(retlist[-1]))
        return retlist
