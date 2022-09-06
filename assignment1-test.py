# Create a function that checks whether two words are anagrams of each other.

# Two words are anagrams of each other if they have the same number of characters (letters) and use all of the same letters.

# For example: star and rats are anagrams of each other because they are of the same length and use all the same letters, the same number of times.

# Another example is cars and scar. Note again that they not only use the same letters but they use these letters the same amount of times.

# Your function must take two strings and return "True" if they are anagrams of each other; False otherwise.

# Your solution must ignore casing (upper, lower) and spaces such that "I am lord voldemort" is found to be an anagram of "Tom Marvolo Riddle".

# Submit your work by sending the link to your GitHub repository containing the described python function.


word1 = "star"
word2 = "rats"

# check the length of the words against each other


def SameLength(word1, word2):
    if len(word1) == len(word2):
        # return True
        print("same length")
    else:
        # return False
        print("not same length")

# check that the words have all the same letters


# def SameChar(word1, word2):
    # find a way to take all the letters of 1 string and see if each individual letter matches any of the letters from the other string

    # find a way to ISOLATE each letter from str1 then compare it to each letter in str2. When the letter is found move on to the next letter from str1 and repeat until all letters from st1 have been compared to str2.
    # chars = word1.integer()
    # if chars == word2.integer():
    #     return True
    #     print(found)
