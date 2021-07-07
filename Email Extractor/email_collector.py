import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii
maham@hyuid'''
print("\n")
k= 1
j=1
patt = re.compile(r'\w+@\w+\.\w+')
# r'\w+@\w+\.\w+'
matches = patt.findall(mystr)
for match in matches:
    print(f"Email No. {k}: {match}")
    k=int(k+1)
    
with open("email.txt", "a") as f:
    for match in matches:
        f.write(f"Email No. {j}: {match}"+"\n")
        j = int(j+1)

print("\nSuccessfully written")
