import re
def replace_exclamation(s):
	return re.sub(r'[AEIOUaeiou]', '!', s)