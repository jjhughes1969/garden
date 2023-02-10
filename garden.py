
# Importing spaCy and loading the English language model.
import spacy
nlp = spacy.load('en_core_web_sm')

# Defining a list of five garden path sentences.
gardenpathSentences = [
    "The French government plans to raise taxes were defeated.",
    "Red tape holds up new £1 million bridge.",
    "The man whistling Matilda tunes pianos.",
    "The florist sent the flowers was pleased.",
    "British Left Waffles on Falkland Islands."
]

# Tokenise each sentence in the list.
for i in range(len(gardenpathSentences)):
    gardenpathnlp = nlp(gardenpathSentences[i])
    print("")
    print([(token, token.orth_, token.orth) for token in gardenpathnlp])
    print("")

# Perform entity recognition on each sentence in the list and using spacy.explain to print the explanation for each entity.
for i in range(len(gardenpathSentences)):
    gardenpathnlp = nlp(gardenpathSentences[i])
    for ent in gardenpathnlp.ents:
        print(ent.text, ent.label_, ent.label)
        print(f"{ent.label_} = {spacy.explain(ent.label_)}\n")

'''
The entity "Matilda" was classified ORG, as an organisation ("companies, agencies, institutions, etc") 
In the context of the sentence it was meant to refer to the musical "Matilda" from which the man was whistling tunes
The entiry WORK_OF_ART would therefore have been more appropriate in this context

The entity "Falkland Islands" was classified GPE, as "countries, cities, states"
This is the correct classification
However the original version of the sentence used "Falklands" (also in common usage) which was incorrectly classified ORG
'''        



