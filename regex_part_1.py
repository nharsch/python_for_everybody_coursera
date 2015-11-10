import re

# search returns True False
# hand = open('test.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search(r'.*', line):
#         print line

# findall: will extract matches 
hand = open('test.txt')
text = hand.read()
matches = re.findall('l\S+', text)
print matches

# email matching
email_pattern = r'\S+@\S+'
emails = re.findall(email_pattern, text)
print emails

# capture group, only grab what's in the match group
preample_email_pattern = r'From ({})'.format(email_pattern)
print re.findall(preample_email_pattern, text) 
