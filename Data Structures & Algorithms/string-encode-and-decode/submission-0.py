class Solution:

    def encode(self, strs: List[str]) -> str:
        pieces = []
        for string in strs:
            length = str(len(string))
            final_string = f"{length}#{string}"
            pieces.append(final_string)
        encoded_string = "".join(pieces)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            start = j + 1
            end = start + length
            decoded_string = s[start:end]

            decoded_list.append(decoded_string)
            i = end
        
        return decoded_list

        




