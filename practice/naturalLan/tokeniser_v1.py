from nltk import word_tokenize, sent_tokenize, pos_tag 
 
text = """On the whole, SPECTRE that maintains the essence of Bond film with 
enough doses of gadgets, car chases, stunts, wine and women, could have
featured a better title track, since Sam Smith's 'Writing's On The Wall'
appears to be rather sluggish when compared to other Bond films. However
SPECTRE that in essence features the return of Bond is definitely worth a
watch."""

tokens = word_tokenize(text)

print tokens
print len(tokens)

tagged_tokens = pos_tag(tokens)

print type(tagged_tokens)
print tagged_tokens
