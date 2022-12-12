import string
test_string = "The Centre for Development of Advanced Computing is an Indian autonomous scientific society, operating under the Ministry of Electronics and Information Technology"
# printing original string
print ("The original string is: " + test_string)
# using sum() + strip() + split() function
res = sum([i.strip(string.punctuation).isalpha() for i in
test_string.split()])
# no of words
print ("The number of words in string are : " + str(res))