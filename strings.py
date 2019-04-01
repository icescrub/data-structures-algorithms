"""
String algorithms are another name for pattern matching algorithms.

manacher's alg (G4G)
levenshtein distance (string *similarity*, not exact matching)
tries
suffix trees
regexes
COMPLEX:
	aho-corasick's algo (resources not readily available)
	NLP (n-gram models, bayesian hierarchial models, clustering)
	Google/MS implementations (PageRank etc for search engines)



string algos: HUGE with google. be ready...
most important algos for MS, amazon?

exec(open('/home/duchess/Desktop/strings').read())
s = 'xabcabzabc'
pattern = 'abc'

exec(open('/home/duchess/Desktop/strings').read())
s = [0,1,1,0,0,0,1,1,1,0,0,0,1]
pattern = [0,0,1]

exec(open('/home/duchess/Desktop/strings').read())
s = "GEEKS FOR GEEKS"
pattern = "GEEK"
"""

import string

def naive_search(s, pattern):
    """Returns whether pattern found in string."""
    for i in range(len(s) - len(pattern) + 1):
        matched = all(s[i+j] == pattern[j] for j in range(len(pattern)))
        if matched:
            return True
    return False

def naive_search_all(s, pattern):
    """Returns positions of all occurrences of the pattern in the string. O(m^2)."""
    for i in range(len(s) - len(pattern) + 1):
        matched = all(s[i+j] == pattern[j] for j in range(len(pattern)))
        if matched:
            print("match found at index " + str(i))

def naive_search_2(s, pattern):
    """Optimized naive search. Jumps ahead by j instead of 1 (by default)."""
    i = 0
    while i < len(s) - len(pattern) + 1:
        for j in range(len(pattern)):
            if s[i+j] != pattern[j]:
                break
            j += 1
        if j == len(pattern):
            print("match found at index " + str(i))
            i += len(pattern)
        else:
            i += max(1, j)

def z_algorithm(s, pattern):
    """Linear search. O(m+n) time complexity, linear space complexity. Same complexity as KMP but easier to understand."""

    def compute_z_naive(str):
        N = len(str)
        z = [0]*N

        for i in range(1, N):
            count = 0
            while i+count < N and str[n] == str[i+count]:
                count += 1
            z[i] = count

        return z

    def compute_z(str, sentinel=False):
        N = len(str)
        z = [0]*N # NOTE: pre-allocation of list is better than dynamically reallocating, apparently.
        z[0] = N

        zbox_L, zbox_R = 0, 0
        for i in range(1, N):
            # CASE 1: i is within the box.
            if i < zbox_R:
                k = i - zbox_L
                if z[k] < zbox_R - i:
                    z[i] = z[k]
                    continue
                zbox_L = i
            else:
                zbox_L = zbox_R = i
            while zbox_R < N and str[zbox_R - zbox_L] == str[zbox_R]:
                zbox_R += 1
            z[i] = zbox_R - zbox_L
            if not sentinel: # THIS IS FOR STRINGS WITHOUT SENTINEL VALUES GIVEN
                z[i] = min(N, z[i])

        return z

    z = compute_z(pattern + s)
    z_corrected = z[len(pattern):]
    result = [i for i,x in enumerate(z_corrected) if x == len(pattern)]
    return result

def boyer_moore_horspool(text, pattern):
    """Uses Bad Match Table ONLY."""

    def make_bad_match_table(pattern):
        # Make dictionary using the letters in the text. All other letters are equal to length of pattern.

        M = len(pattern)
        d = dict()

        for i,letter in enumerate(pattern):
            if i == M-1 and letter not in d:
                d[letter] = M
            else:
                d[letter] = M-i-1
        return d

    table = make_bad_match_table(pattern)
    M = len(pattern)
    N = len(text)
    i = M-1
    j = M-1
    result = []

    while i < N:
        if text[i] == pattern[j]:
            if j == 0: # Complete success. Reset j, and skip ahead ENTIRE pattern length in text index.
                result.append(i)
                i += 2*M-1
                j = M-1
            else: # Partial success. Checks next pair of letters backwards.
                i -= 1
                j -= 1
        else: # Failure. Reset j, and skip ahead MAXIMAL characters in text index.
            i += table.get(text[i], M)
            j = M-1 # Resets j position.
    return result

