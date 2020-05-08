from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://www.mother.ly/news/the-most-popular-baby-names-of-2018/check-out-the-full-top-100-list-below"

#Now we can connect to the website using urllib .
maleNames = []
femaleNames = []


try:
    page = urllib.request.urlopen(url)
except:
    print("page access error")

soup = BeautifulSoup(page,'html.parser')

regex = re.compile('^tocsection-')
rows = soup.find_all('tr')

rowText = []
  
for row in rows:
    cells = row.findChildren('td')
    rowOfCells = []   
    for cell in cells:
        rowOfCells.append(cell.text)
    print(rowOfCells)
    if(len(rowOfCells)> 0):
        maleNames.append(rowOfCells[1])
        femaleNames.append(rowOfCells[2])


#just to check the scrape worked correctly


maleFile = open("maleNames.txt","w")
print("Male Names:")
for name in maleNames:
    maleFile.write(""+name+"\n")
    print(name)
maleFile.close()
print("-----------------")
print("Female Names:")
femaleFile = open("femaleNames.txt","w")
for name in femaleNames:
    femaleFile.write(""+name+"\n")
    print(name)
femaleFile.close()

    
       
