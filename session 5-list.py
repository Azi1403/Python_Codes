people = ['mehrnaz','azam','mehdi','matin']
nums = [45,101,55,12.5]
mix = ['sara',15,'azam',55.5]

information = ['sara','hatami',33,1.64,True,['saman','sasan']]



print(people[0]) #mehrnaz
print(people[2]) #mehdi
print(people[-1]) #matin
print(people[1:3]) #azam,mehdi
print(people[::-1])# reverse
print(information[5])# saman , sasan
print(information[5][1]) #sasan


people.append('ilia')
print(people)

nums.remove(55) # remove a member of list
mix.remove('sara')
print(nums)

langs = ['java','c','c++','sql','ruby']
langs.pop(3) #index num remove
print(langs)

langs.pop() # remove last member
print(langs)

langs[1] = 'c#' # replace
print (langs)

scores = [10,12.5,55,14,101,1]
print (sum(scores))
print (max(scores))
print (min(scores))
 
print(sorted(scores)) #sort num
print(sorted(people)) #sort alphabet

print(sorted(scores,reverse=True))

print(len(scores))