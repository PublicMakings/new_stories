## IMPORTS
import pronounced, json, random

#########################################################################

title = "NEW NURSERY RHYMES for A NEW NATURE"
## Nursery Rhymes
print("*"*42 + "\n"+" "*3+title+"\n"+"*" *42 + "\n")

text = title.lower()
out = list()
for word in text.split():
   rhymes = pronounced.rhymes(word)
   if len(rhymes) > 0:
     out.append(random.choice(rhymes))
   else:
     out.append(word)

print(' '.join(out).title())


#########################################################################

## LOAD JSON Pattern data


with open('rhymes.json') as json_data:
	data = json.load(json_data) ##okay I have a list with indexs

### pick a random poem
###	measure length & if it is long take a slice of it


### iterate through ## not necessary
#	for i in data['rhymes']:
#		print(i)
	#       print(data['rhymes'][i])
        

#########################################################################
##~~FOR THE FUTURE~~~ 
## LOAD TEXTS -- this may actually live in json, but could be scraped, eventually
## URLS - 	http://www.gutenberg.org/files/23794/23794-h/23794-h.htm
## 		http://www.gutenberg.org/files/10607/10607-h/10607-h.htm
#########################################################################

## LOAD DICTIONARIES - CMU & WORDNIK do i need to do this???

#########################################################################
## FUNCTIONS

def makeMeter():
phones_list = pronouncing.phones_for_word("snappiest")
pronouncing.stresses(phones_list[0])

## RANDOMLY SELECT PATTERN


## CREATE WORD ARRAY of forest meanings
## MAKE A DICTIONARY?



## OUTPUT

#########################################################################
## post python?

## SEND TO SPEAKER BOT

######################
## ARDUINO/PI - generates nightlight from text data
## plays audio