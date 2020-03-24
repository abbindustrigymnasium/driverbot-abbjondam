from random import randint
import math
import matplotlib.pyplot as plt

partierna = [
     {
    "namn" : "Socialdemokratiska arbetareparti",
    "färg" : "red",
    "inriktning" : False,
    "ideologi" : ["Socialism"],
    "ledare" : "Olof palme",
    "block" : "Vänsterblocket",
    "min" : 4.0,
    "max": 53.8,
    "röster" : 0,
    "riksdag" : True
    },
     {
    "namn" : "Vänsterpartiet Kommunisterna",
    "färg" : "darkred",
    "inriktning" : False,
    "ideologi" : ["Kommunism","Marxism"],
    "block" : "Vänsterblocket",
    "ledare" : "Jonas Sjöstedt",
    "min" : 3,
    "max": 50, #om v röster > 23.5 valfusk
    "röster" : 0,
    "riksdag" : True
    },
     {
    "namn" : "Miljöpartiet de gröna",
    "färg" : "lightgreen",
    "inriktning" : False,
    "ideologi" : ["Anarkism"],
    "block" : "Vänsterblocket",
    "min": 3.5,
    "max": 24.0,
    "röster" : 0,
    "riksdag" : True
    },
    {
    "namn" : "Fi",
    "färg" : "pink",
    "Ledare" : "Gudrun Schyman",
    "inriktning" : True,
    "ideologi" : ["Anarkism"],
    "block" : "Inget block",
    "min": 0,
    "max": 2,
    "röster" : 0,
    },
    {
    "namn" : "Moderaterna",
    "färg" : "blue",
    "Ledare" : "Fredrik Reinfeldt",
    "inriktning" : True,
    "ideologi" : ["Kapitalism"],
    "block" : "Borgerliga blocket",
    "min": 3.0,
    "max": 50.0,
    "röster" : 0,
    "riksdag" : True
    },
     {
    "namn" : "Folkpartiet/Liberalerna",
    "färg" : "lightskyblue",
    "inriktning" : True,
    "ideologi" : ["Liberalism"],
    "ledare" : "",
    "block" : "Borgerliga blocket",
    "min": 3.5,
    "max": 24.0,
    "röster" : 0,
    "riksdag" : True
    },
    {
    "namn" : "Kristdemokraterna",
    "färg" : "darkblue",
    "inriktning" : True,
    "ideologi" : ["Kapitalism","Facism"],
    "block" : "Borgerliga blocket",
    "min": 3.5,
    "max": 24.0,
    "röster" : 0,
    "riksdag" : True
    },
    {
    "namn" : "Centerpartiet",
    "färg" : "darkgreen",
    "inriktning" : True,
    "ideologi" : ["Liberalism"],
    "block" : "Borgerliga blocket",
    "min": 3.5,
    "max": 24.0,
    "röster" : 0,
    "riksdag" : True
    },
    {
    "namn" : "Sverigedemokraterna",
    "färg" : "gold",
    "inriktning" : True,
    "ideologi" : ["Facism"],
    "block" : "Inget block",
    "min": 3.5,
    "max": 24.0,
    "röster" : 0,
    "riksdag" : True
    },
    {
    "namn" : "Som inte röstade",
    "färg" : "grey",
    "block" : "Inget block",
    "min": 3.5,
    "max": 24.0,
    "röster" : 0,
    },
    {
    "namn" : "Som röstade blankt",
    "färg" : "lightgrey",
    "inriktning" : True,
    "block" : "Inget block",
    "min": 3.5,
    "max": 24.0,
    "röster" : 0
    },
    
]


totalaröster = 0
borgröster = 0
vänsterröster = 0
blocklösa = 0

#procent
partinamnen = []
partiochprocent = []
procent = []
färger = []

#röstfördelning
röstfördelningfärger = []
totalaröstfördelnigsstorlekar = 0
rösfördelnigtext = []
counter = 0

#mandat


for i in partierna: #Slumpar röster mellan min och max 
    i["röster"] = ((randint(i["min"]*10,(i["max"])*10))/10)
    totalaröster = totalaröster + i["röster"] #En variable för totalaröster


#procent

if totalaröster > 100:
    for i in partierna:
        tidigare = i["röster"]
        i["röster"] = (tidigare/totalaröster) * 100
        partinamnen.append(str(i["namn"]))
        partiochprocent.append(str(i["namn"]) + " (" + str(round(i["röster"],1)) + "%)")
        procent.append(i["röster"])
        färger.append(i["färg"])
        if i["block"] == "Borgerliga blocket":
            borgröster = borgröster + i["röster"]
        elif i["block"] == "Vänsterblocket":
            vänsterröster = vänsterröster + i["röster"]
        else:
            blocklösa = blocklösa + i["röster"]


