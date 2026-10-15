text=input("Введите текст:")
print(text)

words=text.split()
print(words)
print(len(words))

frequency={}
for word in words:
    if word in frequency:
        frequency[word]=frequency[word]+1
    else:
        frequency[word]=1

print(frequency)

print("Частота каждого слова:")
for i in frequency:
    print(f"{i} - {frequency[i]}")
    
max_count= 0
most_common=""
for word in frequency:
    if frequency[word]>max_count:
        max_count= frequency[word]
        most_common = word


print(f"Самое частое слово: {most_common}, встречается {max_count} раз")



shortest=words[0]
longest=words[0]

for word in words:
    if len(word)<len(shortest):
        shortest=word
    if len(word)>len(longest):
        longest=word

print("Cамое короткое слово:",shortest)
print("Cамое длинное слово:",longest)


filtered=[]
for word in words:
    if len(word)>=3:
        filtered.append(word)

print("Анализ без слов короче 3 символов")
print("Общее количество слов:",len(filtered))

freq2={}
for word in filtered:
    if word in freq2:
        freq2[word]=freq2[word]+1
    else:
        freq2[word]=1

print()
print("Частота каждого слова:")
for word in freq2:
    print(word,"-",freq2[word])

max_count2=0
most_common2=""
for word in freq2:
    if freq2[word]>max_count2:
        max_count2=freq2[word]
        most_common2=word

print()
print("Самое частое слово:",most_common2,"-",max_count2,"раз")

shortest2=filtered[0]
longest2=filtered[0]

for word in filtered:
    if len(word)<len(shortest2):
        shortest2=word
    if len(word)>len(longest2):
        longest2=word

print("Самое короткое слово:",shortest2)
print("Самое длинное слово:",longest2)