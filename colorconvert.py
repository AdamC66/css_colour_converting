# Breaking down the problem
# This task can be broken down into several sub-tasks, each of which may be handled by separate libraries:

# Open the CSS file in Python
# Parse the CSS code into a useful data structure that allows you to iterate through the style rules and isolate the property 
# (e.g. 'color', 'background-color') from the value (e.g. 'palegoldenrod')
# Automatically convert the named CSS colour into a hex code string
# Put it back together into a string
# Save the results into a new .css file
# Libraries to use
# Use the Python standard library to open and read the CSS file, and to save to a new file at the end (steps 1 and 5)
# Use cssutils to parse the contents of the file (steps 2 and 4)
# Use webcolors to convert from colour name to hex code (step 3)

import cssutils
import webcolors

# stylesheet = open('main.css','w+')

sheet = cssutils.parseFile('main.css')

for rule in sheet:
    if rule.type == rule.STYLE_RULE:
        for property in rule.style:
            if property.name == 'color':
                if property.value[0]!= '#':
                    if property.value not in ['inherit']:
                        print(property.value)
                        print(webcolors.CSS3_NAMES_TO_HEX[property.value])
                        property.value = (webcolors.CSS3_NAMES_TO_HEX[property.value])


# Write to a new file
with open('style_new.css', 'wb') as f:
    f.write(sheet.cssText)