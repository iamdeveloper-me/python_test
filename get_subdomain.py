import re

"""
	Url for test on regex101 https://regex101.com/r/Yeh7KO/1
"""



regex = r"(^(?:http[s]?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)*(.*?)\.(?=[^\/]*\..{2,5}))"

# Urls for testing all the cases
urls = [
	"https://test.google.com",
	"http://www.test.google.com",
	"https://blog.microsoft.com/test.html",
	"https://www.blog.microsoft.com/test/test",
	"https://www.microsoft.com",
	"https://google.com"
]


# Loop to get subdomain for each url
for url in urls:

	# Find match case
	result = re.findall(regex, url)

	if result and result[0][1]!="www":
		print (url, result[0][1])

	else:
		print(url, "no subdomain")  