#röstfördelning

röstfördelningfärger = färger[:len(färger)-2]
röstfördelningstorlekar = procent[:len(procent)-2]
partiröstfördelningnamn = partinamnen[:len(partinamnen)-2]


for i in röstfördelningstorlekar:
    totalaröstfördelnigsstorlekar = totalaröstfördelnigsstorlekar + röstfördelningstorlekar[counter]
    counter += 1
counter = 0

for i in röstfördelningstorlekar:
    röstfördelningstorlekar[counter] = round((procent[counter]/totalaröstfördelnigsstorlekar) * 100,1)
    counter += 1
counter = 0

for i in partiröstfördelningnamn:
    rösfördelnigtext.append(str(partiröstfördelningnamn[counter]) + " (" + str(röstfördelningstorlekar[counter]) + "%)")
    counter += 1

#mandat 
röstberättigad = 7588740 #0.73 * befolkningen januari 2020, 0.73 = antalröstberättigade/befolkningsmängd 2018
counter = 0
index = []
mandatfärger = röstfördelningfärger.copy()
jämförelsetal = röstfördelningstorlekar.copy()
mandatnamn = partinamnen[:len(partinamnen)-2]
mandatnamnochplatser = []
totalamandat = 0
mandat = []



for i in mandatnamn:
    if jämförelsetal[counter] < 4.0:
        mandatnamn.pop(counter)
        index.append(int(counter))
  
    if len(index) >= 1:
        mandatfärger.pop(index[0])
        jämförelsetal.pop(index[0])
        index.pop(0)
    counter += 1
counter = 0

antalöverspärr = len(mandatnamn)
mandat = [0] * int(antalöverspärr)
print(mandat)

for i in jämförelsetal:
    totalamandat = totalamandat + jämförelsetal[counter]
    counter +=1 
counter = 0    

for i in jämförelsetal:
    jämförelsetal[counter] = (röstberättigad*(jämförelsetal[counter]/totalamandat))
    counter +=1 
counter = 1
röstetal = jämförelsetal.copy()
while counter <= 349:
    # print(max(jämförelsetal))
    högstsindex = jämförelsetal.index(max(jämförelsetal))
    print("högstindex" + str(högstsindex))
    mandat[högstsindex] = mandat[högstsindex] + 1 
    print(mandat[högstsindex])
    jämförelsetal[högstsindex] = röstetal[högstsindex]/((2*mandat[högstsindex])+1)
    counter += 1

counter = 0
for i in mandatnamn:
    mandatnamnochplatser.append(str(mandatnamn[counter]) + " (" + str(mandat[counter]) + " personer)")
    counter += 1

#graf mandat
plt.figure("Mandat")
patches, texts = plt.pie(mandat, colors=mandatfärger, shadow=False, startangle=100,wedgeprops={"edgecolor":"0",'linewidth': 1, 'antialiased': True})
plt.legend(patches, mandatnamnochplatser, loc="best")
plt.rcParams['lines.linewidth'] = 5
plt.axis('equal')
plt.tight_layout()
plt.title("Mandat", bbox={'facecolor':'0.8', 'pad':5})
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.subplots_adjust(left=None, bottom=None, right=None, top=0.9, wspace=None, hspace=None)

#graf röstfördelning

plt.figure("Röstfördelning")
patches, texts = plt.pie(röstfördelningstorlekar, colors=röstfördelningfärger, shadow=False, startangle=100,wedgeprops={"edgecolor":"0",'linewidth': 1, 'antialiased': True})
plt.legend(patches, rösfördelnigtext, loc="best")
plt.rcParams['lines.linewidth'] = 5
plt.axis('equal')
plt.tight_layout()
plt.title("Röstfördelning", bbox={'facecolor':'0.8', 'pad':5})
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.subplots_adjust(left=None, bottom=None, right=None, top=0.9, wspace=None, hspace=None)


#graf rösterna

plt.figure("Röster")
patches, texts = plt.pie(procent, colors=färger, shadow=False, startangle=100,wedgeprops={"edgecolor":"0",'linewidth': 1, 'antialiased': True})
plt.legend(patches, partiochprocent, loc="best")
plt.rcParams['lines.linewidth'] = 5
plt.axis('equal')
plt.tight_layout()
plt.title("Rösterna", bbox={'facecolor':'0.8', 'pad':5})
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.subplots_adjust(left=None, bottom=None, right=None, top=0.9, wspace=None, hspace=None)


plt.show()