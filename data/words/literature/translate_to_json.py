#!/usr/bin/env python

import json
import collections

input = open('input.json', 'r')

body = input.readlines()

word_dict = {}

word_dict['description'] = 'Words coined by shakespeare'

words = []

for line in body:
    subdict = {}
    components = line.split('(')
    #print components[0]
    #subdict['word'] = components[0]
    #if len(components) > 1:
    #    subdict['source'] = components[1].split(')')[0]
    #    print components[1].split(')')[0]
    #words.append(subdict)
    words.append(components[0])

word_dict['words'] = words
    
print word_dict

with open('output.json','w') as outfile:
    json.dump(word_dict, outfile)

input.close()