def boyer_moore(haystack, needle):
    """
    This uses Bad Match Table AND Good Suffix Table.
    """

    def make_char_table(needle):
        """
        Makes the jump table based on the mismatched character information.
        """
        table = {}
        for i in range(len(needle) - 1):
            table[needle[i]] = len(needle) - 1 - i
        return table
     
    def make_offset_table(needle):
        """
        Makes the jump table based on the scan offset in which mismatch occurs.
        """
        table = []
        last_prefix_position = len(needle)
        for i in reversed(range(len(needle))):
            if is_prefix(needle, i + 1):
                last_prefix_position = i + 1
            table.append(last_prefix_position - i + len(needle) - 1)

        print(table)

        for i in range(len(needle) - 1):
            slen = suffix_length(needle, i)
            print(slen)
            table[slen] = len(needle) - 1 - i + slen
            print(table)
        return table
     
    def is_prefix(needle, p):
        """
        Is needle[p:end] a prefix of needle?
        """
        j = 0
        for i in range(p, len(needle)):
            if needle[i] != needle[j]:
                return 0
            j += 1   
        return 1
         
    def suffix_length(needle, p):
        """
        Returns the maximum length of the substring ending at p that is a suffix.
        """
        length = 0;
        j = len(needle) - 1
        for i in reversed(range(p + 1)):
            if needle[i] == needle[j]:
                length += 1
            else:
                break
            j -= 1
        return length

    if len(needle) == 0:
        return 0
    char_table = make_char_table(needle)
    offset_table = make_offset_table(needle)
    i = len(needle) - 1
    while i < len(haystack):
        j = len(needle) - 1
        while needle[j] == haystack[i]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += max(offset_table[len(needle) - 1 - j], char_table.get(haystack[i],-1));
    return -1

def rabin_karp(s, pattern):
    """Uses rolling hash to find pattern. Rolling hashes used in rsync and Low Bandwidth Network Filesystem, too."""
    d = 256 # Number of characters in the input alphabet.
    q = 101 # A prime number. Any large prime will do.
    N = len(s)
    M = len(pattern)
    i = j = 0
    hash_p = hash_s = 0
    h = 1
    result = []

    # This is equal to [d**(M-1)]%q.
    for i in range(M-1):
        h = (h*d)%q

    # Calculate hash of pattern.
    for i in range(M):
        hash_p = (d*hash_p + ord(pattern[i]))%q

    # Calculate hash of first window of text, so we can begin comparing hashes.
    for i in range(M):
        hash_s = (d*hash_s + ord(s[i]))%q

    for i in range(N-M+1):
        if hash_p == hash_s: # Partial success. False positives are possible, so manually check for equality.
            match = True
            for j in range(M):
                if s[i+j] != pattern[j]:
                    match = False
                    break
            if match: # Complete success.
                result.append(i)

        # Rolling hash. Remove leading digit, add trailing digit, make positive.
        if i < N-M:
            hash_s = (hash_s - h*ord(s[i]))%q # Remove letter at index i.
            hash_s = (d*hash_s + ord(s[i+M]))%q # Add letter at index i+M.
            hash_s = (hash_s+q)%q # Make sure hash_s >= 0.

    return result

def KMP(s, pattern):
    """ 
    Creates Longest Prefix-Suffix table to skip prefixes that match the suffixes of the pattern and text.
    String -> String -> [Int]
    """

    def LSP(pattern):
        """ Longest Prefix-Suffix table. String -> [Int]"""
        arr = [0]*len(pattern)

        for i in range(1, len(pattern)):
            j = arr[i-1]
            while j>0 and pattern[j] != pattern[i]:
                j = arr[j-1]
            if pattern[j] == pattern[i]:
                j += 1
            arr[i] = j

        return arr

    LSP_list = LSP(pattern)
    result = []
    j = 0

    for i in range(len(s)):
        while j>0 and s[i] != pattern[j]:
            j = LSP[j-1]
        if s[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            result.append(i-(j-1))
            j = LSP[j-1]
    
    return result
