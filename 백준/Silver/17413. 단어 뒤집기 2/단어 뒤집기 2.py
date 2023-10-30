string = input()

tmp = ""
result = ""
reverse = True
for s in string:
	if s == " ":
		result += tmp
		tmp = ""
		result += " "
	elif s == "<":
		reverse = False
		result += tmp
		result += "<"
		tmp = ""
	elif s == ">":
		result += tmp
		result += ">"
		reverse = True
		tmp = ""
	else:
		if reverse:
			tmp = s + tmp
		else:
			tmp += s

result += tmp

print(result)