dict = {
"piekarnia": ["chleb", "pączek", "bułki"],
"warzywniak": ["marchew", "seler", "rukola"]
}

key_list = list(dict.keys())
counter = 0
print()

for key in dict:
  values = dict.get(key)
  values_titled = []
  for value in values:
    values_titled.append(value.title())
    counter += 1
  print("Idę do", key.title(), "kupuję tu następujące rzeczy:", values_titled)
