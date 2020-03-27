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
    },
     {
    "namn" : "Miljöpartiet de gröna",
    "färg" : "lightgreen",
    "inriktning" : False,
    "ideologi" : ["Anarkism"],
    "ledare" : "",
    "block" : "Vänsterblocket",
    "min": 3.5,
    "max": 24.0,
    },
    {
    "namn" : "Fi",
    "färg" : "pink",
    "Ledare" : "Gudrun Schyman",
    "inriktning" : True,
    "ideologi" : ["Anarkism"],
    "block" : "Inget block",
    "min": 0.1,
    "max": 3.5,
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
    },
    {
    "namn" : "Kristdemokraterna",
    "färg" : "darkblue",
    "inriktning" : True,
    "ideologi" : ["Kapitalism","Facism"],
    "block" : "Borgerliga blocket",
    "min": 3.5,
    "max": 24.0,
    },
    {
    "namn" : "Centerpartiet",
    "färg" : "darkgreen",
    "inriktning" : True,
    "ideologi" : ["Liberalism"],
    "block" : "Borgerliga blocket",
    "min": 3.5,
    "max": 24.0,
    },
    {
    "namn" : "Sverigedemokraterna",
    "färg" : "gold",
    "inriktning" : True,
    "ideologi" : ["Facism"],
    "block" : "Inget block",
    "min": 3.5,
    "max": 24.0,
    },
    {
    "namn" : "Som inte röstade",
    "färg" : "grey",
    "inriktning" : None,
    "block" : "",
    "min": 3.5,
    "max": 24.0,
    },
    {
    "namn" : "Som röstade blankt",
    "färg" : "lightgrey",
    "inriktning" : None,
    "block" : "",
    "min": 3.5,
    "max": 24.0,
    },
    
]


totalaröster = 0
borgröster = 0
vänsterröster = 0
blocklösa = 0
block = []

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
print(totalaröster)


#procent


for i in partierna:
    tidigare = i["röster"]
    i["röster"] = (tidigare/totalaröster) * 100
    partinamnen.append(str(i["namn"]))
    block.append(str(i["block"]))
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
    högstsindex = jämförelsetal.index(max(jämförelsetal))
    mandat[högstsindex] = mandat[högstsindex] + 1 
    jämförelsetal[högstsindex] = röstetal[högstsindex]/((2*mandat[högstsindex])+1)
    counter += 1

counter = 0
for i in mandatnamn:
    mandatnamnochplatser.append(str(mandatnamn[counter]) + " (" + str(mandat[counter]) + " mandat)")
    counter += 1

#block fördelning

vänsterblock = []
vänsterblockmandat = 0
borgerliga = []
borgerligamandat = 0
blocklösa = []
blocklösamandat = 0
partinamnen
counter = 0
blockfördelning = []
blocklegend = []
# blockfärger = [red, green, yellow]
print(färger)

for i in partierna:     
    for items in mandatnamn:
        if items == partinamnen[counter] and block[counter] == "Vänsterblocket":
            vänsterblock.append(partinamnen[counter])
        elif items == partinamnen[counter] and block[counter] == "Borgerliga blocket":
            borgerliga.append(partinamnen[counter])
        elif items == partinamnen[counter]:
            blocklösa.append(partinamnen[counter])
    counter +=1

counter = 0
# vänsterblockmandat += (mandat[mandatnamn.index(vänsterblock[counter])])

while counter < len(vänsterblock):
    vänsterblockmandat += (mandat[mandatnamn.index(vänsterblock[counter])])
    counter += 1


counter = 0
while counter < len(borgerliga):
    borgerligamandat += (mandat[mandatnamn.index(borgerliga[counter])])
    counter += 1


counter = 0
while counter < len(blocklösa):
    blocklösamandat += (mandat[mandatnamn.index(blocklösa[counter])])
    counter += 1

blocklegend.append("Vänsterblocket" + " (" + str(vänsterblockmandat) + " mandat)")
blocklegend.append("Borgerliga blocket" + " (" + str(borgerligamandat) + " mandat)")
blocklegend.append("Blocklösa partier" + " (" + str(blocklösamandat) + " mandat)")

blockfördelning.append(vänsterblockmandat)
blockfördelning.append(borgerligamandat)
blockfördelning.append(blocklösamandat)


#graf block

plt.figure("Blockfördelning")
patches, texts = plt.pie(blockfördelning, colors=['red', 'blue', 'gold'], shadow=False, startangle=100,wedgeprops={"edgecolor":"0",'linewidth': 1, 'antialiased': True})
plt.legend(patches, blocklegend, loc="best")
plt.rcParams['lines.linewidth'] = 5
plt.axis('equal')
plt.tight_layout()
plt.title("Blockfördelning", bbox={'facecolor':'0.8', 'pad':5})
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.subplots_adjust(left=None, bottom=None, right=None, top=0.9, wspace=None, hspace=None)


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