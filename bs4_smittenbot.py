from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen('http://smittenicecream.com/menu/')
html_doc = response.read()
soup = BeautifulSoup(html_doc, "html.parser")

seasonal_flavor = []	# contains [ flavor_name ]
flavors = []			# contains [ flavor_name, [topping1, topping2, ...] ]
sundaes = []			# contains [ sundae_name1, sundae_name2, .. ]
vegan_pops = []			# contains [ vegan_pop_name1, vegan_pop_name2, .. ]
other_goodies = []		# contains [ goodie_name1, goodie_name2, .. ]


for item in soup.find_all("div", class_="row"):					# Go through each div with the class name "row"
	for child in item.findChildren():							# Go through each row's children
		
		if "Seasonal Flavor" in child.text:							# if the text "Seasonal Flavor" is found in this child
			item_child = item.find("div", class_="col title")			# Find child with seasonal flavor text
			flavor_text = item_child.text								# seasonal flavor text
			seasonal_flavor.append( flavor_text )						# put into seasonal_flavor array
		
		elif "Sundaes" in child.text:								# If the text "Sundaes" is found somewhere in this child
			for sundae in child.find_all("h5", class_="title"):		# Go through each title
				sundaes.append(sundae.text)							# Add each sundae to the sundaes array
		
		elif "Vegan Pops" in child.text:							# If the text "Vegan Pops" is found somewhere in this child
			for vegan_pop in child.find_all("h5", class_="title"):		# Go through each title
				vegan_pops.append(vegan_pop.text)						# Add each vegan pop to the vegan_pops array

		elif "Other Goodies" in child.text:							# If the text "Other Goodies" is found somewhere in this child
			for goodie in child.find_all("h5", class_="title"):			# Go through each title
				other_goodies.append(goodie.text)						# Add each goodie to the other_goodies array

# Find flavors
# Not included with the rest cause the data is not in a child div
for item in soup.find_all("a", class_="flavor-select"):			# Find all flavors through "flavor-select" class
	flavor_name = item.text											# Get flavor name
	data_toppings = item.get('data-toppings').split(',')			# Get toppings
	topping_names = []												# Create array for topping names
	for topping in data_toppings:									# For each topping
		name = soup.find("li", { "id" : topping }).text					# Find topping name on page by its ID
		topping_names.append(name)										# Add to topping name array
	flavors.append( [flavor_name, topping_names] )					# Add flavor and its toppings to the flavors list
				

print(seasonal_flavor)
print(flavors)
print(sundaes)
print(vegan_pops)
print(other_goodies)