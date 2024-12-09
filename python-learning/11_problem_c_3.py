name = input("Enter your name ")
print(f"Good morning {name}")

letter = '''Dear <|Name|>,
You are selected:
<|Date|> 
'''

print(letter.replace(f"<|Name|>", "Rahul").replace("<|Date|>","2 oct 2058"))