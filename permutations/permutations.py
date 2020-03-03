import unittest

def permutations(string):
    # Base case
    if len(string) <= 1:
        return string
    
    ret = []
    for i in range(len(string)):
        first_letter = string[i]
        
        perm_string = string[:i]
        perm_string += string[i+1:]

        perms = permutations(perm_string)
        
        # Build up the permutations
        for perm in perms:
            temp_perm = first_letter + perm
            if temp_perm not in ret:
                ret.append(temp_perm)
      
    return ret

# Test it
class TestIt(unittest.TestCase):
    def test(self):
        # self.assertEqual(sorted(permutations('a')), ['a']);
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])

if __name__ == '__main__':
    unittest.main()