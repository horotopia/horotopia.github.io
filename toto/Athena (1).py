import discord
from discord.ext import commands

TOKEN = "NzA2MTI1OTEzMTMzMjg1NDM3.Xq1tAA.33ws5I4plwjFKXegzXbH5-D0dXE"

client = discord.Client()

@client.event
async def on_message(message):
 if message.author == client.user:
     return

########################################
##############  Epv  ###################
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

 if message.content.startswith("ePV "):
     a = 0
     b = 0
     x = ""
     invalid = False
     spacerequired = True
     info = message.content.replace("ePV ", "")
     for i in range(0,len(info)):
         if spacerequired == True and info[i] == " ":
             spacerequired = False
         elif list(info)[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
             invalid = True
     if spacerequired == True:
         invalid = True
     if invalid == False:

         for i in range(0,info.find(" ")):
             x += info[i]

         a = int(x)
         x = ""

         for i in range(info.find(" ") + 1, len(info)):
             x += info[i]

         b = int(x)

         c = round(a/(1-(b/(b+1200))))

         embed=discord.Embed(title="", description=" ", url="", color=0xffffff)
         embed.set_author(name=" ")
         embed.set_thumbnail(url="")
         embed.add_field(name="Calculs effectués avec:", value="\nPV: " + str(a) +"\nDéfense: " + str(b) + "\n\n__**ePV**__: " + str(c), inline=False)
         await message.channel.send(embed=embed)


     else:
         await message.channel.send("Ecrivez ePV suivi des PV et de la Def")

########################################
## Choisir ses gemmes (2 Def ou 2 Pv) ##
########################################
#EpvGem 5454 36546546
 if message.content.startswith("EpvGem "):
    ListElementInMessage = message.content.split

 if ListElementInMessage[0] == "EpvGem":
     if len(ListElementInMessage) == 3 and ListElementInMessage[2].isnumeric():
         a = int(ListElementInMessage[1])
         b = int(ListElementInMessage[2])
         c = round((a * 2.36) / (1 - ((b * 1.68) / ((b * 1.68) + 1200))))
         d = round((a * 1.68) / (1 - ((b * 2.36) / ((b * 2.36) + 1200))))
         embed = discord.Embed(title="", description=" ", url="", color=0xffffff)
         embed.set_author(name=" ")
         embed.set_thumbnail(url="")
         embed.add_field(name="Calculs effectués avec:", value="\nPV de base: " + str(a) + "\nDéfense de base: " + str(b) + "\n\nEpv avec 2Pv + 1Def: " + str(c) + "\nEpv avec 1Pv + 2Def: " + str(d), inline=False)
         await message.channel.send(embed=embed)

         
     else:
         await message.channel.send ("Erreur, Ecrivez EpvGem suivi des PV de base et de la Def de base")

########################################
#############  Dégats   ################
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

 if message.content.startswith("D "):
     a = 0
     b = 0
     c = 0
     x = ""
     y = ""
     invalid = False
     spacerequired = 2
     info = message.content.replace("D ", "")
     for i in range(0,len(info)):
         if spacerequired > 0 and info[i] == " ":
             spacerequired -= 1
         elif list(info)[i] not in [".","0","1","2","3","4","5","6","7","8","9"]:
             invalid = True
     if spacerequired != 0:
         invalid = True
     if invalid == False:

         for i in range(0,info.find(" ")):
             x += info[i]
             y += "x"
         try:
             a = float(x)
         except:
             invalid = True
         x = ""
         for i in range(info.find(" ") + 1, len(info)):
             y += info[i]
         for i in range(info.find(" ") + 1, y.find(" ") + 1):
             x += info[i]
         try:
             b = float(x)
         except:
             invalid = True
         x = ""
             
         for i in range(y.find(" ") + 1, len(info)):
             x += info[i]
         
         try:
             c = float(x)
         except:
             invalid = True

         d = round(( 5.5 * a *( 1 + (b / 100 ) * (c/100))))
         
         print(a,b,c)
         
         if invalid == False:
             embed=discord.Embed(title="", description=" ", url="", color=0xffffff)
             embed.set_author(name=" ")
             embed.set_thumbnail(url="")
             embed.add_field(name="Calculs effectués avec:", value="\nAttaque: " + str(a) + "\nDommages critiques: " + str(b) + "\nTaux critique: " + str(c) + "\n\n__**Dégâts moyens**__: " + str(d) + "\n__**Dégâts Min**__: " + str(round(5.5 * a)) + " (no crit)\n__**Dégâts Max**__ : " + str(round(( 5.5 * a *( 1 + (b / 100 ) * (1)))))+ " (crit)", inline=False)
             await message.channel.send(embed=embed)
         else:
             await message.channel.send("Ecrivez 'D' suivi de l'attaque, du dommage critique et du taux critique")
     else:
         await message.channel.send("Ecrivez 'D' suivi de l'attaque, du dommage critique et du taux critique")



########################################
###########  Agression Def   ###########
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

#faire un calcul d'agression def 
#appel avec "AgrDef"

########################################
###########  Agression pv   ###########
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

#faire un calcul d'agression pv 
# appel avec "AgrPv"

########################################
###########  Agression Rec   ###########
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

#faire un calcul d'agression recup 
# Appel avec "AgrRec"

########################################
###############  heal   ################
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

# faire un calcul de heal

# recup du heal x 4 + recup du soigné x 2
# demander la récup du heal + soigné


########################################
######  activation de commandes   ######
########################################		

 if " " in message.content:
     return

 if "." in message.content:
     return

    
 if "?" in message.content:
     return

    
 if "/" in message.content:
     return
    

########################################
##############   Menu   ################
########################################
#   Mettre un message pour expliquer   #
#   toutes les commandes disponible    #
#         un peu comme Help            #
########################################

 if any([message.content ==(item) for item in ['Athena','Ath','athena']]):
     embed=discord.Embed(title="", url="https://vignette.wikia.nocookie.net/saint-seiya-cosmo-fantasy/images/f/f9/Athena_armure_divine.png/revision/latest/top-crop/width/360/height/450?cb=20171204120613&path-prefix=fr", color=0xffffff)
     embed.set_author(name="'Ath' ou 'Athena' Pour faire apparaître ce message.\n'Help' Pour obtenir en MP une version plus détaillée")
     embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/saint-seiya-cosmo-fantasy/images/f/f9/Athena_armure_divine.png/revision/latest/top-crop/width/360/height/450?cb=20171204120613&path-prefix=fr")
     embed.add_field(name="★★★★★★★★★★", value="__>Astromons__\nEcrivez le nom d'un astromon sans espace et avec la première lettre en majuscule pour montrer tous les éléments de l'astromons.\nExemple : Miho\nPour faire apparaître un astomon précis, veuillez préciser son élément avant le nom.\nExemple : FeuMiho\n__>ePV__\nEcrivez ePV puis vos statistiques PV suivi des statistiques DEF\nExemple: ePV 30245 2461\n__>Dégâts__\nEcrivez 'D' puis vos statistiques ATQ, le % dégâts critiques puis le % taux critique.\nExemple: D 3240 50 10\nNB : Si la valeur du taux critique est > 100 les résultats seront incohérents.\n__>Boss__\nDragons, Golems : 'Dragon' ou 'Dragons', 'Golem' ou 'Golems' pour avoir une vue globale des statistiques de ces boss.\n__>Compétences__\nEcrivez le nom d'une compétence sans espace ni majuscule pour en avoir une description ainsi que les astromons possédant cette compétence.\nExemple: siphondepv", inline=False)
     await message.channel.send(embed=embed)
             
 if message.content.startswith("Ath"):
     return

###########################
######### Help ##################
###########################	
	 
 if any([message.content ==(item) for item in ['Help','help']]):
        await message.author.send("__- - > Astromons__\nEcrivez le nom d'un astromons sans espaces et avec la première lettre en majuscule pour montrer tous les éléments de l'astromons.\nExemple : Miho\nLa plupart du temps Athéna a seulement besoin des 3 ou 4 premières lettres. 'Shivobi' sera compris par 'Shiva' et non 'Shinobi'\nPour trouver un astromon Super Evo, veuillez rajouter devant son nom la lettre 'S'\nExemple: SYuki ou SLeo\n\n__- - > ePV__\nEcrivez ePV puis vos statistiques PV puis vos statistiques DEF\nExemple: ePV 30245 2461\n\n__- - > Dégâts__\nEcrivez 'D' puis vos statistiques ATQ, le % dégâts critiques puis le % taux critique.\nExemple: D 3240 50 10\nNB : Dégâts critiques et Taux Critique s'expriment en %. Si la valeur entrée est > 100 les résultats seront incohérents.\n\n__- - > Horaires des Batailles de Clan__\nEcrivez la timezone de votre clan pour avoir toutes les timezones.\nExemple: UTC+3\nLa plupart des formats de timezone sont pris en compte (JST,MST...) vous ne devriez pas avoir besoin de convertir vous-même au format UTC.\n\n__- - > Boss__\n'dragon' ou 'dragons', 'golem' ou 'golems' pour avoir  une vue globale des statistiques de ces boss.\n'DB' ou 'GB' suivi d'un nombre pour avoir le descriptif d'un niveau précis. Exemple : GB8, DB5...\n\n__- - > Compétences__\nEcrivez le nom d'une compétence sans espace ni majuscule pour en avoir une description ainsi que les astromons possédant cette compétence. \nExemple: siphondepv\n\n__- - > Events__\nEcrivez 'Rebirth3', 'Rebirth4' ou 'exotique' pour faire apparaître une liste des renaissances 3*, 4* ou exotique\n\n__- - > Divers__\n'Help' pour voir ce message en version courte, entrez 'Ath' ou 'Athena'\n'Titan' ou 'Titans' pour voir les attaques des titans et leurs HP.\n'TitanPV' ou 'TitansPV' pour les PV des titans\n'Toc' ou 'ToC' pour la liste des boss et les récompenses associées")
		
###########################
######### Sony ##################
###########################	

 if message.content.startswith('Knuc'):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634702953611285/Knuckles3Evo_large.jpg", color=0xffffff)
     embed.set_author(name="#1 Knuckles (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634702953611285/Knuckles3Evo_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Persévérance\n(Dmg : +20%)\n**Actif**: Persévérance\n(Dmg : +20%)\n**PV**: 27996\n**Attaque**: 3344\n**Défense**: 2009\n**Récupération**:2043", inline=False)
     
     await message.channel.send(embed=embed)

 if message.content.startswith("Soni"):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634807807279104/Sonic3Evo_large.jpg", color=0xffffff)
     embed.set_author(name="#2 Sonic (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634807807279104/Sonic3Evo_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Dégâts -50% 1 tour\n(Dmg : +20% +1 tour)\n**Actif**: Attaque augmentée +50%  2 tours (soi-même)\n(Dmg : +25%)\n**PV**: 26927\n**Attaque**: 3344\n**Défense**: 2384\n**Récupération**:2159", inline=False)
     
     await message.channel.send(embed=embed)
     
 if message.content.startswith("Tail"):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634818213085194/Tails3Evo_large.jpg", color=0xffffff)
     embed.set_author(name="#3 Tails (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634818213085194/Tails3Evo_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%\n**Passif**: Défense réduite 80% 2 tours\n(Dmg : +25%)\n**Actif**: Faiblesse exposée 80% 2 tours\n(Dmg : +20% Effect : +10%)\n**PV**: 26440\n**Attaque**: 2812\n**Défense**: 2856\n**Récupération**:2692", inline=False)
     
     await message.channel.send(embed=embed)

 if message.content.startswith("Tail"):
     return
  
     
 if message.content.startswith("Silv"):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634795052269689/Silver3Evo_large.jpg", color=0xffffff)
     embed.set_author(name="#4 Silver (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634795052269689/Silver3Evo_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Resist +20~25%\n**Passif**: Siphon de PA 30%\n(Dmg : +20% Effect : +5%)\n**Actif**: Réduction de dégâts 2 tours (allies)\n(Dmg : +20% +1tour)\n**PV**: 32160\n**Attaque**: 2696\n**Défense**: 3128\n**Récupération**:1889", inline=False)
     
     await message.channel.send(embed=embed)
     

 if message.content.startswith("Shad"):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634767080456202/Shadow3Evo_large.jpg", color=0xffffff)
     embed.set_author(name="#5 Shadow (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634767080456202/Shadow3Evo_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25%\n**Passif**: Vague martiale 10% (allies)\n(Dmg +25%)\n**Actif**: Attaque augmentée  2 tours\n(Dmg +20% +1tour)\n**PV**: 24380\n**Attaque**: 3916\n**Défense**: 2377\n**Récupération**:1880", inline=False)
     
     await message.channel.send(embed=embed)

 if message.content.startswith("Shad"):
     return
     
###########################
######### Alpaga ##################
###########################	

 if any([message.content.startswith (item) for item in ['Alp','FeuAlp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559613791174668/StrangeAlpacaR_large.jpeg", color=0xffffff)
     embed.set_author(name="#6 Alpaca (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559613791174668/StrangeAlpacaR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Tc +15~20%(Même élément)\n**Passif**: Brise-Bonus 100%\n(Dmg +25%)\n**Actif**: Sceau 80% 3 tours\n(Dmg +20% Effect +10%)\n**PV**: 30921\n**Attaque**: 1826\n**Défense**: 1942\n**Récupération**:1533", inline=False)
     
     await message.channel.send(embed=embed)
  
 if any([message.content.startswith (item) for item in ['Alp','EauAlp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559608523128862/StrangeAlpacaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#7 Alpaca (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559608523128862/StrangeAlpacaB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Tc +15~20%(Même élément)\n**Passif**: Boost de moral 100% (de ses PA, on crit)\n(Dmg +25%)\n**Actif**: Siphon de PA 30% (On crit)\n(Dmg +20% Effect +10%)\n**PV**: 24965\n**Attaque**: 3051\n**Défense**: 1648\n**Récupération**:1444", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Alp','BoisAlp','TopAlp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559602701697029/StrangeAlpaca_large.jpeg", color=0xffffff)
     embed.set_author(name="#8 Alpaca (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559602701697029/StrangeAlpaca_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Tc +15~20%(Même élément)\n**Passif**: Chasseur (eau) 50%\n(Dmg +25%)\n**Actif**: Frappe indéfectible (On crit) \n(Dmg +25%)\n**PV**: 26893\n**Attaque**: 2847\n**Défense**: 1498\n**Récupération**:1355", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Alp','LightAlp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559616010223628/StrangeAlpacaW_large.jpeg", color=0xffffff)
     embed.set_author(name="#9 Alpaca (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559616010223628/StrangeAlpacaW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Tc +15~20%(Même élément)\n**Passif**: Choc 50% 2 tours\n(Dmg +20% Taux +20%)\n**Actif**: Étourdissement 50% 2 tours\n(Dmg +20% Taux + 20%)\n**PV**: 32024\n**Attaque**: 2389\n**Défense**: 2685\n**Récupération**:1752", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Alp','DarkAlp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559612277030931/StrangeAlpacaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#10 Alpaca (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559612277030931/StrangeAlpacaD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Tc +15~20%(Même élément)\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20% +1tour)\n**Actif**: Avantage élémentaire\n(Dmg +30%)\n**PV**: 22555\n**Attaque**: 3173\n**Défense**: 2670\n**Récupération**:2023", inline=False)
     
     await message.channel.send(embed=embed)
     
###########################
######### Ammonore ##################
###########################	
	 
 if any([message.content.startswith (item) for item in ['Ammo','FeuAmmo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556861866508314/MortArchleR_large.jpeg", color=0xffffff)
     embed.set_author(name="#11 Ammonore (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556861866508314/MortArchleR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Att +20~25%\n**Passif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Nécrose 60% 1 tour\n(No skillbooks)\n**PV**: 41143\n**Attaque**: 1506\n**Défense**: 1125\n**Récupération**:1329", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ammo','EauAmmo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556816991649812/MortArchle_large.jpeg", color=0xffffff)
     embed.set_author(name="#12 Ammonore (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556816991649812/MortArchle_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +20~25%\n**Passif**: Étourdissement 40% 1 tour\n(No skillbooks)\n**Actif**: Provocation 80% 1 tour\n(No skillbooks)\n**PV**: 29484\n**Attaque**: 1742\n**Défense**: 1800\n**Récupération**:1732", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ammo','BoisAmmo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556860650029077/MortArchleG_large.jpeg", color=0xffffff)
     embed.set_author(name="#13 Ammonore (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556860650029077/MortArchleG_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Att +20~25%\n**Passif**: Nécrose x2 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 80% 2 tour\n(No skillbooks)\n**PV**: 25272\n**Attaque**: 1784\n**Défense**: 2813\n**Récupération**:1355", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ammo','LightAmmo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556862235607049/MortArchleW_large.jpeg", color=0xffffff)
     embed.set_author(name="#14 Ammonore (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556862235607049/MortArchleW_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +20~25%\n**Passif**: Attaque réduite 40% 1 tours\n(No skillbooks)\n**Actif**: Fatigue 80% 2 tours\n(No skillbooks)\n**PV**: 30403\n**Attaque**: 1892\n**Défense**: 1889\n**Récupération**:1119", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ammo','DarkAmmo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556839519125504/MortArchleD_large.jpeg", color=0xffffff)
     embed.set_author(name="#15 Ammonore (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556839519125504/MortArchleD_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Att +20~25%\n**Passif**: Provocation 40% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**PV**: 26327\n**Attaque**: 2615\n**Défense**: 1573\n**Récupération**:1457", inline=False)
     
     await message.channel.send(embed=embed)
     
###########################
######### Anubis ##################
###########################	

 if any([message.content.startswith (item) for item in ['Anu','FeuAnu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551381249032192/AnubisR_large.jpeg", color=0xffffff)
     embed.set_author(name="#16 Anu (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551381249032192/AnubisR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 38684\n**Attaque**: 2112\n**Défense**: 2439\n**Récupération**:1772", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Anu','EauAnu','TopAnu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551368997470218/AnubisB_large.jpeg", color=0xffffff)
     embed.set_author(name="#18 Anu (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551368997470218/AnubisB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Prédateur 50%\n(No skillbooks)\n**PV**: 22739\n**Attaque**: 3296\n**Défense**: 2111\n**Récupération**:1920", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Anu','BoisAnu','TopAnu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551378271207424/AnubisG_large.jpeg", color=0xffffff)
     embed.set_author(name="#20 Anu (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551378271207424/AnubisG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Chasseur 50%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 23494\n**Attaque**: 3092\n**Défense**: 2322\n**Récupération**:1948", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Anu','LightAnu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551366741196820/Anubis_large.jpeg", color=0xffffff)
     embed.set_author(name="#22 Anu (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551366741196820/Anubis_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Défense réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Soif 60% -30% 2 tours\n(No skillbooks)\n**PV**: 39604\n**Attaque**: 2351\n**Défense**: 1772\n**Récupération**:1915", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Anu','DarkAnu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607326188053987328/AnubisD_large.jpg", color=0xffffff)
     embed.set_author(name="#24 Anu (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607326188053987328/AnubisD_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +15~20%\n**Passif**: Nécrose x2 60% 1 tours\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 29617\n**Attaque**: 2288\n**Défense**: 3296\n**Récupération**:1709", inline=False)
     
     await message.channel.send(embed=embed)
     
###########################
######### Anubis S Evo ##################
###########################	
	 
 if any([message.content.startswith (item) for item in ['FeuAnu','SAnu','FeuSAnu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559766572892191/SuperAnubisR_large.jpeg", color=0xffffff)
     embed.set_author(name="#17 Anu SE (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559766572892191/SuperAnubisR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR +15~20%\n**Passif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 42722\n**Attaque**: 2324\n**Défense**: 2684\n**Récupération**:1949", inline=False)
     
     await message.channel.send(embed=embed)
	 
 if any([message.content.startswith (item) for item in ['EauAnu','SAnu','EauSAnu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559755193876501/SuperAnubisB_large.jpeg", color=0xffffff)
     embed.set_author(name="#19 Anu SE (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559755193876501/SuperAnubisB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Prédateur 50%\n(No skillbooks)\n**PV**: 25020\n**Attaque**: 3657\n**Défense**: 2329\n**Récupération**:2118", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['BoisAnu','SAnu','BoisSAnu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559761200119823/SuperAnubisG_large.jpeg", color=0xffffff)
     embed.set_author(name="#21 Anu SE (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559761200119823/SuperAnubisG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR +15~20%\n**Passif**: Chasseur 50%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 25851\n**Attaque**: 3432\n**Défense**: 2561\n**Récupération**:2152", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['LightAnu','SAnu','LightSAnu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559733983412273/SuperAnubis_large.jpeg", color=0xffffff)
     embed.set_author(name="#23 Anu SE (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559733983412273/SuperAnubis_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR +15~20%\n**Passif**: Défense réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Soif 60% -30% 2 tours\n(No skillbooks)\n**PV**: 43730\n**Attaque**: 2589\n**Défense**: 1949\n**Récupération**:2112", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['DarkAnu','SAnu','DarkSAnu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559752039890964/SuperAnubisD_large.jpeg", color=0xffffff)
     embed.set_author(name="#25 Anu SE (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559752039890964/SuperAnubisD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR +15~20%\n**Passif**: Nécrose x2 60% 1 tours\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 32586\n**Attaque**: 2527\n**Défense**: 3657\n**Récupération**:1886", inline=False)
     
     await message.channel.send(embed=embed)
     
###########################
######### Arch ##################
###########################	

 if any([message.content.startswith (item) for item in ['Arch','FeuArch']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551455308120064/Archhelon_large.jpeg", color=0xffffff)
     embed.set_author(name="#26 Arch (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551455308120064/Archhelon_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Resist +10~15%\n**Passif**: Reduction dégâts 50% 1 tour\n(Dmg: +20%, +1 tour)\n**Actif**:  Provocation intrépide 60% 2 tours\n(Dmg: +25%, Taux: +20%)\n**PV**: 29412\n**Attaque**: 1321\n**Défense**: 2642\n**Récupération**:1628", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Arch','EauArch']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551458386477076/ArchhelonB_large.jpeg", color=0xffffff)
     embed.set_author(name="#27 Arch (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551458386477076/ArchhelonB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Resist +10~15%\n**Passif**: Reduction dégâts 50% 1 tour\n(Dmg: +25%, +1 tour)\n**Actif**: Etourdissement 60% 2 tours \n(Dmg: +25%, Taux: +20%)\n**PV**: 28439\n**Attaque**: 1668\n**Défense**: 2486\n**Récupération**:1192", inline=False)
     
     await message.channel.send(embed=embed)
  
 if any([message.content.startswith (item) for item in ['Arch','BoisArch']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551468025118722/ArchhelonG_large.jpeg", color=0xffffff)
     embed.set_author(name="#28 Arch (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551468025118722/ArchhelonG_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Resist +10~15%\n**Passif**: Reduction dégâts 50% 1 tour\n(Dmg: +25%, +1 tour)\n**Actif**: Chasseur 50%\n(Dmg: +30%)\n**PV**: 33737\n**Attaque**: 2152\n**Défense**: 1328\n**Récupération**:1362", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Artemis ##################
###########################	
	 
 if any([message.content.startswith (item) for item in ['Arte','FeuArte','TopArte']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558810489683978/SeleneR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#31 Artemis (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558810489683978/SeleneR_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Resist +20~25%\n**Passif**: Étourdissement 80% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Provocation 80% 1 tour\n(Dmg +15% Taux: +20%)\n**PV**: 37247\n**Attaque**: 2746\n**Défense**: 2807\n**Récupération**:2316", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Arte','EauArte']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558776893440013/SeleneB_Large.jpeg", color=0xffffff)
     embed.set_author(name="#32 Artemis (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558776893440013/SeleneB_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Nécrose x2 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Nécrose x2 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 30856\n**Attaque**: 3173\n**Défense**: 2833\n**Récupération**:2486", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Arte','BoisArte']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558775291346980/Selene_Large.jpeg", color=0xffffff)
     embed.set_author(name="#33 Artemis (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558775291346980/Selene_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Siphon de PV (Allies)\n(Dmg +20%)\n**Actif**: Siphon de PV (Allies) \n(Dmg +20%)\n**PV**: 28016\n**Attaque**: 3575\n**Défense**: 2492\n**Récupération**:2281", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Arte','LightArte']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558807260069891/SeleneW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#34 Artemis (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558807260069891/SeleneW_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Vague Martiale 10% pv/pa (alliés)\n(Dmg +30%)\n**Actif**: Prédateur 50% \n(Dmg +20%)\n**PV**: 29222\n**Attaque**: 3575\n**Défense**: 2588\n**Récupération**:2172", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Arte','DarkArte']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558779636514836/SeleneD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#35 Artemis (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558779636514836/SeleneD_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +15%; +Effect.: +5%)\n**Actif**: Silence 80% 2 tours\n(Dmg +15%, Taux: +20%, +1tour)\n**PV**: 31946\n**Attaque**: 2533\n**Défense**: 3650\n**Récupération**:2206", inline=False)
     
     await message.channel.send(embed=embed)
     
###########################
######### Arthur ##################
###########################	
	 
 if any([message.content.startswith (item) for item in ['Arth','FeuArth','TopArth']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557209668171202574/ArthurpendragonR_large.jpeg", color=0xffffff)
     embed.set_author(name="#36 Arthur (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557209668171202574/ArthurpendragonR_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%, (Donjons)\n**Passif**: Étourdissement 100% 1 tour\n(Dmg +15%, tour: +1)\n**Actif**: Défense réduite 70% 3 tours\n(???)\n**PV**: 27948\n**Attaque**: 3466\n**Défense**: 2717\n**Récupération**:2349", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Arth','EauArth']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607326391658086421/ArthurpendragonB_large.jpg", color=0xffffff)
     embed.set_author(name="#37 Arthur (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607326391658086421/ArthurpendragonB_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: PV +40~45% (Donjons)\n**Passif**: Boost de moral 100% 50% of de ses PA\n(Dmg +20%, +Effect.: +10%)\n**Actif**: Attaque réduite 70% 3 tours\n(???)\n**PV**: 32453\n**Attaque**: 2784\n**Défense**: 2930\n**Récupération**:2644", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Arth','BoisArth']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551565345554433/ArthurpendragonG_large.jpeg", color=0xffffff)
     embed.set_author(name="#38 Arthur (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551565345554433/ArthurpendragonG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45% (Donjons)\n**Passif**: Siphon de PV (soi-même)\n(Dmg +25%)\n**Actif**: Étourdissement 60% 2 tours\n(Dmg +15%, Taux: +10%, tour: +1)\n**PV**: 28166\n**Attaque**: 3766\n**Défense**: 2479\n**Récupération**:2288", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Arth','LightArth']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551549591617611/Arthurpendragon_large.jpeg", color=0xffffff)
     embed.set_author(name="#39 Arthur (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551549591617611/Arthurpendragon_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45% (Donjons)\n**Passif**: Choc 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Chasseur 50% \n(No skillbooks)\n**PV**: 26416\n**Attaque**: 3936\n**Défense**: 2411\n**Récupération**:2023", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Arth','DarkArth']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551561923002368/ArthurpendragonD_large.jpeg", color=0xffffff)
     embed.set_author(name="#40 Arthur (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551561923002368/ArthurpendragonD_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45% (Donjons)\n**Passif**: Agression (PV)\n(Dmg +30%)\n**Actif**: Nécrose x3 100% 1 tour\n(Dmg +25%, tour: +1)\n**PV**: 49696\n**Attaque**: 1976\n**Défense**: 2487\n**Récupération**:2024", inline=False)
     
     await message.channel.send(embed=embed)
     
###########################
######### Balrona ##################
###########################	
	 
 if any([message.content.startswith (item) for item in ['Bal','FeuBal']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551642940178442/Balrakaris_large.jpeg", color=0xffffff)
     embed.set_author(name="#41 Balrona (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551642940178442/Balrakaris_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +35~40%\n**Passif**: Siphon de PV\n(Dmg +25%)\n**Actif**: Avantage élémentaire\n(Dmg +20%)\n**PV**: 25684\n**Attaque**: 3152\n**Défense**: 3216\n**Récupération**:2999", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bal','EauBal','TopBal']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551647943852052/BalrakarisB_large.jpeg", color=0xffffff)
     embed.set_author(name="#42 Balrona (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551647943852052/BalrakarisB_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +35~40%\n**Passif**: Frappe Courageuse\n(Dmg +20%)\n**Actif**: Défense réduite 80% 2 tours\n(Dmg +25%)\n**PV**: 28813\n**Attaque**: 3562\n**Défense**: 2452\n**Récupération**:2390", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bal','BoisBal']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551656152367118/BalrakarisG_large.jpeg", color=0xffffff)
     embed.set_author(name="#43 Balrona (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551656152367118/BalrakarisG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Att +35~40%\n**Passif**: Boost de moral 100% 50% of de ses PA \n(Dmg +10%, +Effect.: +10%)\n**Actif**: Sceau 60% 2 tours \n(Dmg +10%, Taux: +20%)\n**PV**: 31115\n**Attaque**: 2683\n**Défense**: 3466\n**Récupération**:2084", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bal','LightBal']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551675655618562/Balrakarisw_large.jpeg", color=0xffffff)
     embed.set_author(name="#44 Balrona (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551675655618562/Balrakarisw_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +35~40%\n**Passif**: Choc 100% 1 tour \n(Dmg +20%, tour: +1)\n**Actif**: Avantage élémentaire\n(Dmg +20%)\n**PV**: 32698\n**Attaque**: 2866\n**Défense**: 2842\n**Récupération**:1963", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bal','DarkBal']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551650644983819/BalrakarisD_large.jpeg", color=0xffffff)
     embed.set_author(name="#45 Balrona (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551650644983819/BalrakarisD_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Att +35~40%\n**Passif**: Boost de moral (Allies) 20% SP \n(Dmg +20%)\n**Actif**: Adrénaline (Allies) 10% de ses PV \n(Dmg +25%)\n**PV**: 48212\n**Attaque**: 2133\n**Défense**: 2507\n**Récupération**:2017", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Banshee ##################
###########################	
	 
 if any([message.content.startswith (item) for item in ['Ban','FeuBan']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556797349593096/MorrighanR_large.jpeg", color=0xffffff)
     embed.set_author(name="#46 Banshee (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556797349593096/MorrighanR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Malédiction 80% 2 tours\n(Dmg: +10%, Taux: +20%)\n**Actif**: Malédiction foudroyante\n(Dmg: +30%)\n**PV**: 29382\n**Attaque**: 2362\n**Défense**: 2433\n**Récupération**:2147", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ban','EauBan']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556766131388416/MorrighanB_large.jpeg", color=0xffffff)
     embed.set_author(name="#47 Banshee (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556766131388416/MorrighanB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%, \n**Passif**: Abondance d'âmes rouges\n(Dmg +35%)\n**Actif**: Nécrose x2 80% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**PV**: 40040\n**Attaque**: 2364\n**Défense**: 1976\n**Récupération**:1887", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ban','BoisBan','TopBan']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556767108792321/MorrighanG_large.jpeg", color=0xffffff)
     embed.set_author(name="#48 Banshee (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556767108792321/MorrighanG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%, \n**Passif**: Boost de moral 30% de ses PA \n(???)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 29760\n**Attaque**: 3092\n**Défense**: 2152\n**Récupération**:1968", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ban','LightBan']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607326992823615498/MorrighanW_large.jpg", color=0xffffff)
     embed.set_author(name="#49 Banshee (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607326992823615498/MorrighanW_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Choc 80% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Choc 70% 1 tour\n(Dmg: +15% Taux: +10%)\n**PV**: 31575\n**Attaque**: 2321\n**Défense**: 2631\n**Récupération**:2311", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ban','DarkBan']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556762058850305/Morrighan_large.jpeg", color=0xffffff)
     embed.set_author(name="#50 Banshee (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556762058850305/Morrighan_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Nécrose x3 100% 1 tours\n(Dmg +30%)\n**Actif**: Agression (PV)\n(Dmg +25%)\n**PV**: 42001\n**Attaque**: 2405\n**Défense**: 1744\n**Récupération**:1847", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Banshee S Evo ##################
###########################	
	 
 if any([message.content.startswith (item) for item in ['FeuBan','SBan','FeuSBan']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707493851698430012/20200506_092733.jpg", color=0xffffff)
     embed.set_author(name="#828 Banshee SE (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707493851698430012/20200506_092733.jpg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Malédiction 80% 2 tours\n(Dmg: +10%, Taux: +20%)\n**Actif**: Malédiction foudroyante\n(Dmg: +30%)\n**PV**: 32343\n**Attaque**: 3121\n**Défense**: 2684\n**Récupération**:2371", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['EauBan','SBan','EauSBan']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707494654911709214/20200506_092902.jpg", color=0xffffff)
     embed.set_author(name="#829 Banshee SE (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707494654911709214/20200506_092902.jpg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%, \n**Passif**: Abondance d'âmes rouges\n(Dmg +35%)\n**Actif**: Nécrose x2 80% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**PV**: 44206\n**Attaque**: 2821\n**Défense**: 2249\n**Récupération**:2078", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['BoisBan','SBan','BoisSBan']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707494655079612536/20200506_092921.jpg", color=0xffffff)
     embed.set_author(name="#830 Banshee SE (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707494655079612536/20200506_092921.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%, \n**Passif**: Boost de moral 30% de ses PA \n(???)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 32742\n**Attaque**: 3759\n**Défense**: 2377\n**Récupération**:2172", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['LightBan','SBan','LightSBan']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707495450969899038/20200506_093405.jpg", color=0xffffff)
     embed.set_author(name="#831 Banshee SE (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707495450969899038/20200506_093405.jpg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Choc 80% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Choc 70% 1 tour\n(Dmg: +15% Taux: +10%)\n**PV**: 38207\n**Attaque**: 2563\n**Défense**: 2902\n**Récupération**:2555", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['DarkBan','SBan','DarkSBan']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707494655469551687/20200506_093037.jpg", color=0xffffff)
     embed.set_author(name="#832 Banshee SE (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707494655469551687/20200506_093037.jpg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Nécrose x3 100% 1 tours\n(Dmg +30%)\n**Actif**: Agression (PV)\n(Dmg +25%)\n**PV**: 48626\n**Attaque**: 2650\n**Défense**: 2085\n**Récupération**:2038", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Bast ##################
###########################	
	 
 if any([message.content.startswith (item) for item in ['Bast','FeuBast']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551797122793484/Bastet_large.jpeg", color=0xffffff)
     embed.set_author(name="#51 Bast (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551797122793484/Bastet_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Récupération\n**Lead**: CR +20~25%\n**Passif**: Vague martiale 20%\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Domination 3 tours\n(Dmg +25%)\n**PV**: 30591\n**Attaque**: 2343\n**Défense**: 3201\n**Récupération**:3255", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Bast','EauBast','TopBast']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551798490136591/BastetB_large.jpeg", color=0xffffff)
     embed.set_author(name="#52 Bast (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551798490136591/BastetB_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: CR +20~25%\n**Passif**: Affaiblissement 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense augmentée 3 tours\n(Dmg +25%)\n**PV**: 43662\n**Attaque**: 2705\n**Défense**: 2112\n**Récupération**:2228", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bast','BoisBast','TopBast']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551804236464137/BastetG_large.jpeg", color=0xffffff)
     embed.set_author(name="#53 Bast (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551804236464137/BastetG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Récupération\n**Lead**: CR +20~25%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Attaque augmentée  3 tours\n(Dmg +25%)\n**PV**: 31973\n**Attaque**: 1914\n**Défense**: 2581\n**Récupération**:3303", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bast','LightBast']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551805310074881/BastetW_large.jpeg", color=0xffffff)
     embed.set_author(name="#54 Bast (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551805310074881/BastetW_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: CR +20~25%\n**Passif**: Siphon de PA 30%\n(No skillbooks)\n**Actif**: Vigueur 3 tours\n(No skillbooks)\n**PV**: 28779\n**Attaque**: 2860\n**Défense**: 3562\n**Récupération**:2091", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bast','DarkBast']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551801132548097/BastetD_large.jpeg", color=0xffffff)
     embed.set_author(name="#55 Bast (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551801132548097/BastetD_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: CR +20~25%\n**Passif**: Boost de moral 30% (de ses PA)\n(Dmg +25%)\n**Actif**: Bouclier (PV) 3 tours\n(Dmg +25%)\n**PV**: 42546\n**Attaque**: 2487\n**Défense**: 2487\n**Récupération**:2487", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Scarabo ##################
###########################	
	 
 if any([message.content.startswith (item) for item in ['Scar','FeuScar']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554775711842304/HerculeR_large.jpeg", color=0xffffff)
     embed.set_author(name="#56 Scarabo (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554775711842304/HerculeR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Défense réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Sommeil 100% 1 tour \n(No skillbooks)\n**PV**: 27172\n**Attaque**: 2588\n**Défense**: 3099\n**Récupération**:2234", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Scar','EauScar']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554769105813530/HerculeB_large.jpeg", color=0xffffff)
     embed.set_author(name="#57 Scarabo (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554769105813530/HerculeB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Sceau 60% 2 tours\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 41374\n**Attaque**: 2105\n**Défense**: 2037\n**Récupération**:2051", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Scar','BoisScar','TopScar']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554769189699584/Hercule_large.jpeg", color=0xffffff)
     embed.set_author(name="#58 Scarabo (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554769189699584/Hercule_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Attaque réduite 60% 2 Truns \n(No skillbooks)\n**Actif**: Étourdissement 70% 1 tour \n(No skillbooks)\n**PV**: 29998\n**Attaque**: 2377\n**Défense**: 3221\n**Récupération**:1832", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Scar','LightScar']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554784729727037/HerculeW_large.jpeg", color=0xffffff)
     embed.set_author(name="#59 Scarabo (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554784729727037/HerculeW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**Actif**: Siphon de PV ,Greatly)\n(No skillbooks)\n**PV**: 30223\n**Attaque**: 2166\n**Défense**: 3133\n**Récupération**:2016", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Scar','DarkScar']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554771760939021/HerculeD_large.jpeg", color=0xffffff)
     embed.set_author(name="#60 Scarabo (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554771760939021/HerculeD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Défense réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 24148\n**Attaque**: 3194\n**Défense**: 2234\n**Récupération**:1839", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Zabeille ##################
###########################	
	 
 if any([message.content.startswith (item) for item in ['Zab','LightZab']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552142364475402/BumblekingW_large.jpeg", color=0xffffff)
     embed.set_author(name="#64 Zabeille (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552142364475402/BumblekingW_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Resist +10~15%\n**Passif**: Défense réduite 60% 2 tours \n(No skillbooks)\n**Actif**: Attaque augmentée de 50% 2 tours \n(No skillbooks)\n**PV**: 28731\n**Attaque**: 2356\n**Défense**: 1559\n**Récupération**:1437", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Zab','DarkZab']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552139411685376/Bumbleking_large.jpeg", color=0xffffff)
     embed.set_author(name="#65 Zabeille (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552139411685376/Bumbleking_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Resist +10~15%\n**Passif**: Nécrose 40% 1 tour \n(No skillbooks)\n**Actif**: Attaque augmentée de 50% 2 tours \n(No skillbooks)\n**PV**: 34837\n**Attaque**: 1404\n**Défense**: 1683\n**Récupération**:1588", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Rubani ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Ruba','FeuRuba']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558359937548300/Ribonia_large.jpeg", color=0xffffff)
     embed.set_author(name="#66 Rubani (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558359937548300/Ribonia_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Abondance d'âmes rouges\n(Dmg +30%)\n**Actif**: Zèle 3 tours\n(Dmg +30%)\n**PV**: 23685\n**Attaque**: 1696\n**Défense**: 1559\n**Récupération**:2472", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ruba','EauRuba']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558362290683944/RiboniaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#67 Rubani (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558362290683944/RiboniaB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Attaque réduite 50% 2 tours \n(Dmg +10%,Taux: +15%)\n**Actif**: Récupération augmentée 3 tours\n(Dmg +30%)\n**PV**: 26222\n**Attaque**: 2001\n**Défense**: 1991\n**Récupération**:1923", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ruba','BoisRuba']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558364136046593/RiboniaG_large.jpeg", color=0xffffff)
     embed.set_author(name="#68 Rubani (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558364136046593/RiboniaG_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Étourdissement 60% 1 tour \n(Dmg +10%, Taux: +20%)\n**Actif**: Vigueur 3 tours\n(Dmg +30%)\n**PV**: 31026\n**Attaque**: 1566\n**Défense**: 1444\n**Récupération**:2472", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Benjabuton ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Ben','FeuBen','TopBen']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033120484589591/Benjamin1.png", color=0xffffff)
     embed.set_author(name="#71 Benjabuton (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033120484589591/Benjamin1.png")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%, \n**Passif**: Traqueur +30% CR\n(Dmg +20%, Taux: +10%)\n**Actif**: Traqueur +30% CR\n(Dmg +20%, Taux: +10%)\n**PV**: 30556\n**Attaque**: 3085\n**Défense**: 1907\n**Récupération**:2050", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ben','EauBen','TopBen']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033123835707393/Benjamin2.png", color=0xffffff)
     embed.set_author(name="#72 Benjabuton (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033123835707393/Benjamin2.png")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Aveuglement 70% 2 tours\n(Dmg +10%, Taux: +10%, tour: +1)\n**Actif**: Aveuglement 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 30454\n**Attaque**: 1920\n**Défense**: 3187\n**Récupération**:2206", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ben','BoisBen']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033127316455454/Benjamin3.png", color=0xffffff)
     embed.set_author(name="#73 Benjabuton (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033127316455454/Benjamin3.png")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Sceau 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 41388\n**Attaque**: 2085\n**Défense**: 2439\n**Récupération**:1704", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ben','LightBen']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033136103260160/Benjamin5.png", color=0xffffff)
     embed.set_author(name="#74 Benjabuton (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033136103260160/Benjamin5.png")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Persévérance 10 tours\n(Dmg +20%)\n**Actif**: Persévérance 10 tours\n(Dmg +20%)\n**PV**: 26389\n**Attaque**: 3364\n**Défense**: 2343\n**Récupération**:2036", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ben','DarkBen']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033131238653962/Benjamin4.png", color=0xffffff)
     embed.set_author(name="#75 Benjabuton (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033131238653962/Benjamin4.png")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Persévérance 10 tours\n(Dmg +20%)\n**PV**: 27243\n**Attaque**: 2886\n**Défense**: 2774\n**Récupération**:2386", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Beth ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Bet','FeuBet','TopBeth']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551923698368513/BethanyR_large.jpeg", color=0xffffff)
     embed.set_author(name="#76 Beth (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551923698368513/BethanyR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35% (League)\n**Passif**: Prédateur (bois) 30%\n(Dmg: +35%)\n**Actif**: Prédateur (bois) 100%\n(Dmg: +35%)\n**PV**: 28871\n**Attaque**: 1994\n**Défense**: 1793\n**Récupération**: 1691", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bet','EauBet','TopBeth']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551918807810060/Bethany_large.jpeg", color=0xffffff)
     embed.set_author(name="#77 Beth (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551918807810060/Bethany_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35% (League)\n**Passif**: Prédateur (feu) 30%\n(Dmg: +35%)\n**Actif**: Prédateur (feu) 100%\n(Dmg: +35%)\n**PV**: 25367\n**Attaque**: 2595\n**Défense**: 1818\n**Récupération**: 1580", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bet','BoisBet''TopBeth']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551921584439298/BethanyG_large.jpeg", color=0xffffff)
     embed.set_author(name="#78 Beth (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551921584439298/BethanyG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Def +30~35% (League)\n**Passif**: Prédateur (eau) 30%\n(Dmg: +35%)\n**Actif**: Prédateur (eau) 100%\n(Dmg: +35%)\n**PV**: 43901\n**Attaque**: 1676\n**Défense**: 1295\n**Récupération**: 1513", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Piou ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Pio','FeuPio']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560068093018114/SwiftR_large.jpeg", color=0xffffff)
     embed.set_author(name="#81 Piou (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560068093018114/SwiftR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%(Donjons)\n**Passif**: Provocation 80% 1 tour\n(Dmg +10%, Taux: +20%)\n**Actif**: Nécrose x2 60% 1 tour\n(Dmg +10%, Taux: +20%)\n**PV**: 28752\n**Attaque**: 1784\n**Défense**: 2527\n**Récupération**:1355", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pio','EauPio','TopPiou']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560053186723882/SwiftB_large.jpeg", color=0xffffff)
     embed.set_author(name="#82 Piou (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560053186723882/SwiftB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%(Donjons)\n**Passif**: Étourdissement 80% 1 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Soif 60% -30% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 30451\n**Attaque**: 1763\n**Défense**: 1943\n**Récupération**:1705", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pio','BoisPio']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560050309300225/Swift_large.jpeg", color=0xffffff)
     embed.set_author(name="#83 Piou (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560050309300225/Swift_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: PV +30~35%(Donjons)\n**Passif**: Nécrose 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +10%, Taux: +20%)\n**PV**: 36812\n**Attaque**: 1758\n**Défense**: 1247\n**Récupération**:1336", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pio','LightPio']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560069754093586/SwiftW_large.jpeg", color=0xffffff)
     embed.set_author(name="#84 Piou (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560069754093586/SwiftW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%(Donjons)\n**Passif**: Boost de moral 20% (de ses PA)\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Prédateur 30%\n(Dmg +30%)\n**PV**: 27029\n**Attaque**: 3133\n**Défense**: 2159\n**Récupération**:2023", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pio','DarkPio']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560064679116820/SwiftD_large.jpeg", color=0xffffff)
     embed.set_author(name="#85 Piou (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560064679116820/SwiftD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%(Donjons)\n**Passif**: Agression (PV)\n(Dmg +20%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%)\n**PV**: 44643\n**Attaque**: 2010\n**Défense**: 1942\n**Récupération**:1915", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### tipiaf ##########
###########################
	 
 if any([message.content.startswith (item) for item in ['Tip','FeuTip','TopTip']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557838963179521/Phoenix_large.jpeg", color=0xffffff)
     embed.set_author(name="#86 Tipiaf (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557838963179521/Phoenix_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +20%,Taux: +20%)\n**Actif**: Attaque réduite 70% 2 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 24291\n**Attaque**: 3058\n**Défense**: 2138\n**Récupération**:2288", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tip','EauTip']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557856696827969/PhoenixB_large.jpeg", color=0xffffff)
     embed.set_author(name="#87 Tipiaf (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557856696827969/PhoenixB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Pétrification 100% 1 tour\n(Dmg +15%, Taux: +10%, tour: +1)\n**Actif**: Pétrification 80% 1 tour\n(???)\n**PV**: 24250\n**Attaque**: 2424\n**Défense**: 3173\n**Récupération**:1948", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tip','BoisTip']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557861427871770/PhoenixG_large.jpeg", color=0xffffff)
     embed.set_author(name="#88 Tipiaf (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557861427871770/PhoenixG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Siphon de PV \n(Dmg +15%, Taux: +10%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg +15%, Taux: +10%)\n**PV**: 26096\n**Attaque**: 3085\n**Défense**: 2281\n**Récupération**:1628", inline=False)
     
     await message.channel.send(embed=embed)
	 
 if any([message.content.startswith (item) for item in ['Tipiaf','LightTipiaf']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569195048337524/Screenshot_20200907-183739_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#1000 Tipiaf (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569195048337524/Screenshot_20200907-183739_Monster_Super_League.jpg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques 40-45%\n**Passif**: Frappe courageuse\n(Dmg +25%)\n**Actif**: Faiblesse exposée\n(Dmg +20%, Taux: +10%)\n**PV**: 30029\n**Attaque**: 2812\n**Défense**: 2610\n**Récupération**:2161", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tipiaf','DarkTipiaf']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569195186880622/Screenshot_20200907-183853_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#1001 Tipiaf (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569195186880622/Screenshot_20200907-183853_Monster_Super_League.jpg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques 40-45%\n**Passif**: Boost de moral 10% PA Alliés\n(Dmg +20%, efficacité +5%)\n**Actif**: Nécrose x3 80% 2 tours\n(Dmg +20%, Taux +10%)\n**PV**: 29603\n**Attaque**: 2206\n**Défense**: 3099\n**Récupération**:2036", inline=False)
     
     await message.channel.send(embed=embed) 

###########################
######### Bron ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Bro','FeuBro']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557003684315146/MustangB_large.jpeg", color=0xffffff)
     embed.set_author(name="#97 Bron (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557003684315146/MustangB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: PV +20~25%\n**Passif**: Prédateur (bois) 30%\n(no skillbooks)\n**Actif**: Nécrose x2 80% 1 tour\n(no skillbooks)\n**PV**: 28568\n**Attaque**: 2404\n**Défense**: 1512\n**Récupération**: 1396", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bro','EauBro']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557003684315146/MustangB_large.jpeg", color=0xffffff)
     embed.set_author(name="#97 Bron (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557003684315146/MustangB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: PV +20~25%\n**Passif**: Prédateur (feu) 30%\n(No skillbooks)\n**Actif**: Étourdissement 60% 1 tour\n(No skillbooks)\n**PV**: 29048\n**Attaque**: 1681\n**Défense**: 1807\n**Récupération**:1596", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bro','BoisBro']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557011636584463/MustangG_large.jpeg", color=0xffffff)
     embed.set_author(name="#98 Bron (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557011636584463/MustangG_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Prédateur (eau) 30%\n(No skillbooks)\n**Actif**: Sommeil 60% 1 tour\n(No skillbooks)\n**PV**: 29331\n**Attaque**: 1321\n**Défense**: 2554\n**Récupération**:1573", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### bulbie ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Bul','FeuBul']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327107101753376/BarometzR_large.jpg", color=0xffffff)
     embed.set_author(name="#101 Bulbie (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327107101753376/BarometzR_large.jpg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Soif 60% -30% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 33032\n**Attaque**: 1881\n**Défense**: 1874\n**Récupération**:1806", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bul','EauBul','TopBul']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327101481254918/BarometzB_large.jpg", color=0xffffff)
     embed.set_author(name="#102 Bulbie (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327101481254918/BarometzB_large.jpg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Brise bouclier 100%\n(Dmg +30%)\n**Actif**: Frappe indéfectible \n(Dmg +25%)\n**PV**: 21499\n**Attaque**: 3357\n**Défense**: 2363\n**Récupération**:1777", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bul','BoisBul']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327097999982613/Barometz_large.jpg", color=0xffffff)
     embed.set_author(name="#103 Bulbie (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327097999982613/Barometz_large.jpg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Nécrose x2 60% 1 tour\n(Dmg +10%, Taux: +30%)\n**Actif**: Brise-Bonus 100%\n(Dmg +30%)\n**PV**: 27427\n**Attaque**: 2192\n**Défense**: 2372\n**Récupération**:1671", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bul','LightBul']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327109634850817/BarometzW_large.jpg", color=0xffffff)
     embed.set_author(name="#104 Bulbie (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327109634850817/BarometzW_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Récupération réduite 80% 2 tour\n(Dmg +30%)\n**Actif**: Récupération réduite 100% 2 tour\n(Dmg +30%)\n**PV**: 32225\n**Attaque**: 2023\n**Défense**: 3139\n**Récupération**:2349", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Bul','DarkBul']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327104186581002/BarometzD_large.jpg", color=0xffffff)
     embed.set_author(name="#105 Bulbie (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327104186581002/BarometzD_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Faiblesse exposée 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Faiblesse exposée 100% 1 tours\n(Dmg +20%, tour: +1)\n**PV**: 24475\n**Attaque**: 3378\n**Défense**: 2349\n**Récupération**:2043", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Lumignon ##################
###########################

 if any([message.content.startswith (item) for item in ['Lumignon','FeuLumi','TopLumi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555572877197322/Lantra_large.jpeg", color=0xffffff)
     embed.set_author(name="#106 Lumignon (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555572877197322/Lantra_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Donjons)\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 28813\n**Attaque**: 2595\n**Défense**: 1975\n**Récupération**:1825", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Lumignon','EauLumi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555575649632296/LantraB_large.jpeg", color=0xffffff)
     embed.set_author(name="#107 Lumignon (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555575649632296/LantraB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Donjons)\n**Passif**: Traqueur +20% CR\n(Dmg +20%, Taux: +10%)\n**Actif**: Traqueur +20% CR\n(Dmg +15%, Taux: +10%)\n**PV**: 24795\n**Attaque**: 2601\n**Défense**: 1832\n**Récupération**:1811", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Lumignon','BoisLumi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555577016844300/LantraG_large.jpeg", color=0xffffff)
     embed.set_author(name="#108 Lumignon (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555577016844300/LantraG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%(Donjons)\n**Passif**: Chasseur (eau) 50%\n(Dmg +15%, Taux: +10%)\n**Actif**: Chasseur (eau) 50%\n(???)\n**PV**: 29457\n**Attaque**: 1742\n**Défense**: 1963\n**Récupération**:1861", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### canna ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Canna','FeuCanna']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552232940208140/CanariaR_large.jpeg", color=0xffffff)
     embed.set_author(name="#111 Canna (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552232940208140/CanariaR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: SP Rec +20~25%\n**Passif**: Pétrification 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Soif 80% -20% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 34053\n**Attaque**: 2267\n**Défense**: 2277\n**Récupération**:2277", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Canna','EauCanna']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552226124464139/CanariaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#112 Canna (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552226124464139/CanariaB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%\n**Passif**: Défense réduite 80% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 28752\n**Attaque**: 1948\n**Défense**: 3235\n**Récupération**:2254", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Canna','BoisCanna','TopCanna']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552230591660050/CanariaG_large.jpeg", color=0xffffff)
     embed.set_author(name="#113 Canna (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552230591660050/CanariaG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: SP Rec +20~25%\n**Passif**: Attaque réduite 70% 1 tour\n(Dmg +10%, Taux: +5%, tour: +1)\n**Actif**: Frappe Courageuse (On crit)\n(Dmg +20%)\n**PV**: 29484\n**Attaque**: 2396\n**Défense**: 2447\n**Récupération**:2352", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Canna','LightCanna']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552224300072980/Canaria_large.jpeg", color=0xffffff)
     embed.set_author(name="#114 Canna (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552224300072980/Canaria_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: SP Rec +20~25%\n**Passif**: Sceau 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Choc 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 35443\n**Attaque**: 1956\n**Défense**: 2316\n**Récupération**:2187", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Canna','DarkCanna']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552228615880715/CanariaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#115 Canna (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552228615880715/CanariaD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%\n**Passif**: Siphon de PV \n(Dmg +20%)\n**Actif**: Siphon de PV ,Greatly)\n(Dmg +20%)\n**PV**: 25776\n**Attaque**: 3262\n**Défense**: 2349\n**Récupération**:1907", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Cerise ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Ceri','FeuCeri','TopCeri']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033505872838686/Cherry1.png", color=0xffffff)
     embed.set_author(name="#796 Cerise (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033505872838686/Cherry1.png")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35% (clan)\n**Passif**: Nécrose 80% 2 tours\n(Dmg: +10% Taux +20%)\n**Actif**: Défense augmentée 2 tours\n(Dmg: +25% tour: +1)\n**PV**: 23501\n**Attaque**: 2036\n**Défense**: 2969\n**Récupération**: 2009", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ceri','EauCeri']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033508372774912/Cherry2.png", color=0xffffff)
     embed.set_author(name="#797 Cerise (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033508372774912/Cherry2.png")
     embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Att +30~35% (clan)\n**Passif**: Défense réduite 60% 1 tour\n(Dmg: +10% Taux +20%)\n**Actif**: Bouclier 2 tours\n(Dmg: +25% tour +1)\n**PV**: 28643\n**Attaque**: 1743\n**Défense**: 1580\n**Récupération**: 2540", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ceri','BoisCeri']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033511829405736/Cherry3.png", color=0xffffff)
     embed.set_author(name="#798 Cerise (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033511829405736/Cherry3.png")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Att +30~35% (clan)\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg: +30%)\n**Actif**: Bouclier (PV) 2 tours\n(Dmg: +25% tour: +1)\n**PV**: 30553\n**Attaque**: 1656\n**Défense**: 1826\n**Récupération**: 2180", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ceri','LightCeri']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033520024944650/Cherry5.png", color=0xffffff)
     embed.set_author(name="#799 Cerise (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033520024944650/Cherry5.png")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Att +30~35% (clan)\n**Passif**: Nécrose x2 60% 2 tours\n(Dmg: +15% Taux: +20%)\n**Actif**: Défense augmentée 2 tours\n(Dmg: +20% tour +1)\n**PV**: 24645\n**Attaque**: 2458\n**Défense**: 1948\n**Récupération**: 2792", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ceri','DarkCeri']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033515268079626/Cherry4.png", color=0xffffff)
     embed.set_author(name="#800 Cerise (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033515268079626/Cherry4.png")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Att +30~35% (clan)\n**Passif**: Défense réduite 60% 1 tour\n(Dmg: +15% Taux: +20%)\n**Actif**: Attaque augmentée  2 tours\n(Dmg: +20% tour: +1)\n**PV**: 25715\n**Attaque**: 1982\n**Défense**: 1920\n**Récupération**: 3153", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### chiroptie ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Chir','FeuChir']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552787842564109/CloakR_large.jpeg", color=0xffffff)
     embed.set_author(name="#116 Chiroptie (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552787842564109/CloakR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Attaque réduite 60% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 40% 2 tours\n(No skillbooks)\n**PV**: 27049\n**Attaque**: 2527\n**Défense**: 1403\n**Récupération**:1478", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Chir','EauChir']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557210231248125963/Cloak_large.jpeg", color=0xffffff)
     embed.set_author(name="#117 Chiroptie (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557210231248125963/Cloak_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Def +20~25%\n**Passif**: Récupération réduite 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 40% 2 tours\n(No skillbooks)\n**PV**: 36675\n**Attaque**: 1710\n**Défense**: 1206\n**Récupération**:1343", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chir','BoisChir']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552782914256897/CloakG_large.jpeg", color=0xffffff)
     embed.set_author(name="#118 Chiroptie (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552782914256897/CloakG_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Def +20~25%\n**Passif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Défense réduite 40% 2 tours\n(No skillbooks)\n**PV**: 29334\n**Attaque**: 1933\n**Défense**: 1895\n**Récupération**:1691", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chir','LightChir']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552795610546176/CloakW_large.jpeg", color=0xffffff)
     embed.set_author(name="#119 Chiroptie (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552795610546176/CloakW_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Def +20~25%\n**Passif**: Prédateur (light) 50%\n(No skillbooks)\n**Actif**: Choc 80% 1 tour\n(No skillbooks)\n**PV**: 29249\n**Attaque**: 1321\n**Défense**: 2527\n**Récupération**:1573", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chir','DarkChir']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552774186041344/CloakD_large.jpeg", color=0xffffff)
     embed.set_author(name="#120 Chiroptie (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552774186041344/CloakD_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Prédateur (dark) 50%\n(No skillbooks)\n**Actif**: Silence 80% 1 tour\n(No skillbooks)\n**PV**: 26041\n**Attaque**: 2343\n**Défense**: 1566\n**Récupération**:1403", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Chloe ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Chlo','FeuChlo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553694080663562/FateR_large.jpeg", color=0xffffff)
     embed.set_author(name="#121 Chloe (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553694080663562/FateR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Adrénaline 50% 50% de ses PV\n(Dmg +10%, Taux: +20%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**PV**: 39873\n**Attaque**: 1976\n**Défense**: 2323\n**Récupération**:1915", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chlo','EauChlo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553689555009557/FateB_large.jpeg", color=0xffffff)
     embed.set_author(name="#122 Chloe (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553689555009557/FateB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Pétrification 100% 1 tour\n(Dmg +30%)\n**Actif**: Nécrose x2 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 26675\n**Attaque**: 2240\n**Défense**: 3173\n**Récupération**:2384", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chlo','BoisChlo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553692314992653/FateG_large.jpeg", color=0xffffff)
     embed.set_author(name="#123 Chloe (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553692314992653/FateG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Traqueur 30%\n(Dmg +10%, Taux: +20%)\n**Actif**: Traqueur 30%\n(Dmg +10%, Taux: +20%)\n**PV**: 23712\n**Attaque**: 3323\n**Défense**: 2309\n**Récupération**:1948", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chlo','LightChlo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553696224083989/FateW_large.jpeg", color=0xffffff)
     embed.set_author(name="#124 Chloe (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553696224083989/FateW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Boost de moral 30%  100% (de ses PA)\n(Dmg +15%, Taux: +10%)\n**Actif**: Choc 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 30175\n**Attaque**: 2261\n**Défense**: 3323\n**Récupération**:1811", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chlo','DarkChlo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553685998370820/Fate_large.jpeg", color=0xffffff)
     embed.set_author(name="#125 Chloe (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553685998370820/Fate_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Attaque réduite 70% 2 tours\n(Dmg +10%, Taux: +30%)\n**Actif**: Frappe Courageuse\n(Dmg +25%)\n**PV**: 26733\n**Attaque**: 2716\n**Défense**: 2658\n**Récupération**:2522", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### cocomaru ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Coco','FeuCoco']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552911675064325/CocoemongR_large.jpeg", color=0xffffff)
     embed.set_author(name="#126 Cocomaru (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552911675064325/CocoemongR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35% (Même élément)\n**Passif**: Attaque réduite 60% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Sommeil 40% 1 tour\n(Taux: +30%)\n**PV**: 29419\n**Attaque**: 1437\n**Défense**: 2847\n**Récupération**:1702", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Coco','EauCoco']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552903211089922/CocoemongB_large.jpeg", color=0xffffff)
     embed.set_author(name="#127 Cocomaru (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552903211089922/CocoemongB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Récupération réduite 60% 1 tour\n(Dmg +30%, tour: +1)\n**Actif**: Pétrification 40% 1 tour\n(Taux: +30%)\n**PV**: 23706\n**Attaque**: 2384\n**Défense**: 1709\n**Récupération**:1866", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Coco','BoisCoco','TopCoco']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552801033650176/Cocoemong_large.jpeg", color=0xffffff)
     embed.set_author(name="#128 Cocomaru (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552801033650176/Cocoemong_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35% (Même élément)\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Nécrose 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 31646\n**Attaque**: 2642\n**Défense**: 1784\n**Récupération**:1716", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Coco','LightCoco']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552970559160342/CocoemongW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#129 Cocomaru (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552970559160342/CocoemongW_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Agression (PV)\n(Dmg +20%)\n**Actif**: Agression (PV)\n(Dmg +20%)\n**PV**: 37520\n**Attaque**: 2235\n**Défense**: 1751\n**Récupération**:2385", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Coco','DarkCoco']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552906637967386/CocoemongD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#130 Cocomaru (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552906637967386/CocoemongD_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Attaque réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Aveuglement 70% 2 tours\n(Dmg +10%, Taux: +10%)\n**PV**: 33141\n**Attaque**: 2812\n**Défense**: 2365\n**Récupération**:1970", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Poulichon ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Poul','LightPoul']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558022694666240/Ponicon_large.jpeg", color=0xffffff)
     embed.set_author(name="#134 Poulichon (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558022694666240/Ponicon_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Attaque réduite 70% 2 tours\n(Dmg: +20% Taux: +10%)\n**Actif**: Choc 80% 2 tours\n(Dmg: +20% Taux: +15%)\n**PV**: 30417\n**Attaque**: 1749\n**Défense**: 1895\n**Récupération**: 1807", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Poul','DarkPoul']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558034140790846/PoniconD_large.jpeg", color=0xffffff)
     embed.set_author(name="#135 Poulichon (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558034140790846/PoniconD_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Défense réduite 70% 2 tours\n(Dmg: +20% Taux: +10%)\n**Actif**: Prédateur (light) 100%\n(Dmg: +35%)\n**PV**: 26430\n**Attaque**: 2384\n**Défense**: 1818\n**Récupération**: 1600", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### cosmo ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Cosmo','LightCosmo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558953041756160/Shootingstar_large.jpeg", color=0xffffff)
     embed.set_author(name="#139 Cosmo (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558953041756160/Shootingstar_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: CR +13~18%\n**Passif**: Adrénaline (Allies) 10% de ses PV  (On crit)\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Nécrose x2 60% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**PV**: 32991\n**Attaque**: 2076\n**Défense**: 2106\n**Récupération**:1786", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Cosmo','DarkCosmo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558983840399361/ShootingstarD_large.jpeg", color=0xffffff)
     embed.set_author(name="#140 Cosmo (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558983840399361/ShootingstarD_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: CR +13~18%\n**Passif**: Brise bouclier 100%\n(Dmg +30%)\n**Actif**: Silence 60% 1 tour\n(Dmg +20%, Taux: +20%)\n**PV**: 45522\n**Attaque**: 1411\n**Défense**: 1445\n**Récupération**:1281", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### cotonou ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Coto','FeuCoto']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553079292035082/CottonsongR_large.jpeg", color=0xffffff)
     embed.set_author(name="#141 Cotonou (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553079292035082/CottonsongR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +10~15%\n**Passif**: Nécrose 60% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**Actif**: Attaque augmentée  3 tours\n(Dmg +25%)\n**PV**: 27696\n**Attaque**: 1362\n**Défense**: 1702\n**Récupération**:2574", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Coto','EauCoto']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553075357909014/Cottonsong_large.jpeg", color=0xffffff)
     embed.set_author(name="#142 Cotonou (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553075357909014/Cottonsong_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +10~15%\n**Passif**: Brise bouclier 100%\n(Dmg +25%)\n**Actif**: Défense augmentée 3 tours\n(Dmg +25%)\n**PV**: 30216\n**Attaque**: 1457\n**Défense**: 1730\n**Récupération**:2492", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Coto','BoisCoto']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553077203533826/CottonsongG_large.jpeg", color=0xffffff)
     embed.set_author(name="#143 Cotonou (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553077203533826/CottonsongG_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +10~15%\n**Passif**: Provocation 40% 1 tour \n(Dmg +10%, Taux: +20%)\n**Actif**: Purification 100%\n(Dmg +25%)\n**PV**: 31054\n**Attaque**: 1532\n**Défense**: 1430\n**Récupération**:2574", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Coto','LightCoto']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731541347722592369/CotoL.png", color=0xffffff)
     embed.set_author(name="#142 Cotonou (Light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731541347722592369/CotoL.png")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +10~15%\n**Passif**: Nécrose 60%\n(Dmg +20%, Taux: +10%)\n**Actif**: Bouclier 2 tours\n(Dmg +20%, +1 tour)\n**PV**: 26314\n**Attaque**: 1362\n**Défense**: 1968\n**Récupération**:2663", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Coto','DarkCoto']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731541425467949056/CotoD.png", color=0xffffff)
     embed.set_author(name="#143 Cotonou (Dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731541425467949056/CotoD.png")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: SP Rec +10~15%\n**Passif**: Résistance réduite 100% 1 tour \n(Dmg +20%, +1 tour)\n**Actif**: Domination 2 tours\n(Dmg +20%, +1 tour)\n**PV**: 25483\n**Attaque**: 1607\n**Défense**: 2411\n**Récupération**:1525", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### croquignol ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Croq','FeuCroq']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327215167733829/CaptainCroR_large.jpg", color=0xffffff)
     embed.set_author(name="#146 Croquignol (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327215167733829/CaptainCroR_large.jpg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45% (League)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg: +30%, Taux: +20%)\n**Actif**: Nécrose x2 80% 1 tour\n(Dmg: 20%, +1 tour)\n**PV**: 29368\n**Attaque**: 2015\n**Défense**: 1684\n**Récupération**:1664", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Croq','EauCroq','TopCroq']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327218745475082/CaptainCro_large.jpg", color=0xffffff)
     embed.set_author(name="#147 Croquignol (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327218745475082/CaptainCro_large.jpg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45% (League)\n**Passif**: Chasseur 50%\n(Dmg: +35%)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg: +20%, +1 tour)\n**PV**: 25926\n**Attaque**: 2581\n**Défense**: 1777\n**Récupération**:1682", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Croq','BoisCroq']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327223275323402/CaptainCroG_large.jpg", color=0xffffff)
     embed.set_author(name="#148 Croquignol (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327223275323402/CaptainCroG_large.jpg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%(League)\n**Passif**: Chasseur 50%\n(Dmg: +35%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg: +20%, +1 tour)\n**PV**: 25565\n**Attaque**: 2717\n**Défense**: 1784\n**Récupération**:1226", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### cupidon ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Cupi','FeuCupi','TopCupi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553671330889754/ErosR_large.jpeg", color=0xffffff)
     embed.set_author(name="#151 Cupidon (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553671330889754/ErosR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: PV +30~35%\n**Passif**: Attaque réduite 60% 1 tour\n(No skillbooks)\n**Actif**: Attaque augmentée  3 tours\n(No skillbooks)\n**PV**: 32456\n**Attaque**: 2159\n**Défense**: 1989\n**Récupération**:3323", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Cupi','EauCupi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553664129138710/ErosB_large.jpeg", color=0xffffff)
     embed.set_author(name="#152 Cupidon (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553664129138710/ErosB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: PV +30~35%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**Actif**: Purification 100%\n(No skillbooks)\n**PV**: 30693\n**Attaque**: 2036\n**Défense**: 2452\n**Récupération**:3003", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Cupi','BoisCupi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553668583489536/ErosG_large.jpeg", color=0xffffff)
     embed.set_author(name="#153 Cupidon (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553668583489536/ErosG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: PV +30~35%\n**Passif**: Abondance d'âmes rouges\n(No skillbooks)\n**Actif**: Bouclier (Flat) 2 tours\n(No skillbooks)\n**PV**: 29875\n**Attaque**: 2179\n**Défense**: 1989\n**Récupération**:3099", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Cupi','LightCupi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553662711332866/Eros_large.jpeg", color=0xffffff)
     embed.set_author(name="#154 Cupidon (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553662711332866/Eros_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: PV +30~35%\n**Passif**: Agression (Def)\n(No skillbooks)\n**Actif**: Zèle 3 tours \n(No skillbooks)\n**PV**: 29630\n**Attaque**: 2023\n**Défense**: 3303\n**Récupération**:2731", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Cupi','DarkCupi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553666050129921/ErosD_large.jpeg", color=0xffffff)
     embed.set_author(name="#155 Cupidon (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553666050129921/ErosD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Bouclier (PV) 3 tours\n(No skillbooks)\n**PV**: 37731\n**Attaque**: 1806\n**Défense**: 2323\n**Récupération**:2153", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### cura ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Cura','FeuCura','TopCura']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557601397669908/PandoraR_large.jpeg", color=0xffffff)
     embed.set_author(name="#156 Cura (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557601397669908/PandoraR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: PV Rec +20~25%\n**Passif**: Boost de moral (Allies)10% SP\n(No skillbooks)\n**Actif**: Bouclier (Level) 3 tours\n(No skillbooks)\n**PV**: 30679\n**Attaque**: 2036\n**Défense**: 2452\n**Récupération**:2996", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Cura','EauCura','TopCura']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557593608847370/PandoraB_large.jpeg", color=0xffffff)
     embed.set_author(name="#157 Cura (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557593608847370/PandoraB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV Rec +20~25%\n**Passif**: Boost de moral 25% de ses PA\n(No skillbooks)\n**Actif**: Attaque augmentée  3 tours\n(No skillbooks)\n**PV**: 38378\n**Attaque**: 1928\n**Défense**: 2024\n**Récupération**:2133", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Cura','BoisCura']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557598805590016/PandoraG_large.jpeg", color=0xffffff)
     embed.set_author(name="#158 Cura (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557598805590016/PandoraG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV Rec +20~25%\n**Passif**: Adrénaline 20% de ses PV\n(No skillbooks)\n**Actif**: Volonté 2 tours\n(No skillbooks)\n**PV**: 37533\n**Attaque**: 1962\n**Défense**: 2316\n**Récupération**:2194", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Cura','LightCura']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557591276945408/Pandora_large.jpeg", color=0xffffff)
     embed.set_author(name="#159 Cura (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557591276945408/Pandora_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV Rec +20~25%\n**Passif**: Choc 60% 2 tours\n(No skillbooks)\n**Actif**: Domination 2 tours\n(No skillbooks)\n**PV**: 26178\n**Attaque**: 2281\n**Défense**: 3194\n**Récupération**:2050", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Cura','DarkCura']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557595852800000/PandoraD_large.jpeg", color=0xffffff)
     embed.set_author(name="#160 Cura (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557595852800000/PandoraD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV Rec +20~25%\n**Passif**: Boost de moral (Allies) 10% SP\n(No skillbooks)\n**Actif**: Boost de moral 2 tours\n(No skillbooks)\n**PV**: 29014\n**Attaque**: 2532\n**Défense**: 2345\n**Récupération**:2100", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### d'artagnan ##################
###########################
	 
 if any([message.content.startswith (item) for item in ["D'art","FeuD'art","Dart","FeuDart"]]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553332091387914/DartagnanR_large.jpeg", color=0xffffff)
     embed.set_author(name="#161 D'artagnan (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553332091387914/DartagnanR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Soif 100% -20% 2 tours\n(No skillbooks)\n**PV**: 27220\n**Attaque**: 3092\n**Défense**: 2418\n**Récupération**:1954", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ["D'art","EauD'art","Dart","EauDart"]]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553327485779970/DartagnanB_large.jpeg", color=0xffffff)
     embed.set_author(name="#162 D'artagnan (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553327485779970/DartagnanB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Fatigue 100% 3 tours\n(No skillbooks)\n**PV**: 35579\n**Attaque**: 2282\n**Défense**: 2058\n**Récupération**:2010", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ["D'art","BoisD'art","Dart","BoisDart"]]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553329314496522/DartagnanG_large.jpeg", color=0xffffff)
     embed.set_author(name="#163 D'artagnan (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553329314496522/DartagnanG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Récupération réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Étourdissement 100% 1 tour\n(No skillbooks)\n**PV**: 29933\n**Attaque**: 2253\n**Défense**: 2386\n**Récupération**:2311", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ["D'art","LightD'art","Dart","LightDart"]]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553339238481922/DartagnanW_large.jpeg", color=0xffffff)
     embed.set_author(name="#164 D'artagnan (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553339238481922/DartagnanW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Boost de moral 50% de ses PA\n(No skillbooks)\n**Actif**: Prédateur 40%%\n(No skillbooks)\n**PV**: 24734\n**Attaque**: 3269\n**Défense**: 2254\n**Récupération**:2091", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ["D'art","DarkD'art","Dart","DarkDart"]]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553326928199710/Dartagnan_large.jpeg", color=0xffffff)
     embed.set_author(name="#165 D'artagnan (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553326928199710/Dartagnan_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Nécrose x2 100% 1 tour\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 26736\n**Attaque**: 2322\n**Défense**: 3194\n**Récupération**:2036", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### draka ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Drak','FeuDrak','TopDrak']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553542011846692/Drakoness_large.jpeg", color=0xffffff)
     embed.set_author(name="#166 Draka (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553542011846692/Drakoness_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%\n**Passif**: Boost de moral 15% (Allies SP)\n(No skillbooks)\n**Actif**: Perforation 100% 2 tours\n(No skillbooks)\n**PV**: 24856\n**Attaque**: 3902\n**Défense**: 2520\n**Récupération**:2125", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Drak','EauDrak']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553546072195091/DrakonessB_large.jpeg", color=0xffffff)
     embed.set_author(name="#167 Draka (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553546072195091/DrakonessB_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%\n**Passif**: Affaiblissement 80% 2 tours\n(No skillbooks)\n**Actif**: Affaiblissement 60% 3 tours\n(No skillbooks)\n**PV**: 28643\n**Attaque**: 3568\n**Défense**: 2622\n**Récupération**:2213", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Drak','BoisDrak']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553553454170113/DrakonessG_large.jpeg", color=0xffffff)
     embed.set_author(name="#168 Draka (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553553454170113/DrakonessG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 50098\n**Attaque**: 2010\n**Défense**: 2827\n**Récupération**:1840", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Drak','LightDrak']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553560928157696/DrakonessW_large.jpeg", color=0xffffff)
     embed.set_author(name="#169 Draka (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553560928157696/DrakonessW_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%\n**Passif**: Affaiblissement 80% 2 tours\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 30556\n**Attaque**: 4038\n**Défense**: 2206\n**Récupération**:1852", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Drak','DarkDrak']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553556293451797/DrakonessD_large.jpeg", color=0xffffff)
     embed.set_author(name="#170 Draka (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553556293451797/DrakonessD_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: PV +40~45%\n**Passif**: Affaiblissement 80% 2 tours\n(No skillbooks)\n**Actif**: Sceau 80% 2 tours\n(No skillbooks)\n**PV**: 28946\n**Attaque**: 3104\n**Défense**: 3162\n**Récupération**:2454", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### somnol ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Somn','FeuSomn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554918968295429/HypnosR_large.jpeg", color=0xffffff)
     embed.set_author(name="#171 Somnol (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554918968295429/HypnosR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Adrénaline 25% de ses PV\n(No skillbooks)\n**Actif**: Sommeil 90% 1 tours\n(No skillbooks)\n**PV**: 41688\n**Attaque**: 2126\n**Défense**: 2487\n**Récupération**:1751", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Somn','EauSomn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554914027536417/HypnosB_large.jpeg", color=0xffffff)
     embed.set_author(name="#172 Somnol (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554914027536417/HypnosB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%\n**Passif**: Sommeil 80% 1 tours\n(No skillbooks)\n**Actif**: Sommeil 90% 1 tours\n(No skillbooks)\n**PV**: 26971\n**Attaque**: 2682\n**Défense**: 2672\n**Récupération**:2501", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Somn','BoisSomn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554916955160576/HypnosG_large.jpeg", color=0xffffff)
     embed.set_author(name="#173 Somnol (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554916955160576/HypnosG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Sommeil 80% 1 tours\n(No skillbooks)\n**Actif**: Défense réduite (On crit) 2 tours\n(No skillbooks)\n**PV**: 25394\n**Attaque**: 3255\n**Défense**: 2261\n**Récupération**:2118", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Somn','LightSomn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554938102841344/HypnosW_large.jpeg", color=0xffffff)
     embed.set_author(name="#174 Somnol (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554938102841344/HypnosW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Sommeil 70% 2 tours\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 27492\n**Attaque**: 3194\n**Défense**: 2206\n**Récupération**:2363", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Somn','DarkSomn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554911980716033/Hypnos_large.jpeg", color=0xffffff)
     embed.set_author(name="#175 Somnol (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554911980716033/Hypnos_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Sommeil 70% 2 tours\n(No skillbooks)\n**Actif**: Chasseur 40%\n(No skillbooks)\n**PV**: 26041\n**Attaque**: 3323\n**Défense**: 2281\n**Récupération**:2254", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### fennec ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Fenn','FeuFenn','TopFenn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558622144593948/SandhiefR_large.jpeg", color=0xffffff)
     embed.set_author(name="#176 Fennec (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558622144593948/SandhiefR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Chasseur (bois) 50%\n(Dmg +20%)\n**Actif**: Attaque réduite 80%(On crit) 2 tours\n(Dmg +15%Taux: +20%)\n**PV**: 27179\n**Attaque**: 2527\n**Défense**: 1566\n**Récupération**:1628", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fenn','EauFenn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558617488785433/SandhiefB_large.jpeg", color=0xffffff)
     embed.set_author(name="#177 Fennec (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558617488785433/SandhiefB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Feu Chasseur 50%\n(Dmg +20%)\n**Actif**: Attaque réduite 80%(On crit) 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 26940\n**Attaque**: 2629\n**Défense**: 1525\n**Récupération**:1607", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fenn','BoisFenn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558616155258890/Sandhief_large.jpeg", color=0xffffff)
     embed.set_author(name="#178 Fennec (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558616155258890/Sandhief_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%, (Même élément)\n**Passif**: Chasseur (eau) 50%\n(Dmg +20%)\n**Actif**: Attaque réduite 80%(On crit) 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 23733\n**Attaque**: 2574\n**Défense**: 1818\n**Récupération**:1805", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fenn','LightFenn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558623381913610/SandhiefW_large.jpeg", color=0xffffff)
     embed.set_author(name="#179 Fennec (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558623381913610/SandhiefW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Défense réduite (On crit) 2 tours\n(Dmg +20%)\n**PV**: 26293\n**Attaque**: 3269\n**Défense**: 2281\n**Récupération**:1668", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fenn','DarkFenn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558619623948298/SandhiefD_large.jpeg", color=0xffffff)
     embed.set_author(name="#180 Fennec (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558619623948298/SandhiefD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Vague martiale (On crit) 20%\n(Dmg +20%)\n**Actif**: Silence 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 45951\n**Attaque**: 1874\n**Défense**: 1874\n**Récupération**:1717", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### flora ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Flor','BoisFlor']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558079909298225/Primavera_large.jpeg", color=0xffffff)
     embed.set_author(name="#183 Flora (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558079909298225/Primavera_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20% (Même élément)\n**Passif**: Sommeil 80% 2 tours\n(No skillbooks)\n**Actif**: Sommeil 80% 1 tour\n(No skillbooks)\n**PV**: 30866\n**Attaque**: 2131\n**Défense**: 2032\n**Récupération**:1351", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Flor','LightFlor']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558086003621889/PrimaveraW_large.jpeg", color=0xffffff)
     embed.set_author(name="#184 Flora (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558086003621889/PrimaveraW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20% (Même élément)\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**PV**: 37527\n**Attaque**: 2133\n**Défense**: 1874\n**Récupération**:2065", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Flor','DarkFlor']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558083969384469/PrimaveraD_large.jpeg", color=0xffffff)
     embed.set_author(name="#185 Flora (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558083969384469/PrimaveraD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20% (Même élément)\n**Passif**: Nécrose x3 80% 1 tour\n(Dmg : +10%, Taux : +20%)\n**Actif**: Nécrose x2 70% 2 tours\n(Dmg : +20%, Taux : +10%)\n**PV**: 29675\n**Attaque**: 2389\n**Défense**: 2535\n**Récupération**:2474", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### gargor ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Garg','FeuGarg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554134377857026/GagolosR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#186 Gargor (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554134377857026/GagolosR_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: -10/15% resistance ennemie\n**Passif**: Pétrification 80% 1 tour\n(Dmg: +20%, +1 tour)\n**Actif**: Adrénaline 30% de ses PV\n(Dmg: +20%, Taux: +20%)\n**PV**: 32923\n**Attaque**: 1593\n**Défense**: 1521\n**Récupération**:1412", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Garg','EauGarg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554106233946147/Gagolos_Large.jpeg", color=0xffffff)
     embed.set_author(name="#187 Gargor (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554106233946147/Gagolos_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: -10/15% resistance ennemie\n**Passif**: Adrénaline 20% de ses PV\n(Dmg: +20%, Taux: +10%)\n**Actif**: Adrénaline 20% PV (Allies)\n(Dmg: +20%)\n**PV**: 33488\n**Attaque**: 1452\n**Défense**: 1670\n**Récupération**:1336", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Garg','BoisGarg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554130753847326/GagolosG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#188 Gargor (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554130753847326/GagolosG_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: -10/15% resistance ennemie\n**Passif**: Boost de moral 30% de ses PA\n(Dmg: +20%, Taux: +20%)\n**Actif**: Pétrification 80% 2 tours\n(Dmg: +20%, +1 tour)\n**PV**: 25374\n**Attaque**: 1702\n**Défense**: 2581\n**Récupération**:1362", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### félinelame ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Feli','FeuFeli']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607329066328129553/MastercatR_large.jpg", color=0xffffff)
     embed.set_author(name="#191 Félinelame (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607329066328129553/MastercatR_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35% (ToC)\n**Passif**: Récupération réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Pétrification 100% 1 tour\n(No skillbooks)\n**PV**: 28272\n**Attaque**: 2267\n**Défense**: 2106\n**Récupération**:1691", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Feli','EauFeli']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607329056559595520/MastercatB_large.jpg", color=0xffffff)
     embed.set_author(name="#192 Félinelame (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607329056559595520/MastercatB_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35% (ToC)\n**Passif**: Attaque réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Nécrose x2 80% 2 tours\n(No skillbooks)\n**PV**: 24210\n**Attaque**: 1730\n**Défense**: 2697\n**Récupération**:1648", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Feli','BoisFeli']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607329061882036225/MastercatG_large.jpg", color=0xffffff)
     embed.set_author(name="#193 Félinelame (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607329061882036225/MastercatG_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35% (ToC)\n**Passif**: Défense réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Fatigue 100% 3 tours\n(No skillbooks)\n**PV**: 26212\n**Attaque**: 2588\n**Défense**: 1737\n**Récupération**:1566", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Feli','LightFeli']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607329054106058762/Mastercat_large.jpg", color=0xffffff)
     embed.set_author(name="#194 Félinelame (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607329054106058762/Mastercat_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35% (ToC)\n**Passif**: Nécrose 100% 2 tours\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 34203\n**Attaque**: 2221\n**Défense**: 2391\n**Récupération**:1881", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Feli','DarkFeli']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607329059239624714/MastercatD_large.jpg", color=0xffffff)
     embed.set_author(name="#195 Félinelame (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607329059239624714/MastercatD_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%(ToC)\n**Passif**: Boost de moral 30% de ses PA\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 23283\n**Attaque**: 3255\n**Défense**: 2363\n**Récupération**:1948", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### garuda ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Garu','FeuGaru']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556066714681347/MahagarudaR_large.jpeg", color=0xffffff)
     embed.set_author(name="#196 Garuda (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556066714681347/MahagarudaR_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: CR +20~25%\n**Passif**: Sceau 100% 2 tours\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 80% 1 tour\n(???)\n**PV**: 30965\n**Attaque**: 2247\n**Défense**: 3609\n**Récupération**:1968", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Garu','EauGaru']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556035668181005/MahagarudaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#197 Garuda (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556035668181005/MahagarudaB_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: CR +20~25%\n**Passif**: Défense réduite 80% 2 tours\n(Dmg +15%, Taux: +20%)\n**Actif**: Avantage élémentaire\n(Dmg +35%)\n**PV**: 24938\n**Attaque**: 3643\n**Défense**: 2901\n**Récupération**:2213", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Garu','BoisGaru','TopGaru']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556034820931595/Mahagaruda_large.jpeg", color=0xffffff)
     embed.set_author(name="#198 Garuda (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556034820931595/Mahagaruda_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: CR +20~25%\n**Passif**: Affaiblissement 70% 2 tours\n(Dmg +10%, Taux: +10%, tour: +1)\n**Actif**: Frappe Courageuse\n(Dmg +30%)\n**PV**: 31976\n**Attaque**: 3036\n**Défense**: 2787\n**Récupération**:2181", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Garu','LightGaru']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556068534747136/MahagarudaW_large.jpeg", color=0xffffff)
     embed.set_author(name="#199 Garuda (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556068534747136/MahagarudaW_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: CR +20~25%\n**Passif**: Choc 80% 2 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Choc 70% 1 tour\n(???)\n**PV**: 25367\n**Attaque**: 3616\n**Défense**: 2670\n**Récupération**:2091", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Garu','DarkGaru']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556061941432353/MahagarudaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#200 Garuda (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556061941432353/MahagarudaD_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: CR +20~25%\n**Passif**: Avantage élémentaire\n(Dmg +40%)\n**Actif**: Avantage élémentaire\n(Dmg +40%)\n**PV**: 28207\n**Attaque**: 4018\n**Défense**: 2635\n**Récupération**:2343", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### gemini cricket ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Gem','FeuGem']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554192645128212/GemMiaR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#201 Gemini (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554192645128212/GemMiaR_Large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Siphon de PV   \n(No skillbooks)\n**Actif**: Siphon de PV (Allies)  \n(No skillbooks)\n**PV**: 28881\n**Attaque**: 2615\n**Défense**: 1777\n**Récupération**:1403", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Gem','LightGem']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554188228263960/GemMia_Large.jpeg", color=0xffffff)
     embed.set_author(name="#204 Gemini (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554188228263960/GemMia_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Adrénaline (Allies) 5% de ses PV\n(No skillbooks)\n**Actif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**PV**: 36301\n**Attaque**: 2221\n**Défense**: 2432\n**Récupération**:1853", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Gem','DarkGem']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554190753234961/GemMiaD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#205 Gemini (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554190753234961/GemMiaD_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%\n**Passif**: Siphon de PA (On crit) 30%\n(No skillbooks)\n**Actif**: Sommeil (On crit) 100%\n(No skillbooks)\n**PV**: 30832\n**Attaque**: 2362\n**Défense**: 2481\n**Récupération**:2352", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### spectros ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Spectro','LightSpectro']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557824001966091/PhantomW_large.jpeg", color=0xffffff)
     embed.set_author(name="#209 Spectros (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557824001966091/PhantomW_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Att +20~25%\n**Passif**: Étourdissement 100% (On crit) 1 tour\n(Dmg: +25%, +1 tour)\n**Actif**: Sommeil 100% (On crit) 1 tour\n(Dmg: +30%)\n**PV**: 35375\n**Attaque**: 1554\n**Défense**: 1758\n**Récupération**:1329", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Spectro','DarkSpectro']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557820390932500/Phantom_large.jpeg", color=0xffffff)
     embed.set_author(name="#210 Spectros (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557820390932500/Phantom_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Att +20~25%\n**Passif**: Attaque réduite 40% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 40% 2 tours\n(No skillbooks)\n**PV**: 26041\n**Attaque**: 2343\n**Défense**: 1566\n**Récupération**:1403", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### sacstère ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Sac','FeuSac']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557581956485873677/Musuri_large.jpeg", color=0xffffff)
     embed.set_author(name="#211 Sacstère (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557581956485873677/Musuri_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Rec +30~35%(Même élément)\n**Passif**: Boost de moral 20% de ses PA\n(No skillbooks)\n**Actif**: Vigueur 2 tours \n(No skillbooks)\n**PV**: 28878\n**Attaque**: 2137\n**Défense**: 1923\n**Récupération**:1854", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sac','EauSac']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556913166909440/MusuriB_large.jpeg", color=0xffffff)
     embed.set_author(name="#212 Sacstère (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556913166909440/MusuriB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Rec +30~35%(Même élément)\n**Passif**: Adrénaline (On crit)(Allies) 10% de ses PV\n(No skillbooks)\n**Actif**: Zèle 2 tours \n(No skillbooks)\n**PV**: 33802\n**Attaque**: 1704\n**Défense**: 1881\n**Récupération**:1704", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sac','BoisSac']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556902652051476/MusuriG_large.jpeg", color=0xffffff)
     embed.set_author(name="#213 Sacstère (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556902652051476/MusuriG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35%(Même élément)\n**Passif**: Nécrose 70% 1 tour\n(No skillbooks)\n**Actif**: Attaque augmentée  2 tours\n(No skillbooks)\n**PV**: 26327\n**Attaque**: 1873\n**Défense**: 1580\n**Récupération**:2492", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sac','LightSac']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556908092063747/MusuriW_large.jpeg", color=0xffffff)
     embed.set_author(name="#214 Sacstère (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556908092063747/MusuriW_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Rec +30~35%(Même élément)\n**Passif**: Adrénaline 20% de ses PV\n(No skillbooks)\n**Actif**: Attaque augmentée  2 tours\n(No skillbooks)\n**PV**: 37459\n**Attaque**: 1384\n**Défense**: 1881\n**Récupération**:1744", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sac','DarkSac']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556943722545167/MusuriD_large.jpeg", color=0xffffff)
     embed.set_author(name="#215 Sacstère (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556943722545167/MusuriD_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Rec +30~35%(Même élément)\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Bouclier (Flat) 2 tours\n(No skillbooks)\n**PV**: 34292\n**Attaque**: 1663\n**Défense**: 1697\n**Récupération**:1799", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### gupp ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Gupp','EauGupp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555792293953578/Longchu_large.jpeg", color=0xffffff)
     embed.set_author(name="#217 Gupp (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555792293953578/Longchu_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Resist +10~15%\n**Passif**: Nécrose 60% 2 tours\n(No skillbooks)\n**Actif**: Sommeil 60% 1 tour\n(No skillbooks)\n**PV**: 26225\n**Attaque**: 2343\n**Défense**: 1696\n**Récupération**:1566", inline=False)
     
     await message.channel.send(embed=embed)
     
###########################
######### hades ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Hade','FeuHade']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553436533620736/DisPaterR_large.jpeg", color=0xffffff)
     embed.set_author(name="#221 Hades (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553436533620736/DisPaterR_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25%\n**Passif**: Malédiction 80% 2 tours\n(Dmg: +15% tour: +1)\n**Actif**: Malédiction foudroyante\n(Dmg: +25%)\n**PV**: 27281\n**Attaque**: 3480\n**Défense**: 2492\n**Récupération**:2622", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Hade','EauHade','TopHade']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553423887794207/DisPaterB_large.jpeg", color=0xffffff)
     embed.set_author(name="#222 Hades (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553423887794207/DisPaterB_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Resist -20~25%\n**Passif**: Défense réduite 70% 3 tours\n(Dmg: +25% Taux: +10%)\n**Actif**: Frappe Courageuse\n(Dmg: +20%)\n**PV**: 31922\n**Attaque**: 2703\n**Défense**: 2747\n**Récupération**:2644", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Hade','BoisHade']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553426559565855/DisPaterG_large.jpeg", color=0xffffff)
     embed.set_author(name="#223 Hades (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553426559565855/DisPaterG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Resist -20~25%\n**Passif**: Soif 80% -30% 2 tour\n(Dmg: +20%tour: +1)\n**Actif**: Agression (PV)\n(Dmg: +25%)\n**PV**: 41109\n**Attaque**: 2296\n**Défense**: 2609\n**Récupération**:2521", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Hade','LightHade']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553439352061952/DisPaterW_large.jpeg", color=0xffffff)
     embed.set_author(name="#224 Hades (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553439352061952/DisPaterW_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25%\n**Passif**: Prédateur 40%\n(Dmg: +25%)\n**Actif**: Prédateur 50%\n(Dmg: +30%)\n**PV**: 33137\n**Attaque**: 3718\n**Défense**: 2418\n**Récupération**:2159", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Hade','DarkHade']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553421815676929/DisPater_large.jpeg", color=0xffffff)
     embed.set_author(name="#225 Hades (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553421815676929/DisPater_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25%\n**Passif**: Malédiction 80% 3 tours\n(Dmg: +20% Taux: +10%)\n**Actif**: Malédiction foudroyante\n(Dmg: +20%)\n**PV**: 32967\n**Attaque**: 3677\n**Défense**: 2595\n**Récupération**:2036", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### hana ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Hana','FeuHana']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554558396694528/HanahimeR_large.jpeg", color=0xffffff)
     embed.set_author(name="#226 Hana (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554558396694528/HanahimeR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35%\n**Passif**: Sommeil 70% 1 tour\n(???)\n**Actif**: Boost de moral 3 tours\n(Dmg +25%+Effect.: +10%)\n**PV**: 30468\n**Attaque**: 2036\n**Défense**: 2431\n**Récupération**:2881", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Hana','EauHana']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554554244202516/HanahimeB_large.jpeg", color=0xffffff)
     embed.set_author(name="#227 Hana (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554554244202516/HanahimeB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35%\n**Passif**: Nécrose x2 60% 1 tour\n(Taux: +20%, tour: +1)\n**Actif**: Volonté 3 tours\n(Dmg +25%, Taux: +20%)\n**PV**: 32463\n**Attaque**: 2125\n**Défense**: 1954\n**Récupération**:3310", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Hana','BoisHana','TopHana']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554551585275905/Hanahime_large.jpeg", color=0xffffff)
     embed.set_author(name="#228 Hana (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554551585275905/Hanahime_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35%\n**Passif**: Attaque réduite 70% 2 tour\n(Dmg +10%, Taux: +10%)\n**Actif**: Défense augmentée 3 tours\n(Dmg +25%, Taux: +10%)\n**PV**: 32443\n**Attaque**: 2138\n**Défense**: 1989\n**Récupération**:3364", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Hana','LightHana']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554561467056139/HanahimeW_large.jpeg", color=0xffffff)
     embed.set_author(name="#229 Hana (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554561467056139/HanahimeW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Rec +30~35%\n**Passif**: Agression (PV)\n(Dmg +20%)\n**Actif**: Bouclier (PV) 3 tours\n(Dmg +25%)\n**PV**: 36805\n**Attaque**: 1976\n**Défense**: 1996\n**Récupération**:2357", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Hana','DarkHana']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554555599093760/HanahimeD_large.jpeg", color=0xffffff)
     embed.set_author(name="#230 Hana (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554555599093760/HanahimeD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35%\n**Passif**: Abondance d'âmes rouges \n(Dmg +30%)\n**Actif**: Bouclier (Level) 3 tours\n(Dmg +25%)\n**PV**: 29624\n**Attaque**: 2125\n**Défense**: 1982\n**Récupération**:3058", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### lermite ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Lerm','EauLerm']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555361773682718/Komorix_large.jpeg", color=0xffffff)
     embed.set_author(name="#232 Lermite (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555361773682718/Komorix_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +15%, Taux: +10%)\n**Actif**: Provocation intrépide 80% 1 tour\n(???)\n**PV**: 29787\n**Attaque**: 2343\n**Défense**: 3139\n**Récupération**:1750", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### hohenheim ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Hohe','FeuHohe','TopHohe']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607635465113305099/ParacelsusR_large.jpg", color=0xffffff)
     embed.set_author(name="#236 Hohenheim (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607635465113305099/ParacelsusR_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Att +35~40%\n**Passif**: Défense réduite 70% 3 tours\n(Dmg: +25% Taux: +10%)\n**Actif**: Étourdissement 50% 2 tours\n(Dmg: +25% Taux: +10)\n**PV**: 43213\n**Attaque**: 2378\n**Défense**: 2630\n**Récupération**:2412", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Hohe','EauHohe']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607635473526947885/ParacelsusB_large.jpg", color=0xffffff)
     embed.set_author(name="#237 Hohenheim (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607635473526947885/ParacelsusB_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +35~40%\n**Passif**: Vague martiale 20%\n(Dmg: +20% Effect.: +5%)\n**Actif**: Taux critique augmenté 2 tours\n(Dmg: +20% tour: +1)\n**PV**: 32242\n**Attaque**: 3009\n**Défense**: 2999\n**Récupération**:2556", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Hohe','BoisHohe']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607635470511505439/Paracelsus_large.jpg", color=0xffffff)
     embed.set_author(name="#238 Hohenheim (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607635470511505439/Paracelsus_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +35~40%\n**Passif**: Résistance réduite 100% 2 tours\n(Dmg: +30% )\n**Actif**: Nécrose x3 80% 2 tour\n(Dmg: +10% Taux: +20%)\n**PV**: 27233\n**Attaque**: 3582\n**Défense**: 2901\n**Récupération**:2561", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Hohe','LightHohe']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607635467797790729/ParacelsusW_large.jpg", color=0xffffff)
     embed.set_author(name="#239 Hohenheim (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607635467797790729/ParacelsusW_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +35~40%\n**Passif**: Siphon de PA 30%\n(No skillbooks)\n**Actif**: Attaque augmentée 2 tours\n(No skillbooks)\n**PV**: 28105\n**Attaque**: 3841\n**Défense**: 2499\n**Récupération**:2418", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Hohe','DarkHohe']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607635462743654423/ParacelsusD_large.jpg", color=0xffffff)
     embed.set_author(name="#240 Hohenheim (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607635462743654423/ParacelsusD_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +35~40%\n**Passif**: Prédateur 40%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 28357\n**Attaque**: 3718\n**Défense**: 2567\n**Récupération**:2370", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### chasseur ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Chas','FeuChas']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560671754027032/VanhelsingR_large.jpeg", color=0xffffff)
     embed.set_author(name="#241 Chasseur (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560671754027032/VanhelsingR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20(League)\n**Passif**: Boost de moral (On crit) 100% de ses PA\n(Dmg +25%)\n**Actif**: Étourdissement 80% (On crit) 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 25776\n**Attaque**: 2595\n**Défense**: 1573\n**Récupération**:1737", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chas','EauChas']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560665756434453/Vanhelsing_large.jpeg", color=0xffffff)
     embed.set_author(name="#242 Chasseur (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560665756434453/Vanhelsing_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20(League)\n**Passif**: Siphon de PV\n(Dmg +30%)\n**Actif**: Siphon de PV\n(Dmg +30%)\n**PV**: 29164\n**Attaque**: 1960\n**Défense**: 1684\n**Récupération**:1664", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chas','BoisChas']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560669648617482/VanhelsingG_large.jpeg", color=0xffffff)
     embed.set_author(name="#243 Chasseur (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560669648617482/VanhelsingG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: CR +15~20(League)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg +20%, Taux: +5%)\n**Actif**: Nécrose x3 50% 1 tour\n(Dmg +10%Taux: +10%, tour: +1)\n**PV**: 30420\n**Attaque**: 1539\n**Défense**: 2554\n**Récupération**:1832", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chas','LightChas']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560673993916417/VanhelsingW_large.jpeg", color=0xffffff)
     embed.set_author(name="#244 Chasseur (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560673993916417/VanhelsingW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20(League)\n**Passif**: Choc 50% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Siphon de PV\n(Dmg +30%)\n**PV**: 30808\n**Attaque**: 3064\n**Défense**: 1873\n**Récupération**:2070", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chas','DarkChas']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560667505459251/VanhelsingD_large.jpeg", color=0xffffff)
     embed.set_author(name="#245 Chasseur (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560667505459251/VanhelsingD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +15~20(League)\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Nécrose x2 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 30114\n**Attaque**: 2309\n**Défense**: 3139\n**Récupération**:1832", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### incubus ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Incu','FeuIncu','TopIncu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551634056642589/AzazelR_large.jpeg", color=0xffffff)
     embed.set_author(name="#246 Incubus (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551634056642589/AzazelR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Attaque réduite 70% 2 tours (on crit)\n(???)\n**Actif**: Frappe Courageuse (On crit)\n(Dmg +20%)\n**PV**: 31711\n**Attaque**: 2648\n**Défense**: 2535\n**Récupération**:1732", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Incu','EauIncu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557576304405512192/AzazelB_large.jpeg", color=0xffffff)
     embed.set_author(name="#247 Incubus (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557576304405512192/AzazelB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Provocation 80% 1 tour\n(Dmg +15%, Taux: +20%)\n**PV**: 36505\n**Attaque**: 2180\n**Défense**: 2432\n**Récupération**:1874", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Incu','BoisIncu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551631116435457/AzazelG_large.jpeg", color=0xffffff)
     embed.set_author(name="#248 Incubus (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551631116435457/AzazelG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 25095\n**Attaque**: 3173\n**Défense**: 2547\n**Récupération**:1771", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Incu','LightIncu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551638858989576/AzazelW_large.jpeg", color=0xffffff)
     embed.set_author(name="#249 Incubus (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551638858989576/AzazelW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Siphon de PV (Allies)\n(Dmg +20%)\n**Actif**: Choc 80% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 27962\n**Attaque**: 3167\n**Défense**: 2254\n**Récupération**:2091", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Incu','DarkIncu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551623755563008/Azazel_large.jpeg", color=0xffffff)
     embed.set_author(name="#250 Incubus (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551623755563008/Azazel_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Siphon de PV , Greatly)\n(Dmg +20%)\n**Actif**: Sceau 80% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 24822\n**Attaque**: 3221\n**Défense**: 2492\n**Récupération**:2111", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### indra ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Indr','FeuIndr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555001113739296/IndrasakraR_large.jpeg", color=0xffffff)
     embed.set_author(name="#251 Indra (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555001113739296/IndrasakraR_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +40~45%\n**Passif**: Avantage élémentaire\n(Dmg +30%)\n**Actif**: Sceau 70% 2 tours\n(Dmg +15%, Taux: +10%, tour: +1)\n**PV**: 31694\n**Attaque**: 3650\n**Défense**: 2288\n**Récupération**:2329", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Indr','EauIndr','TopIndr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554997502705694/IndrasakraB_large.jpeg", color=0xffffff)
     embed.set_author(name="#252 Indra (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554997502705694/IndrasakraB_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +40~45%\n**Passif**: Attaque réduite 80% 3 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Frappe Courageuse\n(Dmg +20%)\n**PV**: 27768\n**Attaque**: 3043\n**Défense**: 3033\n**Récupération**:2876", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Indr','BoisIndr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555002154188838/IndrasakraG_large.jpeg", color=0xffffff)
     embed.set_author(name="#253 Indra (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555002154188838/IndrasakraG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +40~45%\n**Passif**: Étourdissement 100% 1 tour \n(Dmg +15%, tour: +1)\n**Actif**: Soif 80% -30% 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 32841\n**Attaque**: 2846\n**Défense**: 2910\n**Récupération**:1929", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Indr','LightIndr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555003815002112/IndrasakraW_large.jpeg", color=0xffffff)
     embed.set_author(name="#254 Indra (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555003815002112/IndrasakraW_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +40~45%\n**Passif**: Boost Moral regen 20% PA\n(Dmg +30%)\n**Actif**: prédateur 50%\n(Dmg +30%)\n**PV**: 27281\n**Attaque**: 3977\n**Défense**: 2663\n**Récupération**:2240", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Indr','DarkIndr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554996357529610/Indrasakra_large.jpeg", color=0xffffff)
     embed.set_author(name="#255 Indra (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554996357529610/Indrasakra_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +40~45%\n**Passif**: Frappe Courageuse\n(Dmg +20%)\n**Actif**: Frappe Courageuse\n(Dmg +20%)\n**PV**: 28166\n**Attaque**: 3677\n**Défense**: 2554\n**Récupération**:2295", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### citrouillon ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Citr','FeuCitr','TopCitr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555117426114590/JacquelynR_large.jpeg", color=0xffffff)
     embed.set_author(name="#256 Citrouillon (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555117426114590/JacquelynR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV Rec +20~25%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 37091\n**Attaque**: 2391\n**Défense**: 2099\n**Récupération**:1956", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Citr','EauCitr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555097419284499/JacquelynB_large.jpeg", color=0xffffff)
     embed.set_author(name="#257 Citrouillon (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555097419284499/JacquelynB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV Rec +20~25%\n**Passif**: Sceau 70% 2 tours\n(Dmg +20%, tour: +1)\n**Actif**: Provocation 80% 1 tour\n(Dmg +20%, tour: +1)\n**PV**: 25374\n**Attaque**: 1954\n**Défense**: 2894\n**Récupération**:1525", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Citr','BoisCitr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555113470754841/JacquelynG_large.jpeg", color=0xffffff)
     embed.set_author(name="#258 Citrouillon (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555113470754841/JacquelynG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV Rec +20~25%\n**Passif**: Prédateur 30%\n(Dmg +10%, Taux: +15%)\n**Actif**: Nécrose 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 23781\n**Attaque**: 2418\n**Défense**: 1696\n**Récupération**:1818", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Citr','LightCitr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555119665741825/JacquelynW_large.jpeg", color=0xffffff)
     embed.set_author(name="#259 Citrouillon (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555119665741825/JacquelynW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV Rec +20~25%\n**Passif**: Boost de moral (On crit) 30% de ses PA\n(Dmg +20%, +Effect.: +10%)\n**Actif**: Chasseur 50%\n(Dmg +20%, Taux: +5%)\n**PV**: 25143\n**Attaque**: 3173\n**Défense**: 2281\n**Récupération**:2084", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Citr','DarkCitr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555093002813458/Jacquelyn_large.jpeg", color=0xffffff)
     embed.set_author(name="#260 Citrouillon (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555093002813458/Jacquelyn_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV Rec +20~25%\n**Passif**: Adrénaline (Allies) 5% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Nécrose x2 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 38759\n**Attaque**: 1813\n**Défense**: 2316\n**Récupération**:2133", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### jeanne ! Au secours !! ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Jean','FeuJean']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553975396827195/FreyjaR_large.jpeg", color=0xffffff)
     embed.set_author(name="#261 Jeanne (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553975396827195/FreyjaR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Abondance d'âmes rouges\n(No skillbooks)\n**PV**: 37942\n**Attaque**: 2194\n**Défense**: 1853\n**Récupération**:2058", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jean','EauJean']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553955138338847/FreyjaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#262 Jeanne (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553955138338847/FreyjaB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Sommeil 100% 1 tour\n(No skillbooks)\n**Actif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**PV**: 27049\n**Attaque**: 2220\n**Défense**: 3208\n**Récupération**:2050", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jean','BoisJean','TopJean']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557213220709072906/FreyjaG_large.jpeg", color=0xffffff)
     embed.set_author(name="#263 Jeanne (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557213220709072906/FreyjaG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Traqueur +30% CR\n(No skillbooks)\n**Actif**: Traqueur +30% CR\n(No skillbooks)\n**PV**: 23842\n**Attaque**: 3262\n**Défense**: 2091\n**Récupération**:1839", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jean','LightJean']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553920019300384/Freyja_large.jpeg", color=0xffffff)
     embed.set_author(name="#264 Jeanne (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553920019300384/Freyja_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 43560\n**Attaque**: 1472\n**Défense**: 2337\n**Récupération**:1874", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jean','DarkJean']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553955897376768/FreyjaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#265 Jeanne (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553955897376768/FreyjaD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Boost de moral 50% de ses PA\n(No skillbooks)\n**Actif**: Silence 80% 2 tours\n(No skillbooks)\n**PV**: 31544\n**Attaque**: 2206\n**Défense**: 3153\n**Récupération**:2138", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Jeanne S Evo ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['SJean','FeuJean','FeuSJean']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/706455947987386369/713107143728955534/20200521_210719.jpg", color=0xffffff)
     embed.set_author(name="#824 Jeanne SE (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706455947987386369/713107143728955534/20200521_210719.jpg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Abondance d'âmes rouges\n(No skillbooks)\n**PV**: 41905\n**Attaque**: 2419\n**Défense**: 1853\n**Récupération**: 2269", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['SJean','EauJean','EauSJean']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/706455947987386369/713107143959511151/20200521_210739.jpg", color=0xffffff)
     embed.set_author(name="#825 Jeanne SE (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706455947987386369/713107143959511151/20200521_210739.jpg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Sommeil 100% 1 tour\n(No skillbooks)\n**Actif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**PV**: 29760\n**Attaque**: 2452\n**Défense**: 3562\n**Récupération**: 2261", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['SJean','BoisJean','BoisSJean']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/706455947987386369/713107144240660580/20200521_210757.jpg", color=0xffffff)
     embed.set_author(name="#826 Jeanne SE (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706455947987386369/713107144240660580/20200521_210757.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Traqueur +30% CR\n(No skillbooks)\n**Actif**: Traqueur +30% CR\n(No skillbooks)\n**PV**: 28854\n**Attaque**: 3800\n**Défense**: 2309\n**Récupération**: 2029", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['SJean','LightJean','LightSJean']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/706455947987386369/713107144668348456/20200521_210814.jpg", color=0xffffff)
     embed.set_author(name="#827 Jeanne SE (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706455947987386369/713107144668348456/20200521_210814.jpg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 48081\n**Attaque**: 1622\n**Défense**: 2576\n**Récupération**: 2065", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['SJean','DarkJean','DarkSJean']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/706455947987386369/713107144945303695/20200521_210833.jpg", color=0xffffff)
     embed.set_author(name="#828 Jeanne SE (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706455947987386369/713107144945303695/20200521_210833.jpg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Boost de moral 50% de ses PA\n(No skillbooks)\n**Actif**: Silence 80% 2 tours\n(No skillbooks)\n**PV**: 34704\n**Attaque**: 2431\n**Défense**: 3500\n**Récupération**: 2356", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Médusine ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Medusi','FeuMedusi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555220014596136/JellionR_large.jpeg", color=0xffffff)
     embed.set_author(name="#266 Médusine (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555220014596136/JellionR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%(ToC)\n**Passif**: Siphon de PV \n(Dmg: +30%)\n**Actif**: Pétrification 40% 1 tour\n(Taux: +30%)\n**PV**: 25306\n**Attaque**: 2615\n**Défense**: 1784\n**Récupération**:1267", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Medusi','EauMedusi','TopMedusi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555191816290304/Jellion_large.jpeg", color=0xffffff)
     embed.set_author(name="#267 Médusine (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555191816290304/Jellion_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: PV +30~35%(ToC)\n**Passif**: Brise bouclier 100%\n(Dmg: +30%)\n**Actif**: Adrénaline (Allies) 5% de ses PV\n(Dmg: +20% Effect.: +5%)\n**PV**: 35599\n**Attaque**: 1717\n**Défense**: 1915\n**Récupération**:1465", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Medusi','BoisMedusi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555219054231559/JellionG_large.jpeg", color=0xffffff)
     embed.set_author(name="#268 Médusine (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555219054231559/JellionG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%(ToC)\n**Passif**: Attaque réduite 60% 1 tour\n(Dmg: +15% Taux: +10% tour: +1)\n**Actif**: Récupération réduite 60% 2 tours\n(Dmg: +10% Taux: +10% tour: +1)\n**PV**: 30206\n**Attaque**: 1763\n**Défense**: 1929\n**Récupération**:1752", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Medusi','LightMedusi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555221620883477/JellionW_large.jpeg", color=0xffffff)
     embed.set_author(name="#269 Médusine (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555221620883477/JellionW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%(ToC)\n**Passif**: Sceau 100% 2 tours\n(Dmg: +20% tour: +1)\n**Actif**: Défense réduite (On crit) 2 tours\n(Dmg: +20% tour: +1)\n**PV**: 22793\n**Attaque**: 3405\n**Défense**: 2077\n**Récupération**:1914", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Medusi','DarkMedusi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555215572697119/JellionD_large.jpeg", color=0xffffff)
     embed.set_author(name="#270 Médusine (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555215572697119/JellionD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%(ToC)\n**Passif**: Adrénaline (Allies) 5% de ses PV\n(Dmg: +20% Effect.: +5%)\n**Actif**: Agression (PV)\n(Dmg: +25%)\n**PV**: 32698\n**Attaque**: 2267\n**Défense**: 2311\n**Récupération**:2134", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Jiangshi ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Jiang','FeuJiang']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/553210252976324639/Jiangshi3EvoR_large.jpg", color=0xffffff)
     embed.set_author(name="#271 Jiangshi (Feu)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/553210252976324639/Jiangshi3EvoR_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Provocation intrépide -50% damage 1 tour 80% Provocation 2 tours\n(No skillbooks)\n**Actif**: Nécrose x2 60% 2 tours\n(No skillbooks)\n**PV**: 24918\n**Attaque**: 1832\n**Défense**: 2772\n**Récupération**:1594", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jiang','EauJiang']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/553210250979704835/Jiangshi3EvoB_large.jpg", color=0xffffff)
     embed.set_author(name="#272 Jiangshi (Eau)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/553210250979704835/Jiangshi3EvoB_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Malédiction 80% 2 tours\n(No skillbooks)\n**Actif**: Malédiction 80% 2 tours\n(No skillbooks)\n**PV**: 38855\n**Attaque**: 1799\n**Défense**: 1806\n**Récupération**:1622", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jiang','BoisJiang']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/553210252204703744/Jiangshi3EvoG_large.jpg", color=0xffffff)
     embed.set_author(name="#273 Jiangshi (Bois)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/553210252204703744/Jiangshi3EvoG_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Sommeil 80% 1 tours\n(No skillbooks)\n**Actif**: Frappe indéfectible \n(No skillbooks)\n**PV**: 26345\n**Attaque**: 2219\n**Défense**: 2358\n**Récupération**:1657", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jiang','LightJiang']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/553210254725480457/Jiangshi3EvoW_large.jpg", color=0xffffff)
     embed.set_author(name="#274 Jiangshi (light)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/553210254725480457/Jiangshi3EvoW_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Boost de moral (soi-même) 20% SP\n(No skillbooks)\n**Actif**: Siphon de PV (Allies, Greatly)\n(No skillbooks)\n**PV**: 26552\n**Attaque**: 3201\n**Défense**: 2247\n**Récupération**:1961", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jiang','DarkJiang']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/553210249843048461/Jiangshi3Evo_large.jpg", color=0xffffff)
     embed.set_author(name="#275 Jiangshi (dark)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/553210249843048461/Jiangshi3Evo_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Malédiction 80% 2 tours\n(No skillbooks)\n**Actif**: Malédiction foudroyante\n(No skillbooks)\n**PV**: 27322\n**Attaque**: 3255\n**Défense**: 2309\n**Récupération**:1954", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Djinn ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Djinn','FeuDjinn','TopDjinn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554941957406785/Ifrit_large.jpeg", color=0xffffff)
     embed.set_author(name="#276 Djinn (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554941957406785/Ifrit_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Boost de moral\n(No skillbooks)\n**Actif**: Prédateur 40%\n(No skillbooks)\n**PV**: 26927\n**Attaque**: 3337\n**Défense**: 2193\n**Récupération**:1982", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Djinn','EauDjinn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554941974183958/IfritB_large.jpeg", color=0xffffff)
     embed.set_author(name="#277 Djinn (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554941974183958/IfritB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +15~20%\n**Passif**: Boost de moral (Allies) 10% SP\n(No skillbooks)\n**Actif**: Pétrification 80% 1 tour\n(No skillbooks)\n**PV**: 29957\n**Attaque**: 2322\n**Défense**: 2595\n**Récupération**:2206", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Djinn','BoisDjinn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554946260893714/IfritG_large.jpeg", color=0xffffff)
     embed.set_author(name="#278 Djinn (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554946260893714/IfritG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Nécrose x3 80% 1 tour\n(No skillbooks)\n**PV**: 28919\n**Attaque**: 3018\n**Défense**: 1976\n**Récupération**:1996", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Djinn','LightDjinn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554948643127296/IfritW_large.jpeg", color=0xffffff)
     embed.set_author(name="#279 Djinn (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554948643127296/IfritW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Chasseur 50%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 25156\n**Attaque**: 3296\n**Défense**: 2704\n**Récupération**:2077", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Djinn','DarkDjinn']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554944339902536/IfritD_large.jpeg", color=0xffffff)
     embed.set_author(name="#280 Djinn (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554944339902536/IfritD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%\n**Passif**: Résistance réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Affaiblissement 80% 2 tour\n(No skillbooks)\n**PV**: 38827\n**Attaque**: 2294\n**Défense**: 1889\n**Récupération**:2140", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### kiki ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Kiki','FeuKiki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557213368314888192/KikimoraR_large.jpeg", color=0xffffff)
     embed.set_author(name="#281 Kiki (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557213368314888192/KikimoraR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(ToC)\n**Passif**: Brise bouclier 100%\n(Dmg +25%)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 25316\n**Attaque**: 2335\n**Défense**: 2345\n**Récupération**:2038", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Kiki','EauKiki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555271101218816/KikimoraB_large.jpeg", color=0xffffff)
     embed.set_author(name="#282 Kiki (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555271101218816/KikimoraB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(ToC)\n**Passif**: Brise-Bonus 100%\n(Dmg +25%)\n**Actif**: Aveuglement 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 28742\n**Attaque**: 1885\n**Défense**: 2038\n**Récupération**:2004", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Kiki','BoisKiki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555266462187520/Kikimora_large.jpeg", color=0xffffff)
     embed.set_author(name="#283 Kiki (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555266462187520/Kikimora_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(ToC)\n**Passif**: Pétrification (On crit) 1 tour\n(Dmg +20%)\n**Actif**: Chasseur 30%\n(Dmg +20%)\n**PV**: 25897\n**Attaque**: 2751\n**Défense**: 1621\n**Récupération**:1730", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Kiki','LightKiki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555287530438656/KikimoraW_large.jpeg", color=0xffffff)
     embed.set_author(name="#284 Kiki (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555287530438656/KikimoraW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(ToC)\n**Passif**: Faiblesse exposée 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Choc 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 26246\n**Attaque**: 2452\n**Défense**: 3568\n**Récupération**:1941", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Kiki','DarkKiki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555282191089686/KikimoraD_large.jpeg", color=0xffffff)
     embed.set_author(name="#285 Kiki (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555282191089686/KikimoraD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(ToC)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Prédateur 30%\n(Dmg +20%)\n**PV**: 27744\n**Attaque**: 3357\n**Défense**: 2309\n**Récupération**:2036", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### kiloptère ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Kilo','LightKilo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560481378893864/UltrabatW_large.jpeg", color=0xffffff)
     embed.set_author(name="#289 Kiloptère (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560481378893864/UltrabatW_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: CR +10~15%\n**Passif**: Attaque réduite 100% 1 tour\n(No skillbooks)\n**Actif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**PV**: 29249\n**Attaque**: 1321\n**Défense**: 2527\n**Récupération**:1573", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Kilo','DarkKilo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560476828205056/Ultrabat_large.jpeg", color=0xffffff)
     embed.set_author(name="#290 Kiloptère (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560476828205056/Ultrabat_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: CR +10~15%\n**Passif**: Traqueur (Dark) 20%\n(No skillbooks)\n**Actif**: Pétrification 40% 1 tour\n(No skillbooks)\n**PV**: 25776\n**Attaque**: 2302\n**Défense**: 1471\n**Récupération**:1641", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Latt ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Latt','FeuLatt']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552058390052879/BlizzardR_large.jpeg", color=0xffffff)
     embed.set_author(name="#291 Latt (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552058390052879/BlizzardR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(League)\n**Passif**: Étourdissement 40% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Récupération réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 26838\n**Attaque**: 2622\n**Défense**: 1532\n**Récupération**:1600", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Latt','EauLatt','TopLatt']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552051075317780/Blizzard_large.jpeg", color=0xffffff)
     embed.set_author(name="#292 Latt (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552051075317780/Blizzard_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Att +30~35%(League)\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 38140\n**Attaque**: 1574\n**Défense**: 1506\n**Récupération**:1887", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Latt','BoisLatt']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552056536301588/BlizzardG_large.jpeg", color=0xffffff)
     embed.set_author(name="#293 Latt (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552056536301588/BlizzardG_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(League)\n**Passif**: Nécrose 40% 1 tour\n(Dmg +10%, Taux: +20%)\n**Actif**: Fatigue 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 30015\n**Attaque**: 1620\n**Défense**: 1766\n**Récupération**:1623", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Latt','LightLatt']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557584671039422474/BlizzardW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#294 Latt (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557584671039422474/BlizzardW_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(League)\n**Passif**: Choc 60% 1 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite 80% 2 tours\n(Dmg +25%)\n**PV**: 29688\n**Attaque**: 2389\n**Défense**: 2501\n**Récupération**:2474", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Latt','DarkLatt']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552053319270426/BlizzardD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#295 Latt (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552053319270426/BlizzardD_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35% (League)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Chasseur 30%\n(Dmg +20%)\n**PV**: 30652\n**Attaque**: 2996\n**Défense**: 1907\n**Récupération**:2002", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Léo ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Leo','FeuLeo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555628963561473/Leon_large.jpeg", color=0xffffff)
     embed.set_author(name="#296 Leo (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555628963561473/Leon_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 26348\n**Attaque**: 3173\n**Défense**: 2281\n**Récupération**:1641", inline=False)
     
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Leo','EauLeo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555634298716162/LeonB_large.jpeg", color=0xffffff)
     embed.set_author(name="#298 Leo (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555634298716162/LeonB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Provocation intrépide 90% 2 tour\n(???)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 36941\n**Attaque**: 2364\n**Défense**: 1813\n**Récupération**:1922", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Leo','BoisLeo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555655307722797/LeonG_large.jpeg", color=0xffffff)
     embed.set_author(name="#300 Leo (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555655307722797/LeonG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 30059\n**Attaque**: 2363\n**Défense**: 3139\n**Récupération**:1880", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Leo','LightLeo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555657581035527/LeonW_large.jpeg", color=0xffffff)
     embed.set_author(name="#302 Leo (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555657581035527/LeonW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Boost de moral 50% de ses PA\n(Dmg +10%, +Effect.: +10%)\n**Actif**: Étourdissement 50% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 27281\n**Attaque**: 3139\n**Défense**: 2261\n**Récupération**:2118", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Leo','DarkLeo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555651872849930/LeonD_large.jpeg", color=0xffffff)
     embed.set_author(name="#304 Leo (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555651872849930/LeonD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Attaque réduite 100% 2 tours\n(Dmg +15%, tour: +1)\n**Actif**: Silence 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 28091\n**Attaque**: 3276\n**Défense**: 2002\n**Récupération**:2070", inline=False)
     
     await message.channel.send(embed=embed)

	 
###########################
######### Léo S Evo ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['FeuLeo','SLeo','FeuSLeo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559867416805376/SuperLionking_large.jpeg", color=0xffffff)
     embed.set_author(name="#297 Leo SE (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559867416805376/SuperLionking_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 28990\n**Attaque**: 3521\n**Défense**: 2520\n**Récupération**:1811", inline=False)
     
     await message.channel.send(embed=embed)
 
 if any([message.content.startswith (item) for item in ['EauLeo','SLeo','EauSLeo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559870100897812/SuperLionkingB_large.jpeg", color=0xffffff)
     embed.set_author(name="#299 Leo SE (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559870100897812/SuperLionkingB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Provocation 80% 1 tour\n(Dmg +10%, Taux: +20%)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 40801\n**Attaque**: 2603\n**Défense**: 1997\n**Récupération**:2119", inline=False)
     
     await message.channel.send(embed=embed)
	 
 if any([message.content.startswith (item) for item in ['BoisLeo','SLeo','BoisSLeo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559889382113295/SuperLionkingG_large.jpeg", color=0xffffff)
     embed.set_author(name="#301 Leo SE (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559889382113295/SuperLionkingG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 33069\n**Attaque**: 2608\n**Défense**: 3487\n**Récupération**:2077", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['LightLeo','SLeo','LightSLeo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559892381040640/SuperLionkingW_large.jpeg", color=0xffffff)
     embed.set_author(name="#303 Leo SE (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559892381040640/SuperLionkingW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Boost de moral 50% de ses PA\n(Dmg +10%, +Effect.: +10%)\n**Actif**: Étourdissement 50% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 30018\n**Attaque**: 3487\n**Défense**: 2492\n**Récupération**:2336", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['DarkLeo','SLeo','DarkSLeo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559885582204928/SuperLionkingD_large.jpeg", color=0xffffff)
     embed.set_author(name="#305 Leo SE (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559885582204928/SuperLionkingD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Attaque réduite 100% 2 tours\n(Dmg +15%, tour: +1)\n**Actif**: Silence 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 30911\n**Attaque**: 3637\n**Défense**: 2206\n**Récupération**:2281", inline=False)
     
     await message.channel.send(embed=embed)

###########################
######### Loki ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Loki','FeuLoki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560415549423619/TricksterlokiR_large.jpeg", color=0xffffff)
     embed.set_author(name="#306 Loki (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560415549423619/TricksterlokiR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Nécrose 80% 2 tours\n(Dmg +15%, tour: +1)\n**Actif**: Nécrose x2 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 33856\n**Attaque**: 2253\n**Défense**: 2229\n**Récupération**:2066", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Loki','EauLoki','TopLoki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560403012517889/TricksterlokiB_large.jpeg", color=0xffffff)
     embed.set_author(name="#307 Loki (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560403012517889/TricksterlokiB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Prédateur 30%\n(Dmg +25%)\n**PV**: 30556\n**Attaque**: 3139\n**Défense**: 2023\n**Récupération**:1907", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Loki','BoisLoki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560400420569099/Tricksterloki_large.jpeg", color=0xffffff)
     embed.set_author(name="#308 Loki (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560400420569099/Tricksterloki_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Sommeil 70% 1 tour\n(Dmg +15%, tour: +1)\n**PV**: 24496\n**Attaque**: 2418\n**Défense**: 3391\n**Récupération**:1900", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Loki','LightLoki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557586319992291339/TricksterlokiW_large.jpeg", color=0xffffff)
     embed.set_author(name="#309 Loki (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557586319992291339/TricksterlokiW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Attaque réduite 60% 3 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 31391\n**Attaque**: 2430\n**Défense**: 2474\n**Récupération**:2365", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Loki','DarkLoki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560407211147275/TricksterlokiD_large.jpeg", color=0xffffff)
     embed.set_author(name="#310 Loki (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560407211147275/TricksterlokiD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Sceau 80% 2 tours\n(Dmg +20%, tour: +1)\n**Actif**: Sceau 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 36757\n**Attaque**: 2180\n**Défense**: 2405\n**Récupération**:1853", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### lucy ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Lucy','FeuLucy']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559334324830219/SnowwhiteR_large.jpeg", color=0xffffff)
     embed.set_author(name="#311 Lucy (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559334324830219/SnowwhiteR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%(League)\n**Passif**: Siphon de PV \n(Dmg +25%)\n**Actif**: Sceau 80% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 23494\n**Attaque**: 3378\n**Défense**: 2349\n**Récupération**:1900", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Lucy','EauLucy','TopLucy']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559321473482764/Snowwhite_large.jpeg", color=0xffffff)
     embed.set_author(name="#312 Lucy (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559321473482764/Snowwhite_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%(League)\n**Passif**: Attaque réduite 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 28098\n**Attaque**: 3276\n**Défense**: 2009\n**Récupération**:2043", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Lucy','BoisLucy']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559324556427267/SnowwhiteG_large.jpeg", color=0xffffff)
     embed.set_author(name="#313 Lucy (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559324556427267/SnowwhiteG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR -15~20%(League)\n**Passif**: Nécrose 90% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 30689\n**Attaque**: 2376\n**Défense**: 2481\n**Récupération**:2331", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Lucy','LightLucy']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559383763222588/SnowwhiteW_large.jpeg", color=0xffffff)
     embed.set_author(name="#314 Lucy (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559383763222588/SnowwhiteW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR -15~20%(League)\n**Passif**: Choc 70% 1 tour\n(Dmg +15%)\n**Actif**: Choc 70% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 38984\n**Attaque**: 2084\n**Défense**: 2405\n**Récupération**:1853", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Lucy','DarkLucy']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559322496761866/SnowwhiteD_large.jpeg", color=0xffffff)
     embed.set_author(name="#315 Lucy (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559322496761866/SnowwhiteD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%(League)\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Faiblesse exposée 80% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 27349\n**Attaque**: 3439\n**Défense**: 2288\n**Récupération**:2084", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### lumo ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Lumo','FeuLumo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557213503161892894/LuminaR_large.jpeg", color=0xffffff)
     embed.set_author(name="#316 Lumo (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557213503161892894/LuminaR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +20~25%\n**Passif**: Défense réduite 40% 2 tours\n(No skillbooks)\n**Actif**: Récupération augmentée 2 tours\n(No skillbooks)\n**PV**: 25497\n**Attaque**: 1648\n**Défense**: 1682\n**Récupération**:2315", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Lumo','EauLumo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555923709886484/LuminaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#317 Lumo (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555923709886484/LuminaB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%\n**Passif**: Récupération réduite 40% 1 tours\n(No skillbooks)\n**Actif**: Attaque augmentée  2 tours\n(No skillbooks)\n**PV**: 28977\n**Attaque**: 1743\n**Défense**: 2384\n**Récupération**:1301", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Lumo','BoisLumo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555924376518678/Lumina_large.jpeg", color=0xffffff)
     embed.set_author(name="#318 Lumo (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555924376518678/Lumina_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +20~25%\n**Passif**: Attaque réduite 40% 1 tours\n(No skillbooks)\n**Actif**: Blue souls SP up 2 tours\n(No skillbooks)\n**PV**: 29290\n**Attaque**: 1410\n**Défense**: 1832\n**Récupération**:2288", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### lupin ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Lupin','FeuLupin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556893927899138/MysteriousLupinR_large.jpeg", color=0xffffff)
     embed.set_author(name="#321 Lupin (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556893927899138/MysteriousLupinR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Prédateur 30%\n(No skillbooks)\n**Actif**: Défense réduite (On crit) 2 tours\n(No skillbooks)\n**PV**: 25122\n**Attaque**: 3262\n**Défense**: 2295\n**Récupération**:2084", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Lupin','EauLupin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556905772482580/MysteriousLupinB_large.jpeg", color=0xffffff)
     embed.set_author(name="#322 Lupin (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556905772482580/MysteriousLupinB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Adrénaline 25% de ses PV\n(No skillbooks)\n**Actif**: Sommeil 80% 1 tour\n(No skillbooks)\n**PV**: 41402\n**Attaque**: 2391\n**Défense**: 1785\n**Récupération**:1922", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Lupin','BoisLupin','TopLupin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556898126135297/MysteriousLupinG_large.jpeg", color=0xffffff)
     embed.set_author(name="#323 Lupin (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556898126135297/MysteriousLupinG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**PV**: 30151\n**Attaque**: 2614\n**Défense**: 2440\n**Récupération**:2311", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Lupin','DarkLupin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328062346100736/BossMysteriousLupin_large.jpg", color=0xffffff)
     embed.set_author(name="#325 Lupin (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328062346100736/BossMysteriousLupin_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Siphon de PA 25%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 27451\n**Attaque**: 3310\n**Défense**: 2261\n**Récupération**:2084", inline=False)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('Lupina'):
        return

 if message.content.startswith('DarkLupina'):
        return

 if message.content.startswith('BoisLupina'):
        return

 if message.content.startswith('EauLupina'):
        return

 if message.content.startswith('FeuLupina'):
        return

 if message.content.startswith('LightLupina'):
        return
		
###########################
######### mammont ##################
###########################
		
 if any([message.content.startswith (item) for item in ['Mam','FeuMam']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556260046667777/MaroudonR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#326 Mammont (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556260046667777/MaroudonR_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Rec +30~35%\n**Passif**: Provocation 80% 2 tours\n(No skillbooks)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**PV**: 35313\n**Attaque**: 2364\n**Défense**: 2092\n**Récupération**:2017", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mam','EauMam','TopMam']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556255621939201/Maroudon_Large.jpeg", color=0xffffff)
     embed.set_author(name="#327 Mammont (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556255621939201/Maroudon_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Rec +30~35%\n**Passif**: Chasseur 50%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 22793\n**Attaque**: 3126\n**Défense**: 1989\n**Récupération**:2138", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mam','BoisMam']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556258184527873/MaroudonG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#328 Mammont (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556258184527873/MaroudonG_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Rec +30~35%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**Actif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**PV**: 30134\n**Attaque**: 1907\n**Défense**: 3173\n**Récupération**:2220", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mam','LightMam']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556267126652931/MaroudonW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#329 Mammont (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556267126652931/MaroudonW_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Rec +30~35%\n**Passif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Aveuglement 80% 2 tours\n(No skillbooks)\n**PV**: 34115\n**Attaque**: 2253\n**Défense**: 2195\n**Récupération**:2059", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mam','DarkMam']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556256762658816/MaroudonD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#330 Mammont (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556256762658816/MaroudonD_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Rec +30~35%\n**Passif**: Adrénaline 20% de ses PV\n(No skillbooks)\n**Actif**: Vengeance\n(No skillbooks)\n**PV**: 30611\n**Attaque**: 3017\n**Défense**: 1982\n**Récupération**:2023", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### mandragore ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Mand','FeuMand','TopMand']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556758892281870/MoonflowerR_large.jpeg", color=0xffffff)
     embed.set_author(name="#331 Mandragore (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556758892281870/MoonflowerR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%(Même élément)\n**Passif**: Sommeil (On crit) 1 tour\n(Dmg +25%)\n**Actif**: Chasseur 30%\n(Dmg +20%)\n**PV**: 29385\n**Attaque**: 2608\n**Défense**: 1886\n**Récupération**:1559", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mand','EauMand']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556750818115585/MoonflowerB_large.jpeg", color=0xffffff)
     embed.set_author(name="#332 Mandragore (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556750818115585/MoonflowerB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%,(Même élément)\n**Passif**: Fatigue 60% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**Actif**: Récupération réduite 60% 2 tours\n(Dmg +10%, Taux: +10%, tour: +1)\n**PV**: 26838\n**Attaque**: 2622\n**Défense**: 1512\n**Récupération**:1580", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mand','BoisMand']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556750705000448/Moonflower_large.jpeg", color=0xffffff)
     embed.set_author(name="#333 Mandragore (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556750705000448/Moonflower_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%(Même élément)\n**Passif**: Nécrose 60% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**Actif**: Sommeil 40% 1 tour\n(Taux: +30%)\n**PV**: 29603\n**Attaque**: 1430\n**Défense**: 2833\n**Récupération**:1702", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mand','LightMand']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556759823155220/MoonflowerW_large.jpeg", color=0xffffff)
     embed.set_author(name="#334 Mandragore (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556759823155220/MoonflowerW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%(Même élément)\n**Passif**: Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Nécrose x3 90% 1 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 30611\n**Attaque**: 1907\n**Défense**: 3439\n**Récupération**:2159", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mand','DarkMand']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556754228084739/MoonflowerD_large.jpeg", color=0xffffff)
     embed.set_author(name="#335 Mandragore (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556754228084739/MoonflowerD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35% (Même élément)\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 30441\n**Attaque**: 3187\n**Défense**: 1880\n**Récupération**:2036", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### végédalle ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Vege','FeuVege']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556196398366720/VégédalleR_large.jpeg", color=0xffffff)
     embed.set_author(name="#336 Végédalle (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556196398366720/VégédalleR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Récupération réduite 80% 2 tours\n(No skillbooks)\n**PV**: 27049\n**Attaque**: 2527\n**Défense**: 1403\n**Récupération**:1478", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Vege','EauVege']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556173111590966/VégédalleB_large.jpeg", color=0xffffff)
     embed.set_author(name="#337 Végédalle (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556173111590966/VégédalleB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Def +20~25%\n**Passif**: Sommeil 60% 1 tour\n(No skillbooks)\n**Actif**: Fatigue 80% 2 tours\n(No skillbooks)\n**PV**: 36675\n**Attaque**: 1710\n**Défense**: 1206\n**Récupération**:1343", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Vege','BoisVege']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556172411142144/Végédalle_large.jpeg", color=0xffffff)
     embed.set_author(name="#338 Végédalle (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556172411142144/Végédalle_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Def +20~25%\n**Passif**: Pétrification 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 80% 2 tours\n(No skillbooks)\n**PV**: 29334\n**Attaque**: 1933\n**Défense**: 1895\n**Récupération**:1691", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### mari ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Mari','FeuMari']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551483875524614/AriaR_large.jpeg", color=0xffffff)
     embed.set_author(name="#341 Mari (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551483875524614/AriaR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Adrénaline 30% de ses PV\n(No skillbooks)\n**Actif**: Nécrose x2 80% 1 tour\n(No skillbooks)\n**PV**: 20219\n**Attaque**: 3037\n**Défense**: 2036\n**Récupération**:1559", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mari','EauMari']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551473771184149/Aria_Large.jpeg", color=0xffffff)
     embed.set_author(name="#342 Mari (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551473771184149/Aria_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**Actif**: Attaque réduite 70% 1 tour\n(No skillbooks)\n**PV**: 28749\n**Attaque**: 2521\n**Défense**: 2473\n**Récupération**:2432", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mari','BoisMari']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557213757726785557/AriaG_large.jpeg", color=0xffffff)
     embed.set_author(name="#343 Mari (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557213757726785557/AriaG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Défense réduite (On crit) 2 tours\n(No skillbooks)\n**Actif**: Défense réduite 70% 2 tours\n(No skillbooks)\n**PV**: 26825\n**Attaque**: 2581\n**Défense**: 1907\n**Récupération**:1607", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mari','LightMari']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551487277105152/AriaW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#344 Mari (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551487277105152/AriaW_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Agression (Def)\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 27649\n**Attaque**: 2009\n**Défense**: 3568\n**Récupération**:1989", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mari','DarkMari']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557587010664267789/AriaD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#345 Mari (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557587010664267789/AriaD_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Vague martiale\n(No skillbooks)\n**Actif**: Prédateur 40%\n(No skillbooks)\n**PV**: 29549\n**Attaque**: 3092\n**Défense**: 2118\n**Récupération**:2009", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### médusa ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Medusa','FeuMedusa','TopMedusa']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559575547641887/Sthenno_large.jpeg", color=0xffffff)
     embed.set_author(name="#346 Médusa (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559575547641887/Sthenno_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: SP Rec +20~25%(Même élément)\n**Passif**: Pétrification 60% 1 tour\n(No skillbooks)\n**Actif**: Pétrification 60% 1 tour\n(No skillbooks)\n**PV**: 34523\n**Attaque**: 1642\n**Défense**: 1942\n**Récupération**:1336", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Medusa','EauMedusa']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559577225363477/SthennoB_large.jpeg", color=0xffffff)
     embed.set_author(name="#347 Médusa (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559577225363477/SthennoB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: SP Rec +20~25%(Même élément)\n**Passif**: Sommeil 80% 1 tour\n(No skillbooks)\n**Actif**: Soif 60% -10% 1 tour\n(No skillbooks)\n**PV**: 30403\n**Attaque**: 2049\n**Défense**: 2025\n**Récupération**:1225", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Medusa','BoisMedusa']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559581746954240/SthennoG_large.jpeg", color=0xffffff)
     embed.set_author(name="#348 Médusa (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559581746954240/SthennoG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%(Même élément)\n**Passif**: Nécrose 60% 3 tours\n(No skillbooks)\n**Actif**: Aveuglement 60% 1 tour\n(No skillbooks)\n**PV**: 29732\n**Attaque**: 1580\n**Défense**: 2472\n**Récupération**:1811", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Medusa','LightMedusa']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559604802912307/SthennoW_large.jpeg", color=0xffffff)
     embed.set_author(name="#349 Médusa (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559604802912307/SthennoW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%(Même élément)\n**Passif**: Étourdissement (On crit) 1 tour\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 27546\n**Attaque**: 2956\n**Défense**: 2288\n**Récupération**:2043", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Medusa','DarkMedusa']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559579305869332/SthennoD_large.jpeg", color=0xffffff)
     embed.set_author(name="#350 Médusa (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559579305869332/SthennoD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: SP Rec +20~25%(Même élément)\n**Passif**: Aveuglement 70% 2 tour\n(No skillbooks)\n**Actif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**PV**: 36056\n**Attaque**: 1942\n**Défense**: 2432\n**Récupération**:2010", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### mera ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Mera','FeuMera','TopMera']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552527086878733/Chimaira_large.jpeg", color=0xffffff)
     embed.set_author(name="#351 Mera (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552527086878733/Chimaira_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Traqueur 30%\n(Dmg +10%, Taux: +20%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg +20%)\n**PV**: 26212\n**Attaque**: 3187\n**Défense**: 2261\n**Récupération**:1641", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mera','EauMera']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552530798968832/ChimairaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#352 Mera (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552530798968832/ChimairaB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%\n**Passif**: Sceau 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 24445\n**Attaque**: 2812\n**Défense**: 2828\n**Récupération**:2658", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mera','BoisMera']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552561224187918/ChimairaG_large.jpeg", color=0xffffff)
     embed.set_author(name="#353 Mera (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552561224187918/ChimairaG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Fatigue 80% 3 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Soif 80% -30% 2 tours\n(Dmg +25%)\n**PV**: 36757\n**Attaque**: 2228\n**Défense**: 1881\n**Récupération**:2051", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mera','LightMera']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552562847383554/ChimairaW_large.jpeg", color=0xffffff)
     embed.set_author(name="#354 Mera (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552562847383554/ChimairaW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Sceau 60% 2 tours\n(Dmg  +15%, Taux: +15%)\n**PV**: 30822\n**Attaque**: 2043\n**Défense**: 2962\n**Récupération**:2322", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mera','DarkMera']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552558334443521/ChimairaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#355 Mera (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552558334443521/ChimairaD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Récupération réduite 80% 2 tours\n(Dmg +15%, Taux: +20%)\n**Actif**: Sommeil 100% 1 tour\n(Dmg +15%, tour: +1)\n**PV**: 39059\n**Attaque**: 1853\n**Défense**: 2303\n**Récupération**:2187", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### merlin ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Merl','FeuMerl']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556391848476672/MerlinusR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#356 Merlin (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556391848476672/MerlinusR_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25% \n**Passif**: Boost de moral 50% de ses PA\n(Dmg +20%, +Effect.: +10%)\n**Actif**: Chasseur 50%%\n(Dmg +30%)\n**PV**: 28037\n**Attaque**: 3398\n**Défense**: 2554\n**Récupération**:2384", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Merl','EauMerl']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556388795023365/Merlinus_Large.jpeg", color=0xffffff)
     embed.set_author(name="#357 Merlin (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556388795023365/Merlinus_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25%\n**Passif**: Boost de moral (Allies) 15% SP\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Avantage élémentaire\n(Dmg +30%)\n**PV**: 31537\n**Attaque**: 3494\n**Défense**: 2213\n**Récupération**:2343", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Merl','BoisMerl','TopMerl']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556390053576734/MerlinusG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#358 Merlin (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556390053576734/MerlinusG_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Resist -20~25%\n**Passif**: Frappe Courageuse\n(Dmg +30%)\n**Actif**: Frappe Courageuse\n(Dmg +30%)\n**PV**: 31037\n**Attaque**: 2982\n**Défense**: 2787\n**Récupération**:2576", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Merl','LightMerl']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556393345974282/MerlinusW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#359 Merlin (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556393345974282/MerlinusW_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Resist -20~25%\n**Passif**: Choc 70% 2 tours\n(Dmg: +15% Taux: +10%)\n**Actif**: Avantage élémentaire\n(Dmg: +30%)\n**PV**: 32222\n**Attaque**: 3213\n**Défense**: 2924\n**Récupération**:1977", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Merl','DarkMerl']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556388769988608/MerlinusD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#360 Merlin (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556388769988608/MerlinusD_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Resist -20~25%\n**Passif**: Siphon de PA 30%\n(Dmg +15%, Taux: +5%)\n**Actif**: Étourdissement 80% 1 tour\n(Dmg +10%, Taux: +20%)\n**PV**: 40298\n**Attaque**: 2398\n**Défense**: 2834\n**Récupération**:1996", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### miho ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Miho','FeuMiho','TopMiho']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554848990789667/Horan_large.jpeg", color=0xffffff)
     embed.set_author(name="#361 Miho (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554848990789667/Horan_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg +20%, Taux: +20%)\n**PV**: 37363\n**Attaque**: 2180\n**Défense**: 1806\n**Récupération**:1397", inline=False)
     
     await message.channel.send(embed=embed)
	 
 if any([message.content.startswith (item) for item in ['Miho','EauMiho']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554851318628373/HoranB_large.jpeg", color=0xffffff)
     embed.set_author(name="#363 Miho (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554851318628373/HoranB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%\n**Passif**: Nécrose 100% 2 tours\n(Dmg +30%)\n**Actif**: Nécrose 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 31234\n**Attaque**: 2096\n**Défense**: 2072\n**Récupération**:1827", inline=False)
     
     await message.channel.send(embed=embed)
	 
 if any([message.content.startswith (item) for item in ['Miho','BoisMiho','TopMiho']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554855798013974/HoranG_large.jpeg", color=0xffffff)
     embed.set_author(name="#365 Miho (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554855798013974/HoranG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 28207\n**Attaque**: 2676\n**Défense**: 1798\n**Récupération**:1900", inline=False)
     
     await message.channel.send(embed=embed)
	 
 if any([message.content.startswith (item) for item in ['Miho','LightMiho']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554858708860949/HoranW_large.jpeg", color=0xffffff)
     embed.set_author(name="#367 Miho (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554858708860949/HoranW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Attaque réduite 60% 3 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 31701\n**Attaque**: 2023\n**Défense**: 3085\n**Récupération**:2329", inline=False)
     
     await message.channel.send(embed=embed)
	 
 if any([message.content.startswith (item) for item in ['Miho','DarkMiho']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554853897994253/HoranD_large.jpeg", color=0xffffff)
     embed.set_author(name="#370 Miho (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554853897994253/HoranD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Agression (PV)\n(Dmg: +20%)\n**Actif**: Agression (PV)\n(Dmg: +20%)\n**PV**: 37261\n**Attaque**: 1806\n**Défense**: 2303\n**Récupération**: 2167", inline=False)
     
     await message.channel.send(embed=embed)
   	 
###########################
######### miho S Evo ##################
###########################
	
 if any([message.content.startswith (item) for item in ['Miho','FeuMiho','SMiho','FeuSMiho']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559814811713548/SuperHoran_large.jpeg", color=0xffffff)
     embed.set_author(name="#362 Miho SE (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559814811713548/SuperHoran_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: \n**Lead**: Resist +15~20%\n**Passif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg +20%, Taux: +20%)\n**PV**: 41265\n**Attaque**: 2398\n**Défense**: 1990\n**Récupération**:1540", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Miho','EauMiho','SMiho','EauSMiho']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559818963943445/SuperHoranB_large.jpeg", color=0xffffff)
     embed.set_author(name="#364 Miho SE (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559818963943445/SuperHoranB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: \n**Lead**: Resist +15~20%\n**Passif**: Nécrose 100% 2 tours\n(Dmg +30%)\n**Actif**: Nécrose 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 34380\n**Attaque**: 2318\n**Défense**: 2289\n**Récupération**:2024", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Miho','BoisMiho','SMiho','BoisSMiho']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559824123199498/SuperHoranG_large.jpeg", color=0xffffff)
     embed.set_author(name="#366 Miho SE (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559824123199498/SuperHoranG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: \n**Lead**: Resist +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 31033\n**Attaque**: 2976\n**Défense**: 1982\n**Récupération**:2097", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Miho','LightMiho','SMiho','LightSMiho']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559829718401036/SuperHoranW_large.jpeg", color=0xffffff)
     embed.set_author(name="#368 Miho SE (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559829718401036/SuperHoranW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Resist +15~20%\n**Passif**: Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Attaque réduite 60% 3 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 34881\n**Attaque**: 2234\n**Défense**: 3425\n**Récupération**:2567", inline=False)
     
     await message.channel.send(embed=embed)
       
 if any([message.content.startswith (item) for item in ['Miho','DarkMiho','SMiho','DarkSMiho']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559821338050580/SuperHoranD_large.jpeg", color=0xffffff)
     embed.set_author(name="#371 Miho SE (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559821338050580/SuperHoranD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Agression (PV)\n(no skillbooks)\n**Actif**: Agression (PV)\n(no skillbooks)\n**PV**: 41156\n**Attaque**: 1990\n**Défense**: 2535\n**Récupération**: 2385", inline=False)
     
     await message.channel.send(embed=embed)
     
###########################
######### mildeu ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['Mild','FeuMild']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554096197107733/FungusR_large.jpeg", color=0xffffff)
     embed.set_author(name="#371 Mildeu (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554096197107733/FungusR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Nécrose 60% 1 tour\n\n**Actif**: Attaque augmentée  3 tours\n(No skillbooks)\n**PV**: 26498\n**Attaque**: 1730\n**Défense**: 1444\n**Récupération**:2485", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Mild','EauMild']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554093449838602/FungusB_large.jpeg", color=0xffffff)
     embed.set_author(name="#372 Mildeu (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554093449838602/FungusB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Rec +20~25%\n**Passif**: Brise bouclier 100%\n(No skillbooks)\n**Actif**: Défense augmentée 3 tours\n(No skillbooks)\n**PV**: 25953\n**Attaque**: 1614\n**Défense**: 2343\n**Récupération**:1771", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mild','BoisMild']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554090236870676/Fungus_large.jpeg", color=0xffffff)
     embed.set_author(name="#373 Mildeu (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554090236870676/Fungus_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Provocation 40% 1 tour\n(No skillbooks)\n**Actif**: Purification 100%\n(No skillbooks)\n**PV**: 28003\n**Attaque**: 1342\n**Défense**: 1702\n**Récupération**:2697", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mild','LightMild']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554098432540672/FungusW_large.jpeg", color=0xffffff)
     embed.set_author(name="#374 Mildeu (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554098432540672/FungusW_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Rec +20~25%\n**Passif**: Adrénaline 10% de ses PV (Allies)\n(No skillbooks)\n**Actif**: Domination 3 tours\n(No skillbooks)\n**PV**: 27975\n**Attaque**: 1491\n**Défense**: 2499\n**Récupération**:1485", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mild','DarkMild']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554093772537887/FungusD_large.jpeg", color=0xffffff)
     embed.set_author(name="#375 Mildeu (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554093772537887/FungusD_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral 30%\n(No skillbooks)\n**Actif**: Bouclier (Flat) 2 tours \n(No skillbooks)\n**PV**: 24768\n**Attaque**: 1777\n**Défense**: 1662\n**Récupération**:2574", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### mimic ##################
###########################

 if any([message.content.startswith (item) for item in ['Mimi','FeuMimi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554274010169364/GoldmickR_large.jpeg", color=0xffffff)
     embed.set_author(name="#376 Mimic (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554274010169364/GoldmickR_large.jpeg")
     embed.add_field(name="★", value="**Type**: Attaquant\n**Lead**: TC +10~15%(Donjons)\n**Passif**: Provocation 20% 1 tour\n(No skillbooks)\n**Actif**: Provocation 60% 1 tour\n(No skillbooks)\n**PV**: 26246\n**Attaque**: 2206\n**Défense**: 1607\n**Récupération**:1559", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mimi','EauMimi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554270839537664/GoldmickB_large.jpeg", color=0xffffff)
     embed.set_author(name="#377 Mimic (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554270839537664/GoldmickB_large.jpeg")
     embed.add_field(name="★", value="**Type**: Tank\n**Lead**: TC +10~15%(Donjons)\n**Passif**: Nécrose 40% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 60% 2 tours\n(No skillbooks)\n**PV**: 38555\n**Attaque**: 1193\n**Défense**: 1792\n**Récupération**:1343", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mimi','BoisMimi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554264698945567/Goldmick_large.jpeg", color=0xffffff)
     embed.set_author(name="#378 Mimic (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554264698945567/Goldmick_large.jpeg")
     embed.add_field(name="★", value="**Type**: Défenseur\n**Lead**: TC +10~15%(Donjons)\n**Passif**: Attaque réduite 40% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**PV**: 28881\n**Attaque**: 1668\n**Défense**: 2404\n**Récupération**:1273", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mimi','LightMimi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554275079847937/GoldmickW_large.jpeg", color=0xffffff)
     embed.set_author(name="#379 Mimic (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554275079847937/GoldmickW_large.jpeg")
     embed.add_field(name="★", value="**Type**: Récupération\n**Lead**: TC +10~15%(Donjons)\n**Passif**: Récupération réduite 40% 1 tour\n(No skillbooks)\n**Actif**: Récupération réduite 60% 2 tours\n(No skillbooks)\n**PV**: 27955\n**Attaque**: 1403\n**Défense**: 1662\n**Récupération**:2343", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mimi','DarkMimi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554271824936962/GoldmickD_large.jpeg", color=0xffffff)
     embed.set_author(name="#380 Mimic (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554271824936962/GoldmickD_large.jpeg")
     embed.add_field(name="★", value="**Type**: Équilibré\n**Lead**: TC +10~15%(Donjons)\n**Passif**: Fatigue 40% 1 tour\n(No skillbooks)\n**Actif**: Fatigue 60% 2 tours\n(No skillbooks)\n**PV**: 27816\n**Attaque**: 1831\n**Défense**: 1664\n**Récupération**:1534", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### chapillon ##################
###########################

 if any([message.content.startswith (item) for item in ['Chapi','FeuChapi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556529417715737/ChapillonR_large.jpeg", color=0xffffff)
     embed.set_author(name="#381 Chapillon (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556529417715737/ChapillonR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Rec +30~35% (ToC)\n**Passif**: Nécrose x2 60% 1 tour\n(Dmg: +10% Taux: +20%)\n**Actif**: Purification 100%\n(Dmg: +30%)\n**PV**: 35279\n**Attaque**: 1744\n**Défense**: 1452\n**Récupération**: 1642", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chapi','EauChapi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556527693725707/ChapillonB_large.jpeg", color=0xffffff)
     embed.set_author(name="#382 Chapillon (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556527693725707/ChapillonB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35% (ToC)\n**Passif**: Boost de moral 30% de ses PA\n(???)\n**Actif**: Bouclier (Flat) 2 tours\n(Dmg: +20% tour: +1)\n**PV**: 28561\n**Attaque**: 1648\n**Défense**: 1525\n**Récupération**: 2595", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Chapi','BoisChap','TopChapi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556526770847754/Chapillon_large.jpeg", color=0xffffff)
     embed.set_author(name="#383 Chapillon (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556526770847754/Chapillon_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35% (ToC)\n**Passif**: Faiblesse exposée 80% 1 tour\n(???)\n**Actif**: Attaque augmentée  2 tours\n(???)\n**PV**: 23563\n**Attaque**: 1818\n**Défense**: 1668\n**Récupération**: 2663", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### mini camilla ##################
###########################

 if any([message.content.startswith (item) for item in ['MiniC','LightMiniC','Minicam','LightMinicam','Camilla','LightCami']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728588644974592/MiniCamilla3Evo_large.jpg", color=0xffffff)
     embed.set_author(name="#389 Mini Camilla (light)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728588644974592/MiniCamilla3Evo_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Choc 80% 1 tour\n(no skillbooks)\n**Actif**: Faiblesse exposée 80% 1 tours\n(no skillbooks)\n**PV**: 40046\n**Attaque**: 2105\n**Défense**: 2242\n**Récupération**: 2037", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['MiniC','DarkMiniC','Minicam','DarkMinicam','Camilla','DarkCami']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728590691794954/MiniCamilla3EvoD_large.jpg", color=0xffffff)
     embed.set_author(name="#390 Mini Camilla (dark)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728590691794954/MiniCamilla3EvoD_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Siphon de PA 25%\n(no skillbooks)\n**Actif**: Agression (PV)\n(no skillbooks)\n**PV**: 41272\n**Attaque**: 2119\n**Défense**: 2167\n**Récupération**: 1983", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### mini seira ##################
###########################

 if any([message.content.startswith (item) for item in ['MiniS','LightMiniS','Minis','LightMinis','Seira','LightSeira']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557103714402306/NavigatorSeira_large.jpeg", color=0xffffff)
     embed.set_author(name="#394 Mini Seira light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557103714402306/NavigatorSeira_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Vague martiale 20%\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Avantage élémentaire\n(Dmg +25%)\n**PV**: 24216\n**Attaque**: 3425\n**Défense**: 2390\n**Récupération**:2479", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['MiniS','DarkMiniS','Minis','DarkMinis','Seira','DarkSeira']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557106322997249/NavigatorSeiraD_large.jpeg", color=0xffffff)
     embed.set_author(name="#395 Mini Seira (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557106322997249/NavigatorSeiraD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Vague martiale 20%\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Avantage élémentaire\n(Dmg +25%)\n**PV**: 24216\n**Attaque**: 3425\n**Défense**: 2390\n**Récupération**:2479", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### mini tina ##################
###########################
	 
 if any([message.content.startswith (item) for item in ['MiniT','LightMiniT','Minit','LightMinit','Tina','LightTina']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557596216792317967/GemsmithTina_large.jpeg", color=0xffffff)
     embed.set_author(name="#399 Mini Tina (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557596216792317967/GemsmithTina_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Boost de moral (Allies) 10% SP\n(Dmg +30%)\n**Actif**: Avantage élémentaire\n(Dmg +30%)\n**PV**: 21492\n**Attaque**: 3357\n**Défense**: 2384\n**Récupération**:2853", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['MiniT','DarkMiniT','Minit','DarkMinit','Tina','DarkTina']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554235573698591/GemsmithTinaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#400 Mini Tina (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554235573698591/GemsmithTinaD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Chasseur 40%\n(Dmg +35%)\n**PV**: 24816\n**Attaque**: 3378\n**Défense**: 2479\n**Récupération**:2384", inline=False)
     
     await message.channel.send(embed=embed)
	 	 
	 #######################################
	 ############ Mini Zephyros ############
	 #######################################

 if any([message.content.startswith (item) for item in ['Mini Zephyros','DarkMiniZephy','DarkZephyr','Zephyr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569194846879904/Screenshot_20200907-183823_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#1002 Mini Zephyros (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569194846879904/Screenshot_20200907-183823_Monster_Super_League.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Taux critique 15-20%\n**Passif**: Vague martiale 20% PA/PV\n(Dmg +20%, taux +5%)\n**Actif**: Persévérance\n(Dmg +25%)\n**PV**: 26811\n**Attaque**: 3473\n**Défense**: 2377\n**Récupération**:1941", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mini Zephyros','LightMiniZephy','LightZephyr','Zephyr']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569194465460254/Screenshot_20200907-183711_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#1003 Mini Zephyros (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569194465460254/Screenshot_20200907-183711_Monster_Super_League.jpg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Taux critique 15-20%\n**Passif**: Résistance réduite 100% 2 tours\n(Dmg +30%)\n**Actif**: Choc 60% 2 tours\n(Dmg +20%, Taux +10%)\n**PV**: 40639\n**Attaque**: 1928\n**Défense**: 2432\n**Récupération**:2044", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### mino ############
###########################

 if any([message.content.startswith (item) for item in ['Mino','FeuMino']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560144970416130/TaurusR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#401 Mino (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560144970416130/TaurusR_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(No skillbooks)\n**Actif**: Chasseur (bois) 100%\n(No skillbooks)\n**PV**: 24713\n**Attaque**: 2452\n**Défense**: 1682\n**Récupération**:1525", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mino','EauMino']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560130055602189/Taurus_Large.jpeg", color=0xffffff)
     embed.set_author(name="#402 Mino (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560130055602189/Taurus_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(No skillbooks)\n**Actif**: Feu Chasseur 100%\n(No skillbooks)\n**PV**: 25885\n**Attaque**: 2370\n**Défense**: 1498\n**Récupération**:1641", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mino','BoisMino']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560142860681264/TaurusG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#403 Mino (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560142860681264/TaurusG_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(No skillbooks)\n**Actif**: Chasseur (eau) 100%\n(No skillbooks)\n**PV**: 26246\n**Attaque**: 2172\n**Défense**: 1696\n**Récupération**:1525", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mino','LightMino']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560164453089280/TaurusW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#404 Mino (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560164453089280/TaurusW_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(No skillbooks)\n**Actif**: Chasseur (dark) 100%\n(No skillbooks)\n**PV**: 22384\n**Attaque**: 2642\n**Défense**: 1539\n**Récupération**:1702", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mino','DarkMino']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560140684099587/TaurusD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#405 Mino (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560140684099587/TaurusD_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(No skillbooks)\n**Actif**: Chasseur (light) 100%\n(No skillbooks)\n**PV**: 29188\n**Attaque**: 2336\n**Défense**: 1308\n**Récupération**:1498", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### misha ############
###########################
	 
 if any([message.content.startswith (item) for item in ['Mish','FeuMish']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558515118538756/Runeclaw_large.jpeg", color=0xffffff)
     embed.set_author(name="#406 Misha (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558515118538756/Runeclaw_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: PV +30~35% (Même élément)\n**Passif**: Adrénaline 30% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Prédateur 30%\n(Dmg +30%)\n**PV**: 35395\n**Attaque**: 1922\n**Défense**: 1622\n**Récupération**:1486", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mish','EauMish']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558529266057278/RuneclawB_large.jpeg", color=0xffffff)
     embed.set_author(name="#407 Misha (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558529266057278/RuneclawB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%(Même élément)\n**Passif**: Nécrose x2 50% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Frappe impitoyable\n(Dmg +30%)\n**PV**: 29293\n**Attaque**: 2083\n**Défense**: 2011\n**Récupération**:1732", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mish','BoisMish']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558532088561695/RuneclawG_large.jpeg", color=0xffffff)
     embed.set_author(name="#408 Misha (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558532088561695/RuneclawG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35% (Même élément)\n**Passif**: Provocation 80% 1 tour\n(Dmg +30%)\n**Actif**: Aveuglement 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 25476\n**Attaque**: 1866\n**Défense**: 2969\n**Récupération**:1512", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mish','LightMish']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558534160678935/RuneclawW_large.jpeg", color=0xffffff)
     embed.set_author(name="#409 Misha (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558534160678935/RuneclawW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35% (Même élément)\n**Passif**: Vague martiale 20% (On crit)\n(Dmg +30%)\n**Actif**: Choc 70%(On crit) 1 tour\n(Dmg +10%, Taux: +20%)\n**PV**: 40312\n**Attaque**: 2221\n**Défense**: 2364\n**Récupération**:1874", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mish','DarkMish']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558521913311242/RuneclawD_large.jpeg", color=0xffffff)
     embed.set_author(name="#410 Misha (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558521913311242/RuneclawD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%(Même élément)\n**Passif**: Vengeance\n(Dmg +35%)\n**Actif**: Vengeance\n(Dmg +35%)\n**PV**: 26287\n**Attaque**: 2663\n**Défense**: 3105\n**Récupération**:2009", inline=False)
     
     await message.channel.send(embed=embed)
	 
###########################
######### taupinou ############
###########################if any([message.content.startswith (item) for item in ['Taup','FeuTaup']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553566196203520/DrillmonR_large.jpeg", color=0xffffff)
     embed.set_author(name="#411 Taupinou (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553566196203520/DrillmonR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV Rec +10~15%\n**Passif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Nécrose 60% 1 tour\n(No skillbooks)\n**PV**: 28731\n**Attaque**: 1709\n**Défense**: 2486\n**Récupération**:1192", inline=False)
     
     await message.channel.send(embed=embed)
###########################     
	 
 if any([message.content.startswith (item) for item in ['Taup','EauTaup']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553564493578270/DrillmonB_large.jpeg", color=0xffffff)
     embed.set_author(name="#412 Taupinou (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553564493578270/DrillmonB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: PV Rec +10~15%\n**Passif**: Étourdissement 40% 1 tour\n(No skillbooks)\n**Actif**: Provocation 80% 1 tour\n(No skillbooks)\n**PV**: 36069\n**Attaque**: 1622\n**Défense**: 1329\n**Récupération**:1506", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Taup','BoisTaup']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553561985122337/Drillmon_large.jpeg", color=0xffffff)
     embed.set_author(name="#413 Taupinou (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553561985122337/Drillmon_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: PV Rec +10~15%\n**Passif**: Nécrose x2 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 80% 2 tours\n(No skillbooks)\n**PV**: 28857\n**Attaque**: 1831\n**Défense**: 1637\n**Récupération**:1596", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Taup','FeuTaup']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553566196203520/DrillmonR_large.jpeg", color=0xffffff)
     embed.set_author(name="#411 Taupinou (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553566196203520/DrillmonR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV Rec +10~15%\n**Passif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Nécrose 60% 1 tour\n(No skillbooks)\n**PV**: 28731\n**Attaque**: 1709\n**Défense**: 2486\n**Récupération**:1192", inline=False)
     
     await message.channel.send(embed=embed)
     
###########################
######### mona ############
###########################
 if any([message.content.startswith (item) for item in ['Mona','FeuMona','mona','MonaFeu', 'MonaF']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556697726746634/MonArchh_large.jpeg", color=0xffffff)
     embed.set_author(name="#416 Mona (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556697726746634/MonArchh_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank \n**Lead**: Att +30~35% (Même élément)\n**Passif**: Siphon de PA 20%\n(dmg +20%, Taux : +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 42627\n**Attaque**: 1431\n**Défense**: 1785\n**Récupération**:1411", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mona', 'mona', 'MonaEau','EauMona', 'MonaE', 'TopMona']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556704307347466/MonArchhB_large.jpeg", color=0xffffff)
     embed.set_author(name="#417 Mona (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556704307347466/MonArchhB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35(Même élément)\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Défense réduite 50% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 25081\n**Attaque**: 2853\n**Défense**: 2016\n**Récupération**:1641", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mona', 'mona', 'MonaBois','BoisMona', 'MonaB']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557214074111262720/MonArchhG_large.jpeg", color=0xffffff)
     embed.set_author(name="#418 Mona (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557214074111262720/MonArchhG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Provocation intrépide 80% 1 tour\n(???)\n**PV**: 27860\n**Attaque**: 1491\n**Défense**: 2554\n**Récupération**:1839", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mona', 'mona', 'MonaLight','LightMona', 'MonaL']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556709810274319/MonArchhW_large.jpeg", color=0xffffff)
     embed.set_author(name="#419 Mona (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556709810274319/MonArchhW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Adrénaline 25% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Agression (Def)\n(Dmg +40%)\n**PV**: 30686\n**Attaque**: 2486\n**Défense**: 3255\n**Récupération**:1771", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mona','mona', 'MonaDark', 'MonaD','DarkMona']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556707352412185/MonArchhD_large.jpeg", color=0xffffff)
     embed.set_author(name="#420 Mona (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556707352412185/MonArchhD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg +25%)\n**Actif**: Chasseur(Dc) 30%\n(Dmg +25%, +Effect.: +10%)\n**PV**: 28030\n**Attaque**: 3391\n**Défense**: 2070\n**Récupération**:2077", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ########### Mona S Evo ############
	 ###################################
	 
	 
 if any([message.content.startswith (item) for item in ['Mona','mona','FeuMona','MonaF','MonaFeu','SMonaF','SMona','FeuSMona','SMonaFeu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569222143410236/Screenshot_20200907-183956_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#362 Mona SE (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569222143410236/Screenshot_20200907-183956_Monster_Super_League.jpg")
     embed.add_field(name="★★★", value="**Type**: Tank \n**Lead**: Att +30~35% (Même élément)\n**Passif**: Siphon de PA 20%\n(dmg +20%, Taux : +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 47053\n**Attaque**: 1474\n**Défense**: 1969\n**Récupération**:1554", inline=False)
     
     await message.channel.send(embed=embed)     

 if any([message.content.startswith (item) for item in ['Mona','mona','MonaEau','MonaE','EauMona','SMonaE','Smona','SmonaEau','EauSMona']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569221883363409/Screenshot_20200907-183923_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#364 Mona SE (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569221883363409/Screenshot_20200907-183923_Monster_Super_League.jpg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35(Même élément)\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Défense réduite 50% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 27594\n**Attaque**: 3173\n**Défense**: 2227\n**Récupération**:1811", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mona','mona','MonaBois','MonaB','BoisMona','SMonaB','Smona','SmonaBois','BoisSMona']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569222294536274/Screenshot_20200907-184021_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#366 Mona SE (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569222294536274/Screenshot_20200907-184021_Monster_Super_League.jpg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Provocation intrépide 80% 1 tour\n(???)\n**PV**: 30652\n**Attaque**: 1648\n**Défense**: 2840\n**Récupération**:2029", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Mona','mona','MonaLight','MonaL','LightMona','SMonaL','Smona','SmonaLight','LightSMona']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569222491799573/Screenshot_20200907-184043_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#368 Mona SE (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569222491799573/Screenshot_20200907-184043_Monster_Super_League.jpg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Adrénaline 25% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Agression (Def)\n(Dmg +40%)\n**PV**: 33764\n**Attaque**: 2744\n**Défense**: 3609\n**Récupération**:1954", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mona','mona','MonaDark','MonaD','DarkMona','SMonaD','Smona','SmonaDark','DarkSMona']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569222772555816/Screenshot_20200907-184103_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#371 Mona SE (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569222772555816/Screenshot_20200907-184103_Monster_Super_League.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg +25%)\n**Actif**: Chasseur(Dc) 30%\n(Dmg +25%, +Effect.: +10%)\n**PV**: 30842\n**Attaque**: 3759\n**Défense**: 2281\n**Récupération**:2295", inline=False)
     
     await message.channel.send(embed=embed)     

	 ###################################
	 ############ Monkiki ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Monk','FeuMonk']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552082805358612/Bluemong_large.jpeg", color=0xffffff)
     embed.set_author(name="#421 Monkiki (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552082805358612/Bluemong_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +25~30%\n**Passif**: Sommeil (On crit) 1 tour\n(Dmg +25%)\n**Actif**: Sommeil (On crit) 2 tours\n(Dmg +25%)\n**PV**: 27676\n**Attaque**: 2867\n**Défense**: 1914\n**Récupération**:1382", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Monk','EauMonk','TopMonkiki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552085267283968/BluemongB_large.jpeg", color=0xffffff)
     embed.set_author(name="#422 Monkiki (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552085267283968/BluemongB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +25~30%\n**Passif**: Défense réduite 80% 2 tours\n(Dmg +25%)\n**Actif**: Soif 80% -10% 1 tour\n(Dmg +15%, tour: +1)\n**PV**: 28697\n**Attaque**: 1852\n**Défense**: 2588\n**Récupération**:1328", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Monk','BoisMonk']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552097451737091/BluemongG_large.jpeg", color=0xffffff)
     embed.set_author(name="#423 Monkiki (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552097451737091/BluemongG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Att +25~30%\n**Passif**: Récupération réduite 60% 1 tour\n(Dmg +10%, Taux: +20%, tour: +1)\n**Actif**: Étourdissement 100% 1 tour\n(Dmg +25%)\n**PV**: 28476\n**Attaque**: 1892\n**Défense**: 1963\n**Récupération**:1725", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Monk','LightMonk']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552099897147403/BluemongW_large.jpeg", color=0xffffff)
     embed.set_author(name="#424 Monkiki (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552099897147403/BluemongW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +25~30%\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Aveuglement (On crit) 3 tours\n(Dmg +25%)\n**PV**: 26917\n**Attaque**: 2662\n**Défense**: 2658\n**Récupération**:2488", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Monk','DarkMonk']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552088807276544/BluemongD_large.jpeg", color=0xffffff)
     embed.set_author(name="#425 Monkiki (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552088807276544/BluemongD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +25~30%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Défense 100% 2 tours\n(Dmg +15%, tour: +1)\n**PV**: 28731\n**Attaque**: 1941\n**Défense**: 3167\n**Récupération**:2309", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ Mowgli ###############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Mowg','FeuMowg','TopMowg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556868510285825/MowgliaR_large.jpeg", color=0xffffff)
     embed.set_author(name="#426 Mowgli (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556868510285825/MowgliaR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Chasseur (bois) 50%\n(Dmg +25%)\n**Actif**: Prédateur (bois) 40%\n(Dmg +25%)\n**PV**: 26900\n**Attaque**: 2717\n**Défense**: 1525\n**Récupération**:1580", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mowg','EauMowg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557085313859602/MowgliaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#427 Mowgli (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557085313859602/MowgliaB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Feu Chasseur 50%\n(Dmg +25%)\n**Actif**: Prédateur (feu) 40%\n(Dmg +25%)\n**PV**: 28670\n**Attaque**: 2615\n**Défense**: 1648\n**Récupération**:1566", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mowg','BoisMowg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556869877760002/Mowglia_large.jpeg", color=0xffffff)
     embed.set_author(name="#428 Mowgli (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556869877760002/Mowglia_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Chasseur (eau) 50%\n(Dmg +25%)\n**Actif**: Prédateur (eau) 40%\n(Dmg +25%)\n**PV**: 26900\n**Attaque**: 2847\n**Défense**: 1532\n**Récupération**:1580", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mowg','LightMowg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556869768445972/MowgliaW_large.jpeg", color=0xffffff)
     embed.set_author(name="#429 Mowgli (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556869768445972/MowgliaW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Chasseur (dark) 40%\n(Dmg +25%)\n**Actif**: Prédateur (dark) 30%\n(Dmg +25%)\n**PV**: 28016\n**Attaque**: 3133\n**Défense**: 2036\n**Récupération**:1989", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Mowg','DarkMowg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556868711743510/MowgliaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#430 Mowgli (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556868711743510/MowgliaD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Chasseur (light) 40%\n(Dmg +25%)\n**Actif**: Prédateur (light) 30%\n(Dmg +25%)\n**PV**: 27288\n**Attaque**: 3085\n**Défense**: 2193\n**Récupération**:1968", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ champi ###############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Champ','FeuChamp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559527850147843/SporeR_large.jpeg", color=0xffffff)
     embed.set_author(name="#431 Champi (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559527850147843/SporeR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Nécrose x2 60% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Provocation 100% 1 tour\n(Dmg +20%, tour: +1)\n**PV**: 29092\n**Attaque**: 1321\n**Défense**: 2540\n**Récupération**:1641", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Champ','EauChamp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559525757190164/SporeB_large.jpeg", color=0xffffff)
     embed.set_author(name="#432 Champi (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559525757190164/SporeB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: PV +20~25%\n**Passif**: Provocation 40% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Prédateur (eau) 20%\n(Dmg +20%)\n**PV**: 28054\n**Attaque**: 1879\n**Défense**: 1725\n**Récupération**:1555", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Champ','BoisChamp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559523706044417/Spore_large.jpeg", color=0xffffff)
     embed.set_author(name="#433 Champi (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559523706044417/Spore_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: PV +20~25%\n**Passif**: Boost de moral (On crit) 100% de ses PA\n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 23862\n**Attaque**: 2785\n**Défense**: 1702\n**Récupération**:1662", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############# Nezha ###############
	 ################################### 


 if any([message.content.startswith (item) for item in ['Nez','FeuNez','TopNez']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556889733464064/Nalakuvara_large.jpeg", color=0xffffff)
     embed.set_author(name="#436 Nezha (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556889733464064/Nalakuvara_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Défense réduite 70% 3 tours\n(No skillbooks)\n**PV**: 38643\n**Attaque**: 2323\n**Défense**: 1806\n**Récupération**:1922", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Nez','EauNez','TopNez']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557093924765706/NalakuvaraB_large.jpeg", color=0xffffff)
     embed.set_author(name="#437 Nezha (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557093924765706/NalakuvaraB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Aveuglement 70% 2 tours\n(No skillbooks)\n**PV**: 30199\n**Attaque**: 2444\n**Défense**: 2542\n**Récupération**:2774", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Nez','BoisNez']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557099780145163/NalakuvaraG_large.jpeg", color=0xffffff)
     embed.set_author(name="#438 Nezha (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557099780145163/NalakuvaraG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Siphon de PV \n(No skillbooks)\n**Actif**: Sceau 60% 1 tour\n(No skillbooks)\n**PV**: 27696\n**Attaque**: 3092\n**Défense**: 2329\n**Récupération**:2023", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Nez','LightNez']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557214207414894632/Nalakuvaraw_large.jpeg", color=0xffffff)
     embed.set_author(name="#439 Nezha (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557214207414894632/Nalakuvaraw_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Aveuglement 80% 3 tours\n(No skillbooks)\n**Actif**: Affaiblissement 80% 2 tours\n(No skillbooks)\n**PV**: 38752\n**Attaque**: 1853\n**Défense**: 2323\n**Récupération**:2133", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Nez','DarkNez']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552557097187803167/NalakuvaraD_large.jpeg", color=0xffffff)
     embed.set_author(name="#440 Nezha (dark)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552557097187803167/NalakuvaraD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Siphon de PV , Greatly)\n(No skillbooks)\n**Actif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**PV**: 25640\n**Attaque**: 3153\n**Défense**: 2431\n**Récupération**:2111", inline=False)
     
     await message.channel.send(embed=embed)
     
	 ###################################
	 ############## Nifa ###############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Nif','LightNif']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551351289118721/Angelmon_Large.jpeg", color=0xffffff)
     embed.set_author(name="#444 Nifa (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551351289118721/Angelmon_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Chasseur 50%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 25292\n**Attaque**: 3024\n**Défense**: 2288\n**Récupération**:2084", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Nif','DarkNif']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551357824106537/AngelmonD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#445 Nifa (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551357824106537/AngelmonD_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**PV**: 47027\n**Attaque**: 1853\n**Défense**: 1915\n**Récupération**:1751", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ Cauchemar ############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Cauc','FeuCauc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557419897683968/NyxR_large.jpeg", color=0xffffff)
     embed.set_author(name="#446 Cauchemar (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557419897683968/NyxR_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Soif 80% -30% 2 tours\n(No skillbooks)\n**PV**: 32000\n**Attaque**: 3616\n**Défense**: 2172\n**Récupération**:2424", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Cauc','EauCauc','TopCauc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557413228609557/NyxB_large.jpeg", color=0xffffff)
     embed.set_author(name="#447 Cauchemar (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557413228609557/NyxB_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Sceau 100% 3 tours\n(No skillbooks)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**PV**: 27247\n**Attaque**: 2601\n**Défense**: 3514\n**Récupération**:2343", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Cauc','BoisCauc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557418219962388/NyxG_large.jpeg", color=0xffffff)
     embed.set_author(name="#448 Cauchemar (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557418219962388/NyxG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Boost de moral 30% de ses PA\n(No skillbooks)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**PV**: 26906\n**Attaque**: 2595\n**Défense**: 3602\n**Récupération**:2349", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Cauc','LightCauc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557421390856192/NyxW_large.jpeg", color=0xffffff)
     embed.set_author(name="#449 Cauchemar (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557421390856192/NyxW_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Agression (Def)\n(Dmg +25%)\n**Actif**: Provocation intrépide 80% 2 tours\n(Dmg + 20%, Taux: +20%)\n**PV**: 32456\n**Attaque**: 2561\n**Défense**: 3875\n**Récupération**:2254", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Cauc','DarkCauc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557389174538252/Nyx_large.jpeg", color=0xffffff)
     embed.set_author(name="#450 Cauchemar (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557389174538252/Nyx_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Resist +20~25%\n**Passif**: Boost de moral 40% de ses PA\n(No skillbooks)\n**Actif**: Sceau 80% 3 tours\n(No skillbooks)\n**PV**: 41143\n**Attaque**: 2316\n**Défense**: 2534\n**Récupération**:2916", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############## Odin ###############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Odin','FeuOdin','TopOdin']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558094786363394/PrimeodinR_large.jpeg", color=0xffffff)
     embed.set_author(name="#451 Odin (Feu)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558094786363394/PrimeodinR_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%\n**Passif**: Défense réduite 80% 2 tours\n(Dmg +15%, Taux: +20%)\n**Actif**: Attaque réduite 80% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 43077\n**Attaque**: 2010\n**Défense**: 3066\n**Récupération**:2432", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Odin','EauOdin','TopOdin']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558094077526026/PrimeodinB_large.jpeg", color=0xffffff)
     embed.set_author(name="#452 Odin (Eau)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558094077526026/PrimeodinB_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: PV +40~45%\n**Passif**: Étourdissement 100% 1 tour\n(Dmg +15%, tour: +1)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +15%, Taux: +30%)\n**PV**: 25378\n**Attaque**: 3172\n**Défense**: 3155\n**Récupération**:3012", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Odin','BoisOdin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558094253555745/PrimeodinG_large.jpeg", color=0xffffff)
     embed.set_author(name="#453 Odin (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558094253555745/PrimeodinG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%\n**Passif**: Siphon de PV ,  Greatly))\n(Dmg +25%)\n**Actif**: Défense réduite 80% 2 tours\n(Dmg +25%)\n**PV**: 28473\n**Attaque**: 3909\n**Défense**: 2595\n**Récupération**:2152", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Odin','LightOdin']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558098632540170/PrimeodinW_large.jpeg", color=0xffffff)
     embed.set_author(name="#454 Odin (light)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558098632540170/PrimeodinW_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%\n**Passif**: Agression (PV)\n(Dmg +25%)\n**Actif**: Adrénaline (Allies) 10% de ses PV par mob attaqué\n(Dmg +25%)\n**PV**: 48048\n**Attaque**: 2099\n**Défense**: 2916\n**Récupération**:2677", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Odin','DarkOdin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558087924351006/Primeodin_large.jpeg", color=0xffffff)
     embed.set_author(name="#455 Odin (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558087924351006/Primeodin_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: PV +40~45%\n**Passif**: Vague martiale 20%\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Défense réduite 80% 3 tours\n(Dmg +25%)\n**PV**: 32024\n**Attaque**: 2975\n**Défense**: 2828\n**Récupération**:1889", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ Onmyoji ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Onm','FeuOnm','TopOnm']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558730898571288/SeimeiR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#456 Onmyoji (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558730898571288/SeimeiR_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Resist +20~25%\n**Passif**: Siphon de PA 30%\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense réduite 80% 2 tours\n(Dmg +25%)\n**PV**: 37772\n**Attaque**: 2521\n**Défense**: 2705\n**Récupération**:2494", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Onm','EauOnm','TopOnm']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558724070244352/Seimei_Large.jpeg", color=0xffffff)
     embed.set_author(name="#457 Onmyoji (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558724070244352/Seimei_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Chasseur 50%\n(Dmg +30%)\n**Actif**: Chasseur 50%\n(Dmg +30%)\n**PV**: 31626\n**Attaque**: 3677\n**Défense**: 2070\n**Récupération**:2091", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Onm','BoisOnm']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558729330032651/SeimeiG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#458 Onmyoji (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558729330032651/SeimeiG_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Sceau 100% 2 tours\n(Dmg +30%)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +20%)\n**PV**: 29569\n**Attaque**: 2363\n**Défense**: 3562\n**Récupération**:2588", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Onm','LightOnm']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558753854259201/SeimeiW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#459 Onmyoji (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558753854259201/SeimeiW_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Siphon de PA 30%%\n(Dmg +20%, Taux: +10%)\n**Actif**: Choc 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 25068\n**Attaque**: 2792\n**Défense**: 3609\n**Récupération**:2254", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Onm','DarkOnm']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558727438401537/SeimeiD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#460 Onmyoji (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558727438401537/SeimeiD_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Siphon de PV \n(Dmg +30%)\n**Actif**: Siphon de PV (Allies) Greatly\n(Dmg +30%)\n**PV**: 25878\n**Attaque**: 3698\n**Défense**: 2479\n**Récupération**:2452", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############## Otari ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Ota','FeuOta']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558815204212758/SelkieR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#461 Otari (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558815204212758/SelkieR_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Aveuglement 60% 2 tours\n(No skillbooks)\n**PV**: 35048\n**Attaque**: 1635\n**Défense**: 1302\n**Récupération**:1486", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ota','EauOta']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558803640385584/Selkie_Large.jpeg", color=0xffffff)
     embed.set_author(name="#462 Otari (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558803640385584/Selkie_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Resistance réduite  100% 2 tours\n(Dmg: +30%)\n**Actif**: Attaque réduite 80% 2 tours\n(Dmg: +20%, +1 tour)\n**PV**: 28687\n**Attaque**: 1742\n**Défense**: 1854\n**Récupération**:1807", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ota','BoisOta']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558813245472771/SelkieG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#463 Otari (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558813245472771/SelkieG_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Étourdissement 60% 1 tour\n(No skillbooks)\n**Actif**: Étourdissement 80% 1 tour\n(No skillbooks)\n**PV**: 28820\n**Attaque**: 1478\n**Défense**: 2336\n**Récupération**:1614", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ota','LightOta']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557607503815376906/SelkieW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#464 Otari (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557607503815376906/SelkieW_Large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Boost de moral 30% de ses PA\n(No skillbooks)\n**Actif**: Prédateur 30%\n(No skillbooks)\n**PV**: 25667\n**Attaque**: 2574\n**Défense**: 1709\n**Récupération**:1614", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ota','DarkOta']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558799148285964/SelkieD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#465 Otari (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558799148285964/SelkieD_Large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Aveuglement 100% 2 tours\n(No skillbooks)\n**PV**: 28473\n**Attaque**: 1873\n**Défense**: 2724\n**Récupération**:1362", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############## Cayou ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Cayou','FeuCayou']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556020711292943/Magton_large.jpeg", color=0xffffff)
     embed.set_author(name="#466 Cayou (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556020711292943/Magton_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%\n**Passif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**Actif**: Provocation 80% 1 tour\n(No skillbooks)\n**PV**: 29773\n**Attaque**: 2240\n**Défense**: 3058\n**Récupération**:1852", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############# Pégase ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Pega','FeuPega']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551852319703080/BellerophonR_large.jpeg", color=0xffffff)
     embed.set_author(name="#471 Pégase (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551852319703080/BellerophonR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%\n**Passif**: Siphon de PV \n(No skillbooks)\n**Actif**: Chasseur 40%\n(No skillbooks)\n**PV**: 25619\n**Attaque**: 3208\n**Défense**: 2309\n**Récupération**:1893", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pega','EauPega']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551844161912867/BellerophonB_large.jpeg", color=0xffffff)
     embed.set_author(name="#472 Pégase (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551844161912867/BellerophonB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: SP Rec +20~25%\n**Passif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Silence 80% 2 tours\n(No skillbooks)\n**PV**: 27666\n**Attaque**: 2328\n**Défense**: 2610\n**Récupération**:2263", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pega','BoisPega']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551849719496724/BellerophonG_large.jpeg", color=0xffffff)
     embed.set_author(name="#473 Pégase (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551849719496724/BellerophonG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%\n**Passif**: Attaque réduite 80% 2 tour\n(No skillbooks)\n**Actif**: Soif 60% -30% 2 tours\n(No skillbooks)\n**PV**: 30522\n**Attaque**: 2261\n**Défense**: 3099\n**Récupération**:2016", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pega','LightPega']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551841762770945/Bellerophon_large.jpeg", color=0xffffff)
     embed.set_author(name="#474 Pégase (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551841762770945/Bellerophon_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%\n**Passif**: Choc 80% 1 tour\n(No skillbooks)\n**Actif**: Adrénaline 10% de ses PV (Allies)\n(No skillbooks)\n**PV**: 30849\n**Attaque**: 2036\n**Défense**: 3221\n**Récupération**:2152", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pega','DarkPega']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551846833684480/BellerophonD_large.jpeg", color=0xffffff)
     embed.set_author(name="#475 Pégase (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551846833684480/BellerophonD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%\n**Passif**: Boost de moral 30%\n(No skillbooks)\n**Actif**: Chasseur 30%\n(No skillbooks)\n**PV**: 27560\n**Attaque**: 3242\n**Défense**: 2193\n**Récupération**:2084", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############# Penpen ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Pen','FeuPen']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557687053877255/PenkingR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#476 Penpen (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557687053877255/PenkingR_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Def +20~25%\n**Passif**: Boost de moral (On crit) 100% de ses PA\n(No skillbooks)\n**Actif**: Attaque réduite (On crit) 2 tours\n(No skillbooks)\n**PV**: 31033\n**Attaque**: 1199\n**Défense**: 2581\n**Récupération**:1491", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pen','EauPen']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557680087138304/Penking_Large.jpeg", color=0xffffff)
     embed.set_author(name="#477 Penpen (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557680087138304/Penking_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Def +20~25%\n**Passif**: Attaque réduite 80% 1 tours\n(No skillbooks)\n**Actif**: Aveuglement 60% 2 tours\n(No skillbooks)\n**PV**: 27969\n**Attaque**: 1342\n**Défense**: 2506\n**Récupération**:1580", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pen','BoisPen']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557684235436054/PenkingG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#478 Penpen (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557684235436054/PenkingG_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Def +20~25%\n**Passif**: Fatigue 60% 2 tours\n(No skillbooks)\n**Actif**: Récupération réduite 80% 1 tour\n(No skillbooks)\n**PV**: 39951\n**Attaque**: 1506\n**Défense**: 1145\n**Récupération**:1295", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pen','LightPen']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557690346274828/PenkingW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#479 Penpen (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557690346274828/PenkingW_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Def +20~25%\n**Passif**: Provocation 80% 2 tours\n(No skillbooks)\n**Actif**: Adrénaline 30% de ses PV\n(No skillbooks)\n**PV**: 28806\n**Attaque**: 1866\n**Défense**: 2418\n**Récupération**:1410", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pen','DarkPen']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557682301730836/PenkingD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#480 Penpen (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557682301730836/PenkingD_Large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Boost de moral (On crit) 40% de ses PA\n(No skillbooks)\n**Actif**: Vengeance\n(No skillbooks)\n**PV**: 26041\n**Attaque**: 2588\n**Défense**: 1696\n**Récupération**:1539", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ Persephone ###########
	 ################################### 

 if any([message.content.startswith (item) for item in ['Pers','FeuPers']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558136058314752/QueenPerseponeR_large.jpeg", color=0xffffff)
     embed.set_author(name="#481 Persephone (Feu)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558136058314752/QueenPerseponeR_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: CR +20~25%(Donjons)\n**Passif**: Nécrose x2 80% 1 tour\n(???)\n**Actif**: Nécrose x2 100% 1 tours\n(Dmg +20%, tour: +1)\n**PV**: 30110\n**Attaque**: 3077\n**Défense**: 2801\n**Récupération**:2617", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pers','EauPers','TopPerse']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558136326619136/QueenPerseponeB_large.jpeg", color=0xffffff)
     embed.set_author(name="#482 Persephone (Eau)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558136326619136/QueenPerseponeB_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: CR +20~25%(Donjons)\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +10%, Taux: +20%)\n**PV**: 32494\n**Attaque**: 2784\n**Défense**: 2883\n**Récupération**:2624", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pers','BoisPers']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558134594371586/QueenPerseponeG_large.jpeg", color=0xffffff)
     embed.set_author(name="#483 Persephone (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558134594371586/QueenPerseponeG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: CR +20~25%(Donjons)\n**Passif**: Nécrose x3 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Attaque réduite 100% 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 32800\n**Attaque**: 2737\n**Défense**: 2903\n**Récupération**:2610", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pers','LightPers']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558136893112321/QueenPerseponeW_large.jpeg", color=0xffffff)
     embed.set_author(name="#484 Persephone (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558136893112321/QueenPerseponeW_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: CR +20~25% (Donjons)\n**Passif**: Boost de moral (Allies) 20% SP\n(Dmg +30%)\n**Actif**: Choc 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 31094\n**Attaque**: 2649\n**Défense**: 3548\n**Récupération**:2023", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pers','DarkPers']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558131624935424/QueenPersepone_large.jpeg", color=0xffffff)
     embed.set_author(name="#485 Persephone (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558131624935424/QueenPersepone_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: CR +20~25%(Donjons)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg +25%)\n**Actif**: Prédateur 50%\n(Dmg +25%)\n**PV**: 27151\n**Attaque**: 3834\n**Défense**: 2704\n**Récupération**:2043", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############# Peyote ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Peyo','FeuPeyo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557781618524180/PeyotesR_large.jpeg", color=0xffffff)
     embed.set_author(name="#486 Peyote (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557781618524180/PeyotesR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Att +20~25%\n**Passif**: Pétrification 80% 1 tour\n(No skillbooks)\n**Actif**: Adrénaline 30% de ses PV \n(No skillbooks)\n**PV**: 36451\n**Attaque**: 1418\n**Défense**: 1411\n**Récupération**:1704", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Peyo','EauPeyo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557775247376403/PeyotesB_large.jpeg", color=0xffffff)
     embed.set_author(name="#487 Peyote (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557775247376403/PeyotesB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +20~25%\n**Passif**: Adrénaline 20% de ses PV \n(No skillbooks)\n**Actif**: Adrénaline 20% de ses PV (allies)\n(No skillbooks)\n**PV**: 24090\n**Attaque**: 2171\n**Défense**: 2147\n**Récupération**:2100", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Peyo','BoisPeyo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557772651233346/Peyotes_large.jpeg", color=0xffffff)
     embed.set_author(name="#488 Peyote (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557772651233346/Peyotes_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Att +20~25%\n**Passif**: Boost de moral 30%\n(No skillbooks)\n**Actif**: Pétrification 80% 2 tour\n(No skillbooks)\n**PV**: 29453\n**Attaque**: 1342\n**Défense**: 2445\n**Récupération**:1573", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Peyo','LightPeyo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557807480602625/PeyotesW_large.jpeg", color=0xffffff)
     embed.set_author(name="#489 Peyote (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557807480602625/PeyotesW_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +20~25%\n**Passif**: Attaque réduite 100% 1 tour\n(No skillbooks)\n**Actif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**PV**: 27972\n**Attaque**: 1892\n**Défense**: 1725\n**Récupération**:1562", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Peyo','DarkPeyo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557776547741697/PeyotesD_large.jpeg", color=0xffffff)
     embed.set_author(name="#490 Peyote (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557776547741697/PeyotesD_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Att +20~25%\n**Passif**: Traqueur (Dark) 20%\n(No skillbooks)\n**Actif**: Pétrification 40% 1 tour\n(No skillbooks)\n**PV**: 35375\n**Attaque**: 1554\n**Défense**: 1758\n**Récupération**:1329", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ Phibian ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Phib','FeuPhib','TopPhib']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554042300039168/FroskeR_large.jpeg", color=0xffffff)
     embed.set_author(name="#491 Phibian (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554042300039168/FroskeR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Clan)\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Aveuglement 80% 2 tours\n(Dmg +25%)\n**PV**: 29889\n**Attaque**: 2860\n**Défense**: 1709\n**Récupération**:1764", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Phib','EauPhib']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554033261576212/Froske_large.jpeg", color=0xffffff)
     embed.set_author(name="#492 Phibian (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554033261576212/Froske_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Att +30~35%(Clan)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 46993\n**Attaque**: 1499\n**Défense**: 1479\n**Récupération**:1404", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Phib','BoisPhib','TopPhib']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554044896313348/FroskeG_large.jpeg", color=0xffffff)
     embed.set_author(name="#493 Phibian (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554044896313348/FroskeG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Clan)\n**Passif**: Défense réduite 80% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 35974\n**Attaque**: 1953\n**Défense**: 1889\n**Récupération**:1786", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Phib','LightPhib']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554049355120671/FroskeW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#494 Phibian (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554049355120671/FroskeW_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Clan)\n**Passif**: Sceau 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 26096\n**Attaque**: 2424\n**Défense**: 3269\n**Récupération**:1914", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Phib','DarkPhib']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554035396214806/FroskeD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#495 Phibian (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554035396214806/FroskeD_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(Clan)\n**Passif**: Vague martiale 20% (On crit)\n(Dmg +25%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +30%)\n**PV**: 32017\n**Attaque**: 2580\n**Défense**: 2576\n**Récupération**:1664", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ Pincemi ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Pinc','FeuPinc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553117510795309/CrabigR_large.jpeg", color=0xffffff)
     embed.set_author(name="#496 Pincemi (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553117510795309/CrabigR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Def +20~25%\n**Passif**: Reduction des dégâts 50% 1 tour\n(Dmg: 20%, +1 tour)\n**Actif**: Persévérance\n(Dmg: +25%)\n**PV**: 38678\n**Attaque**: 1247\n**Défense**: 1683\n**Récupération**:1547", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pinc','EauPinc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553087177588756/Crabig_large.jpeg", color=0xffffff)
     embed.set_author(name="#497 Pincemi (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553087177588756/Crabig_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Reduction des dégâts 50% 1 tour\n(Dmg: 20%, +1 tour)\n**Actif**: Prédateur 30%\n(Dmg: +20%, Taux: +10%)\n**PV**: 29147\n**Attaque**: 2302\n**Défense**: 1328\n**Récupération**:1444", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pinc','BoisPinc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553089673199616/CrabigG_large.jpeg", color=0xffffff)
     embed.set_author(name="#498 Pincemi (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553089673199616/CrabigG_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Def +20~25%\n**Passif**: Reduction des dégâts 50% 1 tour\n(Dmg: +20%, +1 tour)\n**Actif**: Pétrification 80% 1 tour\n(Dmg: +20%, +1 tour)\n**PV**: 29930\n**Attaque**: 1471\n**Défense**: 2275\n**Récupération**:1743", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############# Pinolo ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Pino','BoisPino']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557873591222310/Pinocchio_large.jpeg", color=0xffffff)
     embed.set_author(name="#503 Pinolo (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557873591222310/Pinocchio_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20% (Clan)\n**Passif**: Frappe Courageuse\n(No skillbooks)\n**Actif**: Frappe indéfectible\n(No skillbooks)\n**PV**: 21308\n**Attaque**: 2315\n**Défense**: 1730\n**Récupération**:1730", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pino','LightPino']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557905673453588/PinocchioW_large.jpeg", color=0xffffff)
     embed.set_author(name="#504 Pinolo (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557905673453588/PinocchioW_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Clan)\n**Passif**: Choc 60% - 2 tours\n**Actif**: Prédateur 40%\n(No skillbooks)\n**PV**: 23433\n**Attaque**: 2683\n**Défense**: 1614\n**Récupération**:1668", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pino','DarkPino']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557883984707584/PinocchioD_large.jpeg", color=0xffffff)
     embed.set_author(name="#505 Pinolo (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557883984707584/PinocchioD_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%(Clan)\n**Passif**: Frappe indéfectible\n**Actif**: Attaque réduite 60% - 1 tour\n**PV**: 26195\n**Attaque**: 2103\n**Défense**: 2113\n**Récupération**:2011", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ Pinolo Lie ###########
	 ################################### 

 if any([message.content.startswith (item) for item in ['Pino','BoisPino']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557895871365120/Pinocchiofake_large.jpeg", color=0xffffff)
     embed.set_author(name="#508 Pinolo Lie (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557895871365120/Pinocchiofake_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20% (Clan)\n**Passif**: Frappe Courageuse\n(No skillbooks)\n**Actif**: Frappe Courageuse\n(No skillbooks)\n**PV**: 2152\n**Attaque**: 402\n**Défense**: 197\n**Récupération**:197", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pino','LightPino']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557903957983305/PinocchiofakeW_large.jpeg", color=0xffffff)
     embed.set_author(name="#509 Pinolo Lie (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557903957983305/PinocchiofakeW_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: CR +15~20%(Clan)\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**Actif**: Aveuglement 100% 2 tours\n(No skillbooks)\n**PV**: 2149\n**Attaque**: 103\n**Défense**: 103\n**Récupération**:103", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pino','DarkPino']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557901286211584/PinocchiofakeD_large.jpeg", color=0xffffff)
     embed.set_author(name="#510 Pinolo Lie (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557901286211584/PinocchiofakeD_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%(Clan)\n**Passif**: Chasseur 100%\n(No skillbooks)\n**Actif**: Chasseur 100%\n(No skillbooks)\n**PV**: 1195\n**Attaque**: 142\n**Défense**: 152\n**Récupération**:152", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############   Fée   ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Fee','FeuFee','TopFee']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553317029642250/DaphneR_large.jpeg", color=0xffffff)
     embed.set_author(name="#511 Fée (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553317029642250/DaphneR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Défense augmentée 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 33202\n**Attaque**: 2099\n**Défense**: 2180\n**Récupération**:2528", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fee','EauFee']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553304765235202/DaphneB_large.jpeg", color=0xffffff)
     embed.set_author(name="#512 Fée (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553304765235202/DaphneB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: CR +15~20%\n**Passif**: Nécrose x2 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Domination 2 tours\n(Dmg +30%)\n**PV**: 29753\n**Attaque**: 2125\n**Défense**: 2002\n**Récupération**:3133", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fee','BoisFee']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553300948680763/Daphne_large.jpeg", color=0xffffff)
     embed.set_author(name="#513 Fée (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553300948680763/Daphne_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: CR +15~20%\n**Passif**: Sommeil 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Vigueur 2 tours\n(Dmg +20%, Taux: +5%)\n**PV**: 28262\n**Attaque**: 2431\n**Défense**: 2138\n**Récupération**:2881", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fee','LightFee']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557214559467864074/DaphneW_large.jpeg", color=0xffffff)
     embed.set_author(name="#514 Fée (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557214559467864074/DaphneW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: CR +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Vigueur 2 tours\n(Dmg +20%, Taux: +5%)\n**PV**: 29113\n**Attaque**: 1907\n**Défense**: 2322\n**Récupération**:3139", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fee','DarkFee']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553315062251520/DaphneD_large.jpeg", color=0xffffff)
     embed.set_author(name="#515 Fée (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553315062251520/DaphneD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: CR +15~20%\n**Passif**: Vague martiale\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Volonté 3 tours\n(Dmg +30%)\n**PV**: 24543\n**Attaque**: 2343\n**Défense**: 2125\n**Récupération**:3173", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ Poséïdon #############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Pose','FeuPose','TopPose']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557157216682012/NeptunegodR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#516 Poseidon (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557157216682012/NeptunegodR_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45% (Clan)\n**Passif**:Frappe Courageuse\n(No skillbooks)\n**Actif**: Affaiblissement 70% 2 tours\n(No skillbooks)\n**PV**: 40312\n**Attaque**: 2187\n**Défense**: 2677\n**Récupération**:2534", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pose','EauPose']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557151705628693/Neptunegod_Large.jpeg", color=0xffffff)
     embed.set_author(name="#517 Poseidon (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557151705628693/Neptunegod_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Clan)\n**Passif**: Boost de moral (Allies) 10% SP\n(No skillbooks)\n**Actif**: Prédateur 40%\n(No skillbooks)\n**PV**: 28513\n**Attaque**: 3391\n**Défense**: 2588\n**Récupération**:2329", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pose','BoisPose']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557155165667338/NeptunegodG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#518 Poseidon (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557155165667338/NeptunegodG_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%(Clan)\n**Passif**:  Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(No skillbooks)\n**Actif**: Étourdissement 80% 1 tour\n(No skillbooks)\n**PV**: 27281\n**Attaque**: 2792\n**Défense**: 3773\n**Récupération**:2206", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pose','LightPose']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557172412776448/NeptunegodW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#519 Poseidon (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557172412776448/NeptunegodW_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Clan)\n**Passif**: Boost de moral 50% de ses PA\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 24216\n**Attaque**: 3854\n**Défense**: 2635\n**Récupération**:2240", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pose','DarkPose']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607337948358115329/NeptunegodD_Large.jpg", color=0xffffff)
     embed.set_author(name="#520 Poseidon (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607337948358115329/NeptunegodD_Large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%(Clan)\n**Passif**: Vague martiale\n(No skillbooks)\n**Actif**: Attaque réduite 80% 3 tours\n(No skillbooks)\n**PV**: 29732\n**Attaque**: 2281\n**Défense**: 3602\n**Récupération**:2561", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############# Torpin ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Torpin','BoisTorpin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558137807470592/Rabbeatles_large.jpeg", color=0xffffff)
     embed.set_author(name="#523 Torpin (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558137807470592/Rabbeatles_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35% (Donjons)\n**Passif**: Attaque réduite 70% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 50% 2 tours \n(No skillbooks)\n**PV**: 28840\n**Attaque**: 1784\n**Défense**: 2717\n**Récupération**:1355", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Torpin','LightTorpin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558166039199765/RabbeatlesW_large.jpeg", color=0xffffff)
     embed.set_author(name="#524 Torpin (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558166039199765/RabbeatlesW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%(Donjons)\n**Passif**: Vengeance\n(No skillbooks)\n**Actif**: Vengeance\n(No skillbooks)\n**PV**: 29208\n**Attaque**: 3139\n**Défense**: 2152\n**Récupération**:2193", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Torpin','DarkTorpin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558139518615555/RabbeatlesD_large.jpeg", color=0xffffff)
     embed.set_author(name="#525 Torpin (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558139518615555/RabbeatlesD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%(Donjons)\n**Passif**: Nécrose x2 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose x2 80% 2 tours\n(No skillbooks)\n**PV**: 35906\n**Attaque**: 2439\n**Défense**: 2146\n**Récupération**:2092", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############   Raic  ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Radi','FeuRadi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558210452815892/RadiossR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#526 Radic (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558210452815892/RadiossR_Large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%(Donjons)\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Prédateur 30%\n(Dmg +20%)\n**PV**: 26709\n**Attaque**: 2527\n**Défense**: 1811\n**Récupération**:1607", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Radi','EauRadi']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558180689772548/RadiossB_Large.jpeg", color=0xffffff)
     embed.set_author(name="#527 Radic (Eau)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558180689772548/RadiossB_Large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: SP Rec +20~25%(Donjons)\n**Passif**: Étourdissement 40% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Étourdissement 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 34353\n**Attaque**: 1874\n**Défense**: 1540\n**Récupération**:1588", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Radi','BoisRadi','TopRadi']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558183160217650/RadiossG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#528 Radic (Bois)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558183160217650/RadiossG_Large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%(Donjons)\n**Passif**: Attaque réduite 30% 3 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Attaque réduite 70% 1 tour\n(Dmg +15%, tour: +1)\n**PV**: 28936\n**Attaque**: 1832\n**Défense**: 2411\n**Récupération**:1437", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Radi','LightRadi']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558214349062157/RadiossW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#529 Radic (light)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558214349062157/RadiossW_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%(Donjons)\n**Passif**: Nécrose 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Nécrose 60% 2 tours\n(Dmg +10%, Taux: +15%)\n**PV**: 24380\n**Attaque**: 3126\n**Défense**: 2581\n**Récupération**:2091", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Radi','DarkRadi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558178467053574/Radioss_Large.jpeg", color=0xffffff)
     embed.set_author(name="#530 Radic (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558178467053574/Radioss_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%(Donjons)\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Agression (Def)\n(Dmg +20%)\n**PV**: 29998\n**Attaque**: 2111\n**Défense**: 3187\n**Récupération**:1839", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############   Ramu  ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Ramu','FeuRamu','TopRamu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554283472781334/GoldonRamsayR_large.jpeg", color=0xffffff)
     embed.set_author(name="#531 Ramu (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554283472781334/GoldonRamsayR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Siphon de PA (On crit) 20%\n(Dmg +20%, Taux: +5%)\n**Actif**: Adrénaline (On crit)(Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**PV**: 26552\n**Attaque**: 2792\n**Défense**: 1682\n**Récupération**:1573", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ramu','EauRamu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554279181746176/GoldonRamsayB_large.jpeg", color=0xffffff)
     embed.set_author(name="#532 Ramu (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554279181746176/GoldonRamsayB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Provocation 80% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Soif 60% -30% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 25204\n**Attaque**: 1954\n**Défense**: 2983\n**Récupération**:1491", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ramu','BoisRamu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554277135056898/GoldonRamsay_large.jpeg", color=0xffffff)
     embed.set_author(name="#533 Ramu (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554277135056898/GoldonRamsay_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Étourdissement 40% 2 tours\n(Dmg +10%, Taux: +25%)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 28817\n**Attaque**: 2137\n**Défense**: 1970\n**Récupération**:1875", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ramu','LightRamu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554317941309450/GoldonRamsayW_large.jpeg", color=0xffffff)
     embed.set_author(name="#534 Ramu (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554317941309450/GoldonRamsayW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20% (Donjons)\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 30335\n**Attaque**: 2784\n**Défense**: 2399\n**Récupération**:2100", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ramu','DarkRamu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554280700215327/GoldonRamsayD_large.jpeg", color=0xffffff)
     embed.set_author(name="#535 Ramu (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554280700215327/GoldonRamsayD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20% (Donjons)\n**Passif**: Silence 80% 2 tours\n(Dmg +20%, tour: +1)\n**Actif**: Provocation 80% 1 tour\n(Dmg +15%, Taux: +20%)\n**PV**: 37281\n**Attaque**: 2044\n**Défense**: 2487\n**Récupération**:1717", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ Robobot ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Robo','LightRobo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556427697324034/Metalion_large.jpeg", color=0xffffff)
     embed.set_author(name="#539 Robobot (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556427697324034/Metalion_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Attaque réduite 40% 1 tour\n(No skillbooks)\n**Actif**: Fatigue 80% 2 tours\n(No skillbooks)\n**PV**: 27165\n**Attaque**: 2547\n**Défense**: 1403\n**Récupération**:1525", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Robo','DarkRobo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556423486242847/MetalionD_large.jpeg", color=0xffffff)
     embed.set_author(name="#540 Robobot (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556423486242847/MetalionD_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Def +20~25%\n**Passif**: Provocation 40% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**PV**: 27972\n**Attaque**: 1892\n**Défense**: 1725\n**Récupération**:1562", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############  Pottus ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Pottus','FeuPottus']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557214830839463946/DePottusR_large.jpeg", color=0xffffff)
     embed.set_author(name="#541 Pottus (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557214830839463946/DePottusR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: PV +20~25%\n**Passif**: Nécrose 40% 2 tours\n(No skillbooks)\n**Actif**: Étourdissement 40% 1 tour\n(No skillbooks)\n**PV**: 36451\n**Attaque**: 1418\n**Défense**: 1411\n**Récupération**:1704", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pottus','EauPottus']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553360528637954/DePottusB_large.jpeg", color=0xffffff)
     embed.set_author(name="#542 Pottus (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553360528637954/DePottusB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: PV +20~25%\n**Passif**: Récupération réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Nécrose 60% 2 tours\n(No skillbooks)\n**PV**: 24090\n**Attaque**: 2171\n**Défense**: 2147\n**Récupération**:2100", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pottus','BoisPottus']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553359018819592/DePottus_large.jpeg", color=0xffffff)
     embed.set_author(name="#543 Pottus (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553359018819592/DePottus_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Attaque réduite 50% 2 tours\n(No skillbooks)\n**Actif**: Défense réduite 40% 2 tours\n(No skillbooks)\n**PV**: 29453\n**Attaque**: 1342\n**Défense**: 2445\n**Récupération**:1573", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ Gravel  ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Grav','LightGrav']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555580645048330/Lemstone_large.jpeg", color=0xffffff)
     embed.set_author(name="#549 Gravel (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555580645048330/Lemstone_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Boost de moral 30% de ses PA\n(No skillbooks)\n**Actif**: Choc 50% 2 tours\n(No skillbooks)\n**PV**: 24271\n**Attaque**: 2458\n**Défense**: 3187\n**Récupération**:1914", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Grav','DarkGrav']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555592972107834/LemstoneD_large.jpeg", color=0xffffff)
     embed.set_author(name="#550 Gravel (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555592972107834/LemstoneD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Fatigue 80% 3 tours\n(No skillbooks)\n**Actif**: Silence 80% 2 tours\n(No skillbooks)\n**PV**: 24414\n**Attaque**: 3024\n**Défense**: 2138\n**Récupération**:2247", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############   Buis  ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Buis','BoisBuis']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560396255494155/Treebear_large.jpeg", color=0xffffff)
     embed.set_author(name="#553 Buis (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560396255494155/Treebear_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Rec +20~25%\n**Passif**: Sommeil 60% 1 tour\n(Dmg: +20%, Taux: +20%, +1 tour)\n**Actif**: Zèle 2 tours\n(Recup: +35%, +1 tour)\n**PV**: 37602\n**Attaque**: 1193\n**Défense**: 1840\n**Récupération**:1343", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ############ Rudolph ##############
	 ################################### 

 if any([message.content.startswith (item) for item in ['Rudo','BoisRudo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557285763711001/Noelle_large.jpeg", color=0xffffff)
     embed.set_author(name="#558 Rudolph (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557285763711001/Noelle_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Boost de moral 50% de ses PA\n(No skillbooks)\n**Actif**: Prédateur 20%\n(No skillbooks)\n**PV**: 26389\n**Attaque**: 2642\n**Défense**: 1539\n**Récupération**:1512", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Rudo','LightRudo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557370304233491/NoelleW_large.jpeg", color=0xffffff)
     embed.set_author(name="#559 Rudolph (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557370304233491/NoelleW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +13~18%\n**Passif**: Siphon de PA 25%\n(No skillbooks)\n**Actif**: Étourdissement 80% 1 tour\n(No skillbooks)\n**PV**: 26470\n**Attaque**: 2492\n**Défense**: 3269\n**Récupération**:2070", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Rudo','DarkRudo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557295930966039/NoelleD_large.jpeg", color=0xffffff)
     embed.set_author(name="#560 Rudolph (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557295930966039/NoelleD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Attaque réduite (On crit) 3 tours\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 28084\n**Attaque**: 3208\n**Défense**: 2023\n**Récupération**:2043", inline=False)
     
     await message.channel.send(embed=embed)

	 ###################################
	 ####### Spectre des sables ########
	 ################################### 

 if any([message.content.startswith (item) for item in ['Spectre','FeuSpectre','TopSpectre']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560820429651969/Void_large.jpeg", color=0xffffff)
     embed.set_author(name="#561 Spectre des sables (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560820429651969/Void_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Attaque réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Faiblesse exposée 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 22568\n**Attaque**: 2077\n**Défense**: 2935\n**Récupération**:1559", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Spectre','EauSpectre','TopSpectre']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560825961807872/VoidB_large.jpeg", color=0xffffff)
     embed.set_author(name="#562 Spectre des sables (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560825961807872/VoidB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Frappe indéfectible (On crit)\n(Dmg +25%)\n**Actif**: Vengeance\n(Dmg +35%)\n**PV**: 23566\n**Attaque**: 2362\n**Défense**: 2331\n**Récupération**:1725", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Spectre','BoisSpectre']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560829095084052/VoidG_large.jpeg", color=0xffffff)
     embed.set_author(name="#563 Spectre des sables (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560829095084052/VoidG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Sceau 70% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Sceau 60% 2 tours\n(Dmg +15%, Taux: +15%)\n**PV**: 31391\n**Attaque**: 1942\n**Défense**: 2092\n**Récupération**:1411", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Spectre','LightSpectre']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560832521699341/VoidW_large.jpeg", color=0xffffff)
     embed.set_author(name="#564 Spectre des sables (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560832521699341/VoidW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Aveuglement 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Frappe indéfectible (On crit)\n(Dmg +25%)\n**PV**: 37493\n**Attaque**: 2473\n**Défense**: 2214\n**Récupération**:1915", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Spectre','DarkSpectre']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560826616381461/VoidD_large.jpeg", color=0xffffff)
     embed.set_author(name="#565 Spectre des sables (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560826616381461/VoidD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Siphon de PA 20%\n(Dmg +15%, Taux: +5%)\n**Actif**: Persévérance\n(Dmg +20%)\n**PV**: 26634\n**Attaque**: 3391\n**Défense**: 2424\n**Récupération**:1784", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Sanzang ##################
	 #######################################	 

 if any([message.content.startswith (item) for item in ['Sanz','sanz','Sanzang','sanzang','SanzangFeu','FeuSanzang','SanzFeu','SanzF','FeuSanz']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554508555780106/GuemtsaiziR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#566 Sanzang (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554508555780106/GuemtsaiziR_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Def +35~40%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Sceau 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 29671\n**Attaque**: 2520\n**Défense**: 3562\n**Récupération**:2622", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sanz','sanz','Sanzang','sanzang','SanzangEau','EauSanzang','SanzEau','SanzE','EauSanz']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554499881959446/GuemtsaiziB_Large.jpeg", color=0xffffff)
     embed.set_author(name="#567 Sanzang (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554499881959446/GuemtsaiziB_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Def +35~40%\n**Passif**: Agression (Def)\n(Dmg +25%)\n**Actif**: Agression (Def)\n(Dmg +10%, Taux: +20%)\n**PV**: 24611\n**Attaque**: 2492\n**Défense**: 3698\n**Récupération**:2690", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sanz','sanz','Sanzang','sanzang','SanzangBois','BoisSanzang','SanzBois','SanzB','BoisSanz']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554503652638740/Guemtsaizi_Large.jpeg", color=0xffffff)
     embed.set_author(name="#568 Sanzang (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554503652638740/Guemtsaizi_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Def +35~40%\n**Passif**: Attaque réduite 90% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 35770\n**Attaque**: 2739\n**Défense**: 2568\n**Récupération**:2316", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sanz','sanz','Sanzang','sanzang','SanzangLight','LightSanzang','SanzLight','SanzL','LightSanz']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554511407906826/GuemtsaiziW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#569 Sanzang (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554511407906826/GuemtsaiziW_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Def +40%~45%\n**Passif**: Vague martiale 20%\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Choc 70% 2 tours\n(Dmg +20%, Taux : +10%)\n**PV**: 34803\n**Attaque**: 2716\n**Défense**: 2917\n**Récupération**:2787", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sanz','sanz','Sanzang','sanzang','SanzangDark','DarkSanzang','SanzDark','SanzD','DarkSanz']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554506383130645/GuemtsaiziD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#570 Sanzang (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554506383130645/GuemtsaiziD_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Def +35~40%\n**Passif**: Siphon de PV \n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 24141\n**Attaque**: 3848\n**Défense**: 2601\n**Récupération**:2384", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Stella ###################
	 #######################################
	 
 if any([message.content.startswith (item) for item in ['Stella','FeuStella','TopStella']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553268417396766/DagonR_large.jpeg", color=0xffffff)
     embed.set_author(name="#571 Stella (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553268417396766/DagonR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Prédateur 30%\n(???)\n**Actif**: Étourdissement 100% 1 tour\n(???)\n**PV**: 22650\n**Attaque**: 2622\n**Défense**: 1852\n**Récupération**:1491", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Stella','EauStella']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553259466752011/Dagon_large.jpeg", color=0xffffff)
     embed.set_author(name="#572 Stella (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553259466752011/Dagon_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Nécrose x2 50% 1 tour\n(???)\n**Actif**: Nécrose 80% 2 tours\n(???)\n**PV**: 24346\n**Attaque**: 2472\n**Défense**: 1771\n**Récupération**:1696", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Stella','BoisStella']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553263841673216/DagonG_large.jpeg", color=0xffffff)
     embed.set_author(name="#573 Stella (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553263841673216/DagonG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: CR +13~18%\n**Passif**: Soif 80% -20% 1 tour\n(???)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 28687\n**Attaque**: 1981\n**Défense**: 1773\n**Récupération**:1691", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Stella','LightStella']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553293172310026/DagonW_large.jpeg", color=0xffffff)
     embed.set_author(name="#574 Stella (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553293172310026/DagonW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +13~18%\n**Passif**: Choc (On crit) 2 tour\n(Dmg +25%)\n**Actif**: Attaque réduite (On crit) 2 tours\n(Dmg +20%)\n**PV**: 38174\n**Attaque**: 2017\n**Défense**: 1983\n**Récupération**:2364", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Stella','DarkStella']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553261710704671/DagonD_large.jpeg", color=0xffffff)
     embed.set_author(name="#575 Stella (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553261710704671/DagonD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +13~18%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Agression (Def)\n(Dmg +20%)\n**PV**: 31442\n**Attaque**: 2036\n**Défense**: 2962\n**Récupération**:2343", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Stella S Evo #############
	 #######################################

 if any([message.content.startswith (item) for item in ['FeuStella','SStella','FeuSStella']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707496845814923264/20200506_093822.jpg", color=0xffffff)
     embed.set_author(name="#823 Stella SE (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707496845814923264/20200506_093822.jpg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Prédateur 30%\n(???)\n**Actif**: Étourdissement 100% 1 tour\n(???)\n**PV**: 24925\n**Attaque**: 3330\n**Défense**: 2043\n**Récupération**:1648", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['EauStella','SStella','EauSStella']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707496846054129664/20200506_093841.jpg", color=0xffffff)
     embed.set_author(name="#824 Stella SE (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707496846054129664/20200506_093841.jpg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Nécrose x2 50% 1 tour\n(???)\n**Actif**: Nécrose 80% 2 tours\n(???)\n**PV**: 26791\n**Attaque**: 2751\n**Défense**: 2152\n**Récupération**:1873", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['BoisStella','SStella','BoisSStella']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707496845517258822/20200506_093744.jpg", color=0xffffff)
     embed.set_author(name="#825 Stella SE (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707496845517258822/20200506_093744.jpg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: CR +13~18%\n**Passif**: Soif 80% -20% 1 tour\n(???)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 31581\n**Attaque**: 2188\n**Défense**: 2357\n**Récupération**:1874", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['LightStella','SStella','LightSStella']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707496846351794216/20200506_093900.jpg", color=0xffffff)
     embed.set_author(name="#826 Stella SE (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707496846351794216/20200506_093900.jpg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +13~18%\n**Passif**: Choc (On crit) 2 tour\n(Dmg +25%)\n**Actif**: Attaque réduite (On crit) 2 tours\n(Dmg +20%)\n**PV**: 42157\n**Attaque**: 2221\n**Défense**: 2187\n**Récupération**:2603", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['DarkStella','SStella','DarkSStella']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707496846670692422/20200506_093919.jpg", color=0xffffff)
     embed.set_author(name="#827 Stella SE (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707496846670692422/20200506_093919.jpg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +13~18%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Agression (Def)\n(Dmg +20%)\n**PV**: 34595\n**Attaque**: 2247\n**Défense**: 3609\n**Récupération**:2336", inline=False)
     
     await message.channel.send(embed=embed)
	 	 
	 #######################################
	 ############  Gren  ###################
	 #######################################

 if any([message.content.startswith (item) for item in ['Gren','FeuGren']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560815924969475/VitaminR_large.jpeg", color=0xffffff)
     embed.set_author(name="#576 Gren (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560815924969475/VitaminR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Sceau 70% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Nécrose 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 28030\n**Attaque**: 1873\n**Défense**: 2676\n**Récupération**:1301", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Gren','EauGren','TopGren']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560773814026241/VitaminB_large.jpeg", color=0xffffff)
     embed.set_author(name="#577 Gren (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560773814026241/VitaminB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 27931\n**Attaque**: 2165\n**Défense**: 2066\n**Récupération**:1432", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Gren','BoisGren']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560771758948377/Vitamin_large.jpeg", color=0xffffff)
     embed.set_author(name="#578 Gren (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560771758948377/Vitamin_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Nécrose x2 60% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Nécrose x2 40% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 37173\n**Attaque**: 1792\n**Défense**: 1976\n**Récupération**:1540", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Gren','LightGren']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560817414078465/VitaminW_large.jpeg", color=0xffffff)
     embed.set_author(name="#579 Gren (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560817414078465/VitaminW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Attaque réduite 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 28806\n**Attaque**: 1954\n**Défense**: 3344\n**Récupération**:2172", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Gren','DarkGren']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560811793448967/VitaminD_large.jpeg", color=0xffffff)
     embed.set_author(name="#580 Gren (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560811793448967/VitaminD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Avantage élémentaire (On crit)\n(Dmg +20%)\n**Actif**: Défense réduite (On crit)\n(Dmg +25%)\n**PV**: 27560\n**Attaque**: 3064\n**Défense**: 2159\n**Récupération**:2002", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Sirène ###################
	 #######################################

 if any([message.content.startswith (item) for item in ['Sire','FeuSire']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557184706281474/NereidR_large.jpeg", color=0xffffff)
     embed.set_author(name="#581 Sirène (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557184706281474/NereidR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Def +30~35%(Même élément)\n**Passif**: Nécrose 30% 2 tours\n(Taux: +25%)\n**Actif**: Volonté 2 tours\n(Dmg +25%, Taux: +20%)\n**PV**: 30822\n**Attaque**: 1696\n**Défense**: 1525\n**Récupération**:2751", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sire','EauSire','TopSire']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557181543645204/Nereid_large.jpeg", color=0xffffff)
     embed.set_author(name="#582 Sirène (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557181543645204/Nereid_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Def +30~35%(Même élément)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Vigueur 2 tours\n(Dmg +25%, Taux: +5%)\n**PV**: 27982\n**Attaque**: 1920\n**Défense**: 2016\n**Récupération**:2867", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sire','BoisSire']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557183951306753/NereidG_large.jpeg", color=0xffffff)
     embed.set_author(name="#583 Sirène (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557183951306753/NereidG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Def +30~35%(Même élément)\n**Passif**: Abondance d'âmes rouges\n(Dmg +25%)\n**Actif**: Récupération augmentée 2 tours\n(Dmg +25%, tour: +1)\n**PV**: 26327\n**Attaque**: 1900\n**Défense**: 1559\n**Récupération**:2458", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Sire','LightSire']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557187432579073/NereidW_large.jpeg", color=0xffffff)
     embed.set_author(name="#584 Sirène (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557187432579073/NereidW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%(Même élément)\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Bouclier (Level) 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 24713\n**Attaque**: 2424\n**Défense**: 3337\n**Récupération**:1914", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sire','DarkSire']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557610553732890632/NereidD_large.jpeg", color=0xffffff)
     embed.set_author(name="#585 Sirène (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557610553732890632/NereidD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Def +30~35%(Même élément)\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Domination 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 24523\n**Attaque**: 2322\n**Défense**: 2118\n**Récupération**:3344", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Sha Wujing ###############
	 #######################################

 if any([message.content.startswith (item) for item in ['ShaW','FeuShaW', 'Sha', 'FeuSha','TopSha']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634748415934464/Sha3EvoR_large.jpg", color=0xffffff)
     embed.set_author(name="#591 Sha wujing (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634748415934464/Sha3EvoR_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Tc +20~25%\n**Passif**: Faiblesse exposée 80% 2 tours\n(No skillbooks)\n**Actif**: Frappe Courageuse\n(No skillbooks)\n**PV**: 30059\n**Attaque**: 3596\n**Défense**: 2206\n**Récupération**:2240", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['ShaW','EauShaW', 'Sha', 'EauSha']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634734813806615/Sha3Evo_large.jpg", color=0xffffff)
     embed.set_author(name="#592 Sha wujing (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634734813806615/Sha3Evo_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Tc +20~25%\n**Passif**: Résistance réduite 2 tours\n(No skillbooks)\n**Actif**: Sceau 70% 2 tours\n(No skillbooks)\n**PV**: 31295\n**Attaque**: 2934\n**Défense**: 2944\n**Récupération**:2181", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['ShaW','BoisShaW', 'Sha', 'BoisSha']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634744225824774/Sha3EvoG_large.jpg", color=0xffffff)
     embed.set_author(name="#593 Sha wujing (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634744225824774/Sha3EvoG_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Tc +20~25%\n**Passif**: Vague martiale 20%\n(No skillbooks)\n**Actif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**PV**: 32698\n**Attaque**: 2907\n**Défense**: 2856\n**Récupération**:2011", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['ShaW','LightShaW', 'Sha', 'LightSha']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634753482653716/Sha3EvoW_large.jpg", color=0xffffff)
     embed.set_author(name="#594 Sha wujing (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634753482653716/Sha3EvoW_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Tc +20~25%\n**Passif**: Sceau 100% 3 tours\n(dmg +25%)\n**Actif**: Réduction de dégâts 2 tours\n(dmg +25%)\n**PV**: 30883\n**Attaque**: 2622\n**Défense**: 3596\n**Récupération**:2479", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['ShaW','DarkShaW', 'Sha', 'DarkSha']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634739678937103/Sha3EvoD_large.jpg", color=0xffffff)
     embed.set_author(name="#595 Sha wujing (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634739678937103/Sha3EvoD_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Tc +20~25%\n**Passif**: Frappe Courageuse\n(No skillbooks)\n**Actif**: Affaiblissement 80% 2 tours\n(No skillbooks)\n**PV**: 28643\n**Attaque**: 3732\n**Défense**: 2465\n**Récupération**:2349", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############  Clamy ###################
	 #######################################

 if any([message.content.startswith (item) for item in ['Clamy','FeuClamy']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558861177978910/ShellkingR_large.jpeg", color=0xffffff)
     embed.set_author(name="#586 Clamy (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558861177978910/ShellkingR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: PV Rec +20~25%\n**Passif**: Provocation 100% 2 tours\n(Dmg: +20% tour: +1)\n**Actif**: Prédateur (feu) 100%\n(Dmg: +35%)\n**PV**: 29293\n**Attaque**: 2001\n**Défense**: 1705\n**Récupération**: 1671", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Clamy','EauClamy','TopClamy']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558855821852673/Shellking_large.jpeg", color=0xffffff)
     embed.set_author(name="#587 Clamy (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558855821852673/Shellking_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV Rec +20~25%\n**Passif**: Défense réduite 100% 2 tours\n(Dmg: +20% tour: +1)\n**Actif**: Prédateur (eau) 100%\n(Dmg: +35%)\n**PV**: 29440\n**Attaque**: 2996\n**Défense**: 1641\n**Récupération**: 1764", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Clamy','BoisClamy']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558857717809165/ShellkingG_large.jpeg", color=0xffffff)
     embed.set_author(name="#588 Clamy (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558857717809165/ShellkingG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV Rec +20~25%\n**Passif**: Nécrose 100% 2 tours\n(Dmg: +20% tour: +1)\n**Actif**: Prédateur (bois) 100%\n(Dmg: +35%)\n**PV**: 25360\n**Attaque**: 1784\n**Défense**: 2663\n**Récupération**: 1566", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Sherlock #################
	 #######################################

 if any([message.content.startswith (item) for item in ['Sher','FeuSher']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553372243329025/DetectiveSherlockR_large.jpeg", color=0xffffff)
     embed.set_author(name="#596 Sherlock (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553372243329025/DetectiveSherlockR_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20% (Clan)\n**Passif**: Traqueur (bois) 50%\n(No skillbooks)\n**Actif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**PV**: 25878\n**Attaque**: 2724\n**Défense**: 1580\n**Récupération**:1750", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sher','EauSher']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553366559916043/DetectiveSherlockB_large.jpeg", color=0xffffff)
     embed.set_author(name="#597 Sherlock (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553366559916043/DetectiveSherlockB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Clan)\n**Passif**: Traqueur (feu) 50%\n(No skillbooks)\n**Actif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**PV**: 28507\n**Attaque**: 2622\n**Défense**: 1641\n**Récupération**:1566", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sher','BoisSher']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553369210716171/DetectiveSherlockG_large.jpeg", color=0xffffff)
     embed.set_author(name="#598 Sherlock (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553369210716171/DetectiveSherlockG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Clan)\n**Passif**: Traqueur (eau) 50%\n(No skillbooks)\n**Actif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**PV**: 26300\n**Attaque**: 2813\n**Défense**: 1696\n**Récupération**:1525", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sher','LightSher']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553364995440660/DetectiveSherlock_large.jpeg", color=0xffffff)
     embed.set_author(name="#599 Sherlock (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553364995440660/DetectiveSherlock_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Clan)\n**Passif**: Faiblesse exposée 80% 2 tours\n(No skillbooks)\n**Actif**: Faiblesse exposée 80% 2 tours\n(No skillbooks)\n**PV**: 29794\n**Attaque**: 3221\n**Défense**: 2091\n**Récupération**:1889", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Shinobi ##################
	 #######################################

 if any([message.content.startswith (item) for item in ['Shin','FeuShin','TopShin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554694837403670/HattoriHanzoR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#601 Shinobi (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554694837403670/HattoriHanzoR_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: PV +40~45% (Clan)\n**Passif**: Frappe Courageuse\n(Dmg +20%)\n**Actif**: Attaque réduite 80% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 32106\n**Attaque**: 3057\n**Défense**: 2883\n**Récupération**:2072", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Shin','EauShin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554677200486401/HattoriHanzoB_Large.jpeg", color=0xffffff)
     embed.set_author(name="#602 Shinobi (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554677200486401/HattoriHanzoB_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Clan)\n**Passif**: Avantage élémentaire \n(Dmg +25%)\n**Actif**: Siphon de PA 50% \n(Dmg +25%)\n**PV**: 25483\n**Attaque**: 3303\n**Défense**: 3071\n**Récupération**:2547", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Shin','BoisShin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554675162054666/HattoriHanzo_Large.jpeg", color=0xffffff)
     embed.set_author(name="#603 Shinobi (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554675162054666/HattoriHanzo_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%(Clan)\n**Passif**: Siphon de PA 30%\n(Dmg +20%, Taux: +10%)\n**Actif**: Étourdissement 100% 2 tours\n(Dmg +30%)\n**PV**: 41436\n**Attaque**: 2017\n**Défense**: 2807\n**Récupération**:2228", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Shin','LightShin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554710520037382/HattoriHanzoW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#604 Shinobi (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554710520037382/HattoriHanzoW_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Clan)\n**Passif**: Boost de Moral +100% PA\n(Dmg +30%)\n**Actif**: Prédateur 50%\n(Dmg +30%)\n**PV**: 28977\n**Attaque**: 3889\n**Défense**: 2935\n**Récupération**:2247", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Shin','DarkShin']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554690584248335/HattoriHanzoD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#605 Shinobi (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554690584248335/HattoriHanzoD_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Clan)\n**Passif**: Siphon de PA 40%\n(Dmg +25%, +Effect.: +10%)\n**Actif**: Chasseur 50%\n(Dmg +30%)\n**PV**: 28949\n**Attaque**: 3957\n**Défense**: 2704\n**Récupération**:2309", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############  Shiva  ##################
	 #######################################

 if any([message.content.startswith (item) for item in ['Shiv','FeuShiv','TopShiv']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556070690881536/Mahakala_large.jpeg", color=0xffffff)
     embed.set_author(name="#606 Shiva (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556070690881536/Mahakala_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%,(Donjons)\n**Passif**: Étourdissement 100% 1 tour\n(Dmg: +15% tour: +1)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg: +25%)\n**PV**: 27689\n**Attaque**: 2295\n**Défense**: 3494\n**Récupération**:2309", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Shiv','EauShiv']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556073115058187/MahakalaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#607 Shiva (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556073115058187/MahakalaB_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%(Donjons)\n**Passif**: Siphon de PA 30%\n(Dmg: +20% Effect.: +10%)\n**Actif**: Soif 80% -30% 2 tours\n(Dmg: +20% tour: +1)\n**PV**: 49104\n**Attaque**: 2214\n**Défense**: 2398\n**Récupération**:2228", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Shiv','BoisShiv']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556087392469022/MahakalaG_large.jpeg", color=0xffffff)
     embed.set_author(name="#608 Shiva (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556087392469022/MahakalaG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Donjons)\n**Passif**: Prédateur 50%\n(Dmg: +25%)\n**Actif**: Sceau 80% 2 tours\n(???)\n**PV**: 28541\n**Attaque**: 3902\n**Défense**: 2819\n**Récupération**:2138", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Shiv','LightShiv']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556088625594384/MahakalaW_large.jpeg", color=0xffffff)
     embed.set_author(name="#609 Shiva (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556088625594384/MahakalaW_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%(Donjons)\n**Passif**: Vague martiale 20%\n(Dmg: +20% Effect.: +5%)\n**Actif**: Agression (PV)\n(Dmg: +25%)\n**PV**: 49376\n**Attaque**: 2568\n**Défense**: 2126\n**Récupération**:1915", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Shiv','DarkShiv']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556081721638914/MahakalaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#610 Shiva (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556081721638914/MahakalaD_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%(Donjons)\n**Passif**: Sceau 100% 2 tours\n(???)\n**Actif**: Étourdissement 80% 2 tour\n(???)\n**PV**: 32273\n**Attaque**: 2349\n**Défense**: 3562\n**Récupération**:2588", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Siegfried ################
	 #######################################

 if any([message.content.startswith (item) for item in ['Sieg','FeuSieg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553469253386243/Dragonslayer_large.jpeg", color=0xffffff)
     embed.set_author(name="#611 Siegfried (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553469253386243/Dragonslayer_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Def +40~45%(Clan)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg: +25%)\n**Actif**: Avantage élémentaire\n(Dmg: +30%)\n**PV**: 24625\n**Attaque**: 4018\n**Défense**: 2629\n**Récupération**:2179", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sieg','EauSieg','TopSieg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553498735018034/DragonslayerB_large.jpeg", color=0xffffff)
     embed.set_author(name="#612 Siegfried (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553498735018034/DragonslayerB_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Def +40~45%(Clan)\n**Passif**: Faiblesse exposée 80% 2 tours\n(Dmg: +15% tour: +1)\n**Actif**: Frappe Courageuse\n(Dmg: +20%)\n**PV**: 28221\n**Attaque**: 3269\n**Défense**: 2629\n**Récupération**:2329", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sieg','BoisSieg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553503533301778/DragonslayerG_large.jpeg", color=0xffffff)
     embed.set_author(name="#613 Siegfried (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553503533301778/DragonslayerG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Def +40~45%(Clan)\n**Passif**: Défense réduite 80% 3 tours\n(Dmg: +25% )\n**Actif**: Étourdissement 80% 1 tour\n(Dmg: +15% Taux: +10%)\n**PV**: 39747\n**Attaque**: 2677\n**Défense**: 2235\n**Récupération**:2194", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sieg','LightSieg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553503814320128/DragonslayerW_large.jpeg", color=0xffffff)
     embed.set_author(name="#614 Siegfried (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553503814320128/DragonslayerW_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Def +40~45%(Clan)\n**Passif**: Frappe Courageuse\n(Dmg: +20%)\n**Actif**: Frappe Courageuse\n(Dmg: +20%)\n**PV**: 31295\n**Attaque**: 3023\n**Défense**: 2692\n**Récupération**:2672", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sieg','DarkSieg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553499968143373/DragonslayerD_large.jpeg", color=0xffffff)
     embed.set_author(name="#615 Siegfried (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553499968143373/DragonslayerD_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Def +40~45%(Clan)\n**Passif**: Agression (Def)\n(Dmg: +25%)\n**Actif**: Agression (Def)\n(Dmg: +25%)\n**PV**: 31578\n**Attaque**: 2213\n**Défense**: 3807\n**Récupération**:2465", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Soldat Slime #############
	 #######################################

 if any([message.content.startswith (item) for item in ['SoldatSlime','FeuSoldatSlime','SoldatSlime','FeuSoldatSlime']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559134994596086/Slimeknight3Evo_large.jpeg", color=0xffffff)
     embed.set_author(name="#621 Soldat Slime (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559134994596086/Slimeknight3Evo_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Attaque réduite 60% 2 tour\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 25783\n**Attaque**: 3044\n**Défense**: 2029\n**Récupération**:1246", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['SoldatSlime','EauSoldatSlime','SoldatSlime','EauSoldatSlime']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559205337399296/Slimeknight3EvoB_large.jpeg", color=0xffffff)
     embed.set_author(name="#622 Soldat Slime (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559205337399296/Slimeknight3EvoB_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%\n**Passif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 24182\n**Attaque**: 2370\n**Défense**: 3064\n**Récupération**:1226", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['SoldatSlime','BoisSoldatSlime','SoldatSlime','BoisSoldatSlime']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557610727095926799/Slimeknight3EvoG_large.jpeg", color=0xffffff)
     embed.set_author(name="#623 Soldat Slime (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557610727095926799/Slimeknight3EvoG_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Nécrose x2 60% 2 tours\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 27117\n**Attaque**: 2738\n**Défense**: 2179\n**Récupération**:1301", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['SoldatSlime','LightSoldatSlime','SoldatSlime','LightSoldatSlime']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559213012844566/Slimeknight3EvoW_large.jpeg", color=0xffffff)
     embed.set_author(name="#624 Soldat Slime (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559213012844566/Slimeknight3EvoW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Boost de moral 50%\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 27070\n**Attaque**: 3058\n**Défense**: 2275\n**Récupération**:2118", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['SoldatSlime','DarkSoldatSlime','SoldatSlime','DarkSoldatSlime']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559202183151616/Slimeknight3EvoD_large.jpeg", color=0xffffff)
     embed.set_author(name="#625 Soldat Slime (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559202183151616/Slimeknight3EvoD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Adrénaline 20% de ses PV\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 37288\n**Attaque**: 1887\n**Défense**: 2180\n**Récupération**:2037", inline=False)
     
     await message.channel.send(embed=embed)

     
 if message.content.startswith("SoldatSlime"):
     return
     
 if message.content.startswith("FeuSoldatSlime"):
     return
     
 if message.content.startswith("EauSoldatSlime"):
     return
     
 if message.content.startswith("BoisSoldatSlime"):
     return
     
 if message.content.startswith("LightSoldatSlime"):
     return
     
 if message.content.startswith("DarkSoldatSlime"):
     return
     
 if message.content.startswith("SoldatSlime"):
     return
     
 if message.content.startswith("FeuSoldatSlime"):
     return
     
 if message.content.startswith("EauSoldatSlime"):
     return
     
 if message.content.startswith("BoisSoldatSlime"):
     return
     
 if message.content.startswith("LightSoldatSlime"):
     return
     
 if message.content.startswith("DarkSoldatSlime"):
     return
	 
	 #######################################
	 ############  Slime  ##################
	 #######################################

 if any([message.content.startswith (item) for item in ['Slime','FeuSlime']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555350977544192/KingslimeR_large.jpeg", color=0xffffff)
     embed.set_author(name="#616 Slime (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555350977544192/KingslimeR_large.jpeg")
     embed.add_field(name="★", value="**Type**: Tank\n**Lead**: PV +20~25%(Même élément)\n**Passif**: Attaque réduite 60% 2 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +25%, Taux: 10%, tour: +1)\n**PV**: 35177\n**Attaque**: 2017\n**Défense**: 1574\n**Récupération**:1554", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Slime','EauSlime']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555344438624257/KingslimeB_large.jpeg", color=0xffffff)
     embed.set_author(name="#617 Slime (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555344438624257/KingslimeB_large.jpeg")
     embed.add_field(name="★", value="**Type**: Défenseur\n**Lead**: PV +20~25%(Même élément)\n**Passif**: Résistance réduite 100% 2 tours\n(Dmg +30%)\n**Actif**: Etourdissement 60% 1 tour\n(Dmg +25%, Taux: 10%, tour: +1)\n**PV**: 24516\n**Attaque**: 1777\n**Défense**: 2574\n**Récupération**:1396", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Slime','BoisSlime']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555321399312395/Kingslime_large.jpeg", color=0xffffff)
     embed.set_author(name="#618 Slime (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555321399312395/Kingslime_large.jpeg")
     embed.add_field(name="★", value="**Type**: Attaquant\n**Lead**: PV +20~25%(Même élément)\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +25%, Taux: 10%, tour: +1)\n**PV**: 26144\n**Attaque**: 2322\n**Défense**: 1525\n**Récupération**:1430", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Slime','LightSlime']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555351954817026/KingslimeW_large.jpeg", color=0xffffff)
     embed.set_author(name="#619 Slime (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555351954817026/KingslimeW_large.jpeg")
     embed.add_field(name="★", value="**Type**: Équilibré\n**Lead**: PV +20~25%(Même élément)\n**Passif**: Choc 60% 1 tour\n(Dmg +25%, Taux: +10%)\n**Actif**: Choc 60% 1 tour\n(Dmg +25%, tour: +1)\n**PV**: 28946\n**Attaque**: 1708\n**Défense**: 1766\n**Récupération**:1562", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Slime','DarkSlime']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/608935531241406475/KingslimeD_large.jpg", color=0xffffff)
     embed.set_author(name="#620 Slime (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/608935531241406475/KingslimeD_large.jpg")
     embed.add_field(name="★", value="**Type**: Tank\n**Lead**: PV +20~25%(Même élément)\n**Passif**: Agression (PV)\n(Dmg +30%)\n**Actif**: Agression (PV)\n(Dmg +30%)\n**PV**: 37792\n**Attaque**: 1411\n**Défense**: 1370\n**Récupération**:1710", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############  Givri  ##################
	 #######################################

 if any([message.content.startswith (item) for item in ['Givri','EauGivri']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557225747415040/nicole_large.jpeg", color=0xffffff)
     embed.set_author(name="#627 Givri (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557225747415040/nicole_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: SP Rec +20~25%\n**Passif**: Provocation 80% 1 tour\n(No skillbooks)\n**Actif**: Nécrose x2 60% 1 tours\n(No skillbooks)\n**PV**: 43240\n**Attaque**: 1622\n**Défense**: 1261\n**Récupération**:1465", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Givri','LightGivri']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557217327511240763/nicoleW_large.jpeg", color=0xffffff)
     embed.set_author(name="#629 Givri (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557217327511240763/nicoleW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%\n**Passif**: Siphon de PV\n(No skillbooks)\n**Actif**: Siphon de PV (Allies) \n(No skillbooks)\n**PV**: 26368\n**Attaque**: 3276\n**Défense**: 2247\n**Récupération**:1682", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Givri','DarkGivri']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557226523361290/nicoleD_large.jpeg", color=0xffffff)
     embed.set_author(name="#630 Givri (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557226523361290/nicoleD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: SP Rec +20~25%\n**Passif**: Attaque réduite 80% 1 tour\n(No skillbooks)\n**Actif**: Étourdissement 80% 1 tour\n(No skillbooks)\n**PV**: 32337\n**Attaque**: 2614\n**Défense**: 2672\n**Récupération**:1739", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Sparkitt #################
	 #######################################

 if any([message.content.startswith (item) for item in ['Sparki','FeuSparki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555509366915082/LaidenR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#631 Sparkitt (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555509366915082/LaidenR_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Étourdissement (On crit) 2 tours\n(Dmg +25%)\n**Actif**: Aveuglement 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 36587\n**Attaque**: 1962\n**Défense**: 2316\n**Récupération**:2214", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sparki','EauSparki','TopSparki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555498851926071/LaidenB_Large.jpeg", color=0xffffff)
     embed.set_author(name="#632 Sparkitt (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555498851926071/LaidenB_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Aveuglement 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Frappe Courageuse (On crit)\n(Dmg +20%)\n**PV**: 30672\n**Attaque**: 3173\n**Défense**: 1900\n**Récupération**:2002", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sparki','BoisSparki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557612523306745858/LaidenG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#633 Sparkitt (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557612523306745858/LaidenG_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%\n**Passif**: Avantage élémentaire\n(Dmg +20%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 24737\n**Attaque**: 2805\n**Défense**: 2576\n**Récupération**:2488", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sparki','LightSparki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555496243200010/Laiden_Large.jpeg", color=0xffffff)
     embed.set_author(name="#634 Sparkitt (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555496243200010/Laiden_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Choc (On crit) 1 tour\n(Dmg +25%)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 30815\n**Attaque**: 3303\n**Défense**: 1920\n**Récupération**:2023", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sparki','DarkSparki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555501116719115/LaidenD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#635 Sparkitt (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555501116719115/LaidenD_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Boost de moral (Allies) 10% SP\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 37152\n**Attaque**: 2024\n**Défense**: 2432\n**Récupération**:1976", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Tincel  ##################
	 #######################################

 if any([message.content.startswith (item) for item in ['Tincel','FeuTincell']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561027070296064/WispkingR_large.jpeg", color=0xffffff)
     embed.set_author(name="#636 Tincel (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561027070296064/WispkingR_large.jpeg")
     embed.add_field(name="★", value="**Type**: Tank\n**Lead**: PV +10~15%\n**Passif**: Défense réduite 40% 2 tours\n(No skillbooks)\n**Actif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**PV**: 35531\n**Attaque**: 1363\n**Défense**: 1772\n**Récupération**:1418", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tincel','EauTincel']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561016165367828/Wispking_large.jpeg", color=0xffffff)
     embed.set_author(name="#637 Tincel (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561016165367828/Wispking_large.jpeg")
     embed.add_field(name="★", value="**Type**: Équilibré\n**Lead**: PV +10~15%\n**Passif**: Fatigue 40% 1 tour\n(No skillbooks)\n**Actif**: Fatigue 60% 2 tours\n(No skillbooks)\n**PV**: 29082\n**Attaque**: 1538\n**Défense**: 1793\n**Récupération**:1684", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tincel','BoisTincel']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561022146314240/WispkingG_large.jpeg", color=0xffffff)
     embed.set_author(name="#638 Tincel (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561022146314240/WispkingG_large.jpeg")
     embed.add_field(name="★", value="**Type**: Récupération\n**Lead**: PV +10~15%\n**Passif**: Nécrose 40% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 60% 2 tours\n(No skillbooks)\n**PV**: 25102\n**Attaque**: 1682\n**Défense**: 1600\n**Récupération**:2418", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tincel','LightTincel']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561045592604672/WispkingW_large.jpeg", color=0xffffff)
     embed.set_author(name="#639 Tincel (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561045592604672/WispkingW_large.jpeg")
     embed.add_field(name="★", value="**Type**: Défenseur\n**Lead**: PV +10~15%\n**Passif**: Étourdissement 20% 1 tour\n(No skillbooks)\n**Actif**: Étourdissement 60% 1 tour\n(No skillbooks)\n**PV**: 27860\n**Attaque**: 1355\n**Défense**: 2418\n**Récupération**:1628", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tincel','DarkTincel']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561019277279238/WispkingD_large.jpeg", color=0xffffff)
     embed.set_author(name="#640 Tincel (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561019277279238/WispkingD_large.jpeg")
     embed.add_field(name="★", value="**Type**: Attaquant\n**Lead**: PV +10~15%\n**Passif**: Silence 20% 1 tour\n(No skillbooks)\n**Actif**: Silence 60% 1 tour\n(No skillbooks)\n**PV**: 23433\n**Attaque**: 2275\n**Défense**: 1662\n**Récupération**:1362", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Sphinx  ##################
	 #######################################

 if any([message.content.startswith (item) for item in ['Sph','FeuSph','TopSph']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552209552900156/CairoR_large.jpeg", color=0xffffff)
     embed.set_author(name="#641 Sphinx (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552209552900156/CairoR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Attaque réduite 70% 2 tours\n(Dmg +10%, Taux: +30%)\n**Actif**: Frappe indéfectible \n(Dmg +30%)\n**PV**: 35586\n**Attaque**: 2494\n**Défense**: 2044\n**Récupération**:1881", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sph','EauSph']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552202804396083/CairoB_large.jpeg", color=0xffffff)
     embed.set_author(name="#642 Sphinx (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552202804396083/CairoB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Frappe indéfectible\n(Dmg +30%)\n**Actif**: Siphon de PV \n(Dmg +30%)\n**PV**: 25442\n**Attaque**: 2390\n**Défense**: 3235\n**Récupération**:2036", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sph','BoisSph','TopSph']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552207573057546/CairoG_large.jpeg", color=0xffffff)
     embed.set_author(name="#643 Sphinx (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552207573057546/CairoG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Faiblesse exposée 70% 2 tours\n(Dmg +10%, Taux: +30%)\n**Actif**: Frappe indéfectible\n(Dmg +30%)\n**PV**: 25415\n**Attaque**: 3221\n**Défense**: 2452\n**Récupération**:1873", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sph','LightSph']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552179563626506/Cairo_large.jpeg", color=0xffffff)
     embed.set_author(name="#644 Sphinx (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552179563626506/Cairo_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Avantage élémentaire (On crit)\n(Dmg +30%)\n**Actif**: Sceau 70% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 30890\n**Attaque**: 3391\n**Défense**: 1968\n**Récupération**:1920", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sph','DarkSph']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557612911468740619/CairoD_large.jpeg", color=0xffffff)
     embed.set_author(name="#645 Sphinx (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557612911468740619/CairoD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Aveuglement 80% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Frappe indéfectible (On crit)\n(Dmg +30%)\n**PV**: 27768\n**Attaque**: 3002\n**Défense**: 2753\n**Récupération**:1854", inline=False)
     
     await message.channel.send(embed=embed)
     	 
	 #######################################
	 ############   Ecurrix   ##############
	 #######################################

 if any([message.content.startswith (item) for item in ['Ecur','FeuEcur']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559563027513367/SqusquR_large.jpeg", color=0xffffff)
     embed.set_author(name="#646 Ecurrix (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559563027513367/SqusquR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +20~25%\n**Passif**: Attaque réduite 60% 1 tour\n(Dmg +10%, Taux: +10%tour: +1)\n**Actif**: Attaque réduite 40% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 29906\n**Attaque**: 1654\n**Défense**: 1752\n**Récupération**:1623", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ecur','EauEcur']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559553175224320/SqusquB_large.jpeg", color=0xffffff)
     embed.set_author(name="#647 Ecurrix (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559553175224320/SqusquB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Att +20~25%\n**Passif**: Récupération réduite 60% 1 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Nécrose 40% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 24720\n**Attaque**: 1607\n**Défense**: 2322\n**Récupération**:1491", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Ecur','BoisEcur']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559549060481024/Squsqu_large.jpeg", color=0xffffff)
     embed.set_author(name="#648 Ecurrix (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559549060481024/Squsqu_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Att +20~25%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**Actif**: Défense réduite 40% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 22514\n**Attaque**: 2574\n**Défense**: 1539\n**Récupération**:1403", inline=False)
     
     await message.channel.send(embed=embed)
     	 
	 #######################################
	 ############   Crustarov   ############
	 #######################################
  
 if any([message.content.startswith (item) for item in ['Crus','FeuCrus']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558472173060109/RocknRollR_large.jpeg", color=0xffffff)
     embed.set_author(name="#651 Crustarov (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558472173060109/RocknRollR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: CR +10~15%\n**Passif**: Boost de moral 20% PA\n(Dmg: +20%, Taux: +10%)\n**Actif**: Perforation 70% défense ennemie\n(Dmg: +30%)\n**PV**: 26041\n**Attaque**: 2486\n**Défense**: 1457\n**Récupération**:1628", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Crus','EauCrus']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558468675010563/RocknRoll_large.jpeg", color=0xffffff)
     embed.set_author(name="#652 Crustarov (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558468675010563/RocknRoll_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: CR +10~15%\n**Passif**: Provocation intrépide 60% 1 tour\n(Dmg: +20%, Taux: +20%)\n**Actif**: Perforation 70% défense ennemie\n(Dmg: +30%)\n**PV**: 29947\n**Attaque**: 1593\n**Défense**: 1766\n**Récupération**:1623", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Crus','BoisCrus']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558470344212490/RocknRollG_large.jpeg", color=0xffffff)
     embed.set_author(name="#653 Crustarov (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558470344212490/RocknRollG_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: CR +10~15%\n**Passif**: Adrenaline 20% PV\n(Dmg: +20%, Taux: +10%)\n**Actif**: Perforation 70% défense ennemie\n(Dmg: +30%)\n**PV**: 26518\n**Attaque**: 2377\n**Défense**: 1696\n**Récupération**:1457", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############    Succube    ############
	 #######################################
  
 if any([message.content.startswith (item) for item in ['Succ','FeuSucc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557218097015029761/LilithR_large.jpeg", color=0xffffff)
     embed.set_author(name="#656 Succube (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557218097015029761/LilithR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Siphon de PV  (On crit)\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite (On crit) 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 26327\n**Attaque**: 3167\n**Défense**: 2288\n**Récupération**:1682", inline=False)
     
     await message.channel.send(embed=embed)
   
 if any([message.content.startswith (item) for item in ['Succ','EauSucc','TopSucc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555663763439616/LilithB_large.jpeg", color=0xffffff)
     embed.set_author(name="#658 Succube (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555663763439616/LilithB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(Dmg +25%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +15%)\n**PV**: 37057\n**Attaque**: 2146\n**Défense**: 2473\n**Récupération**:1710", inline=False)
     
     await message.channel.send(embed=embed)
    
 if any([message.content.startswith (item) for item in ['Succ','BoisSucc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555665948672000/LilithG_large.jpeg", color=0xffffff)
     embed.set_author(name="#660 Succube (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555665948672000/LilithG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%\n**Passif**: Sommeil 60% 2 tours\n(Dmg +20%, Taux: +15%)\n**Actif**: Brise bouclier 100%\n(Dmg +30%)\n**PV**: 31329\n**Attaque**: 2321\n**Défense**: 2352\n**Récupération**:2045", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Succ','LightSucc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555669300183051/LilithW_large.jpeg", color=0xffffff)
     embed.set_author(name="#662 Succube (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555669300183051/LilithW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Boost de moral (Allies) 10% SP\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +25%)\n**PV**: 36812\n**Attaque**: 1976\n**Défense**: 2323\n**Récupération**:2214", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Succ','DarkSucc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555661851099150/Lilith_large.jpeg", color=0xffffff)
     embed.set_author(name="#664 Succube (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555661851099150/Lilith_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%\n**Passif**: Sommeil 80% 2 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Sommeil 80% 1 tour\n(Dmg +20%, tour: +1)\n**PV**: 30012\n**Attaque**: 2343\n**Défense**: 3173\n**Récupération**:1866", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############  Succube S Evo  ##########
	 #######################################
     
 if any([message.content.startswith (item) for item in ['FeuSucc','SSucc','FeuSSucc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607338087747682334/SuperLilithR_large.jpg", color=0xffffff)
     embed.set_author(name="#657 Succube SE (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607338087747682334/SuperLilithR_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Siphon de PV  (On crit)\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite (On crit) 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 28970\n**Attaque**: 3514\n**Défense**: 2527\n**Récupération**:1859", inline=False)
     
     await message.channel.send(embed=embed)
  
 if any([message.content.startswith (item) for item in ['EauSucc','SSucc','EauSSucc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607338082563522571/SuperLilithB_large.jpg", color=0xffffff)
     embed.set_author(name="#659 Succube SE (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607338082563522571/SuperLilithB_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(Dmg +25%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +15%)\n**PV**: 40931\n**Attaque**: 2364\n**Défense**: 2725\n**Récupération**:1888", inline=False)
     
     await message.channel.send(embed=embed)
 
 if any([message.content.startswith (item) for item in ['BoisSucc','SSucc','BoisSSucc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607338084765270030/SuperLilithG_large.jpg", color=0xffffff)
     embed.set_author(name="#661 Succube SE (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607338084765270030/SuperLilithG_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Sommeil 60% 2 tours\n(Dmg +20%, Taux: +15%)\n**Actif**: Brise bouclier 100%\n(Dmg +30%)\n**PV**: 34488\n**Attaque**: 2563\n**Défense**: 2596\n**Récupération**:2262", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['LightSucc','SSucc','LightSSucc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607338090083909652/SuperLilithW_large.jpg", color=0xffffff)
     embed.set_author(name="#663 Succube SE (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607338090083909652/SuperLilithW_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Boost de moral (Allies) 10% SP\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +25%)\n**PV**: 40658\n**Attaque**: 2174\n**Défense**: 2562\n**Récupération**:2439", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['DarkSucc','SSucc','DarkSSucc']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607338079501549570/SuperLilith_large.jpg", color=0xffffff)
     embed.set_author(name="#665 Succube SE (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607338079501549570/SuperLilith_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Sommeil 80% 2 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Sommeil 80% 1 tour\n(Dmg +20%, tour: +1)\n**PV**: 33022\n**Attaque**: 2581\n**Défense**: 3521\n**Récupération**:2057", inline=False)
     
     await message.channel.send(embed=embed)

	 
	 #######################################
	 ############   Sun Wukong  ############
	 #######################################

 if any([message.content.startswith (item) for item in ['Sun','FeuSun','Wukong','FeuWukong','TopSun']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558099710607360/Qitiandasheng_Large.jpeg", color=0xffffff)
     embed.set_author(name="#666 Sun Wukong (Feu)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558099710607360/Qitiandasheng_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +50~55%, (Clan)\n**Passif**: Défense réduite  70% 2 tours\n(???)\n**Actif**: Frappe Courageuse\n(Dmg +25%)\n**PV**: 28262\n**Attaque**: 3473\n**Défense**: 2479\n**Récupération**:2418", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sun','EauSun','Wukong','EauWukong']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558101430272000/QitiandashengB_Large.jpeg", color=0xffffff)
     embed.set_author(name="#667 Sun Wukong (Eau)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558101430272000/QitiandashengB_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +50~55%,(Clan)\n**Passif**: Siphon de PV  \n(Dmg +30%)\n**Actif**: Siphon de PV (Allies) \n(Dmg +30%)\n**PV**: 29801\n**Attaque**: 3323\n**Défense**: 2799\n**Récupération**:2363", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sun','BoisSun','Wukong','BoisWukong']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558126969126927/QitiandashengG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#668 Sun Wukong (Bois)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558126969126927/QitiandashengG_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +50~55%,(Clan)\n**Passif**: Défense réduite 70% 3 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 33328\n**Attaque**: 3405\n**Défense**: 2213\n**Récupération**:2329", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sun','LightSun','Wukong','LightWukong']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558121621651537/QitiandashengW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#669 Sun Wukong (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558121621651537/QitiandashengW_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +50~55%, (Clan)\n**Passif**: Défense réduite 100% 2 tours\n(Dmg +20%, +1 tour)\n**Actif**: Choc 70% 2 tour\n(Dmg +25%, Taux : +10%)\n**PV**: 43118\n**Attaque**: 2705\n**Défense**: 2494\n**Récupération**:2269", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sun','DarkSun','Wukong','DarkWukong']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558128588128277/QitiandashengD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#670 Sun Wukong (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558128588128277/QitiandashengD_Large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +50~55%, (Clan)\n**Passif**: Sceau 100% 3 tours\n(Dmg +30%)\n**Actif**: Étourdissement 70% 2 tour\n(Dmg +25%, Taux: +10%)\n**PV**: 32153\n**Attaque**: 2743\n**Défense**: 2747\n**Récupération**:2576", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############     Sura     #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Sura','FeuSura']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560713479094282/Varuna_large.jpeg", color=0xffffff)
     embed.set_author(name="#671 Sura (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560713479094282/Varuna_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Boost de moral 20% SP\n(Dmg +15%, +Effect.: +10%)\n**Actif**: Adrénaline (Allies) 20% de ses PV\n(Dmg +30%)\n**PV**: 22984\n**Attaque**: 3262\n**Défense**: 2084\n**Récupération**:1954", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sura','EauSura','TopSura']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560720391438336/VarunaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#672 Sura (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560720391438336/VarunaB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Étourdissement (On crit) 2 tours\n(Dmg +30%)\n**Actif**: Prédateur 40%\n(Dmg +30%)\n**PV**: 38412\n**Attaque**: 2044\n**Défense**: 2017\n**Récupération**:2303", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sura','BoisSura']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557613238137651201/VarunaG_large.jpeg", color=0xffffff)
     embed.set_author(name="#673 Sura (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557613238137651201/VarunaG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +15~20%\n**Passif**: Sceau 70% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Nécrose 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 29787\n**Attaque**: 2288\n**Défense**: 3105\n**Récupération**:1771", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sura','LightSura']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560752620470292/VarunaW_large.jpeg", color=0xffffff)
     embed.set_author(name="#674 Sura (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560752620470292/VarunaW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Adrénaline (Allies) 20% de ses PV\n(Dmg +30%)\n**PV**: 31772\n**Attaque**: 2532\n**Défense**: 2542\n**Récupération**:1671", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Sura','DarkSura']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560725671804947/VarunaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#675 Sura (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560725671804947/VarunaD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Siphon de PV \n(Dmg +30%)\n**Actif**: Chasseur 50%\n(Dmg +30%)\n**PV**: 25367\n**Attaque**: 3126\n**Défense**: 2343\n**Récupération**:1954", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############     Tai      #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Tai','LightTai']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559448187469824/Spark_large.jpeg", color=0xffffff)
     embed.set_author(name="#679 Tai (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559448187469824/Spark_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Choc 60% 1 tour\n(Dmg: +25%, Taux: +10%, +1 tour)\n**Actif**: Choc 80% 1 tour\n(Dmg: +25%, +1 tour)\n**PV**: 28667\n**Attaque**: 1722\n**Défense**: 1854\n**Récupération**:1664", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tai','DarkTai']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559450104528907/SparkD_large.jpeg", color=0xffffff)
     embed.set_author(name="#680 Tai (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559450104528907/SparkD_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Silence 60% 1 tour\n(Dmg: +25%, Taux: +10%, +1 tour)\n**Actif**: Chasseur 50%\n(Dmg: +30%)\n**PV**: 24931\n**Attaque**: 2486\n**Défense**: 2036\n**Récupération**:1641", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############    Tanya    ##############
	 #######################################

 if any([message.content.startswith (item) for item in ['Tany','FeuTany']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560089752404003/Talia_large.jpeg", color=0xffffff)
     embed.set_author(name="#681 Tanya (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560089752404003/Talia_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35% (Dungeon)\n**Passif**: Prédateur (bois) 50%\n(No skillbooks)\n**Actif**: Prédateur (bois) 100%\n(No skillbooks)\n**PV**: 24414\n**Attaque**: 2622\n**Défense**: 1832\n**Récupération**:1696", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tany','LightTany']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560093690986506/TaliaW_large.jpeg", color=0xffffff)
     embed.set_author(name="#684 Tanya (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560093690986506/TaliaW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35% (Dungeon)\n**Passif**: Merciless  Strike\n(No skillbooks)\n**Actif**: Merciless  Strike\n(No skillbooks)\n**PV**: 27608\n**Attaque**: 3058\n**Défense**: 2309\n**Récupération**:2050", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tany','DarkTany']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560091874721803/TaliaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#685 Tanya (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560091874721803/TaliaD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Dungeon)\n**Passif**: Provocation intrépide 80% 2 tours\n(No skillbooks)\n**Actif**: Silence 100% 1 tour\n(No skillbooks)\n**PV**: 30822\n**Attaque**: 2050\n**Défense**: 3099\n**Récupération**:2172", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############     Thor     #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Thor','FeuThor']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560207851552800/ThunderthorR_large.jpeg", color=0xffffff)
     embed.set_author(name="#686 Thor (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560207851552800/ThunderthorR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense réduite 50% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 26865\n**Attaque**: 2220\n**Défense**: 3037\n**Récupération**:2411", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Thor','EauThor']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560182400385064/ThunderthorB_large.jpeg", color=0xffffff)
     embed.set_author(name="#687 Thor (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560182400385064/ThunderthorB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Boost de moral 20% SP\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Prédateur 30%\n(Dmg +20%, Taux: +20%)\n**PV**: 26484\n**Attaque**: 3003\n**Défense**: 2111\n**Récupération**:2179", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Thor','BoisThor','TopThor']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560189275111424/ThunderthorG_large.jpeg", color=0xffffff)
     embed.set_author(name="#688 Thor (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560189275111424/ThunderthorG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Frappe Courageuse (On crit)\n(Dmg +20%)\n**Actif**: Aveuglement (On crit) 2 tours\n(Dmg +25%)\n**PV**: 30819\n**Attaque**: 2648\n**Défense**: 2535\n**Récupération**:1603", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Thor','LightThor']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560180529725450/Thunderthor_large.jpeg", color=0xffffff)
     embed.set_author(name="#689 Thor (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560180529725450/Thunderthor_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Choc 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 41374\n**Attaque**: 1717\n**Défense**: 2494\n**Récupération**:1894", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Thor','DarkThor']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560187173765121/ThunderthorD_large.jpeg", color=0xffffff)
     embed.set_author(name="#690 Thor (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560187173765121/ThunderthorD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Défense réduite (On crit) 2 tours\n(Dmg +25%)\n**Actif**: Frappe Courageuse (On crit)\n(Dmg +20%)\n**PV**: 25538\n**Attaque**: 2887\n**Défense**: 2411\n**Récupération**:2349", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############     Tigar    #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Tig','FeuTig']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560257759445013/Tigris_large.jpeg", color=0xffffff)
     embed.set_author(name="#691 Tigar (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560257759445013/Tigris_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Défense réduite 60% 3 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Nécrose 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 24445\n**Attaque**: 2832\n**Défense**: 2862\n**Récupération**:2685", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tig','EauTig']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560270409728010/TigrisB_large.jpeg", color=0xffffff)
     embed.set_author(name="#692 Tigar (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560270409728010/TigrisB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Provocation 70% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 26729\n**Attaque**: 2193\n**Défense**: 3051\n**Récupération**:2411", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tig','BoisTig','TopTig']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560280023072779/TigrisG_large.jpeg", color=0xffffff)
     embed.set_author(name="#693 Tigar (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560280023072779/TigrisG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Talent Var**: Att +30~35%\n**Passif**: Predateur 30%\n(Dgt +30%)\n**Actif**: Etourdissement 60% 1 tour\n(Dgt +15%, Taux: +10%)\n**PV**: 30625\n**Attaque**: 3139\n**Défense**: 1900\n**Recuperation**:2023", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tig','LightTig']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560283395031054/TigrisW_large.jpeg", color=0xffffff)
     embed.set_author(name="#694 Tigar (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560283395031054/TigrisW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Sommeil (On crit) 2 tours\n(Dmg +30%)\n**Actif**: Chasseur 50%\n(Dmg +30%)\n**PV**: 29521\n**Attaque**: 3126\n**Défense**: 2118\n**Récupération**:2002", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Tig','DarkTig']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560274083676160/TigrisD_large.jpeg", color=0xffffff)
     embed.set_author(name="#695 Tigar (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560274083676160/TigrisD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Vague martiale\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Attaque réduite 80% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 37009\n**Attaque**: 1983\n**Défense**: 2010\n**Récupération**:2316", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############   Crapora    #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Crapo','LightCrapo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560349400793109/ToadkingW_large.jpeg", color=0xffffff)
     embed.set_author(name="#699 Crapora (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560349400793109/ToadkingW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Boost de moral 25% SP\n(No skillbooks)\n**Actif**: Nécrose x3 60% 1 tours\n(No skillbooks)\n**PV**: 28817\n**Attaque**: 2491\n**Défense**: 2311\n**Récupération**:2147", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Crapo','DarkCrapo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560347240988702/Toadking_large.jpeg", color=0xffffff)
     embed.set_author(name="#700 Crapora (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560347240988702/Toadking_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Nécrose x2 70% 2 tours\n(No skillbooks)\n**PV**: 30761\n**Attaque**: 1920\n**Défense**: 3187\n**Récupération**:2172", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############   Truffel    #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Truf','FeuTruf']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558611822542862/Rutella_large.jpeg", color=0xffffff)
     embed.set_author(name="#701 Truffel (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558611822542862/Rutella_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Def +30~35% (Clan)\n**Passif**: Adrénaline 30% de ses PV\n(No skillbooks)\n**Actif**: Pétrification 60% 1 tour\n(No skillbooks)\n**PV**: 34898\n**Attaque**: 1499\n**Défense**: 1806\n**Récupération**:1724", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Truf','DarkTruf']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558615517593600/RutellaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#705 Truffel (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558615517593600/RutellaD_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35% (Clan)\n**Passif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**PV**: 28387\n**Attaque**: 1750\n**Défense**: 2744\n**Récupération**:1410", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############   Valkyrie   #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Valk','FeuValk','TopValk']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559037137420298/SigrunR_large.jpeg", color=0xffffff)
     embed.set_author(name="#706 Valkyrie (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559037137420298/SigrunR_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +40~45%(League)\n**Passif**: Boost de moral 50% SP\n(Dmg +20%)\n**Actif**: Étourdissement 80% 1 tour\n(Dmg +25%, Taux: +10%)\n**PV**: 35443\n**Attaque**: 2703\n**Défense**: 2842\n**Récupération**:2372", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Valk','EauValk']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559025477386242/Sigrun_large.jpeg", color=0xffffff)
     embed.set_author(name="#707 Valkyrie (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559025477386242/Sigrun_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +40~45%(League)\n**Passif**: Prédateur 50%\n(Dmg +20%)\n**Actif**: Défense réduite 100% 2 tour\n(Dmg +25%)\n**PV**: 25408\n**Attaque**: 3671\n**Défense**: 2581\n**Récupération**:2397", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Valk','BoisValk']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559035199782928/SigrunG_large.jpeg", color=0xffffff)
     embed.set_author(name="#708 Valkyrie (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559035199782928/SigrunG_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +40~45%(League)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +15%, +Effect.: +10%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%)\n**PV**: 30288\n**Attaque**: 2893\n**Défense**: 2937\n**Récupération**:2624", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Valk','LightValk']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559039393824786/SigrunW_large.jpeg", color=0xffffff)
     embed.set_author(name="#709 Valkyrie (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559039393824786/SigrunW_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +40~45%(League)\n**Passif**: Choc 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Réduction de dégâts 50% 2 tours (allies)\n(???)\n**PV**: 31003\n**Attaque**: 3104\n**Défense**: 2808\n**Récupération**:2515", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Valk','DarkValk']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559034394345474/SigrunD_large.jpeg", color=0xffffff)
     embed.set_author(name="#710 Valkyrie (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559034394345474/SigrunD_large.jpeg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Att +40~45%(League)\n**Passif**: Étourdissement 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Silence 100% 2 tours\n(???)\n**PV**: 48498\n**Attaque**: 2167\n**Défense**: 2357\n**Récupération**:2194", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############   Vampire    #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Vamp','FeuVamp','TopVamp','Requine']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557375907692584/NosferatuR_large.jpeg", color=0xffffff)
     embed.set_author(name="#711 Vampire (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557375907692584/NosferatuR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Adrénaline (On crit) 50% de ses PV\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 26368\n**Attaque**: 3024\n**Défense**: 2254\n**Récupération**:1662", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Vamp','EauVamp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557372388933643/NosferatuB_large.jpeg", color=0xffffff)
     embed.set_author(name="#712 Vampire (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557372388933643/NosferatuB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Prédateur 30%\n(No skillbooks)\n**Actif**: Sommeil 80% 1 tour\n(No skillbooks)\n**PV**: 26416\n**Attaque**: 3262\n**Défense**: 2043\n**Récupération**:2159", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Vamp','BoisVamp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557374204936192/NosferatuG_large.jpeg", color=0xffffff)
     embed.set_author(name="#713 Vampire (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557374204936192/NosferatuG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%\n**Passif**: Boost de moral 20% SP\n(No skillbooks)\n**Actif**: Nécrose x2 80% 1 tour\n(No skillbooks)\n**PV**: 31629\n**Attaque**: 2205\n**Défense**: 2352\n**Récupération**:2236", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Vamp','LightVamp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557377837334548/NosferatuW_large.jpeg", color=0xffffff)
     embed.set_author(name="#714 Vampire (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557377837334548/NosferatuW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Siphon de PV \n(No skillbooks)\n**Actif**: Défense réduite 70% 2 tours\n(No skillbooks)\n**PV**: 27969\n**Attaque**: 3310\n**Défense**: 2002\n**Récupération**:2036", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Vamp','DarkVamp']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557370476068867/Nosferatu_large.jpeg", color=0xffffff)
     embed.set_author(name="#715 Vampire (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557370476068867/Nosferatu_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Nécrose x3 80% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**PV**: 30672\n**Attaque**: 1873\n**Défense**: 3167\n**Récupération**:2179", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############    Venus    ##############
	 #######################################

 if any([message.content.startswith (item) for item in ['Venu','LightVenu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551394285060106/Aphrodite_large.jpeg", color=0xffffff)
     embed.set_author(name="#719 Venus (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551394285060106/Aphrodite_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Adrénaline 20% de ses PV\n(No skillbooks)\n**Actif**: Bouclier (PV) 3 tours\n(No skillbooks)\n**PV**: 37452\n**Attaque**: 1881\n**Défense**: 2521\n**Récupération**:2024", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Venu','DarkVenu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551398823165973/AphroditeD_large.jpeg", color=0xffffff)
     embed.set_author(name="#720 Venus (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551398823165973/AphroditeD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Attaque augmentée  3 tours\n(No skillbooks)\n**PV**: 26859\n**Attaque**: 2118\n**Défense**: 3153\n**Récupération**:2479", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############    Verde     #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Verde','FeuVerde','TopVerde']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553575427866650/DruidR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#721 Verde (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553575427866650/DruidR_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Aveuglement 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Frappe Courageuse\n(Dmg +20%)\n**PV**: 27713\n**Attaque**: 2573\n**Défense**: 2576\n**Récupération**:2311", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Verde','EauVerde']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553571829153792/DruidB_Large.jpeg", color=0xffffff)
     embed.set_author(name="#722 Verde (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553571829153792/DruidB_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Pétrification 100% 1 tour\n(Dmg +25%)\n**Actif**: Sceau 70% 2 tours\n(Dmg +20%)\n**PV**: 32051\n**Attaque**: 2491\n**Défense**: 2501\n**Récupération**:1671", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Verde','BoisVerde']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553568457064448/Druid_Large.jpeg", color=0xffffff)
     embed.set_author(name="#723 Verde (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553568457064448/Druid_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Attaque réduite 60% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +15%)\n**PV**: 44160\n**Attaque**: 1894\n**Défense**: 1881\n**Récupération**:1717", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Verde','LightVerde']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553598832082948/DruidW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#724 Verde (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553598832082948/DruidW_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Siphon de PA 30%\n(Dmg +20%, Taux: +5%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%)\n**PV**: 38848\n**Attaque**: 1813\n**Défense**: 2337\n**Récupération**:2194", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Verde','DarkVerde']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553575994359848/DruidD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#725 Verde (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553575994359848/DruidD_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Nécrose x3 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Silence 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 30979\n**Attaque**: 2813\n**Défense**: 2533\n**Récupération**:1737", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############   Victoria   #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Vic','FeuVic']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551619422846983/AthenaR_large.jpeg", color=0xffffff)
     embed.set_author(name="#726 Victoria (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551619422846983/AthenaR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Provocation intrépide 100% 1 tour\n(???)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 30516\n**Attaque**: 1900\n**Défense**: 3310\n**Récupération**:2172", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Vic','EauVic','TopVic']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551603689750532/AthenaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#728 Victoria (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551603689750532/AthenaB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 27097\n**Attaque**: 3126\n**Défense**: 2213\n**Récupération**:1989", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Vic','BoisVic']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551611847933953/AthenaG_large.jpeg", color=0xffffff)
     embed.set_author(name="#730 Victoria (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551611847933953/AthenaG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +10%, Taux: +30%)\n**PV**: 42478\n**Attaque**: 2085\n**Défense**: 1860\n**Récupération**:1853", inline=False)
     
     await message.channel.send(embed=embed)
    
 if any([message.content.startswith (item) for item in ['Vic','LightVic']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551588372152343/Athena_large.jpeg", color=0xffffff)
     embed.set_author(name="#732 Victoria (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551588372152343/Athena_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Agression (Def)\n(Dmg +20%)\n**PV**: 29889\n**Attaque**: 2295\n**Défense**: 3296\n**Récupération**:1777", inline=False)
     
     await message.channel.send(embed=embed)
 
 if any([message.content.startswith (item) for item in ['Vic','DarkVic']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551609352060982/AthenaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#734 Victoria (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551609352060982/AthenaD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Étourdissement (On crit) 1 tour\n(Dmg +30%)\n**Actif**: Défense réduite 60% 3 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 30580\n**Attaque**: 2165\n**Défense**: 2481\n**Récupération**:2304", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ########### Victoria S Evo ############
	 #######################################
     
 if any([message.content.startswith (item) for item in ['FeuVic','SVic','FeuSVic']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557613575087194154/SuperNikeR_large.jpeg", color=0xffffff)
     embed.set_author(name="#727 Victoria SE (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557613575087194154/SuperNikeR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Att +30~35%\n**Passif**: Provocation 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 33573\n**Attaque**: 2097\n**Défense**: 3671\n**Récupération**:2397", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['EauVic','SVic','EauSVic']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559897544228899/SuperNikeB_large.jpeg", color=0xffffff)
     embed.set_author(name="#729 Victoria SE (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559897544228899/SuperNikeB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Att +30~35%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 29814\n**Attaque**: 3473\n**Défense**: 2445\n**Récupération**:2193", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['BoisVic','SVic','BoisSVic']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559900488630283/SuperNikeG_large.jpeg", color=0xffffff)
     embed.set_author(name="#731 Victoria SE (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559900488630283/SuperNikeG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Att +30~35%\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +10%, Taux: +30%)\n**PV**: 46890\n**Attaque**: 2296\n**Défense**: 2051\n**Récupération**:2044", inline=False)
     
     await message.channel.send(embed=embed)
      
 if any([message.content.startswith (item) for item in ['LightVic','SVic','LightSVic']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559894490775553/SuperNike_large.jpeg", color=0xffffff)
     embed.set_author(name="#733 Victoria SE (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559894490775553/SuperNike_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Att +30~35%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Agression (Def)\n(Dmg +20%)\n**PV**: 32885\n**Attaque**: 2533\n**Défense**: 3657\n**Récupération**:1961", inline=False)
     
     await message.channel.send(embed=embed)
    
 if any([message.content.startswith (item) for item in ['DarkVic','SVic','DarkSVic']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559898974617612/SuperNikeD_large.jpeg", color=0xffffff)
     embed.set_author(name="#735 Victoria SE (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559898974617612/SuperNikeD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Att +30~35%\n**Passif**: Étourdissement (On crit) 1 tour\n(Dmg +30%)\n**Actif**: Défense réduite 60% 3 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 33664\n**Attaque**: 2392\n**Défense**: 2739\n**Récupération**:2548", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############    Wendigo   #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Wend','FeuWend']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557221589649850368/GargantuanR_Large.jpeg", color=0xffffff)
     embed.set_author(name="#736 Wendigo (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557221589649850368/GargantuanR_Large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Prédateur 30%\n(Dmg: +35%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg: +35%)\n**PV**: 27077\n**Attaque**: 2547\n**Défense**: 1559\n**Récupération**: 1784", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Wend','EauWend','TopWendi']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554143064129537/Gargantuan_Large.jpeg", color=0xffffff)
     embed.set_author(name="#737 Wendigo (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554143064129537/Gargantuan_Large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg: +20% Effect.: +5%)\n**Actif**: Provocation 50% 2 tours\n(Dmg: +15% Taux: +30%)\n**PV**: 27758\n**Attaque**: 1668\n**Défense**: 2615\n**Récupération**: 2023", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Wend','BoisWend']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554147136798731/GargantuanG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#738 Wendigo (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554147136798731/GargantuanG_Large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Boost de moral 20%\n(Dmg: +15% Effect.: +10%)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg: +15% Taux: +30%)\n**PV**: 27182\n**Attaque**: 2396\n**Défense**: 1582\n**Récupération**: 1807", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Wend','LightWend']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554150475595786/GargantuanW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#739 Wendigo (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554150475595786/GargantuanW_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Frappe Courageuse (On crit)\n(Dmg: +20%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg: +10% Taux: +20%)\n**PV**: 27063\n**Attaque**: 3105\n**Défense**: 2247\n**Récupération**: 2125", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Wend','DarkWend']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554144934789150/GargantuanD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#740 Wendigo (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554144934789150/GargantuanD_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Vengeance\n(Dmg: +35%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg: +35%)\n**PV**: 30492\n**Attaque**: 2478\n**Défense**: 2406\n**Récupération**: 2331", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############    Fenrir    #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Fenrir','FeuFenrir']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557221260476678162/LunaticFenrirR_large.jpeg", color=0xffffff)
     embed.set_author(name="#741 Fenrir (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557221260476678162/LunaticFenrirR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%\n**Passif**: Siphon de PV (allies)\n(Dmg +35%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg +35%)\n**PV**: 27015\n**Attaque**: 3058\n**Défense**: 2295\n**Récupération**:2138", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fenrir','EauFenrir','TopFenrir']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555961504497674/LunaticFenrir_large.jpeg", color=0xffffff)
     embed.set_author(name="#743 Fenrir (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555961504497674/LunaticFenrir_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR -15~20%\n**Passif**: Étourdissement 80% 1 tour\n(Dmg +10%, Taux: +10%tour: +1)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 39611\n**Attaque**: 2221\n**Défense**: 1840\n**Récupération**:2058", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fenrir','BoisFenrir']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555970912452608/LunaticFenrirG_large.jpeg", color=0xffffff)
     embed.set_author(name="#745 Fenrir (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555970912452608/LunaticFenrirG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR -15~20%\n**Passif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Sommeil 70% 2 tours\n(Dmg +20%, Taux +20%)\n**PV**: 31496\n**Attaque**: 2036\n**Défense**: 2921\n**Récupération**: 2322", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fenrir','LightFenrir']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555974851035137/LunaticFenrirW_large.jpeg", color=0xffffff)
     embed.set_author(name="#747 Fenrir (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555974851035137/LunaticFenrirW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR -15~20%\n**Passif**: Défense réduite 100% 2 tours\n(Dmg +15%, Taux: +20%)\n**Actif**: Choc 70% 1 tour\n(Dmg +20%, Taux: +20%)\n**PV**: 30730\n**Attaque**: 2607\n**Défense**: 2488\n**Récupération**:2066", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Fenrir','DarkFenrir']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555968890667018/LunaticFenrirD_large.jpeg", color=0xffffff)
     embed.set_author(name="#749 Fenrir (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555968890667018/LunaticFenrirD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR -15~20%\n**Passif**: Traqueur 30%\n(Dmg +20%, Taux: +20%)\n**Actif**: Traqueur 30%\n(Dmg +20%, Taux: +20%)\n**PV**: 29964\n**Attaque**: 3295\n**Défense**: 2509\n**Récupération**:2300", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############  Fenir S Evo  ############
	 #######################################
     
 if any([message.content.startswith (item) for item in ['FeuFenrir','SFenrir','FeuSFenrir']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728599722131457/SuperLunaticFenrirR_large.jpg", color=0xffffff)
     embed.set_author(name="#742 Fenrir SE (Feu)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728599722131457/SuperLunaticFenrirR_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%\n**Passif**: Siphon de PV \n(no skillbooks)\n**Actif**: Siphon de PV , Greatly)\n(no skillbooks)\n**PV**: 29726\n**Attaque**: 3398\n**Défense**: 2533\n**Récupération**: 2356", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['EauFenrir','SFenrir','EauSFenrir']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728594302828554/SuperLunaticFenrir_large.jpg", color=0xffffff)
     embed.set_author(name="#744 Fenrir SE (Eau)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728594302828554/SuperLunaticFenrir_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR -15~20%\n**Passif**: Étourdissement 80% 1 tour\n(no skillbooks)\n**Actif**: Pétrification 80% 1 tour\n(no skillbooks)\n**PV**: 43737\n**Attaque**: 2446\n**Défense**: 2024\n**Récupération**: 2269", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['BoisFenrir','SFenrir','BoisSFenrir']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728597876375552/SuperLunaticFenrirG_large.jpg", color=0xffffff)
     embed.set_author(name="#746 Fenrir SE (Bois)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728597876375552/SuperLunaticFenrirG_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR -15~20%\n**Passif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Sommeil 70% 2 tours\n(Dmg +20%, Taux +20%)\n**PV**: 34646\n**Attaque**: 2486\n**Défense**: 3248\n**Récupération**: 2336", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['LightFenrir','SFenrir','LightSFenrir']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728601361973248/SuperLunaticFenrirW_large.jpg", color=0xffffff)
     embed.set_author(name="#748 Fenrir SE (light)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728601361973248/SuperLunaticFenrirW_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR -15~20%\n**Passif**: Défense réduite 100% 2 tours\n(no skillbooks)\n**Actif**: Choc 70% 1 tour\n(no skillbooks)\n**PV**: 33828\n**Attaque**: 2876\n**Défense**: 2745\n**Récupération**: 2282", inline=False)
     
     await message.channel.send(embed=embed)
	
 if any([message.content.startswith (item) for item in ['DarkFenrir','SFenrir','DarkSFenrir']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728596160905218/SuperLunaticFenrirD_large.jpg", color=0xffffff)
     embed.set_author(name="#701 Fenrir SE (dark)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728596160905218/SuperLunaticFenrirD_large.jpg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%\n**Passif**: Traqueur 30%\n(no skillbooks)\n**Actif**: Traqueur 30%\n(no skillbooks)\n**PV**: 29971\n**Attaque**: 3330\n**Défense**: 2520\n**Récupération**: 2309", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############     Lupio    #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Lupio','LightLupio']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552319598854144/CanisW_large.jpeg", color=0xffffff)
     embed.set_author(name="#754 Lupio (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552319598854144/CanisW_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35% (ToC)\n**Passif**: Brise-Bonus 100%\n(Dmg: +35%)\n**Actif**: Choc 80% 1 tour\n(Dmg: +20% Taux: +15%)\n**PV**: 28731\n**Attaque**: 1873\n**Défense**: 2765\n**Récupération**: 1342", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content.startswith (item) for item in ['Lupio','DarkLupio']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552318323654666/Canis_large.jpeg", color=0xffffff)
     embed.set_author(name="#755 Lupio (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552318323654666/Canis_large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Att +30~35% (ToC)\n**Passif**: Agression (PV)\n(Dmg: +35%)\n**Actif**: Agression (PV)\n(Dmg: +35%)\n**PV**: 35817\n**Attaque**: 1676\n**Défense**: 1996\n**Récupération**: 1295", inline=False)
     
     await message.channel.send(embed=embed)
     	 
	 #######################################
	 ############    Lombrix   #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Lombrix','FeuLombrix']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554864539074560/HorntailR_large.jpeg", color=0xffffff)
     embed.set_author(name="#756 Lombrix (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554864539074560/HorntailR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Resist +10~15%\n**Passif**: Étourdissement 50% 1 tour\n(No skillbooks)\n**Actif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**PV**: 34898\n**Attaque**: 1404\n**Défense**: 1445\n**Récupération**:1758", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Lombrix','EauLombrix']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554862555168778/HorntailB_large.jpeg", color=0xffffff)
     embed.set_author(name="#757 Lombrix (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554862555168778/HorntailB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Resist +10~15%\n**Passif**: Nécrose 50% 2 tours\n(No skillbooks)\n**Actif**: Pétrification 80% 1 tour\n(No skillbooks)\n**PV**: 37792\n**Attaque**: 1132\n**Défense**: 1853\n**Récupération**:1363", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Lombrix','BoisLombrix']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554860990562325/Horntail_large.jpeg", color=0xffffff)
     embed.set_author(name="#758 Lombrix (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554860990562325/Horntail_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Resist +10~15%\n**Passif**: Attaque réduite 60% 2 tour\n(No skillbooks)\n**Actif**: Récupération réduite 80% 2 tours\n(No skillbooks)\n**PV**: 25742\n**Attaque**: 2281\n**Défense**: 1525\n**Récupération**:1607", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############    Poulpo    #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Poulpo','FeuPoulpo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561157995495449/WumewraR_large.jpeg", color=0xffffff)
     embed.set_author(name="#761 Poulpo (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561157995495449/WumewraR_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Feu Chasseur 50%\n(No skillbooks)\n**Actif**: Nécrose 40% 2 tours\n(No skillbooks)\n**PV**: 28377\n**Attaque**: 1696\n**Défense**: 2615\n**Récupération**:1219", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Poulpo','EauPoulpo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561154195456020/Wumewra_large.jpeg", color=0xffffff)
     embed.set_author(name="#762 Poulpo (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561154195456020/Wumewra_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Chasseur (eau) 50%\n(No skillbooks)\n**Actif**: Soif 40% -10% 1 tour\n(No skillbooks)\n**PV**: 28561\n**Attaque**: 1737\n**Défense**: 2404\n**Récupération**:1287", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Poulpo','BoisPoulpo']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561155378380801/WumewraG_large.jpeg", color=0xffffff)
     embed.set_author(name="#763 Poulpo (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561155378380801/WumewraG_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: PV +20~25%\n**Passif**: Chasseur (bois) 50%\n(No skillbooks)\n**Actif**: Pétrification 40% 1 tour\n(No skillbooks)\n**PV**: 35838\n**Attaque**: 1275\n**Défense**: 1751\n**Récupération**:1574", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############    Yaksha    #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Yak','FeuYak','TopYak']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555400504016906/Kubera_large.jpeg", color=0xffffff)
     embed.set_author(name="#766 Yaksha (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555400504016906/Kubera_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Attaque réduite 80% 2 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Aveuglement 70% 3 tours\n(Dmg +10%, Taux: +30%)\n**PV**: 30093\n**Attaque**: 2322\n**Défense**: 3037\n**Récupération**:1852", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yak','EauYak','TopYak']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555403435573261/KuberaB_large.jpeg", color=0xffffff)
     embed.set_author(name="#767 Yaksha (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555403435573261/KuberaB_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Traqueur 30%\n(Dmg +15%, Taux: +20%)\n**Actif**: Traqueur 30%\n(Dmg +10%, Taux: +20%)\n**PV**: 29589\n**Attaque**: 3153\n**Défense**: 2152\n**Récupération**:1982", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yak','BoisYak']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555467264491551/KuberaG_large.jpeg", color=0xffffff)
     embed.set_author(name="#768 Yaksha (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555467264491551/KuberaG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Sommeil (On crit) 2 tours\n(Dmg +30%)\n**Actif**: Chasseur 50%\n(Dmg +30%)\n**PV**: 29869\n**Attaque**: 3126\n**Défense**: 2125\n**Récupération**:2002", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yak','LightYak']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555468766052404/KuberaW_large.jpeg", color=0xffffff)
     embed.set_author(name="#769 Yaksha (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555468766052404/KuberaW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Défense réduite 70% 3 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Prédateur 30%\n(Dmg +30%)\n**PV**: 26559\n**Attaque**: 3269\n**Défense**: 2084\n**Récupération**:2193", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yak','DarkYak']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555464580399104/KuberaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#770 Yaksha (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555464580399104/KuberaD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Silence 80% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 30696\n**Attaque**: 2641\n**Défense**: 2542\n**Récupération**:2331", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############     Yeti     #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Yeti','FeuYeti']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772034028252954635/Yeti1.png", color=0xffffff)
     embed.set_author(name="#771 Yeti (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772034028252954635/Yeti1.png")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%,(Donjons)\n**Passif**: Chasseur 40%\n(Dmg +25%)\n**Actif**: Aveuglement 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 28200\n**Attaque**: 2785\n**Défense**: 1614\n**Récupération**:1682", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yeti','EauYeti','TopYeti']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772034031234842624/Yeti2.png", color=0xffffff)
     embed.set_author(name="#772 Yeti (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772034031234842624/Yeti2.png")
     embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45% (Donjons)\n**Passif**: Attaque réduite 60% 2 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 28840\n**Attaque**: 1989\n**Défense**: 2581\n**Récupération**:1457", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yeti','BoisYeti']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558664381366283/SasquatchG_Large.jpeg", color=0xffffff)
     embed.set_author(name="#773 Yeti (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558664381366283/SasquatchG_Large.jpeg")
     embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +40~45%(Donjons)\n**Passif**: Provocation 80% 1 tour\n(Dmg +15%, tour: +1)\n**Actif**: Nécrose x2 60% 1 tours\n(Dmg +20%, tour: +1)\n**PV**: 33434\n**Attaque**: 1894\n**Défense**: 1976\n**Récupération**:1499", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yeti','LightYeti']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558670659977266/SasquatchW_Large.jpeg", color=0xffffff)
     embed.set_author(name="#774 Yeti (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558670659977266/SasquatchW_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%(Donjons)\n**Passif**: Boost de moral 30%\n(Dmg +25%)\n**Actif**: Choc 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 28241\n**Attaque**: 2418\n**Défense**: 3133\n**Récupération**:1941", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yeti','DarkYeti']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558628142448642/SasquatchD_Large.jpeg", color=0xffffff)
     embed.set_author(name="#775 Yeti (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558628142448642/SasquatchD_Large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45%(Donjons)\n**Passif**: Étourdissement 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Sceau 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 35245\n**Attaque**: 2192\n**Défense**: 2134\n**Récupération**:2025", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############     Yuki     #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Yuki','FeuYuki','TopYuki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561323419107342/YukiR_large.jpeg", color=0xffffff)
     embed.set_author(name="#776 Yuki (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561323419107342/YukiR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +30%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 26947\n**Attaque**: 3105\n**Défense**: 2240\n**Récupération**:2118", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yuki','EauYuki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561274509197332/Yuki_large.jpeg", color=0xffffff)
     embed.set_author(name="#778 Yuki (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561274509197332/Yuki_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Nécrose x2 70% 1 tour\n(Taux: +25%)\n**Actif**: Nécrose x2 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 36982\n**Attaque**: 2024\n**Défense**: 1976\n**Récupération**:2316", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yuki','BoisYuki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561278695243786/YukiG_large.jpeg", color=0xffffff)
     embed.set_author(name="#780 Yuki (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561278695243786/YukiG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Faiblesse exposée 80% 2 tour\n(???)\n**Actif**: Faiblesse exposée 80% 2 tours\n(???)\n**PV**: 28857\n**Attaque**: 2546\n**Défense**: 2345\n**Récupération**:2140", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yuki','LightYuki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561325142966302/YukiW_large.jpeg", color=0xffffff)
     embed.set_author(name="#782 Yuki (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561325142966302/YukiW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Choc 80% 2 Turm\n(???)\n**Actif**: Choc 70% 2 tours\n(???)\n**PV**: 25156\n**Attaque**: 3153\n**Défense**: 2309\n**Récupération**:2138", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Yuki','DarkYuki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559989881831464/SuperYukinaD_large.jpeg", color=0xffffff)
     embed.set_author(name="#785 Yuki (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559989881831464/SuperYukinaD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Dégâts critiques +40~45%\n**Passif**: Siphon de PA 30%\n(Dmg +30%)\n**Actif**: Nécrose x3 80% 1 tour\n(Taux: +20%, tour: +1)\n**PV**: 44023\n**Attaque**: 2603\n**Défense**: 1949\n**Récupération**:2065", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############  Yuki S Evo  #############
	 #######################################

 if any([message.content.startswith (item) for item in ['FeuYuki','SYuki','FeuSYuki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559994025934878/SuperYukinaR_large.jpeg", color=0xffffff)
     embed.set_author(name="#777 Yuki SE (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559994025934878/SuperYukinaR_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Dégâts critiques +40~45%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +30%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 29651\n**Attaque**: 3446\n**Défense**: 2472\n**Récupération**:2336", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['EauYuki','SYuki','EauSYuki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559987629490176/SuperYukina_large.jpeg", color=0xffffff)
     embed.set_author(name="#779 Yuki SE (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559987629490176/SuperYukina_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Dégâts critiques +40~45%\n**Passif**: Nécrose x2 70% 1 tour\n(Taux: +25%)\n**Actif**: Nécrose x2 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 40849\n**Attaque**: 2228\n**Défense**: 2174\n**Récupération**:2548", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['BoisYuki','SYuki','BoisSYuki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559992348213268/SuperYukinaG_large.jpeg", color=0xffffff)
     embed.set_author(name="#781 Yuki SE (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559992348213268/SuperYukinaG_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Dégâts critiques +40~45%\n**Passif**: Faiblesse exposée 80% 2 tour\n(???)\n**Actif**: Faiblesse exposée 80% 2 tours\n(???)\n**PV**: 31764\n**Attaque**: 2808\n**Défense**: 2589\n**Récupération**:2364", inline=False)
     
     await message.channel.send(embed=embed)
	 
 if any([message.content.startswith (item) for item in ['LightYuki','SYuki','LightSYuki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560018860408842/SuperYukinaW_large.jpeg", color=0xffffff)
     embed.set_author(name="#783 Yuki SE (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560018860408842/SuperYukinaW_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Dégâts critiques +40~45%\n**Passif**: Choc 80% 2 Turm\n(???)\n**Actif**: Choc 70% 2 tours\n(???)\n**PV**: 27676\n**Attaque**: 3500\n**Défense**: 2547\n**Récupération**:2356", inline=False)
     
     await message.channel.send(embed=embed)
	 
 if any([message.content.startswith (item) for item in ['DarkYuki','SYuki','DarkSYuki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561270834987008/YukiD_large.jpeg", color=0xffffff)
     embed.set_author(name="#784 Yuki SE (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561270834987008/YukiD_large.jpeg")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Siphon de PA 30%\n(Dmg +30%)\n**Actif**: Nécrose x3 80% 1 tour\n(Taux: +20%, tour: +1)\n**PV**: 39869\n**Attaque**: 2364\n**Défense**: 1772\n**Récupération**:1874", inline=False)
     
     await message.channel.send(embed=embed)	 

	 #######################################
	 ############     Zarid    #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Zari','FeuZari']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561371620048896/Zalisk_large.jpeg", color=0xffffff)
     embed.set_author(name="#786 Zarid (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561371620048896/Zalisk_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: PV +20~25%\n**Passif**: Sommeil 60% 1 tour\n(No skillbooks)\n**Actif**: Fatigue 80% 2 tours\n(No skillbooks)\n**PV**: 22514\n**Attaque**: 2574\n**Défense**: 1539\n**Récupération**:1403", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Zari','EauZari']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561373020946433/ZaliskB_large.jpeg", color=0xffffff)
     embed.set_author(name="#787 Zarid (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561373020946433/ZaliskB_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Pétrification 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 80% 2 tours\n(No skillbooks)\n**PV**: 29092\n**Attaque**: 1321\n**Défense**: 2540\n**Récupération**:1641", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Zari','BoisZari']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561378267758622/ZaliskG_large.jpeg", color=0xffffff)
     embed.set_author(name="#788 Zarid (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561378267758622/ZaliskG_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: PV +20~25%\n**Passif**: Étourdissement 50% 1 tour\n(No skillbooks)\n**Actif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**PV**: 28054\n**Attaque**: 1879\n**Défense**: 1725\n**Récupération**:1555", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Zari','LightZari']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561380318773250/ZaliskW_large.jpeg", color=0xffffff)
     embed.set_author(name="#789 Zarid (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561380318773250/ZaliskW_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: PV +20~25%\n**Passif**: Défense réduite 40% 2 tours\n(No skillbooks)\n**Actif**: Sommeil 60% 1 tour\n(No skillbooks)\n**PV**: 35375\n**Attaque**: 1554\n**Défense**: 1758\n**Récupération**:1329", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Zari','DarkZari']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561376040845332/ZaliskD_large.jpeg", color=0xffffff)
     embed.set_author(name="#790 Zarid (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561376040845332/ZaliskD_large.jpeg")
     embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: PV +20~25%\n**Passif**: Nécrose 40% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 80% 2 tours\n(No skillbooks)\n**PV**: 26041\n**Attaque**: 2343\n**Défense**: 1566\n**Récupération**:1403", inline=False)
     
     await message.channel.send(embed=embed)

	 #######################################
	 ############   Zhu Bajie  #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Zhu','FeuZhu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/608737954910830613/Zhu3EvoR_large.jpg", color=0xffffff)
     embed.set_author(name="#791 Zhu Bajie  (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/608737954910830613/Zhu3EvoR_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%\n**Passif**: Prédateur 40%\n(Dmg: +25% )\n**Actif**: Prédateur 40%\n(Dmg: +25% )\n**PV**: 35201\n**Attaque**: 3664\n**Défense**: 2390\n**Récupération**:2663", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Zhu','EauZhu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553821356818483/Zhu3EvoB_large.jpg", color=0xffffff)
     embed.set_author(name="#792 Zhu Bajie  (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553821356818483/Zhu3EvoB_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%\n**Passif**: Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(Dmg: +20% Taux: +10%)\n**Actif**: Étourdissement 80% 2 tours\n(Dmg: +15% Taux: +15%)\n**PV**: 29971\n**Attaque**: 2860\n**Défense**: 3848\n**Récupération**:2574", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Zhu','BoisZhu','TopZhu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557222726306365449/Zhu3Evo_large.jpg", color=0xffffff)
     embed.set_author(name="#793 Zhu Bajie  (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557222726306365449/Zhu3Evo_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%\n**Passif**: Frappe Courageuse\n(Dmg: +20%)\n**Actif**: Aveuglement 80% 3 tours\n(Dmg: +20% Taux: +10%)\n**PV**: 29596\n**Attaque**: 2928\n**Défense**: 3943\n**Récupération**:2581", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Zhu','LightZhu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/608737957133942818/Zhu3EvoW_large.jpg", color=0xffffff)
     embed.set_author(name="#794 Zhu Bajie  (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/608737957133942818/Zhu3EvoW_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%\n**Passif**: Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 29521\n**Attaque**: 2813\n**Défense**: 3957\n**Récupération**:2622", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Zhu','DarkZhu']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553822174838814/Zhu3EvoD_large.jpg", color=0xffffff)
     embed.set_author(name="#795 Zhu Bajie  (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553822174838814/Zhu3EvoD_large.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%\n**Passif**: Agression (PV)\n(Dmg: +25% )\n**Actif**: Agression (PV)\n(Dmg: +25% )\n**PV**: 51998\n**Attaque**: 2548\n**Défense**: 2786\n**Récupération**:2902", inline=False)
     
     await message.channel.send(embed=embed)

	 #######################################
	 ############     Enkidu   #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Enki','FeuEnki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707146670273462312/Enkidu3EvoR.png", color=0xffffff)
     embed.set_author(name="#800 Enkidu  (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707146670273462312/Enkidu3EvoR.png")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense +40~45%\n**Passif**: Siphon de PV\n**Actif**: Sommeil 100% 1 tour\n**PV**: 29392\n**Attaque**: 3596\n**Défense**: 2343\n**Récupération**:2125", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Enki','EauEnki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707146663449591838/Enkidu3Evo.png", color=0xffffff)
     embed.set_author(name="#801 Enkidu  (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707146663449591838/Enkidu3Evo.png")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense +40~45%\n**Passif**: Attaque réduite 80% - 2 tours\n**Actif**: Chasseur 50%\n**PV**: 26089\n**Attaque**: 3909\n**Défense**: 2683\n**Récupération**:2023", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Enki','BoisEnki','TopEnki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707146659339042867/EnkiB.png", color=0xffffff)
     embed.set_author(name="#802 Enkidu  (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707146659339042867/EnkiB.png")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Défense +40~45%\n**Passif**: Frappe courageuse\n**Actif**: Réduction dégâts- 2 tours\n**PV**: 31466\n**Attaque**: 3036\n**Défense**: 2842\n**Récupération**:2433", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Enki','LightEnki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707146672807084082/Enkidu3EvoW.png", color=0xffffff)
     embed.set_author(name="#803 Enkidu  (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707146672807084082/Enkidu3EvoW.png")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense +40~45%\n**Passif**: Affaiblissement 80% - 2 tours\n**Actif**: Frappe courageuse\n**PV**: 27798\n**Attaque**: 3534\n**Défense**: 2629\n**Récupération**:1852", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Enki','DarkEnki']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707146667006230588/Enkidu3EvoD.png", color=0xffffff)
     embed.set_author(name="#804 Enkidu  (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707146667006230588/Enkidu3EvoD.png")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense +40~45%\n**Passif**: Chasseur 50%\n**Actif**: Persévérance\n**PV**: 26927\n**Attaque**: 3596\n**Défense**: 2431\n**Récupération**:1880", inline=False)
     
     await message.channel.send(embed=embed)

	 #######################################
	 ############    Griffon   #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Griffon','FeuGriffon']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177698266710046/20200505_122858.jpg", color=0xffffff)
     embed.set_author(name="#805 Griffon  (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177698266710046/20200505_122858.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Attaque +40~45%\n**Passif**: Agression (Def)\n**Actif**: Agression (Def)\n**PV**: 35991\n**Attaque**: 2159\n**Défense**: 3936\n**Récupération**:2254", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Griffon','EauGriffon','TopGriffon']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177698027503626/20200505_122844.jpg", color=0xffffff)
     embed.set_author(name="#806 Griffon  (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177698027503626/20200505_122844.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Attaque +40~45%\n**Passif**: Contre attaque 100%\n**Actif**: Agression (PV)\n**PV**: 41647\n**Attaque**: 2603\n**Défense**: 2658\n**Récupération**:2725", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Griffon','BoisGriffon']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177698501328976/20200505_122915.jpg", color=0xffffff)
     embed.set_author(name="#807 Griffon  (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177698501328976/20200505_122915.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Attaque +40~45%\n**Passif**: Prédateur 40%\n**Actif**: Prédateur 50%\n**PV**: 28922\n**Attaque**: 3977\n**Défense**: 2595\n**Récupération**:2349", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Griffon','LightGriffon']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177698820227112/20200505_122929.jpg", color=0xffffff)
     embed.set_author(name="#808 Griffon  (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177698820227112/20200505_122929.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Attaque +40~45%\n**Passif**: Boost de moral 50% PA\n**Actif**: Résistance réduite 100% - 2 tours\n**PV**: 33372\n**Attaque**: 3084\n**Défense**: 2842\n**Récupération**:2345", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Griffon','DarkGriffon']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177699151708170/20200505_122942.jpg", color=0xffffff)
     embed.set_author(name="#809 Griffon  (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177699151708170/20200505_122942.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Attaque +40~45%\n**Passif**: Chasseur 40%\n**Actif**: Chasseur 50%\n**PV**: 27792\n**Attaque**: 3548\n**Défense**: 2513\n**Récupération**:2513", inline=False)
     
     await message.channel.send(embed=embed)

	 #######################################
	 ############   Arlequin   #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Arle','FeuArle']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707159778035761223/Clown3EvoR.png", color=0xffffff)
     embed.set_author(name="#810 Arlequin  (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707159778035761223/Clown3EvoR.png")
     embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégats critiques +40~45%\n**Passif**: Soif 80% - 2 tours\n**Actif**: Attaque réduite 60% - 2 tours\n**PV**: 40809\n**Attaque**: 2051\n**Défense**: 1887\n**Récupération**:1976", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Arle','EauArle','TopArle']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707159771790180423/Clown3EvoB.png", color=0xffffff)
     embed.set_author(name="#811 Arlequin  (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707159771790180423/Clown3EvoB.png")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégats critiques +40~45%\n**Passif**: Frappe courageuse (Crit)\n**Actif**: Attaque réduite 80% - 2 tours (Crit)\n**PV**: 29593\n**Attaque**: 2730\n**Défense**: 2399\n**Récupération**:1766", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Arle','BoisArle']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707159775020056606/Clown3EvoG.png", color=0xffffff)
     embed.set_author(name="#812 Arlequin  (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707159775020056606/Clown3EvoG.png")
     embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégats critiques +40~45%\n**Passif**: Siphon PA 20%\n**Actif**: Petrification 80% - 1 tour\n**PV**: 30846\n**Attaque**: 2389\n**Défense**: 2556\n**Récupération**:2433", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Arle','LightArle']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707159781177294919/Clown3EvoW.png", color=0xffffff)
     embed.set_author(name="#813 Arlequin  (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707159781177294919/Clown3EvoW.png")
     embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégats critiques +40~45%\n**Passif**: Réduction dégâts 50% - 1 tour\n**Actif**: Provocation intrépide 80% - 1 tour\n**PV**: 30713\n**Attaque**: 2070\n**Défense**: 3173\n**Récupération**:2091", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Arle','DarkArle']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707159765490597939/Clown3Evo.png", color=0xffffff)
     embed.set_author(name="#814 Arlequin  (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707159765490597939/Clown3Evo.png")
     embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégats critiques +40~45%\n**Passif**: Avantage élementaire (Crit)\n**Actif**: Prédateur 40%\n**PV**: 27063\n**Attaque**: 3194\n**Défense**: 2043\n**Récupération**:1954", inline=False)
     
     await message.channel.send(embed=embed)

	 #######################################
	 ############  Gilgamesh   #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Gilg','FeuGilg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177696396050462/20200505_122711.jpg", color=0xffffff)
     embed.set_author(name="#815 Gilgamesh  (feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177696396050462/20200505_122711.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense réduite 35/40%\n**Passif**: Étourdissement 100% - 1 tour\n**Actif**: Siphon PV\n**PV**:  29058\n**Attaque**: 3936\n**Défense**: 2635\n**Récupération**: 2384", inline=False)
     
     await message.channel.send(embed=embed)
	  
 if any([message.content.startswith (item) for item in ['Gilg','EauGilg','TopGilg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177696693583872/20200505_122730.jpg", color=0xffffff)
     embed.set_author(name="#816 Gilgamesh  (eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177696693583872/20200505_122730.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Défense réduite 35/40%\n**Passif**: Affaiblissement 70% - 2 tours\n**Actif**: Frappe courageuse\n**PV**: 31139\n**Attaque**:  3070\n**Défense**: 2821\n**Récupération**:2535", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Gilg','BoisGilg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177696916013186/20200505_122743.jpg", color=0xffffff)
     embed.set_author(name="#817 Gilgamesh  (bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177696916013186/20200505_122743.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense réduite 35/40%\n**Passif**: Prédateur 50%\n**Actif**: Persévérance\n**PV**: 28336\n**Attaque**: 3814\n**Défense**: 2806\n**Récupération**:2418", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Gilg','LightGilg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177697188642846/20200505_122802.jpg", color=0xffffff)
     embed.set_author(name="#818 Gilgamesh  (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177697188642846/20200505_122802.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Défense réduite 35/40%\n**Passif**: Frappe courageuse\n**Actif**: Attaque augmentée - 2 tours\n**PV**: 33243\n**Attaque**: 3111\n**Défense**: 3080\n**Récupération**:2583", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Gilg','DarkGilg']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177697796948058/20200505_122819.jpg", color=0xffffff)
     embed.set_author(name="#819 Gilgamesh  (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177697796948058/20200505_122819.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense réduite 35/40%\n**Passif**: Vague martiale 20%\n**Actif**: Perforation 90% def ennemie\n**PV**: 28970\n**Attaque**: 3902\n**Défense**: 2670\n**Récupération**:2091", inline=False)
     
     await message.channel.send(embed=embed)

	 #######################################
	 ##########  Imperio Armani    #########
	 #######################################

 if any([message.content.startswith (item) for item in ['Imper','LightImper']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707238669706330122/20200505_163013.jpg", color=0xffffff)
     embed.set_author(name="#820 Imperio  (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707238669706330122/20200505_163013.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**:  Attaque ennemie -35/40%\n**Passif**: Vague martiale 10%\n**Actif**: Choc - 60% - 2 tours\n**PV**: 30073\n**Attaque**: 2704\n**Défense**: 3616\n**Récupération**:2247", inline=False)
     
     await message.channel.send(embed=embed)
	 
 if any([message.content.startswith (item) for item in ['Imper','DarkImper']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707238669513130004/20200505_162949.jpg", color=0xffffff)
     embed.set_author(name="#821 Imperio  (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707238669513130004/20200505_162949.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**:  Attaque ennemie -35/40%\n**Passif**: Vague martiale - 10%\n**Actif**: Chasseur - 40%\n**PV**: 28421\n**Attaque**: 4004\n**Défense**: 2670\n**Récupération**:2322", inline=False)
     
     await message.channel.send(embed=embed)

	 #######################################
	 ############     Shark    #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Shark','LightShark']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/707241241716195428/3181164-6019923722-baby-.png", color=0xffffff)
     embed.set_author(name="#822 Shark  (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/707241241716195428/3181164-6019923722-baby-.png")
     embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**:  PV +30-35% (light)\n**Passif**: Attaque réduite 70% - 1 tour\n**Actif**: Attaque augmentée - 2 tours\n**PV**: 30345\n**Attaque**: 1941\n**Défense**: 1989\n**Récupération**:2881", inline=False)
     
     await message.channel.send(embed=embed)

	 #######################################
	 ############      Pip     #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Pip','FeuPip']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731543372451282976/PipF.png", color=0xffffff)
     embed.set_author(name="#823 Pip (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731543372451282976/PipF.png")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30% (Donjons)\n**Passif**: Résistance réduite 100% 2 tours\n(Dmg +25%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 25027\n**Attaque**: 1989\n**Défense**: 2751\n**Récupération**:1512", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pip','EauPip']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731543367405535242/PipE.png", color=0xffffff)
     embed.set_author(name="#824 Pip (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731543367405535242/PipE.png")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30% (Donjons)\n**Passif**: Sommeil 80% 1 tour\n(Dmg +20%, Taux: +10%, +1 tour)\n**Actif**: Prédateur 30%\n(Dmg +20%, Taux: +10%)\n**PV**: 26416\n**Attaque**: 2813\n**Défense**: 2050\n**Récupération**:1512", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pip','BoisPip']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731543362473164870/PipB.png", color=0xffffff)
     embed.set_author(name="#825 Pip (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731543362473164870/PipB.png")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30% (Donjons)\n**Passif**: Chasseur 50%\n(Dmg +30%)\n**Actif**: Avantage élémentaire\n(Dmg +25%)\n**PV**: 24496\n**Attaque**: 2956\n**Défense**: 2036\n**Récupération**:1437", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pip','LightPip']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731541471747899593/lightp.png", color=0xffffff)
     embed.set_author(name="#826 Pip (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731541471747899593/lightp.png")
     embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30% (Donjons)\n**Passif**: Siphon de PA\n(Dmg +20%, Taux: +5%)\n**Actif**: Prédateur 40%\n(Dmg +20%, Taux: +10%)\n**PV**: 27628\n**Attaque**: 3255\n**Défense**: 2390\n**Récupération**:1818", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Pip','DarkPip']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731540053687533608/Darkp.png", color=0xffffff)
     embed.set_author(name="#827 Pip (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731540053687533608/Darkp.png")
     embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: PV +30% (Donjons)\n**Passif**: Vague martiale 20% de ses PV et PA\n(Dmg +30%)\n**Actif**: Nécrose x3 80% 1 tour\n(Dmg +20%, Taux: +20%)\n**PV**: 31091\n**Attaque**: 2607\n**Défense**: 2386\n**Récupération**:1773", inline=False)
     
     await message.channel.send(embed=embed)

	 #######################################
	 ############   Cernunnos  #############
	 #######################################

 if any([message.content.startswith (item) for item in ['Cern','FeuCern']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/758071281219272775/758687793529880636/Screenshot_20200924-155113_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#828 Cernunnos  (Feu)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/758071281219272775/758687793529880636/Screenshot_20200924-155113_Monster_Super_League.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Defenseur\n**Lead**: Défense réduite 35/40%\n**Passif**: Affaiblissement 70% 2 tours\n**Actif**: Attaque augmentée 3 tours\n**PV**: 27744\n**Attaque**: 2840\n**Défense**: 3432\n**Récupération**:2424", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Cern','EauCern']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/758071281219272775/758687793802248222/Screenshot_20200924-155142_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#829 Cernunnos  (Eau)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/758071281219272775/758687793802248222/Screenshot_20200924-155142_Monster_Super_League.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Défense réduite 35/40%\n**Passif**: Siphon de PA 30%\n**Actif**: Domination 3 tours\n**PV**: 41306\n**Attaque**: 2534\n**Défense**: 2364\n**Récupération**:2466", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Cern','BoisCern']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/758071281219272775/758687793974607882/Screenshot_20200924-155212_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#830 Cernunnos  (Bois)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/758071281219272775/758687793974607882/Screenshot_20200924-155212_Monster_Super_League.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Défense réduite 35/40%\n**Passif**: Nécrose x3 100% 1 tour\n**Actif**: Volonté immortelle 4 tours\n**PV**: 31513\n**Attaque**: 3145\n**Défense**: 2815\n**Récupération**:3033", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Cern','LightCern']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/758071281219272775/758687794184192060/Screenshot_20200924-155237_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#831 Cernunnos  (light)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/758071281219272775/758687794184192060/Screenshot_20200924-155237_Monster_Super_League.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense réduite 35/40%\n**Passif**: Frappe courageuse\n**Actif**: Bouclier basé sur l'attaque 3 tours\n**PV**: 27689\n**Attaque**: 3718\n**Défense**: 2424\n**Récupération**:3044", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Cern','DarkCern']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/758071281219272775/758687794343444480/Screenshot_20200924-155305_Monster_Super_League.jpg", color=0xffffff)
     embed.set_author(name="#832 Cernunnos  (dark)")
     embed.set_thumbnail(url="https://media.discordapp.net/attachments/758071281219272775/758687794343444480/Screenshot_20200924-155305_Monster_Super_League.jpg")
     embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Défense réduite 35/40%\n**Passif**: Traqueur 50%\n**Actif**: Volonté immortelle 4 tours\n**PV**: 28541\n**Attaque**: 3807\n**Défense**: 2629\n**Récupération**:3180", inline=False)
     
     await message.channel.send(embed=embed)

	 #######################################
	 ############   Jormungandr  ###########
	 #######################################

 if any([message.content.startswith (item) for item in ['Jorm','FeuJorm']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772032243219824660/Jormungandfeu.png", color=0xffffff)
     embed.set_author(name="#828 Jormungandr  (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772032243219824660/Jormungandfeu.png")
     embed.add_field(name="★★★★★", value="**Type**: Defenseur\n**Lead**: Résistance -20/25%\n**Passif**: Boost de moral 50% PA\n(Dmg: +20%, effet: +10%)\n**Actif**: Taux critique augmenté (Alliés))\n(Dmg: +20%, +1 tour)\n**PV**: 29773\n**Attaque**: 2901\n**Défense**: 3902\n**Récupération**:2418", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jorm','EauJorm']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772032302255308840/Jormungandeau.png", color=0xffffff)
     embed.set_author(name="#829 Jormungandr  (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772032302255308840/Jormungandeau.png")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Résistance -20/25%\n**Passif**: Bouclier proportionnel à l'attaque 1 tour\n(Dmg: +20%, +1 tour\n**Actif**: Malédiction x2 2 tours\n(Dmg: +20%, +1 tour)\n**PV**: 27676\n**Attaque**: 3773\n**Défense**: 2758\n**Récupération**:2411", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jorm','BoisJorm']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772032329203449857/Jormungandbois.png", color=0xffffff)
     embed.set_author(name="#830 Jormungandr  (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772032329203449857/Jormungandbois.png")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Résistance -20/25%\n**Passif**: Boost de moral 40% PA\n(Dmg: 20%, effet: +10%)\n**Actif**: Nécrose x2 90% 2 tours\n(Dmg: +20%, effet: +10%)\n**PV**: 40557\n**Attaque**: 2494\n**Défense**: 2466\n**Récupération**:2555", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jorm','LightJorm']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772032370911346709/Jormungandlight.png", color=0xffffff)
     embed.set_author(name="#831 Jormungandr  (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772032370911346709/Jormungandlight.png")
     embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Résistance -20/25%\n**Passif**: Vague martiale 10% PA\n(Dmg: +25%)\n**Actif**: Nécrose x3 90% 2 tours\n(Dmg: +20%, effet: +10%)\n**PV**: 46938\n**Attaque**: 2391\n**Défense**: 2637\n**Récupération**:2568", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['Jorm','DarkJorm']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772032350568579082/Jormunganddark.png", color=0xffffff)
     embed.set_author(name="#832 Jormungandr  (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772032350568579082/Jormunganddark.png")
     embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Résistance -20/25%\n**Passif**: Frappe courageuse\n(Dmg: +20%)\n**Actif**: Défense réduite 80% 3 tours\n(Dmg: +20%, effet: +10%)\n**PV**: 27901\n**Attaque**: 3739\n**Défense**: 2547\n**Récupération**:2377", inline=False)
     
     await message.channel.send(embed=embed)

	 #######################################
	 ############     Ushen    #############
	 #######################################
	 
 if any([message.content ==(item) for item in ['Ushen','Ush']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/707567850033905704/zeus.jpg", color=0x000000)
     embed.set_author(name="#999 Ushen (Super Light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/707567850033905704/zeus.jpg")
     embed.add_field(name="★★★★★★", value="**Type**: Dieu\n**Lead**: Lanceur d'éclairs\n**Passif**: Frappe courageuse\n**Actif**: Frappe courageuse\n**PV**: ∞\n**Attaque**: ∞\n**Défense**: ∞\n**Récupération**:∞", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############    Requine   #############
	 #######################################

 if any([message.content ==(item) for item in ['Requinou']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707684198860980224/36ea1344f60d1a4e5eea3df91fd2b4f9.jpg", color=0x000000)
     embed.set_author(name="#998 Requine (Requinou)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707684198860980224/36ea1344f60d1a4e5eea3df91fd2b4f9.jpg")
     embed.add_field(name="★★★★★★", value="**Type**: Chef de gang\n**Lead**:  Tsunami (+100% Popularité)\n**Passif**: Frappe courageuse\n**Actif**: Frappe courageuse\n**PV**: 99999\n**Attaque**: 9999\n**Défense**: 9999\n**Récupération**:9999", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############ Ange Gardien #############
	 #######################################

 if any([message.content ==(item) for item in ['Angegardien','Ange']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/744464233290530866/IMG-20191024-WA0000.jpg", color=0x000000)
     embed.set_author(name="#997 Angegardien (Ange)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/744464233290530866/IMG-20191024-WA0000.jpg")
     embed.add_field(name="★★★★★★", value="**Type**: Immortel\n**Lead**: Griffes poison\n**Passif**: Frappe courageuse\n**Actif**: Frappe courageuse\n**PV**: ∞\n**Attaque**: ∞\n**Défense**: ∞\n**Récupération**:∞", inline=False)
     
     await message.channel.send(embed=embed)
	 
	 #######################################
	 ############     Horo     #############
	 #######################################

 if any([message.content ==(item) for item in ['Horo','Horotopia']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/744484203957190716/Horo2.jpg", color=0x000000)
     embed.set_author(name="#996 Horotopia (Félin)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/744484203957190716/Horo2.jpg")
     embed.add_field(name="★★★★★★", value="**Type**: Chat domestique \n**Lead**: Ronrons 100% Affection\n**Passif**: Griffes on crit \n**Actif**: Sommeil 10 tours\n**PV**: ∞\n**Attaque**: ∞\n**Défense**: ∞\n**Récupération**:∞", inline=False)
     
     await message.channel.send(embed=embed)          
	 
	 #######################################
	 ############ Team Requine #############
	 #######################################

 if any([message.content ==(item) for item in ['teamfeurequine','teamtitanrequine']]):
     embed=discord.Embed(title="Requinou team Feu", url="https://media.discordapp.net/attachments/742090719975571536/742464386945515580/Screenshot_20200810-212750_Monster_Super_League.jpg?width=1125&height=703", color=0xfff99e)
     embed.set_image(url="https://media.discordapp.net/attachments/742090719975571536/742464386945515580/Screenshot_20200810-212750_Monster_Super_League.jpg?width=1125&height=703")
     
     await message.channel.send(embed=embed) 

 if any([message.content ==(item) for item in ['teamboisrequine','teamtitanrequine']]):
     embed=discord.Embed(title="Requinou team Bois", url="https://media.discordapp.net/attachments/742090719975571536/742464387440181288/Screenshot_20200810-212755_Monster_Super_League.jpg?width=557&height=348", color=0xfff99e)
     embed.set_image(url="https://media.discordapp.net/attachments/742090719975571536/742464387440181288/Screenshot_20200810-212755_Monster_Super_League.jpg?width=557&height=348")
     
     await message.channel.send(embed=embed) 

 if any([message.content ==(item) for item in ['teameaurequine','teamtitanrequine']]):
     embed=discord.Embed(title="Requinou team Eau", url="https://media.discordapp.net/attachments/742090719975571536/742464387888971856/Screenshot_20200810-212758_Monster_Super_League.jpg?width=557&height=348", color=0xfff99e)
     embed.set_image(url="https://media.discordapp.net/attachments/742090719975571536/742464387888971856/Screenshot_20200810-212758_Monster_Super_League.jpg?width=557&height=348")
     
     await message.channel.send(embed=embed) 
	 
	 #######################################
	 ############ Duplicata ################
	 #######################################

 if any([message.content ==(item) for item in ['eeeeeee','eeeeeee']]):
     embed=discord.Embed(title="", url="", color=0xfff99e)
     embed.set_image(url="")
     
     await message.channel.send(embed=embed) 

 if any([message.content ==(item) for item in ['eeeeee','eeeeee']]):
     embed=discord.Embed(title="", url="", color=0xfff99e)
     embed.set_image(url="")
     
     await message.channel.send(embed=embed)

     #######################################
     ########### Competences ###############
     #######################################

 if any([message.content ==(item) for item in ['Competence','competence','competences','Competences']]):
     embed=discord.Embed(title="", url="", color=0xfff99e)
     embed.set_author(name="")
     embed.set_thumbnail(url="")
     embed.add_field(name="Liste des compétences", value="Adrénaline, Affaiblissement, Agression défense, Agression PV, Attaque augmentée\nAttaque réduite, Avantage élémentaire, Aveuglement, Boost de moral, Bouclier\nBrise bouclier, Brise-bonus, Chasseur, Chasseur d'eau, Chasseur de bois\nChasseur de feu, Chasseur de lumière, Chasseur de ténèbres, Choc, Défense augmentée\nDéfense réduite, Domination, Étourdissement, Faiblesse exposée, Fatigue\nFrappe courageuse, Frappe impitoyable, Frappe indéfectible, Malédiction, Malédiction foudroyante\nNécrose, Perforation, Persévérance, Pétrification, Prédateur, Prédateur d'eau\nPrédateur de bois, Prédateur de feu, Prédateur de lumière, Prédateur de ténèbres\nProvocation, Purification, Récupération augmentée, Récupération réduite, Réduction des dégâts\nSceau, Silence, Siphon de PA, Siphon de PV, Soif, Sommeil, Traqueur d'eau\nTraqueur de bois, Traqueur de feu, Traqueur de feu, Traqueur de ténèbres\nVague martiale, Vengeance, Vigueur, Volonté, Zèle", inline=False)
     
     await message.channel.send(embed=embed)
	 
 if any([message.content.startswith (item) for item in ['Lynsha']]):
     embed=discord.Embed(title="", url="", color=0xffffff)
     embed.set_author(name="Lynsha")
     embed.set_thumbnail(url="")
     embed.add_field(name="@Lynsha,@Lynsha,@Lynsha", value="@Lynsha,@Lynsha,@Lynsha,@Lynsha,@Lynsha,@Lynsha,@Lynsha,@Lynsha,@Lynsha,@Lynsha,@Lynsha", inline=False)
     
     await message.channel.send(embed=embed)	 
	 #######################################
	 ############  Golem  ##################
	 #######################################

 if any([message.content ==(item) for item in ['Golems','Golem']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328050685673503/BossGolemW_large.jpg", color=0xfff99e)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328050685673503/BossGolemW_large.jpg")
     embed.add_field(name=" Golems 1 -> 5 ", value="__**Golem B1** (light)__\nPassif: Défense réduite 60% 2T\nActif: Choc 20% 1T\nPV: 28'548\nAttaque: 571\nDéfense: 878\nRécupération: 1'903\nDommages critiques:  50%\nTaux critique:  20%\nResist0\n\n__**Golem B2** (Eau)__\nPassif: Fatigue 60% 2T\nActif: Petrify 20% 1T\nPV: 30'140\nAttaque: 658\nDéfense: 6'412\nRécupération: 986\nDommages critiques:  50%\nTaux critique:  20%\nResist: 20%\n\n__**Golem B3** (Feu)__\nPassif: Rec down 60% 2T\nActif: Étourdissement 20% 1T\nPV: 36'480\nAttaque: 1'338\nDéfense: 547\nRécupération: 912\nDommages critiques:  50%\nTaux critique:  20%\nResist: 20%\n\n__**Golem B4** (Bois)__\nPassif: Nécrose 80% 2T\nActif: Nécrose 60% 2T\nPV: 200'400\nAttaque: 695\nDéfense: 301\nRécupération: 1'202\nDommages critiques:  50%\nTaux critique:  20%\nResist: 20%\n\n__**Golem B5** (dark)__\nPassif: Attaque réduite 80% 2T\nActif: Silence 60% 1T\nPV: 189'280\nAttaque: 1'092\nDéfense: 983\nRécupération: 1'310\nDommages critiques:  50%\nTaux critique:  20%\nResist: 20%", inline=False)
     
     await message.channel.send(embed=embed)


 if any([message.content ==(item) for item in ['Golems','Golem']]):
     return

 if any([message.content ==(item) for item in ['GB1','GolemB1']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328050685673503/BossGolemW_large.jpg", color=0xfff99e)
     embed.set_author(name="Golem B1 (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328050685673503/BossGolemW_large.jpg")
     embed.add_field(name="⯀ ▲ ⯁ 2~3*", value="Capacité: Invincibilité, Retribution, Régénération\nPassif: Défense réduite 60% 2 tours\nPower: 180%\nActif: Choc 20% 1 tour\nPower: 150%\n50% PV Actif: Attaque réduite 100% 2 tours\nPower: 230%\nPV: 28'548\nAttaque: 571\nDéfense: 878\nRécupération: 1'903\nDommages critiques: 50%\nTaux critique: 20%\nResist: 0%\n\n__Guard sphere__\nPassif: Adrénaline 10% allies PV (on crit)\nActif: Étourdissement 80% 1 tour\nPV: 10015\nAttaque180\nDéfense: 578\nRécupération: 1156\nDommages critiques: 50%\nTaux critique: 50%\nResist: 0%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['GB2','GolemB2']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328035439378432/BossGolemB_large.jpg", color=0xfff99e)
     embed.set_author(name="Golem B2 (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328035439378432/BossGolemB_large.jpg")
     embed.add_field(name="⯁ 2~4*", value="Capacité: Invincibilité, Retribution\nPassif: Fatigue 60% 2 tours\nPower: 150%\nActif: Petrify 20% 1 tour\nPower: 180%\n50% PV Actif: Nécrose x3 100% 2 tours\nPower: 220.%\nPV: 30'140\nAttaque: 658\nDéfense: 6'412\nRécupération: 986\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%\n\n__Guard sphere__\nPassif: Provocation 20% 1 tour\nActif: Nécrose 100% 2 tours\nPV: 15860\nAttaque190\nDéfense: 3953\nRécupération: 439\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['GB3','GolemB3']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328040531394561/BossGolemR_large.jpg", color=0xfff99e)
     embed.set_author(name="Golem B3 (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328040531394561/BossGolemR_large.jpg")
     embed.add_field(name="⯀ 2~4*", value="Capacité: Invincibilité, Retribution\nPassif: Rec down 60% 2 tours\nPower: 200%\nActif: Étourdissement 20% 1 tour\nPower: 250%\n50% PV Actif: Siphon de PV (de ses PV)\nPower: 300%\nPV: 36'480\nAttaque: 1'338\nDéfense: 547\nRécupération: 912\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%\n\n__Guard sphere__\nPassif: Défense réduite 2 tours\nActif: Étourdissement 80% 1 tour\nPV: 17810\nAttaque296\nDéfense: 493\nRécupération: 493\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['GB4','GolemB4']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328032461422613/BossGolem_large.jpg", color=0xfff99e)
     embed.set_author(name="Golem B4 (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328032461422613/BossGolem_large.jpg")
     embed.add_field(name="▲ 2~4*", value="Capacité: Invincibilité, Retribution\nPassif: Nécrose 80% 2 tours\nPower: 160%\nActif: Nécrose 60% 2 tours\nPower: 150%\n50% PV Actif: Étourdissement 70% 1 tour\nPower: 200%\nPV: 200'400\nAttaque: 695\nDéfense: 301\nRécupération: 1'202\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%\n\n__Guard sphere__\nPassif: Étourdissement 80% 1 tour\nActif: Purification\nPV: 126464\nAttaque237\nDéfense: 274\nRécupération: 1642\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['GB5','GolemB5']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328037725274142/BossGolemD_large.jpg", color=0xfff99e)
     embed.set_author(name="Golem B5 (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328037725274142/BossGolemD_large.jpg")
     embed.add_field(name="⯀ ▲ ⯁ 3~5*", value="Capacité: Invincibilité, Retribution\nPassif: Attaque réduite 80% 2 tours\nPower: 170%\nActif: Silence 60% 1 tour\nPower: 200%\n50% PV Actif: Défense réduite 100% 2 tours\nPower: 250%\nPV: 189'280\nAttaque: 1'092\nDéfense: 983\nRécupération: 1'310\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%\n\n__Guard sphere__\nPassif: Défense réduite 60% 2 tours\nActif: Brise-Bonus\nPV: 86840\nAttaque1503\nDéfense: 601\nRécupération: 601\nDommages critiques: 200%\nTaux critique: 10%\nResist: 20%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['GB6','GolemB6']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328050685673503/BossGolemW_large.jpg", color=0xfff99e)
     embed.set_author(name="Golem B6 (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328050685673503/BossGolemW_large.jpg")
     embed.add_field(name="⯀ ▲ ⯁ 3~6*", value="Capacité: Invincibilité, Retribution, Régénération\nPassif: Défense réduite 100% 2 tours\nPower: 180%\nActif: Choc 60% 1 tour\nPower: 150%\n50% PV Actif: Attaque réduite 100% 2 tours\nPower: 230.%\nPV: 102'440\nAttaque: 1'773\nDéfense: 2'482\nRécupération: 5'122\nDommages critiques: 50%\nTaux critique: 20%\nResist: 0%\n\n__Guard sphere 1__\nPassif: Adrénaline 10% allies PV (on crit)\nActif: Étourdissement 80% 1 tour\nPV: 39910\nAttaque409\nDéfense: 1310\nRécupération: 1310\nDommages critiques: 50%\nTaux critique: 50%\nResist: 0%\n\n__Guard sphere 2__\nPassif: Choc 40% 1 tour\nActif: Purification\nPV: 39749\nAttaque819\nDéfense: 1310\nRécupération: 1310\nDommages critiques: 50%\nTaux critique: 50%\nResist: 0%", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content ==(item) for item in ['GB7','GolemB7']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328035439378432/BossGolemB_large.jpg", color=0xfff99e)
     embed.set_author(name="Golem B7 (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328035439378432/BossGolemB_large.jpg")
     embed.add_field(name="⯁ 4~6*", value="Capacité: Invincibilité, Retribution\nPassif: Fatigue 100% 2 tours\nPower: 150%\nActif: Petrify 40% 2 tours\nPower: 180%\n50% PV Actif: Nécrose x3 100% 2 tours\nPower: 220.%\nPV: 71'914\nAttaque: 2'043\nDéfense: 15'345\nRécupération: 1'634\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%\n\n__Guard sphere 1__\nPassif: Provocation 20% 1 tour\nActif: Nécrose 100% 2 tours\nPV: 27560\nAttaque541\nDéfense: 6869\nRécupération: 763\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%\n\n__Guard sphere 2__\nPassif: Pétrification 40% 1 tour\nActif: Attaque augmentée  2 tours\nPV: 41891\nAttaque763\nDéfense: 6869\nRécupération: 1526\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['GB8','GolemB8']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328040531394561/BossGolemR_large.jpg", color=0xfff99e)
     embed.set_author(name="Golem B8 (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328040531394561/BossGolemR_large.jpg")
     embed.add_field(name="⯀ 4~6*", value="Capacité: Invincibilité, Retribution\nPassif: Rec down 100% 2 tours\nPower: 200%\nActif: Étourdissement 40% 1 tour\nPower: 250%\n50% PV Actif: Siphon de PV (de ses PV)\nPower: 300%\nPV: 111'024\nAttaque: 3'732\nDéfense: 1'157\nRécupération: 1'542\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%\n\n__Guard sphere 1__\nPassif: Défense réduite 2 tours\nActif: Étourdissement 80% 1 tour\nPV: 37752\nAttaque1452\nDéfense: 1045\nRécupération: 871\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%\n\n__Guard sphere 2__\nPassif: Défense réduite 60% 2 tours\nActif: Purification\nPV: 125840\nAttaque871\nDéfense: 1045\nRécupération: 871\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['GB9','GolemB9']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328032461422613/BossGolem_large.jpg", color=0xfff99e)
     embed.set_author(name="Golem B9 (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328032461422613/BossGolem_large.jpg")
     embed.add_field(name="▲ 4~6*", value="Capacité: Invincibilité, Retribution\nPassif: Nécrose x2 100% 2 tours\nPower: 160%\nActif: Nécrose x3 100% 2 tours\nPower: 150%\n50% PV Actif: Étourdissement 70% 1 tour\nPower: 200%\nPV: 568'260\nAttaque: 1'894\nDéfense: 723\nRécupération: 2'066\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%\n\n__Guard sphere 1__\nPassif: Étourdissement 80% 1 tour\nActif: Purification\nPV: 56576\nAttaque3264\nDéfense: 1958\nRécupération: 979\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%\n\n__Guard sphere 2__\nPassif: Nécrose x2 60% 1 tours\nActif: Défense augmentée\nPV: 424320\nAttaque2040\nDéfense: 3133\nRécupération: 1958\nDommages critiques: 50%\nTaux critique: 20%\nResist: 20%", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content ==(item) for item in ['GB10','GolemB10']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328037725274142/BossGolemD_large.jpg", color=0xfff99e)
     embed.set_author(name="Golem B10 (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328037725274142/BossGolemD_large.jpg")
     embed.add_field(name="⯀ ▲ ⯁ 4~6*", value="Capacité: Invincibilité, Retribution\nPassif: Attaque réduite 100% 2 tours\nPower: 170%\nActif: Silence 60% 2 tours\nPower: 200%\n50% PV Actif: Défense réduite 100% 2 tours\nPower: 250%\nPV: 634'000\nAttaque: 2'378\nDéfense: 2'282\nRécupération: 2'282\nDommages critiques: 100%\nTaux critique: 20%\nResist: 30%\n\n__Guard sphere 1__\nPassif: Défense réduite 60% 2 tours\nActif: Brise-Bonus\nPV: 314080\nAttaque1812\nDéfense: 1631\nRécupération: 1087\nDommages critiques: 200%\nTaux critique: 10%\nResist: 20%\n\n__Guard sphere 2__\nPassif: Attaque réduite 60% 2 tours\nActif: Bouclier 2 tours\nPV: 54964\nAttaque4530\nDéfense: 1631\nRécupération: 2175\nDommages critiques: 200%\nTaux critique: 10%\nResist: 20%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['GB12','GolemB12']]):
     embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/684369688645337193/754619473981472818/Gn0rrnJ_d.webp", color=0xfff99e)
     embed.set_image(url="https://media.discordapp.net/attachments/684369688645337193/754619473981472818/Gn0rrnJ_d.webp")
     
     await message.channel.send(embed=embed)     

 if any([message.content ==(item) for item in ['Colosse','Colosse']]):
     embed=discord.Embed(title="", url="", color=0xfff99e)
     embed.set_author(name="Colossi")
     embed.set_thumbnail(url="")
     embed.add_field(name="⯀ ▲ ⯁ 6*", value="Dark Colosse:\nCapacité: Invincibilité, Retribution\nPassif: Soif 100% -30% 1 tour\nActif: Sceau 100% 3 tours\n50% PV Actif: ???\nPV: 1'680'003\nAttaque: 3'940\nDéfense: 56'003\nRécupération: 1'683\nDommages critiques: ???\nTaux critique: ???\nResist: ???\n\nFeu Colosse:\nCapacité: Invincibilité\nPassif: Traqueur 100%\nActif: Traqueur 100%\n50% PV Actif: ???\nPV: 1'400'003\nAttaque: 12'900\nDéfense: 63'003\nRécupération: 2'523\nDommages critiques: ???\nTaux critique: ???\nResist: ???\n\nEau Colosse:\nCapacité: Invincibilité\nPassif: Nécrose 100% x2 3 tours\nActif: Nécrose 100% x3 3 tours\n50% PV Actif: ???\nPV: 630'112\nAttaque: 4'620\nDéfense: 42'000\nRécupération: 33'600\nDommages critiques: ???\nTaux critique: ???\nResist: ???", inline=True)
     embed.add_field(name="- - - - -", value="Bois Colosse:\nCapacité: Invincibilité\nPassif: Prédateur 50%\nActif: Défense réduite 100% 3 tours\n50% PV Actif: ???\nPV: 3'080'014\nAttaque: 1'474\nDéfense: 19\nRécupération: 1'125\nDommages critiques: ???\nTaux critique: ???\nResist: ???\n\nLight Colosse:\nCapacité: Invincibilité\nPassif: Adrénaline 5% of de ses PV\nActif: Choc 60% 2 tour\n50% PV Actif: ???\nPV: 2'240'003\nAttaque: 8'403\nDéfense: 34\nRécupération: 43\nDommages critiques: ???\nTaux critique: ???\nResist: ???", inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['ColosseFeu','FeuColosse']]):
     embed=discord.Embed(title="", url="", color=0xfff99e)
     embed.set_author(name="Colosse (Feu)")
     embed.set_thumbnail(url="")
     embed.add_field(name="⯀ ▲ ⯁ 6*", value="Capacité: Invincibilité\nPassif: Traqueur 100%\nActif: Traqueur 100%\n50% PV Actif: ???\nPV: 1'400'003\nAttaque: 12'900\nDéfense: 63'003\nRécupération: 2'523\nDommages critiques: ???\nTaux critique: ???\nResist: ???\n\n__Guard sphere__\nPassif: ???\\nActif: ???", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['ColosseEau','EauColosse']]):
     embed=discord.Embed(title="", url="", color=0xfff99e)
     embed.set_author(name="Colosse (Eau)")
     embed.set_thumbnail(url="")
     embed.add_field(name="⯀ ▲ ⯁ 6*", value="Capacité: Invincibilité\nPassif: Nécrose 100% x2 3 tours\nActif: Nécrose 100% x3 3 tours\n50% PV Actif: ???\nPV: 630'112\nAttaque: 4'620\nDéfense: 42'000\nRécupération: 33'600\nDommages critiques: ???\nTaux critique: ???\nResist: ???\n\n__Guard sphere__\nPassif: ???\\nActif: ???", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['ColosseBois','BoisColosse']]):
     embed=discord.Embed(title="", url="", color=0xfff99e)
     embed.set_author(name="Colosse (Bois)")
     embed.set_thumbnail(url="")
     embed.add_field(name="⯀ ▲ ⯁ 6*", value="Capacité: Invincibilité\nPassif: Prédateur 50%\nActif: Défense réduite 100% 3 tours\n50% PV Actif: ???\nPV: 3'080'014\nAttaque: 1'474\nDéfense: 19\nRécupération: 1'125\nDommages critiques: ???\nTaux critique: ???\nResist: ???\n\n__Guard sphere__\nPassif: ???\\nActif: ???", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['ColosseDar','DarkColosse']]):
     embed=discord.Embed(title="", url="", color=0xfff99e)
     embed.set_author(name="Colosse (Dark)")
     embed.set_thumbnail(url="")
     embed.add_field(name="⯀ ▲ ⯁ 6*", value="Capacité: Invincibilité, Retribution\nPassif: Soif 100% -30% 1 tour\nActif: Sceau 100% 3 tours\n50% PV Actif: ???\nPV: 1'680'003\nAttaque: 3'940\nDéfense: 56'003\nRécupération: 1'683\nDommages critiques: ???\nTaux critique: ???\nResist: ???\n\n__Guard sphere__\nPassif: ???\\nActif: ???", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['ColosseLight','LightColosse']]):
     embed=discord.Embed(title="", url="", color=0xfff99e)
     embed.set_author(name="Colosse (light)")
     embed.set_thumbnail(url="")
     embed.add_field(name="⯀ ▲ ⯁ 6*", value="Capacité: Invincibilité\nPassif: Adrénaline 5% of de ses PV\nActif: Choc 60% 2 tour\n50% PV Actif: ???\nPV: 2'240'003\nAttaque: 8'403\nDéfense: 34\nRécupération: 43\nDommages critiques: ???\nTaux critique: ???\nResist: ???\n\n__Guard sphere__\nPassif: ???\\nActif: ???", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content ==(item) for item in ['Dragons','Dragon']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328008818130944/BossDragonB_large.jpg", color=0x80b7e8)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328008818130944/BossDragonB_large.jpg")
     embed.add_field(name=" Dragons 1 -> 5 ", value="__**Dragon B1** (Eau)__\nPassif: Petrify 100% 1T\nActif: Nécrose x3 100% 1T\nPV: 94'640\nAttaque: 1'966\nDéfense: 3'931\nRécupération: 1'310\nDommages critiques:  50%\nTaux critique:  20%\nResist:  30%\n\n__**Dragon B2** (dark)__\nPassif: Défense réduite 100% 2T\nActif: Silence 100% 1T\nPV: 256'100\nAttaque2'482\nDéfense709\nRécupération: 1'418\nDommages critiques 50%\nTaux critique 20%\nResist 30%\n\n__**Dragon B3** (Bois)__\nPassif: Nécrose x3 100% 1T\nActif: Soif -50% 100% 2T\nPV: 472'160\nAttaque1'634\nDéfense817\nRécupération: 1'634\nDommages critiques 50%\nTaux critique 20%\nResist 30%\n\n__**Dragon B4** (Feu)__\nPassif: Attaque réduite 100% 2T\nActif: Étourdissement 100% 1T\nPV: 251'680\nAttaque5'227\nDéfense871\nRécupération: 1'742\nDommages critiques 50%\nTaux critique 30%\nResist 30%\n\n__**Dragon B5** (light)__\nPassif: Soif -10% 100% 2T\nActif: Choc 100% 1T\nPV: 282'880\nAttaque3'917\nDéfense1'469\nRécupération: 3'917\nDommages critiques 50%\nTaux critique 30%\nResist 30%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['DB1','DragonB1']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328008818130944/BossDragonB_large.jpg", color=0x80b7e8)
     embed.set_author(name="Dragon B1 (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328008818130944/BossDragonB_large.jpg")
     embed.add_field(name=" ⯀ 4~5* ", value="Capacité: Invincibilité, Bénédiction\nPassif: Petrify 100% 1 tour\nPower: 600%\nActif: Nécrose x3 100% 1 tour\nPower: 300%\n50% PV Actif: Petrify 100% 1 tour\nPower: 600%\nPV: 94'640\nAttaque: 1'966\nDéfense: 3'931\nRécupération: 1'310\nDommages critiques: 50%\nTaux critique: 20%\nResist: 30%\n\n__Guard sphere 1__\nPassif: Nécrose 100% 1 tour\nActif: Attaque réduite 100% 2 tours\nPV: 43420\nAttaque1202\nDéfense: 1804\nRécupération: 902\nDommages critiques: 50%\nTaux critique: 20%\nResist: 60%\n\n__Guard sphere 2__\nPassif: Nécrose 100% 1 tour\nActif: Défense augmentée 2 tours\nPV: 86840\nAttaque1202\nDéfense: 1804\nRécupération: 2405\nDommages critiques: 0%\nTaux critique: 20%\nResist: 60%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['DB2','DragonB2']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328012178030592/BossDragonD_large.jpg", color=0x80b7e8)
     embed.set_author(name="Dragon B2 (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328012178030592/BossDragonD_large.jpg")
     embed.add_field(name=" ▲ 4~5* ", value="Capacité: Invincibilité, Bénédiction\nPassif: Défense réduite 100% 2 tours\nPower: 300%\nActif: Silence 100% 1 tour\nPower: 250%\n50% PV Actif: Soif -10% 100% 2 tours\nPower: 300%\nPV: 256'100\nAttaque: 2'482\nDéfense: 709\nRécupération: 1'418\nDommages critiques: 50%\nTaux critique: 20%\nResist: 30%\n\n__Guard sphere 1__\nPassif: Défense réduite 60% 2 tours\nActif: Nécrose 100% 2 tours\nPV: 47320\nAttaque546\nDéfense: 655\nRécupération: 983\nDommages critiques: 200%\nTaux critique: 10%\nResist: 60%\n\n__Guard sphere 2__\nPassif: Boost de moral 10% (allies)\nActif: Bouclier 2 tours\nPV: 94640\nAttaque546\nDéfense: 655\nRécupération: 2621\nDommages critiques: 200%\nTaux critique: 10%\nResist: 60%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['DB3','DragonB3']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328015663235083/BossDragonG_large.jpg", color=0x80b7e8)
     embed.set_author(name="Dragon B3 (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328015663235083/BossDragonG_large.jpg")
     embed.add_field(name=" ⯁ 4~5* ", value="Capacité: Invincibilité, Bénédiction\nPassif: Nécrose x3 100% 1 tour\nPower: 350%\nActif: Soif -50% 100% 2 tours\nPower: 250%\n50% PV Actif: Nécrose x3 100% 1 tour\nPower: 400%\nPV: 472'160\nAttaque: 1'634\nDéfense: 817\nRécupération: 1'634\nDommages critiques: 50%\nTaux critique: 20%\nResist: 30%\n\n__Guard sphere 1__\nPassif: Étourdissement 60% 1 tour\nActif: Adrénaline 5% own max PV (allies)\nPV: 165360\nAttaque1018\nDéfense: 382\nRécupération: 1145\nDommages critiques: 50%\nTaux critique: 20%\nResist: 60%\n\n__Guard sphere 2__\nPassif: Fatigue 100% 1 tour\nActif: Purification\nPV: 275600\nAttaque1018\nDéfense: 382\nRécupération: 3053\nDommages critiques: 50%\nTaux critique: 20%\nResist: 60%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['DB4','DragonB4']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328002249981955/BossDragon_large.jpg", color=0x80b7e8)
     embed.set_author(name="Dragon B4 (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328002249981955/BossDragon_large.jpg")
     embed.add_field(name=" ⯀ 4~6* ", value="Capacité: Invincibilité, Bénédiction\nPassif: Attaque réduite 100% 2 tours\nPower: 900%\nActif: Étourdissement 100% 1 tour\nPower: 300%\n50% PV Actif: Défense réduite 100% 2 tours\nPower: 400%\nPV: 251'680\nAttaque: 5'227\nDéfense: 871\nRécupération: 1'742\nDommages critiques: 50%\nTaux critique: 30%\nResist: 30%\n\n__Guard sphere 1__\nPassif: Soif -10% 80% 1 tour\nActif: Défense réduite 100% 2 tours\nPV: 59020\nAttaque1636\nDéfense: 572\nRécupération: 1226\nDommages critiques: 50%\nTaux critique: 20%\nResist: 60%\n\n__Guard sphere 2__\nPassif: Fatigue 100% 2 tour\nActif: Défense augmentée 2 tours\nPV: 118040\nAttaque1634\nDéfense: 572\nRécupération: 3269\nDommages critiques: 50%\nTaux critique: 20%\nResist: 60%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['DB5','DragonB5']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328018687590400/BossDragonW_large.jpg", color=0x80b7e8)
     embed.set_author(name="Dragon B5 (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328018687590400/BossDragonW_large.jpg")
     embed.add_field(name=" ▲ 4~6* ", value="Capacité: Invincibilité, Bénédiction, Régénération\nPassif: Soif -10% 100% 2 tours\nPower: 350%\nActif: Choc 100% 1 tour\nPower: 300%\n50% PV Actif: Choc 100% 1 tour\nPower: 400%\nPV: 282'880\nAttaque: 3'917\nDéfense: 1'469\nRécupération: 3'917\nDommages critiques: 50%\nTaux critique: 30%\nResist: 30%\n\n__Guard sphere 1__\nPassif: Brise-Bonus\nActif: Attaque réduite 100% 2 tours\nPV: 66820\nAttaque925\nDéfense: 1110\nRécupération: 1388\nDommages critiques: 50%\nTaux critique: 50%\nResist: 60%\n\n__Guard sphere 2__\nPassif: Défense réduite 100% 2 tours\nActif: Purification\nPV: 133640\nAttaque952\nDéfense: 1110\nRécupération: 3701\nDommages critiques: 50%\nTaux critique: 50%\nResist: 60%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['DB6','DragonB6']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328008818130944/BossDragonB_large.jpg", color=0x80b7e8)
     embed.set_author(name="Dragon B6 (Eau)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328008818130944/BossDragonB_large.jpg")
     embed.add_field(name=" ⯁ 4~6* ", value="Capacité: Invincibilité, Bénédiction\nPassif: Petrify 100% 1 tour\nPower: 600%\nActif: Nécrose x3 100% 2 tours\nPower: 300%\n50% PV Actif: Petrify 100% 1 tour\nPower: 600%\nPV: 149'240\nAttaque: 2'273\nDéfense: 5'166\nRécupération: 2'066\nDommages critiques: 100%\nTaux critique: 30%\nResist: 45%\n\n__Guard sphere 1__\nPassif: Nécrose x3 100% 1 tour\nActif: Attaque réduite 100% 3 tours\nPV: 70720\nAttaque1632\nDéfense: 2938\nRécupération: 1469\nDommages critiques: 50%\nTaux critique: 20%\nResist: 80%\n\n__Guard sphere 2__\nPassif: Nécrose 100% 2 tour\nActif: Défense augmentée 3 tours\nPV: 141440\nAttaque1632\nDéfense: 2938\nRécupération: 3917\nDommages critiques: 50%\nTaux critique: 20%\nResist: 80%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['DB7','DragonB7']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328012178030592/BossDragonD_large.jpg", color=0x80b7e8)
     embed.set_author(name="Dragon B7 (dark)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328012178030592/BossDragonD_large.jpg")
     embed.add_field(name=" ⯀ 5~6* ", value="Capacité: Invincibilité, Bénédiction\nPassif: Défense réduite 100% 2 tours\nPower: 300%\nActif: Silence 100% 2 tours\nPower: 250%\n50% PV Actif: Soif -10% 100% 2 tours\nPower: 300%\nPV: 392'600\nAttaque: 4'349\nDéfense: 1'087\nRécupération: 2'174\nDommages critiques: 100%\nTaux critique: 30%\nResist: 45%\n\n__Guard sphere 1__\nPassif: Défense réduite 100% 2 tours\nActif: Nécrose x2 100% 2 tours\nPV: 104468\nAttaque1550\nDéfense: 1033\nRécupération: 1550\nDommages critiques: 150%\nTaux critique: 20%\nResist: 80%\n\n__Guard sphere 2__\nPassif: Boost de moral 10% (allies)\nActif: Bouclier 3 tours\nPV: 223860\nAttaque1550\nDéfense: 1033\nRécupération: 4133\nDommages critiques: 150%\nTaux critique: 20%\nResist: 80%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['DB8','DragonB8']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328015663235083/BossDragonG_large.jpg", color=0x80b7e8)
     embed.set_author(name="Dragon B8 (Bois)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328015663235083/BossDragonG_large.jpg")
     embed.add_field(name=" ▲ 5~6* ", value="Capacité: Invincibilité, Bénédiction\nPassif: Nécrose x3 100% 2 tours\nPower: 350%\nActif: Soif -50% 100% 2 tours\nPower: 500%\n50% PV Actif: Nécrose x3 100% 2 tour\nPower: 800%\nPV: 1'122'160\nAttaque: 2'988\nDéfense: 1'195\nRécupération: 2'390\nDommages critiques: 100%\nTaux critique: 40%\nResist: 45%\n\n__Guard sphere 1__\nPassif: Étourdissement 80% 1 tour\nActif: Adrénaline 5% own max PV (allies)\nPV: 296712\nAttaque1522\nDéfense: 571\nRécupération: 1712\nDommages critiques: 50%\nTaux critique: 30%\nResist: 80%\n\n__Guard sphere 2__\nPassif: Fatigue 100% 1 tour\nActif: Purification\nPV: 494520\nAttaque1522\nDéfense: 571\nRécupération: 4565\nDommages critiques: 50%\nTaux critique: 30%\nResist: 80%", inline=False)
     
     await message.channel.send(embed=embed)
 
 if any([message.content ==(item) for item in ['DB9','DragonB9']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328002249981955/BossDragon_large.jpg", color=0x80b7e8)
     embed.set_author(name="Dragon B9 (Feu)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328002249981955/BossDragon_large.jpg")
     embed.add_field(name=" ⯁ 5~6* ", value="Capacité: Invincibilité, Bénédiction\nPassif: Attaque réduite 100% 3 tours\nPower: 900%\nActif: Étourdissement 100% 1 tour\nPower: 400%\n50% PV Actif: Défense réduite 100% 3 tours\nPower: 450%\nPV: 487'188\nAttaque: 7'495\nDéfense: 1'249\nRécupération: 2'498\nDommages critiques: 100%\nTaux critique: 40%\nResist: 45%\n\n__Guard sphere 1__\nPassif: Soif -10% 80% 1 tour\nActif: Défense réduite 100% 3 tours\nPV: 258960\nAttaque2789\nDéfense: 837\nRécupération: 1793\nDommages critiques: 50%\nTaux critique: 30%\nResist: 80%\n\n__Guard sphere 2__\nPassif: Fatigue 100% 2 tour\nActif: Défense augmentée 3 tours\nPV: 345280\nAttaque2789\nDéfense: 837\nRécupération: 4781\nDommages critiques: 50%\nTaux critique: 30%\nResist: 80%", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['DB10','DragonB10']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328018687590400/BossDragonW_large.jpg", color=0x80b7e8)
     embed.set_author(name="Dragon B10 (light)")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328018687590400/BossDragonW_large.jpg")
     embed.add_field(name=" ⯀▲⯁ 6* ", value="Capacité: Invincibilité, Bénédiction, Régénération\nPassif: Soif -10% 100% 2 tours\nPower: 350%\nActif: Choc 100% 2 tours\nPower: 300%\n50% PV Actif: Choc 100% 2 tour\nPower: 300%\nPV: 784'160\nAttaque: 6'107\nDéfense: 1'357\nRécupération: 5'429\nDommages critiques: 100%\nTaux critique: 40%\nResist: 45%\n\n__Guard sphere 1__\nPassif: Brise-Bonus\nActif: Attaque réduite 100% 3 tours\nPV: 256308\nAttaque1666\nDéfense: 1499\nRécupération: 1874\nDommages critiques: 50%\nTaux critique: 50%\nResist: 80%\n\n__Guard sphere 2__\nPassif: Défense réduite 100% 3 tours\nActif: Purification\nPV: 270660\nAttaque1666\nDéfense: 1499\nRécupération: 4997\nDommages critiques: 50%\nTaux critique: 50%\nResist: 80%", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content ==(item) for item in ['TitansPV','TitanPV']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" Titans 1 -> 200 ", value="Lv1 à Lv5: 3M PV\nLv6 à Lv10: 3.25M PV\nLv11 à Lv15: 3.5M PV\nLv16 à Lv20: 3.75M PV\nLv21 à Lv25: 4M PV\nLv26 à Lv30: 5.5M PV\nLv31 à Lv35: 7M PV\nLv36 à Lv40: 8.5M PV\nLv41 à Lv45: 10M PV\nLv46 à Lv50: 12.5M PV\nLv51 à Lv55: 15M PV\nLv56 à Lv60: 17.5M PV\nLv61 à Lv65: 20M PV\nLv66 à Lv70: 27.5M PV\nLv71 à Lv75: 35M PV\nLv76 à Lv80: 42.5M PV\nLv81 à Lv85: 50M PV\nLv86 à Lv90: 62.5M PV\nLv91 à Lv95: 75M PV\nLv96 à Lv100: 87.5M PV\nLv101 à Lv105: 100M PV\nLv106 à Lv110: 125M PV\nLv111 à Lv115: 150M PV\nLv116 à Lv120: 175M PV\nLv121 à Lv125: 200M PV\nLv126 à Lv130: 225M PV\nLv131 à Lv135: 250M PV\nLv136 à Lv140: 275M PV\nLv141 à Lv145: 300M PV\nLv146 à Lv150: 325M PV\nLv151 à Lv155: 350M PV\nLv156 à Lv160: 375M PV\nLv161 à Lv165: 400M PV\nLv166 à Lv170: 425M PV\nLv171 à Lv175: 450M PV\nLv176 à Lv180: 475M PV\nLv181 à Lv185: 500M PV\nLv186 à Lv190: 525M PV\nLv191 à Lv195: 550M PV\nLv196 à Lv200: 575M PV", inline=False)
     
     await message.channel.send(embed=embed)

#####################################################################     	 
############                Titi level                   ############
#####################################################################
 
 if message.content.startswith('Titi01'):
        await message.channel.send('Titan 1 :dark: (3m) :\nTitan 2 :eau: (3m) :\nTitan 3 :bois: (3m) :\nTitan 4 :light: (3m) :\nTitan 5 :feu: (3m) :\nTitan 6 :dark: (3.25m) :\nTitan 7 :eau: (3.25m) :\nTitan 8 :bois: (3.25m) :\nTitan 9 :light: (3.25m) :\nTitan 10 :feu: (3.25m) :')

 if message.content.startswith('Titi11'):
        await message.channel.send('Titan 11 :dark: (3.5m) :\nTitan 12 :eau: (3.5m) :\nTitan 13 :bois: (3.5m) :\nTitan 14 :light:  (3.5m) :\nTitan 15 :feu: (3.5m) : \nTitan 16 :dark: (3.75m) : \nTitan 17 :eau: (3.75m) : \nTitan 18 :bois: (3.75m) : \nTitan 19 :light: (3.75m) : \nTitan 20 :feu: (3.75m) :')

 if message.content.startswith('Titi21'):
        await message.channel.send('Titan 21 :dark: (4m) :\nTitan 22 :eau: (4m) : \nTitan 23 :bois: (4m) : \nTitan 24 :light: (4m) :\nTitan 25 :feu: (4m) :\nTitan 26 :dark: (5.5m) :\nTitan 27 :eau: (5.5m) :\nTitan 28 :bois: (5.5m) :\nTitan 29 :light: (5.5m) :\nTitan 30 :feu: (5.5m) :')

 if message.content.startswith('Titi31'):
        await message.channel.send('Titan 31 :dark: (7m) :\nTitan 32 :eau: (7m) : \nTitan 33 :bois: (7m) :\nTitan 34 :light: (7m) : \nTitan 35 :feu: (7m) :\nTitan 36 :dark: (8.5m) :\nTitan 37 :eau: (8.5m) :\nTitan 38 :bois: (8.5m) :\nTitan 39 :light: (8.5m) :\nTitan 40 :feu: (8.5m) :')

 if message.content.startswith('Titi41'):
        await message.channel.send('Titan 41 :dark: (10m) :\nTitan 42 :eau: (10m) : \nTitan 43 :bois: (10m) :\nTitan 44 :light: (10m) : \nTitan 45 :feu: (10m) :\nTitan 46 :dark: (12.5m) :\nTitan 47 :eau: (12.5m) :\nTitan 48 :bois: (12.5m) :\nTitan 49 :light: (12.5m) :\nTitan 50 :feu: (12.5m) :')

 if message.content.startswith('Titi51'):
        await message.channel.send('Titan 51 :dark: (15m) :\nTitan 52 :eau: (15m) : \nTitan 53 :bois: (15m) : \nTitan 54 :light: (15m) :\nTitan 55 :feu: (15m) :\nTitan 56 :dark: (17.5m) :\nTitan 57 :eau: (17.5m) :\nTitan 58 :bois: (17.5m) :\nTitan 59 :light: (17.5m) :\nTitan 60 :feu: (17.5m) :')

 if message.content.startswith('Titi61'):
        await message.channel.send('Titan 61 :dark: (20m) :\nTitan 62 :eau: (20m) :\nTitan 63 :bois: (20m) :\nTitan 64 :light:  (20m) :\nTitan 65 :feu: (20m) : \nTitan 66 :dark: (27.5m) : \nTitan 67 :eau: (27.5m) : \nTitan 68 :bois: (27.5m) : \nTitan 69 :light: (27.5m) : \nTitan 70 :feu: (27.5m) :')

 if message.content.startswith('Titi71'):
        await message.channel.send('Titan 71 :dark: (35m) :\nTitan 72 :eau: (35m) : \nTitan 73 :bois: (35m) : \nTitan 74 :light: (35m) :\nTitan 75 :feu: (35m) :\nTitan 76 :dark: (42.5m) :\nTitan 77 :eau: (42.5m) :\nTitan 78 :bois: (42.5m) :\nTitan 79 :light: (42.5m) :\nTitan 80 :feu: (42.5m) :')

 if message.content.startswith('Titi81'):
        await message.channel.send('Titan 81 :dark: (50m) :\nTitan 82 :eau: (50m) : \nTitan 83 :bois: (50m) :\nTitan 84 :light: (50m) : \nTitan 85 :feu: (50m) :\nTitan 86 :dark: (62.5m) :\nTitan 87 :eau: (62.5m) :\nTitan 88 :bois: (62.5m) :\nTitan 89 :light: (62.5m) :\nTitan 90 :feu: (62.5m) :')

 if message.content.startswith('Titi91'):
        await message.channel.send('Titan 91 :dark: (75m) : \nTitan 92 :eau: (75m) : \nTitan 93 :bois: (75m) :\nTitan 94 :light: (75m) : \nTitan 95 :feu: (75m) :\nTitan 96 :dark: (87.5m) :\nTitan 97 :eau: (87.5m) :\nTitan 98 :bois: (87.5m) :\nTitan 99 :light: (87.5m) :\nTitan 100 :feu: (87.5m) :')

 if message.content.startswith('Titi101'):
        await message.channel.send('Titan 101 :dark: (100m) :\nTitan 102 :eau: (100m) : \nTitan 103 :bois: (100m) : \nTitan 104 :light: (100m) :\nTitan 105 :feu: (100m) :\nTitan 106 :dark: (125m) :\nTitan 107 :eau: (125m) :\nTitan 108 :bois: (125m) :\nTitan 109 :light: (125m) :\nTitan 110 :feu: (125m) :')

 if message.content.startswith('Titi111'):
        await message.channel.send('Titan 111 :dark: (150m) :\nTitan 112 :eau: (150m) :\nTitan 113 :bois: (150m) :\nTitan 114 :light:  (150m) :\nTitan 115 :feu: (150m) : \nTitan 116 :dark: (175) : \nTitan 117 :eau: (175m) : \nTitan 118 :bois: (175m) : \nTitan 119 :light: (175m) : \nTitan 120 :feu: (175m) :')

 if message.content.startswith('Titi121'):
        await message.channel.send('Titan 121 :dark: (200m) :\nTitan 122 :eau: (200m) : \nTitan 123 :bois: (200m) : \nTitan 124 :light: (200m) :\nTitan 125 :feu: (200m) :\nTitan 126 :dark: (225m) :\nTitan 127 :eau: (225m) :\nTitan 128 :bois: (225m) :\nTitan 129 :light: (225m) :\nTitan 130 :feu: (225m) :')

 if message.content.startswith('Titi131'):
        await message.channel.send('Titan 131 :dark: (250m) :\nTitan 132 :eau: (250m) : \nTitan 133 :bois: (250m) :\nTitan 134 :light: (250m) : \nTitan 135 :feu: (250m) :\nTitan 136 :dark: (275m) :\nTitan 137 :eau: (275m) :\nTitan 138 :bois: (275m) :\nTitan 139 :light: (275m) :\nTitan 140 :feu: (275m) :')

 if message.content.startswith('Titi141'):
        await message.channel.send('')

 if any([message.content ==(item) for item in ['Titan','Titans']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" Titans 1 -> 100 \nLow Attaque value = light and dark titans\nHigh Attaque value = Feu, Eau and Bois titans\nDéfense = 1200 pour tous les titans (lvl 1 à 200)", value="__Lv1 à Lv5__: 3M PV\n: Attaque: 1800 à 2700\n__Lv6 à Lv10__: 3.25M PV\n: Attaque: 2000 à 3000\n__Lv11 à Lv15__: 3.5M PV\n: Attaque: 2200 à 3300\n__Lv16 à Lv20__: 3.75M PV\n: Attaque: 2400 à 3600\n__Lv21 à Lv25__: 4M PV\n: Attaque: 2600 à 3900\n__Lv26 à Lv30__: 5.5M PV\n: Attaque: 2800 à 4200\n__Lv31 à Lv35__: 7M PV\n: Attaque: 3000 à 4500\n__Lv36 à Lv40__: 8.5M PV\n: Attaque: 3200 à 4800\n__Lv41 à Lv45__: 10M PV\n: Attaque: 3400 à 5100\n__Lv46 à Lv50__: 12.5M PV\n: Attaque: 3600 à 5400\n__Lv51 à Lv55__: 15M PV\n: Attaque: 4000 à 6000\n__Lv56 à Lv60__: 17.5M PV\n: Attaque: 4400 à 6600\n__Lv61 à Lv65__: 20M PV\n: Attaque: 4800 à 7200\n__Lv66 à Lv70__: 27.5M PV\n: Attaque: 5200 à 7800\n__Lv71 à Lv75__: 35M PV\n: Attaque: 5600 à 8400\n__Lv76 à Lv80__: 42.5M PV\n: Attaque: 6000 à 9000\n__Lv81 à Lv85__: 50M PV\n: Attaque: 6400 à 9600\n__Lv86 à Lv90__: 62.5M PV\n: Attaque: 6800 à 10200\n__Lv91 à Lv95__: 75M PV\n: Attaque: 7200 à 10800\n__Lv96 à Lv100__: 87.5M PV\n: Attaque: 7600 à 11400", inline=False)
     
     await message.channel.send(embed=embed)
     
 if any([message.content ==(item) for item in ['Titan','Titans']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" Titans 100 -> 150 \nLow Attaque value = light and dark titans\nHigh Attaque value = Feu, Eau and Bois titans\nDéfense = 1200 pour tous les titans (lvl 1 à 200)", value="__Lv101 à Lv105__: 100M PV\n: Attaque: 8000 à 12000\n__Lv106 à Lv110__: 125M PV\n: Attaque: 8400 à 12600\n__Lv111 à Lv115__: 150M PV\n: Attaque: 8800 à 13200\n__Lv116 à Lv120__: 175M PV\n: Attaque: 9200 à 13800\n__Lv121 à Lv125__: 200M PV\n: Attaque: 9600 à 14400\n__Lv126 à Lv130__: 225M PV\n: Attaque: 10000 à 15000\n__Lv131 à Lv135__: 250M PV\n: Attaque: 10400 à 15600\n__Lv136 à Lv140__: 275M PV\n: Attaque: 10800 à 16200\n__Lv141 à Lv145__: 300M PV\n: Attaque: 11200 à 16800\n__Lv146 à Lv150__: 325M PV\n: Attaque: 11600 à 17400", inline=False)
     
     await message.channel.send(embed=embed)

#"__Lv151 à Lv155__: 350M PV\n: Attaque: 12000 à 18000\n__Lv156 à Lv160__: 375M PV\n: Attaque: 12400 à 18600\n__Lv161 à Lv165__: 400M PV\n: Attaque: 12800 à 19200\n__Lv166 à Lv170__: 425M PV\n: Attaque: 13200 à 19800\n__Lv171 à Lv175__: 450M PV\n: Attaque: 13600 à 20400\n__Lv176 à Lv180__: 475M PV\n: Attaque: 14000 à 21000\n__Lv181 à Lv185__: 500M PV\n: Attaque: 14400 à 21600\n__Lv186 à Lv190__: 525M PV\n: Attaque: 14800 à 22200\n__Lv191 à Lv195__: 550M PV\n: Attaque: 15200 à 22800\n__Lv196 à Lv200__: 575M PV\n: Attaque: 15600 à 23400"


 if any([message.content ==(item) for item in ['UTC-','HST']]):{
     'content' : "Salut les poulets"
     }

 if any([message.content ==(item) for item in ['UTC-9','AKST','PST-1','HST+1']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC-9 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC-9**  12:0 / 17:0 -  19:0 / 0:0\n**UTC-8** **PST**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC-7** **MST**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC-6** **CST**: 15:0 / 20:0 -  22:0 / 3:0\n**UTC-5** **EST**: 16:0 / 21:0 -  23:0 / 4:0\n**UTC-4**  17:0 / 22:0 -  0:0 / 5:0\n**UTC-3**  18:0 / 23:0 -  1:0 / 6:0\n**UTC-2**  19:0 / 0:0 -  2:0 / 7:0\n**UTC-1**  20:0 / 1:0 -  3:0 / 8:0\n**UTC / GMT**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC+1** **CET**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC+2**  23:0 / 4:0 -  6:0 / 11:0\n**UTC+3** **MSK**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC+4** **+04**: 1:0 / 6:0 -  8:0 / 13:0\n**UTC+5** **IST**: 2:0 / 7:0 -  9:0 / 14:0\n**UTC+6**  3:0 / 8:0 -  10:0 / 15:0\n**UTC+7**  4:0 / 9:0 -  11:0 / 16:0\n**UTC+8** **CST**: 5:0 / 10:0 -  12:0 / 17:0\n**UTC+9** **JST**: 6:0 / 11:0 -  13:0 / 18:0\n**UTC+10**  7:0 / 12:0 -  14:0 / 19:0\n**UTC+11** **AEDT**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC+12**  9:0 / 14:0 -  16:0 / 21:0\n**UTC+13** **NZDT**: 10:0 / 15:0 -  17:0 / 22:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC-','PST']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC-8 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC-9**  11:0 / 16:0 -  18:0 / 23:0\n**UTC-8** **PST**: 12:0 / 17:0 -  19:0 / 0:0\n**UTC-7** **MST**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC-6** **CST**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC-5** **EST**: 15:0 / 20:0 -  22:0 / 3:0\n**UTC-4**  16:0 / 21:0 -  23:0 / 4:0\n**UTC-3**  17:0 / 22:0 -  0:0 / 5:0\n**UTC-2**  18:0 / 23:0 -  1:0 / 6:0\n**UTC-1**  19:0 / 0:0 -  2:0 / 7:0\n**UTC / GMT**: 20:0 / 1:0 -  3:0 / 8:0\n**UTC+1** **CET**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC+2**  22:0 / 3:0 -  5:0 / 10:0\n**UTC+3** **MSK**: 23:0 / 4:0 -  6:0 / 11:0\n**UTC+4** **+04**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC+5** **IST**: 1:0 / 6:0 -  8:0 / 13:0\n**UTC+6**  2:0 / 7:0 -  9:0 / 14:0\n**UTC+7**  3:0 / 8:0 -  10:0 / 15:0\n**UTC+8** **CST**: 4:0 / 9:0 -  11:0 / 16:0\n**UTC+9** **JST**: 5:0 / 10:0 -  12:0 / 17:0\n**UTC+10**  6:0 / 11:0 -  13:0 / 18:0\n**UTC+11** **AEDT**: 7:0 / 12:0 -  14:0 / 19:0\n**UTC+12**  8:0 / 13:0 -  15:0 / 20:0\n**UTC+13** **NZDT**: 9:0 / 14:0 -  16:0 / 21:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC-7','MST']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC-7 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 9:0 / 14:0 -  16:0 / 21:0\n**UTC-9**  10:0 / 15:0 -  17:0 / 22:0\n**UTC-8** **PST**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC-7** **MST**: 12:0 / 17:0 -  19:0 / 0:0\n**UTC-6** **CST**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC-5** **EST**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC-4**  15:0 / 20:0 -  22:0 / 3:0\n**UTC-3**  16:0 / 21:0 -  23:0 / 4:0\n**UTC-2**  17:0 / 22:0 -  0:0 / 5:0\n**UTC-1**  18:0 / 23:0 -  1:0 / 6:0\n**UTC / GMT**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC+1** **CET**: 20:0 / 1:0 -  3:0 / 8:0\n**UTC+2**  21:0 / 2:0 -  4:0 / 9:0\n**UTC+3** **MSK**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC+4** **+04**: 23:0 / 4:0 -  6:0 / 11:0\n**UTC+5** **IST**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC+6**  1:0 / 6:0 -  8:0 / 13:0\n**UTC+7**  2:0 / 7:0 -  9:0 / 14:0\n**UTC+8** **CST**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC+9** **JST**: 4:0 / 9:0 -  11:0 / 16:0\n**UTC+10**  5:0 / 10:0 -  12:0 / 17:0\n**UTC+11** **\nEDT**: 6:0 / 11:0 -  13:0 / 18:0\n**UTC+12**  7:0 / 12:0 -  14:0 / 19:0\n**UTC+13** **NZDT**: 8:0 / 13:0 -  15:0 / 20:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC-6','CST']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC-6 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC-9**  9:0 / 14:0 -  16:0 / 21:0\n**UTC-8** **PST**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC-7** **MST**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC-6** **CST**: 12:0 / 17:0 -  19:0 / 0:0\n**UTC-5** **EST**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC-4**  14:0 / 19:0 -  21:0 / 2:0\n**UTC-3**  15:0 / 20:0 -  22:0 / 3:0\n**UTC-2**  16:0 / 21:0 -  23:0 / 4:0\n**UTC-1**  17:0 / 22:0 -  0:0 / 5:0\n**UTC / GMT**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC+1** **CET**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC+2**  20:0 / 1:0 -  3:0 / 8:0\n**UTC+3** **MSK**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC+4** **+04**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC+5** **IST**: 23:0 / 4:0 -  6:0 / 11:0\n**UTC+6**  0:0 / 5:0 -  7:0 / 12:0\n**UTC+7**  1:0 / 6:0 -  8:0 / 13:0\n**UTC+8** **CST**: 2:0 / 7:0 -  9:0 / 14:0\n**UTC+9** **JST**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC+10**  4:0 / 9:0 -  11:0 / 16:0\n**UTC+11** **\nEDT**: 5:0 / 10:0 -  12:0 / 17:0\n**UTC+12**  6:0 / 11:0 -  13:0 / 18:0\n**UTC+13** **NZDT**: 7:0 / 12:0 -  14:0 / 19:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC-','EST']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC-5 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 7:0 / 12:0 -  14:0 / 19:0\n**UTC-9**  8:0 / 13:0 -  15:0 / 20:0\n**UTC-8** **PST**: 9:0 / 14:0 -  16:0 / 21:0\n**UTC-7** **MST**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC-6** **CST**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC-5** **EST**: 12:0 / 17:0 -  19:0 / 0:0\n**UTC-4**  13:0 / 18:0 -  20:0 / 1:0\n**UTC-3**  14:0 / 19:0 -  21:0 / 2:0\n**UTC-2**  15:0 / 20:0 -  22:0 / 3:0\n**UTC-1**  16:0 / 21:0 -  23:0 / 4:0\n**UTC / GMT**: 17:0 / 22:0 -  0:0 / 5:0\n**UTC+1** **CET**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC+2**  19:0 / 0:0 -  2:0 / 7:0\n**UTC+3** **MSK**: 20:0 / 1:0 -  3:0 / 8:0\n**UTC+4** **+04**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC+5** **IST**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC+6**  23:0 / 4:0 -  6:0 / 11:0\n**UTC+7**  0:0 / 5:0 -  7:0 / 12:0\n**UTC+8** **CST**: 1:0 / 6:0 -  8:0 / 13:0\n**UTC+9** **JST**: 2:0 / 7:0 -  9:0 / 14:0\n**UTC+10**  3:0 / 8:0 -  10:0 / 15:0\n**UTC+11** **\nEDT**: 4:0 / 9:0 -  11:0 / 16:0\n**UTC+12**  5:0 / 10:0 -  12:0 / 17:0\n**UTC+13** **NZDT**: 6:0 / 11:0 -  13:0 / 18:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC-4','AST','EST+1']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC-4 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 6:0 / 11:0 -  13:0 / 18:0\n**UTC-9**  7:0 / 12:0 -  14:0 / 19:0\n**UTC-8** **PST**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC-7** **MST**: 9:0 / 14:0 -  16:0 / 21:0\n**UTC-6** **CST**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC-5** **EST**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC-4**  12:0 / 17:0 -  19:0 / 0:0\n**UTC-3**  13:0 / 18:0 -  20:0 / 1:0\n**UTC-2**  14:0 / 19:0 -  21:0 / 2:0\n**UTC-1**  15:0 / 20:0 -  22:0 / 3:0\n**UTC / GMT**: 16:0 / 21:0 -  23:0 / 4:0\n**UTC+1** **CET**: 17:0 / 22:0 -  0:0 / 5:0\n**UTC+2**  18:0 / 23:0 -  1:0 / 6:0\n**UTC+3** **MSK**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC+4** **+04**: 20:0 / 1:0 -  3:0 / 8:0\n**UTC+5** **IST**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC+6**  22:0 / 3:0 -  5:0 / 10:0\n**UTC+7**  23:0 / 4:0 -  6:0 / 11:0\n**UTC+8** **CST**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC+9** **JST**: 1:0 / 6:0 -  8:0 / 13:0\n**UTC+10**  2:0 / 7:0 -  9:0 / 14:0\n**UTC+11** **\nEDT**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC+12**  4:0 / 9:0 -  11:0 / 16:0\n**UTC+13** **NZDT**: 5:0 / 10:0 -  12:0 / 17:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC-3','ART','EST+2']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC-3 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 5:0 / 10:0 -  12:0 / 17:0\n**UTC-9**  6:0 / 11:0 -  13:0 / 18:0\n**UTC-8** **PST**: 7:0 / 12:0 -  14:0 / 19:0\n**UTC-7** **MST**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC-6** **CST**: 9:0 / 14:0 -  16:0 / 21:0\n**UTC-5** **EST**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC-4**  11:0 / 16:0 -  18:0 / 23:0\n**UTC-3**  12:0 / 17:0 -  19:0 / 0:0\n**UTC-2**  13:0 / 18:0 -  20:0 / 1:0\n**UTC-1**  14:0 / 19:0 -  21:0 / 2:0\n**UTC / GMT**: 15:0 / 20:0 -  22:0 / 3:0\n**UTC+1** **CET**: 16:0 / 21:0 -  23:0 / 4:0\n**UTC+2**  17:0 / 22:0 -  0:0 / 5:0\n**UTC+3** **MSK**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC+4** **+04**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC+5** **IST**: 20:0 / 1:0 -  3:0 / 8:0\n**UTC+6**  21:0 / 2:0 -  4:0 / 9:0\n**UTC+7**  22:0 / 3:0 -  5:0 / 10:0\n**UTC+8** **CST**: 23:0 / 4:0 -  6:0 / 11:0\n**UTC+9** **JST**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC+10**  1:0 / 6:0 -  8:0 / 13:0\n**UTC+11** **\nEDT**: 2:0 / 7:0 -  9:0 / 14:0\n**UTC+12**  3:0 / 8:0 -  10:0 / 15:0\n**UTC+13** **NZDT**: 4:0 / 9:0 -  11:0 / 16:0", inline=False)
     
     await message.channel.send(embed=embed)

 if message.content == "UTC-2":
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC-1 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 4:0 / 9:0 -  11:0 / 16:0\n**UTC-9**  5:0 / 10:0 -  12:0 / 17:0\n**UTC-8** **PST**: 6:0 / 11:0 -  13:0 / 18:0\n**UTC-7** **MST**: 7:0 / 12:0 -  14:0 / 19:0\n**UTC-6** **CST**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC-5** **EST**: 9:0 / 14:0 -  16:0 / 21:0\n**UTC-4**  10:0 / 15:0 -  17:0 / 22:0\n**UTC-3**  11:0 / 16:0 -  18:0 / 23:0\n**UTC-2**  12:0 / 17:0 -  19:0 / 0:0\n**UTC-1**  13:0 / 18:0 -  20:0 / 1:0\n**UTC / GMT**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC+1** **CET**: 15:0 / 20:0 -  22:0 / 3:0\n**UTC+2**  16:0 / 21:0 -  23:0 / 4:0\n**UTC+3** **MSK**: 17:0 / 22:0 -  0:0 / 5:0\n**UTC+4** **+04**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC+5** **IST**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC+6**  20:0 / 1:0 -  3:0 / 8:0\n**UTC+7**  21:0 / 2:0 -  4:0 / 9:0\n**UTC+8** **CST**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC+9** **JST**: 23:0 / 4:0 -  6:0 / 11:0\n**UTC+10**  0:0 / 5:0 -  7:0 / 12:0\n**UTC+11** **\nEDT**: 1:0 / 6:0 -  8:0 / 13:0\n**UTC+12**  2:0 / 7:0 -  9:0 / 14:0\n**UTC+13** **NZDT**: 3:0 / 8:0 -  10:0 / 15:0", inline=False)
     
     await message.channel.send(embed=embed)

 if message.content == "UTC-1":
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC-1 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC-9**  4:0 / 9:0 -  11:0 / 16:0\n**UTC-8** **PST**: 5:0 / 10:0 -  12:0 / 17:0\n**UTC-7** **MST**: 6:0 / 11:0 -  13:0 / 18:0\n**UTC-6** **CST**: 7:0 / 12:0 -  14:0 / 19:0\n**UTC-5** **EST**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC-4**  9:0 / 14:0 -  16:0 / 21:0\n**UTC-3**  10:0 / 15:0 -  17:0 / 22:0\n**UTC-2**  11:0 / 16:0 -  18:0 / 23:0\n**UTC-1**  12:0 / 17:0 -  19:0 / 0:0\n**UTC / GMT**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC+1** **CET**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC+2**  15:0 / 20:0 -  22:0 / 3:0\n**UTC+3** **MSK**: 16:0 / 21:0 -  23:0 / 4:0\n**UTC+4** **+04**: 17:0 / 22:0 -  0:0 / 5:0\n**UTC+5** **IST**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC+6**  19:0 / 0:0 -  2:0 / 7:0\n**UTC+7**  20:0 / 1:0 -  3:0 / 8:0\n**UTC+8** **CST**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC+9** **JST**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC+10**  23:0 / 4:0 -  6:0 / 11:0\n**UTC+11** **\nEDT**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC+12**  1:0 / 6:0 -  8:0 / 13:0\n**UTC+13** **NZDT**: 2:0 / 7:0 -  9:0 / 14:0", inline=False)
     
     await message.channel.send(embed=embed)

 if message.content == "UTC":
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+1 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**HST+1 \nPST-1**:  3:0 / 8:0 -  10:0 / 15:0 \n**UTC-8** **PST**: 4:0 / 9:0 -  11:0 / 16:0 \n**UTC-7** **MST**: 5:0 / 10:0 -  12:0 / 17:0 \n**UTC-6** **CST**: 6:0 / 11:0 -  13:0 / 18:0 \n**UTC-5** **EST**: 7:0 / 12:0 -  14:0 / 19:0 \n**UTC-4** **EST+1**: 8:0 / 13:0 -  15:0 / 20:0 \n**UTC-3** **EST+2**: 9:0 / 14:0 -  16:0 / 21:0 \n**UTC-2**  10:0 / 15:0 -  17:0 / 22:0 \n**UTC-1**  11:0 / 16:0 -  18:0 / 23:0 \n**UTCUTC** **GMT**: 12:0 / 17:0 -  19:0 / 0:0 \n**UTC+1** **CET**: 13:0 / 18:0 -  20:0 / 1:0 \n**UTC+2** **CET+1**: 14:0 / 19:0 -  21:0 / 2:0 \n**UTC+3** **MSK**: 15:0 / 20:0 -  22:0 / 3:0 \n**UTC+4**  16:0 / 21:0 -  23:0 / 4:0 \n**UTC+5** **IST**: 17:0 / 22:0 -  0:0 / 5:0 \n**UTC+6**  18:0 / 23:0 -  1:0 / 6:0 \n**UTC+7** **CST-1**: 19:0 / 0:0 -  2:0 / 7:0 \n**UTC+8** **CST \nJST-1**:  20:0 / 1:0 -  3:0 / 8:0 \n**UTC+9** **JST**: 21:0 / 2:0 -  4:0 / 9:0 \n**UTC+10** **JST+1**: 22:0 / 3:0 -  5:0 / 10:0 \n**UTC+11** ** \nEDT**: 23:0 / 4:0 -  6:0 / 11:0 \n**UTC+12**  0:0 / 5:0 -  7:0 / 12:0 \n**UTC+13** **NZDT**: 1:0 / 6:0 -  8:0 / 13:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC+1','CET','GMT+1']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+1 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 1:0 / 6:0 -  8:0 / 13:0\n**UTC-9**  2:0 / 7:0 -  9:0 / 14:0\n**UTC-8** **PST**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC-7** **MST**: 4:0 / 9:0 -  11:0 / 16:0\n**UTC-6** **CST**: 5:0 / 10:0 -  12:0 / 17:0\n**UTC-5** **EST**: 6:0 / 11:0 -  13:0 / 18:0\n**UTC-4**  7:0 / 12:0 -  14:0 / 19:0\n**UTC-3**  8:0 / 13:0 -  15:0 / 20:0\n**UTC-2**  9:0 / 14:0 -  16:0 / 21:0\n**UTC-1**  10:0 / 15:0 -  17:0 / 22:0\n**UTC / GMT**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC+1** **CET**: 12:0 / 17:0 -  19:0 / 0:0\n**UTC+2**  13:0 / 18:0 -  20:0 / 1:0\n**UTC+3** **MSK**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC+4** **+04**: 15:0 / 20:0 -  22:0 / 3:0\n**UTC+5** **IST**: 16:0 / 21:0 -  23:0 / 4:0\n**UTC+6**  17:0 / 22:0 -  0:0 / 5:0\n**UTC+7**  18:0 / 23:0 -  1:0 / 6:0\n**UTC+8** **CST**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC+9** **JST**: 20:0 / 1:0 -  3:0 / 8:0\n**UTC+10**  21:0 / 2:0 -  4:0 / 9:0\n**UTC+11** **\nEDT**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC+12**  23:0 / 4:0 -  6:0 / 11:0\n**UTC+13** **NZDT**: 0:0 / 5:0 -  7:0 / 12:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC+2','EET','CET+1']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+2 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC-9**  1:0 / 6:0 -  8:0 / 13:0\n**UTC-8** **PST**: 2:0 / 7:0 -  9:0 / 14:0\n**UTC-7** **MST**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC-6** **CST**: 4:0 / 9:0 -  11:0 / 16:0\n**UTC-5** **EST**: 5:0 / 10:0 -  12:0 / 17:0\n**UTC-4**  6:0 / 11:0 -  13:0 / 18:0\n**UTC-3**  7:0 / 12:0 -  14:0 / 19:0\n**UTC-2**  8:0 / 13:0 -  15:0 / 20:0\n**UTC-1**  9:0 / 14:0 -  16:0 / 21:0\n**UTC / GMT**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC+1** **CET**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC+2**  12:0 / 17:0 -  19:0 / 0:0\n**UTC+3** **MSK**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC+4** **+04**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC+5** **IST**: 15:0 / 20:0 -  22:0 / 3:0\n**UTC+6**  16:0 / 21:0 -  23:0 / 4:0\n**UTC+7**  17:0 / 22:0 -  0:0 / 5:0\n**UTC+8** **CST**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC+9** **JST**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC+10**  20:0 / 1:0 -  3:0 / 8:0\n**UTC+11** **\nEDT**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC+12**  22:0 / 3:0 -  5:0 / 10:0\n**UTC+13** **NZDT**: 23:0 / 4:0 -  6:0 / 11:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC+','MSK']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+3 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 23:0 / 4:0 -  6:0 / 11:0\n**UTC-9**  0:0 / 5:0 -  7:0 / 12:0\n**UTC-8** **PST**: 1:0 / 6:0 -  8:0 / 13:0\n**UTC-7** **MST**: 2:0 / 7:0 -  9:0 / 14:0\n**UTC-6** **CST**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC-5** **EST**: 4:0 / 9:0 -  11:0 / 16:0\n**UTC-4**  5:0 / 10:0 -  12:0 / 17:0\n**UTC-3**  6:0 / 11:0 -  13:0 / 18:0\n**UTC-2**  7:0 / 12:0 -  14:0 / 19:0\n**UTC-1**  8:0 / 13:0 -  15:0 / 20:0\n**UTC / GMT**: 9:0 / 14:0 -  16:0 / 21:0\n**UTC+1** **CET**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC+2**  11:0 / 16:0 -  18:0 / 23:0\n**UTC+3** **MSK**: 12:0 / 17:0 -  19:0 / 0:0\n**UTC+4** **+04**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC+5** **IST**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC+6**  15:0 / 20:0 -  22:0 / 3:0\n**UTC+7**  16:0 / 21:0 -  23:0 / 4:0\n**UTC+8** **CST**: 17:0 / 22:0 -  0:0 / 5:0\n**UTC+9** **JST**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC+10**  19:0 / 0:0 -  2:0 / 7:0\n**UTC+11** **\nEDT**: 20:0 / 1:0 -  3:0 / 8:0\n**UTC+12**  21:0 / 2:0 -  4:0 / 9:0\n**UTC+13** **NZDT**: 22:0 / 3:0 -  5:0 / 10:0", inline=False)
     
     await message.channel.send(embed=embed)
 if message.content == "UTC+4":
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+4 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC-9**  23:0 / 4:0 -  6:0 / 11:0\n**UTC-8** **PST**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC-7** **MST**: 1:0 / 6:0 -  8:0 / 13:0\n**UTC-6** **CST**: 2:0 / 7:0 -  9:0 / 14:0\n**UTC-5** **EST**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC-4**  4:0 / 9:0 -  11:0 / 16:0\n**UTC-3**  5:0 / 10:0 -  12:0 / 17:0\n**UTC-2**  6:0 / 11:0 -  13:0 / 18:0\n**UTC-1**  7:0 / 12:0 -  14:0 / 19:0\n**UTC / GMT**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC+1** **CET**: 9:0 / 14:0 -  16:0 / 21:0\n**UTC+2**  10:0 / 15:0 -  17:0 / 22:0\n**UTC+3** **MSK**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC+4** **+04**: 12:0 / 17:0 -  19:0 / 0:0\n**UTC+5** **IST**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC+6**  14:0 / 19:0 -  21:0 / 2:0\n**UTC+7**  15:0 / 20:0 -  22:0 / 3:0\n**UTC+8** **CST**: 16:0 / 21:0 -  23:0 / 4:0\n**UTC+9** **JST**: 17:0 / 22:0 -  0:0 / 5:0\n**UTC+10**  18:0 / 23:0 -  1:0 / 6:0\n**UTC+11** **\nEDT**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC+12**  20:0 / 1:0 -  3:0 / 8:0\n**UTC+13** **NZDT**: 21:0 / 2:0 -  4:0 / 9:0", inline=False)
     
     await message.channel.send(embed=embed)

 if message.content == "UTC+5":
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+5 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC-9**  22:0 / 3:0 -  5:0 / 10:0\n**UTC-8** **PST**: 23:0 / 4:0 -  6:0 / 11:0\n**UTC-7** **MST**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC-6** **CST**: 1:0 / 6:0 -  8:0 / 13:0\n**UTC-5** **EST**: 2:0 / 7:0 -  9:0 / 14:0\n**UTC-4**  3:0 / 8:0 -  10:0 / 15:0\n**UTC-3**  4:0 / 9:0 -  11:0 / 16:0\n**UTC-2**  5:0 / 10:0 -  12:0 / 17:0\n**UTC-1**  6:0 / 11:0 -  13:0 / 18:0\n**UTC / GMT**: 7:0 / 12:0 -  14:0 / 19:0\n**UTC+1** **CET**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC+2**  9:0 / 14:0 -  16:0 / 21:0\n**UTC+3** **MSK**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC+4** **+04**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC+5** **IST**: 12:0 / 17:0 -  19:0 / 0:0\n**UTC+6**  13:0 / 18:0 -  20:0 / 1:0\n**UTC+7**  14:0 / 19:0 -  21:0 / 2:0\n**UTC+8** **CST**: 15:0 / 20:0 -  22:0 / 3:0\n**UTC+9** **JST**: 16:0 / 21:0 -  23:0 / 4:0\n**UTC+10**  17:0 / 22:0 -  0:0 / 5:0\n**UTC+11** **\nEDT**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC+12**  19:0 / 0:0 -  2:0 / 7:0\n**UTC+13** **NZDT**: 20:0 / 1:0 -  3:0 / 8:0", inline=False)
     
     await message.channel.send(embed=embed)

 if message.content == "UTC+6":
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+6 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 20:0 / 1:0 -  3:0 / 8:0\n**UTC-9**  21:0 / 2:0 -  4:0 / 9:0\n**UTC-8** **PST**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC-7** **MST**: 23:0 / 4:0 -  6:0 / 11:0\n**UTC-6** **CST**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC-5** **EST**: 1:0 / 6:0 -  8:0 / 13:0\n**UTC-4**  2:0 / 7:0 -  9:0 / 14:0\n**UTC-3**  3:0 / 8:0 -  10:0 / 15:0\n**UTC-2**  4:0 / 9:0 -  11:0 / 16:0\n**UTC-1**  5:0 / 10:0 -  12:0 / 17:0\n**UTC / GMT**: 6:0 / 11:0 -  13:0 / 18:0\n**UTC+1** **CET**: 7:0 / 12:0 -  14:0 / 19:0\n**UTC+2**  8:0 / 13:0 -  15:0 / 20:0\n**UTC+3** **MSK**: 9:0 / 14:0 -  16:0 / 21:0\n**UTC+4** **+04**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC+5** **IST**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC+6**  12:0 / 17:0 -  19:0 / 0:0\n**UTC+7**  13:0 / 18:0 -  20:0 / 1:0\n**UTC+8** **CST**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC+9** **JST**: 15:0 / 20:0 -  22:0 / 3:0\n**UTC+10**  16:0 / 21:0 -  23:0 / 4:0\n**UTC+11** **\nEDT**: 17:0 / 22:0 -  0:0 / 5:0\n**UTC+12**  18:0 / 23:0 -  1:0 / 6:0\n**UTC+13** **NZDT**: 19:0 / 0:0 -  2:0 / 7:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC+7','CST-1']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+7 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC-9**  20:0 / 1:0 -  3:0 / 8:0\n**UTC-8** **PST**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC-7** **MST**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC-6** **CST**: 23:0 / 4:0 -  6:0 / 11:0\n**UTC-5** **EST**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC-4**  1:0 / 6:0 -  8:0 / 13:0\n**UTC-3**  2:0 / 7:0 -  9:0 / 14:0\n**UTC-2**  3:0 / 8:0 -  10:0 / 15:0\n**UTC-1**  4:0 / 9:0 -  11:0 / 16:0\n**UTC / GMT**: 5:0 / 10:0 -  12:0 / 17:0\n**UTC+1** **CET**: 6:0 / 11:0 -  13:0 / 18:0\n**UTC+2**  7:0 / 12:0 -  14:0 / 19:0\n**UTC+3** **MSK**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC+4** **+04**: 9:0 / 14:0 -  16:0 / 21:0\n**UTC+5** **IST**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC+6**  11:0 / 16:0 -  18:0 / 23:0\n**UTC+7**  12:0 / 17:0 -  19:0 / 0:0\n**UTC+8** **CST**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC+9** **JST**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC+10**  15:0 / 20:0 -  22:0 / 3:0\n**UTC+11** **\nEDT**: 16:0 / 21:0 -  23:0 / 4:0\n**UTC+12**  17:0 / 22:0 -  0:0 / 5:0\n**UTC+13** **NZDT**: 18:0 / 23:0 -  1:0 / 6:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC+8','CST','JST-1']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+8 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC-9**  19:0 / 0:0 -  2:0 / 7:0\n**UTC-8** **PST**: 20:0 / 1:0 -  3:0 / 8:0\n**UTC-7** **MST**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC-6** **CST**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC-5** **EST**: 23:0 / 4:0 -  6:0 / 11:0\n**UTC-4**  0:0 / 5:0 -  7:0 / 12:0\n**UTC-3**  1:0 / 6:0 -  8:0 / 13:0\n**UTC-2**  2:0 / 7:0 -  9:0 / 14:0\n**UTC-1**  3:0 / 8:0 -  10:0 / 15:0\n**UTC / GMT**: 4:0 / 9:0 -  11:0 / 16:0\n**UTC+1** **CET**: 5:0 / 10:0 -  12:0 / 17:0\n**UTC+2**  6:0 / 11:0 -  13:0 / 18:0\n**UTC+3** **MSK**: 7:0 / 12:0 -  14:0 / 19:0\n**UTC+4** **+04**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC+5** **IST**: 9:0 / 14:0 -  16:0 / 21:0\n**UTC+6**  10:0 / 15:0 -  17:0 / 22:0\n**UTC+7**  11:0 / 16:0 -  18:0 / 23:0\n**UTC+8** **CST**: 12:0 / 17:0 -  19:0 / 0:0\n**UTC+9** **JST**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC+10**  14:0 / 19:0 -  21:0 / 2:0\n**UTC+11** **\nEDT**: 15:0 / 20:0 -  22:0 / 3:0\n**UTC+12**  16:0 / 21:0 -  23:0 / 4:0\n**UTC+13** **NZDT**: 17:0 / 22:0 -  0:0 / 5:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC+9','JST']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+9 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 17:0 / 22:0 -  0:0 / 5:0\n**UTC-9**  18:0 / 23:0 -  1:0 / 6:0\n**UTC-8** **PST**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC-7** **MST**: 20:0 / 1:0 -  3:0 / 8:0\n**UTC-6** **CST**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC-5** **EST**: 22:0 / 3:0 -  5:0 / 10:0\n**UTC-4**  23:0 / 4:0 -  6:0 / 11:0\n**UTC-3**  0:0 / 5:0 -  7:0 / 12:0\n**UTC-2**  1:0 / 6:0 -  8:0 / 13:0\n**UTC-1**  2:0 / 7:0 -  9:0 / 14:0\n**UTC / GMT**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC+1** **CET**: 4:0 / 9:0 -  11:0 / 16:0\n**UTC+2**  5:0 / 10:0 -  12:0 / 17:0\n**UTC+3** **MSK**: 6:0 / 11:0 -  13:0 / 18:0\n**UTC+4** **+04**: 7:0 / 12:0 -  14:0 / 19:0\n**UTC+5** **IST**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC+6**  9:0 / 14:0 -  16:0 / 21:0\n**UTC+7**  10:0 / 15:0 -  17:0 / 22:0\n**UTC+8** **CST**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC+9** **JST**: 12:0 / 17:0 -  19:0 / 0:0\n**UTC+10**  13:0 / 18:0 -  20:0 / 1:0\n**UTC+11** **\nEDT**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC+12**  15:0 / 20:0 -  22:0 / 3:0\n**UTC+13** **NZDT**: 16:0 / 21:0 -  23:0 / 4:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC+10','GST','JST+1']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+10 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 16:0 / 21:0 -  23:0 / 4:0\n**UTC-9**  17:0 / 22:0 -  0:0 / 5:0\n**UTC-8** **PST**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC-7** **MST**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC-6** **CST**: 20:0 / 1:0 -  3:0 / 8:0\n**UTC-5** **EST**: 21:0 / 2:0 -  4:0 / 9:0\n**UTC-4**  22:0 / 3:0 -  5:0 / 10:0\n**UTC-3**  23:0 / 4:0 -  6:0 / 11:0\n**UTC-2**  0:0 / 5:0 -  7:0 / 12:0\n**UTC-1**  1:0 / 6:0 -  8:0 / 13:0\n**UTC / GMT**: 2:0 / 7:0 -  9:0 / 14:0\n**UTC+1** **CET**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC+2**  4:0 / 9:0 -  11:0 / 16:0\n**UTC+3** **MSK**: 5:0 / 10:0 -  12:0 / 17:0\n**UTC+4** **+04**: 6:0 / 11:0 -  13:0 / 18:0\n**UTC+5** **IST**: 7:0 / 12:0 -  14:0 / 19:0\n**UTC+6**  8:0 / 13:0 -  15:0 / 20:0\n**UTC+7**  9:0 / 14:0 -  16:0 / 21:0\n**UTC+8** **CST**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC+9** **JST**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC+10**  12:0 / 17:0 -  19:0 / 0:0\n**UTC+11** **\nEDT**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC+12**  14:0 / 19:0 -  21:0 / 2:0\n**UTC+13** **NZDT**: 15:0 / 20:0 -  22:0 / 3:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC+11','AEDT']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+11 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10**  **HST**:  15:0  /  20:0  -  22:0  /  3:0\n**UTC-9**   16:0  /  21:0  -  23:0  /  4:0\n**UTC-8**  **PST**:  17:0  /  22:0  -  0:0  /  5:0\n**UTC-7**  **MST**:  18:0  /  23:0  -  1:0  /  6:0\n**UTC-6**  **CST**:  19:0  /  0:0  -  2:0  /  7:0\n**UTC-5**  **EST**:  20:0  /  1:0  -  3:0  /  8:0\n**UTC-4**   21:0  /  2:0  -  4:0  /  9:0\n**UTC-3**   22:0  /  3:0  -  5:0  /  10:0\n**UTC-2**   23:0  /  4:0  -  6:0  /  11:0\n**UTC-1**   0:0  /  5:0  -  7:0  /  12:0\n**UTCUTC**  **GMT**:  1:0  /  6:0  -  8:0  /  13:0\n**UTC+1**  **CET**:  2:0  /  7:0  -  9:0  /  14:0\n**UTC+2**   3:0  /  8:0  -  10:0  /  15:0\n**UTC+3**  **MSK**:  4:0  /  9:0  -  11:0  /  16:0\n**UTC+4**  **+04**:  5:0  /  10:0  -  12:0  /  17:0\n**UTC+5**  **IST**:  6:0  /  11:0  -  13:0  /  18:0\n**UTC+6**   7:0  /  12:0  -  14:0  /  19:0\n**UTC+7**   8:0  /  13:0  -  15:0  /  20:0\n**UTC+8**  **CST**:  9:0  /  14:0  -  16:0  /  21:0\n**UTC+9**  **JST**:  10:0  /  15:0  -  17:0  /  22:0\n**UTC+10**   11:0  /  16:0  -  18:0  /  23:0\n**UTC+11**  **\nEDT**:  12:0  /  17:0  -  19:0  /  0:0\n**UTC+12**   13:0  /  18:0  -  20:0  /  1:0\n**UTC+13**  **NZDT**:  14:0  /  19:0  -  21:0  /  2:0", inline=False)
     
     await message.channel.send(embed=embed)

 if message.content == "UTC+12":
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+12 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 14:0 / 19:0 -  21:0 / 2:0\n**UTC-9**  15:0 / 20:0 -  22:0 / 3:0\n**UTC-8** **PST**: 16:0 / 21:0 -  23:0 / 4:0\n**UTC-7** **MST**: 17:0 / 22:0 -  0:0 / 5:0\n**UTC-6** **CST**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC-5** **EST**: 19:0 / 0:0 -  2:0 / 7:0\n**UTC-4**  20:0 / 1:0 -  3:0 / 8:0\n**UTC-3**  21:0 / 2:0 -  4:0 / 9:0\n**UTC-2**  22:0 / 3:0 -  5:0 / 10:0\n**UTC-1**  23:0 / 4:0 -  6:0 / 11:0\n**UTC / GMT**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC+1** **CET**: 1:0 / 6:0 -  8:0 / 13:0\n**UTC+2**  2:0 / 7:0 -  9:0 / 14:0\n**UTC+3** **MSK**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC+4** **+04**: 4:0 / 9:0 -  11:0 / 16:0\n**UTC+5** **IST**: 5:0 / 10:0 -  12:0 / 17:0\n**UTC+6**  6:0 / 11:0 -  13:0 / 18:0\n**UTC+7**  7:0 / 12:0 -  14:0 / 19:0\n**UTC+8** **CST**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC+9** **JST**: 9:0 / 14:0 -  16:0 / 21:0\n**UTC+10**  10:0 / 15:0 -  17:0 / 22:0\n**UTC+11** **\nEDT**: 11:0 / 16:0 -  18:0 / 23:0\n**UTC+12**  12:0 / 17:0 -  19:0 / 0:0\n**UTC+13** **NZDT**: 13:0 / 18:0 -  20:0 / 1:0", inline=False)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['UTC+13','NZDT']]):
     embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg", color=0xe6a3a3)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327957161213963/BossTitan_large.jpg")
     embed.add_field(name=" UTC+13 Clan battle times\n 1st phase: start / end - 2nd phase: start / end ", value="**UTC-10** **HST**: 13:0 / 18:0 -  20:0 / 1:0\n**UTC-9**  14:0 / 19:0 -  21:0 / 2:0\n**UTC-8** **PST**: 15:0 / 20:0 -  22:0 / 3:0\n**UTC-7** **MST**: 16:0 / 21:0 -  23:0 / 4:0\n**UTC-6** **CST**: 17:0 / 22:0 -  0:0 / 5:0\n**UTC-5** **EST**: 18:0 / 23:0 -  1:0 / 6:0\n**UTC-4**  19:0 / 0:0 -  2:0 / 7:0\n**UTC-3**  20:0 / 1:0 -  3:0 / 8:0\n**UTC-2**  21:0 / 2:0 -  4:0 / 9:0\n**UTC-1**  22:0 / 3:0 -  5:0 / 10:0\n**UTC / GMT**: 23:0 / 4:0 -  6:0 / 11:0\n**UTC+1** **CET**: 0:0 / 5:0 -  7:0 / 12:0\n**UTC+2**  1:0 / 6:0 -  8:0 / 13:0\n**UTC+3** **MSK**: 2:0 / 7:0 -  9:0 / 14:0\n**UTC+4** **+04**: 3:0 / 8:0 -  10:0 / 15:0\n**UTC+5** **IST**: 4:0 / 9:0 -  11:0 / 16:0\n**UTC+6**  5:0 / 10:0 -  12:0 / 17:0\n**UTC+7**  6:0 / 11:0 -  13:0 / 18:0\n**UTC+8** **CST**: 7:0 / 12:0 -  14:0 / 19:0\n**UTC+9** **JST**: 8:0 / 13:0 -  15:0 / 20:0\n**UTC+10**  9:0 / 14:0 -  16:0 / 21:0\n**UTC+11** **\nEDT**: 10:0 / 15:0 -  17:0 / 22:0\n**UTC+12**  11:0 / 16:0 -  18:0 / 23:0\n**UTC+13** **NZDT**: 12:0 / 17:0 -  19:0 / 0:0", inline=False)
     
     await message.channel.send(embed=embed)

########################################################################

 if message.content == 'Rebirth':
     embed=discord.Embed(title="", url="", color=0xffffff)
     embed.set_author(name="")
     embed.set_thumbnail(url="")
     embed.add_field(name="'Rebirth' isn't a valid command", value="Use 'Rebirth3' or 'Rebirth4' instead", inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['Rebirth3','RebirthNat3','Reb3','rebirth3','renaissance3','renaissances3']]):
     embed=discord.Embed(title="__**Nat3 Renaissances**__", url="", color=0xffffff)
     embed.set_author(name="")
     embed.set_thumbnail(url="")
     embed.add_field(name="1ère année (16/17)", value="Septembre: Miho\nOctobre: Stella\nNovembre: Chasseur\nDecembre: Miho + L/D Victoria\nJanvier: Médusine\nFévrier: Mona + Dark Truffel\nMars: Médusa + Light Bon\nAvril: Monkiki + L/D Stella\nMai: Chasseur + L/D Victoria\nJuin: Cocomaru + Light Gemini\nJuillet: Phibian\nAoût: Latt + L/D Otari\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ", inline=True)
     embed.add_field(name="2ème année (17/18)", value="Septembre: Radic\nOctobre: Piou + L/D Miho\nNovembre: Yeti + Feu Dartagnan\nDecembre: Gren\nJanvier: Fennec\nFévrier: Kiki\nMars: Misha\nAvril: Stella\nMai: Mowgli\nJuin: Ramu\nJuillet: Phibian\nAoût: Bulbie\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ", inline=True)
     embed.add_field(name="3ème année (18/19)", value="Septembre: Spectre des sables\nOctobre: Chasseur\nNovembre: Piou\nDecembre: Yeti\nJanvier: Fennec\nFévrier: Kiki\nMars: Misha\nAvril: Phibian\nMai: Bulbie + L/D Miho\nJuin: Stella\nJuillet: Gren\nAoût: Spectre des sables\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ", inline=True)
     embed.add_field(name="4ème année (19/20)", value="Septembre: Médusine, L/D Fennec\nOctobre: Mowgli\nNovembre: Yéti, L/D Miho\nDécembre: Bulbie\nJanvier: Latt, L/D Mona\nFévrier: Radic\nMars: Phibian, L/D Stella\nAvril: Kiki\nMai: Piou, L/D Cocoramu\nJuin: Gren \nJuillet: Misha, Monkiki L/D\n Août: Spectre des sables\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ", inline=True)
     embed.add_field(name="5ème année (20/21)", value="Septembre: Médusine, Fennec\nOctobre: Mowgli\nNovembre: Yeti, L/D Miho\nDécembre: \nJanvier: \nFévrier: \nMars: \nAvril: \nMai: \nJuin: \nJuillet: \n Août: \n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ", inline=True)

     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['Rebirth4','RebirthNat4','Reb4','rebirth4','renaissance4','renaissances4']]):
     embed=discord.Embed(title="__**Nat4 Renaissances**__", url="", color=0xffffff)
     embed.set_author(name="")
     embed.set_thumbnail(url="")
     embed.add_field(name="1ère année (16/17)", value="Septembre à Mars: - -\n\n\n\nAvril: Thor\nmi-Mai: Verde\nJuillet: Sparkitt\nmi-Août: Fée\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="2ème année (17/18)", value="Octobre: Canna\nmi-Novembre: Incubus\nJanvier: Thor\nmi-Février: Lucy\nAvril: Benjabuton\nmi-Mai: Sphinx\nJuillet: Verde\nmi-Août: Sparkitt\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="3ème année (18/19)", value="Octobre: Fée\nmi-Novembre: Somnol\nJanvier: Pégase\nmi-Février: Canna\nAvril: Incubus\nmi-Mai: Lucy\nJuillet: Thor\nAoût: Benjabuton\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="4ème année (19/20)", value="Septembre: Verde\nOctobre: Sphinx\nNovembre: Sparkitt\nDécembre: Fée\nJanvier: Arlequin\nFévrier: Pégase, Canna\nMars: Incubus, Lucy\nAvril: Thor, Benjamin\nMai: Sphinx, Verde \nJuin: Sparkitt \nJuillet: Arlequin, Somnol\n Août: Pégase, Canariah\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ", inline=True)
     embed.add_field(name="5ème année (20/21)", value="Septembre: Incubus\nOctobre: Lucy, Thor\nNovembre: Benjabuton\nDécembre: \nJanvier: \nFévrier: \nMars: \nAvril: \nMai: \nJuin: \nJuillet: \n Août: \n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ", inline=True)

     await message.channel.send(embed=embed)

 if message.content.startswith('exotique'):
     embed=discord.Embed(title="__**Exotiques**__", url="", color=0xffffff)
     embed.set_author(name="")
     embed.set_thumbnail(url="")
     embed.add_field(name="1ère année (16/17)", value="Septembre: - -\nOctobre: L/D Citrouillon\nNovembre: Félinelame\nDecembre: Eau Givri\nJanvier: L/D Givri\nFévrier: Dark Truffel\nMars: Venus + Eau/Light Bon\nAvril: Pinolo\nMai: Félinelame\nJuin: Gemini\nJuillet: Eau yeti + Eau Penpen\nAoût: Torpin\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="2ème année (17/18)", value="Septembre: Mini Seira\nOctobre: L/D Citrouillon\nNovembre: Dartagnan\nDecembre: Rudolph\nJanvier: Sacstère\nFévrier: Tanya\nMars: Flora\nAvril: Sherlock + Pinolo\nMai: Bon + Venus\nJuin: Gemini\nJuillet: Alpaca\nAoût: Mari\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="3ème année (18/19)", value="Septembre: Mini Tina\nOctobre: Citrouillon\nNovembre: Torpin\nDecembre: Rudolph + Givri\nJanvier: Soldat Slime\nFévrier: Sacstère\nMars: Jiangshi\nAvril: Flora\nMai: Gemini\nJuin: Félinelame\nJuillet: Sonic + Silver\nAoût: Knuckles + Shadow\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="4ème année (19/20)", value="Septembre: Mini Camilla\nOctobre: Cerise\nNovembre: Baby Shark\nDécembre: Rudolph + Givri\nJanvier: Sacstère\nFévrier: Tanya\nMars: Alpaca\nAvril: Pinolo\nMai: Jiangshi\nJuin: Baby Shark \nJuillet: Pip \n Août: Mary\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ", inline=True)
     embed.add_field(name="5ème année (20/21)", value="Septembre: Mini Zephyros\nOctobre: Cerise\nNovembre: Citrouillon\nDécembre: \nJanvier: \nFévrier: \nMars: \nAvril: \nMai: \nJuin: \nJuillet: \n Août: \n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ", inline=True)

     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['ToC','Toc']]):
     embed=discord.Embed(title="__**Tour du Chaos 1 à 100**__", url="", color=0xffffff)
     embed.set_author(name="")
     embed.set_thumbnail(url="")
     embed.add_field(name="Etages 5 à 50\n\nBoss + autres monstres\n*-> Récompense*", value="**5 - Miho Feu** + Arch Feu\n*-> energies x20*\n**10 - Garuda Bois** + Buis Bois\n*-> gold x100k*\n**15 - Valk Eau** + Cotonou Eau\n*-> energies x20*\n**20 - Cauchemar Dark** + Kiloptère Dark\n*-> fruits x5*\n**25 - Bast Feu** + Pottus Bois\n*-> energies x20*\n**30 - Sanzang Feu** + monkiki Feu\n*-> AG x100*\n**35 - Eau Onmyoji** + Beth Eau\n*-> energies x20*\n**40 - Merlin Eau** + Gren Bois\n*-> Oeuf 3/5 x3*\n**45 - Indra Dark** + Cosmo Light\n*-> energies x20*\n**50 - Draka Feu** + Médusa Feu\n*-> Nova sacrée*\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="Etages 50 à 100\n\nBoss + autres monstres\n*-> Récompense*", value="**55 - Shiva Feu** + Misha Feu\n*-> energies x20*\n**60 - Shinobi Bois** + Hana Bois\n*-> Sceaux du dragon x10*\n**65 - Siegfried Feu** + Leo Feu\n*-> energies x20*\n**70 - Balrona Feu** + Cayou Feu\n*-> AG x300*\n**75 - Poseidon Eau** + Lermite Eau\n*-> energies x20*\n**80 - Odin Dark** + Loki Bois\n*-> Oeuf 4/5 (B,E,F)*\n**85 - Sanzang Bois** + Verde Bois\n*-> energies x20*\n**90 - Artemis Bois** + Fée Bois\n*-> gold x300k*\n**95 - Arthur Light** + Benjabuton Light\n*-> energies x20*\n**100 - Hades Dark** + Persephone Dark\n*-> Oeuf nat5 (E,B,F)*\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ", inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('heal'):
     embed=discord.Embed(title="__**Heals à Up**__", url="", color=0xffffff)
     embed.set_author(name="")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/709371051938676766/heal2.jpg")
     embed.add_field(name="Feu", value="Cura (x2)\nCupidon (x2)\nCerise/Fée (x2)\nCotonou (x2)\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="Bois", value="Hana (x4)\nChapillon (2 mini)\nBast\nCupidon\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="Eau", value="Cotonou (x2)\nMildeu (x2)\nBast\nCura\nChapillon\nCerise\nLumo\nSirène\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="Dark/Light", value="Vénus\nShark (2 mini)\nHana\nMildeu\nSirène\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('gemmage'):
     embed=discord.Embed(title="__**Gemmage standard des astromons**__", url="", color=0xffffff)
     embed.set_author(name="")
     embed.set_thumbnail(url="")
     embed.add_field(name="Attaquants + FC", value="__Gemmage de base :__ Atk/Atk/PV ou Atk/TC/PV\n__Gemmage mi-partie :__ Atk/Atk/TC\n__Gemmage fin de partie :__ Atk/Atk/DC\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="Breakers", value="PV/PV/Def ou PV/Def/Def\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     embed.add_field(name="Healers", value="PV/Def/Recup\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
     
     await message.channel.send(embed=embed)
       
######################################################################## 
###########                skillcommands
########################################################################

 if message.content.startswith('adre'):
     embed=discord.Embed(title='Restaure les PV en attaquant', url='', color=0xffffff)
     embed.set_author(name='Adrénaline')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_andren.png')
     embed.add_field(name='(Passif)', value='**Feu**: Chloe, Somnol, Mari, Misha, Fée, Sanzang, Truffel, Vampire\n**Eau**: Cupidon, Gargor, Sacstère, Incubus, Lupin, Mari, Persephone, Peyote, Phibian, Sirène, Wendigo\n**Bois**: Cura, Cerise, Mammont, Mona, Valkyrie\n**Light**: Cosmo, Gemini, Sacstère, Mildeu, Mona, Pinolo, Pinolo Lie, Sura, Venus\n**Dark**: Artemis, Citrouillon, Médusine, Kiki, Latt, Mammont, Sirène, Soldat Slime, Yaksha\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Chloe, Gargor, Mammont, Peyote, Ramu, Shiva, Sura\n**Eau**: Gargor, Médusine, Cauchemar, Peyote\n**Bois**: Cauchemar, Valkyrie\n**Light**: Odin, Pégase, Penpen, Sha wujing, Succube, Sura, Verde\n**Dark**: Balrona, Piou, Nifa, Phibian, Wendigo\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('agressiondef'):
     embed=discord.Embed(title="L'attaque devient proportionnelle à la défense max du lanceur", url='', color=0xffffff)
     embed.set_author(name='Agression (Def)')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_selfreplacedattackbymaxhp.png')
     embed.add_field(name='(Passif)', value='**Feu**:  Griffon\n**Eau**: Sanzang\n**Bois**:  - -\n**Light**:  Cupidon, Gren, Mari, Mera, Cauchemar, Victoria\n**Dark**: Monkiki, Stella, Siegfried,\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Griffon\n**Eau**: Scarabo, Sanzang\n**Bois**: Dartagnan\n**Light**: Mari, Mona, Victoria, Zhu Bajie \n**Dark**: Anu, Dartagnan, Radic, Stella, Siegfried\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('agressionpv'):
     embed=discord.Embed(title="L'attaque devient proportionnelle aux PVs max du lanceur", url='', color=0xffffff)
     embed.set_author(name='Agression (PV)')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_selfreplacedattackbymaxhp.png')
     embed.add_field(name='(Passif)', value='**Feu**: Jeanne\n**Eau**:  - -\n**Bois**: Draka\n**Light**: Cocomaru, Flora, Odin, Cocoramu\n**Dark**: Arthur, Piou, Cupidon, Sacstère, Miho, Lupio, Zhu Bajie, Slime\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Anu\n**Eau**: Griffon\n**Bois**: Draka, Hadès\n**Light**: Félinelame, Cocomaru, Shiva, Jeanne\n**Dark**: Banshee, Médusine, Miho, Mini Camilla, Lupio, Zhu Bajie, Slime\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['brkatk','attaquereduite','breakattaque']]):

     embed=discord.Embed(title="Réduit l'attaque de l'ennemi de 50%", url='', color=0xffffff)
     embed.set_author(name='Attaque réduite')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_debuffattack.png')
     embed.add_field(name='(Passif)', value='**Feu**: Ammonore, Chiroptie, Cocomaru, Cupidon, Incubus, Végédalle, Miho, Taupinou, Nezha, Spectre des sables, Slime, Soldat Slime, Sphinx, Ecurrix, Yaksha\n**Eau**: Rubani, Dartagnan, Enkidu, Félinelame, Indra, Lucy, Nezha, Penpen, Yeti\n**Bois**: Scarabo, Canna, Hana, Médusine, Djinn, Lumo, Lupin, Mimic, Pégase, Torpin, Radic, Pottus, Sanzang, Verde, Lombrix\n**Light**: Ammonore, Poulichon, Kiloptère, Loki, Mammont, Peyote, Robobot, Shark\n**Dark**: Chloe, Cocomaru, Spectros, Leo, Nifa, Otari, Rudolph, Givri, Crapora, Truffel, Venus\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Arch, Tipiaf, Chiroptie, Fennec, Citrouillon, Odin, Penpen, Sherlock, Shinobi, Slime, Ecurrix\n**Eau**: Arlequin, Arthur, Canna, Fennec, Latt, Lucy, Mari, Otari, Sherlock, Succube\n**Bois**: Fennec, Leo, Lupin, Mimic, Persephone, Torpin, Radic, Sanzang, Sherlock, Sparkitt\n**Light**: Flora, Gemini, Gren, Miho, Stella, Wendigo\n**Dark**: Ammonore, Médusa, Poseidon, Pinolo, Robobot, Tigar, Truffel, Vampire\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['attaqueaug','attaqueup']]):

     embed=discord.Embed(title="Augmente l'attaque du lanceur et des alliés de 50%", url='', color=0xffffff)
     embed.set_author(name='Attaque augmentée ')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_buffattack.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Cernunnos,Cotonou, Cupidon, Mildeu\n**Eau**: Sonic, Cura, Lumo\n**Bois**: Bast, Sacstère, Chapillon\n**Light**: Gilgamesh, Hohenheim, Sacstère, Shark, Zabeille\n**Dark**: Cerise, Shadow, Venus, Zabeille\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('vague'):
     embed=discord.Embed(title='Restaure les PV et PA en attaquant', url='', color=0xffffff)
     embed.set_author(name='Vague martiale')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_selfhealmyhpmpbypercentfrommaxhpmpourteam.png')
     embed.add_field(name='(Passif)', value='**Feu**: Bast\n**Eau**: Hohenheim\n**Bois**: Sha wujing\n**Light**: imperio, Jormungandr, Mini Seira, Misha, Sanzang, Shiva\n**Dark**: Shadow, Fennec, Gilgamesh, Imperio, Mari, Mini Seira, Odin, Pip, Phibian, Fée, Poseidon, Tigar, Zephyros\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('aveugl'):
     embed=discord.Embed(title='Diminue les dégâts critiques et le taux critique de la cible de 50%', url='', color=0xffffff)
     embed.set_author(name='Aveuglement')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707515279613231195/se_debuffcriticalprob.png')
     embed.add_field(name='(Passif)', value='**Feu**: Verde\n**Eau**: Benjabuton, Sparkitt\n**Bois**:  - -\n**Light**: Nezha, Spectre des sables\n**Dark**: Médusa, Sphinx\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Otari, Phibian, Sparkitt, Yaksha, Yeti\n**Eau**: Benjabuton, Kiki, Nezha, Penpen\n**Bois**: Médusa, Misha, Thor, Zhu Bajie \n**Light**: Mammont, Monkiki, Pinolo Lie\n**Dark**: Cocomaru, Otari\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('amesbl'):
     embed=discord.Embed(title='Compétence inutile ...', url='', color=0xffffff)
     embed.set_author(name="Abondance d'âmes bleues")
     embed.set_thumbnail(url='')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**: Lumo\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('brisebon'):
     embed=discord.Embed(title='Dissipe tous les effets excepté le bouclier', url='', color=0xffffff)
     embed.set_author(name='Brise-Bonus')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_clearbuff.png')
     embed.add_field(name='(Passif)', value='**Feu**: Alpaca, Crustarov\n**Eau**: Kiki\n**Bois**:  - -\n**Light**: Lupio\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**: Bulbie\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['frappec','fc','FC']]):
     embed=discord.Embed(title="L'attaque augmente considérablement en fonction des PVs max de la cible", url='', color=0xffffff)
     embed.set_author(name='Frappe Courageuse')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_selfadddamagebyenemymaxhp.png')
     embed.add_field(name='(Passif)', value='**Feu**: Poseidon, Shinobi\n**Eau**: Balrona, Arlequin\n**Bois**: Merlin, Pinolo, Pinolo Lie, Thor, Zhu Bajie, Enkidu \n**Light**: Cernunnos, Siegfried, Wendigo, Gilgamesh\n**Dark**: Indra, Jormungandr, Sha wujing\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Incubus, Sha wujing, Sun Wukong, Verde\n**Eau**: Hades, Indra, Siegfried, Sparkitt, Gilgamesh\n**Bois**: Canna, Garuda, Merlin, Pinolo Lie\n**Light**: Siegfried, Enkidu, Tipiaf\n**Dark**: Chloe, Indra, Thor\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['degatscrit','dcrit']]):
     embed=discord.Embed(title='Augmente les dégâts critiques sur la cible de 20%?', url='', color=0xffffff)
     embed.set_author(name='Dégâts critiques augmentés')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_n_criticalsup.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**: Hohenheim\n**Bois**:  - -\n**Light**: Hohenheim\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)


 if message.content.startswith('maledic'):
     embed=discord.Embed(title="Les dégâts sont égaux à l'attaque de la cible", url='', color=0xffffff)
     embed.set_author(name='Malédiction')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_n_curse.png')
     embed.add_field(name='(Passif)', value='**Feu**: Banshee, Hades\n**Eau**: Jiangshi\n**Bois**:  - -\n**Light**:  - -\n**Dark**: Hades, Jiangshi\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: - -\n**Eau**: Jiangshi, Jormungandr\n**Bois**:  - -\n**Light**:  - -\n**Dark**: - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['degats-50','dgt-50']]):
     embed=discord.Embed(title='Réduit les dégâts reçus de 50%', url='', color=0xffffff)
     embed.set_author(name='Dégâts -50%')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_n_reducedamage.png')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**: Sonic\n**Bois**:  - -\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['reductionde']]):
     embed=discord.Embed(title='Réduit les dégâts reçus', url='', color=0xffffff)
     embed.set_author(name='Réduction de dégâts')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_n_reducedamage.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**: Enkidu\n**Light**: Silver, Valk\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['chasseurd','darkchas']]):
     embed=discord.Embed(title='Confère un bonus de dégâts critiques sur les monstres de type dark (en %)', url='', color=0xffffff)
     embed.set_author(name='Chasseur (dark)')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_selfbuffcriticaldamage.png')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**: Mowgli\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**: Mino\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['predateurd','darkpreda']]):
     embed=discord.Embed(title='Augmente les dégâts sur les monstres de type dark (en %)', url='', color=0xffffff)
     embed.set_author(name='Prédateur (dark)')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_selfadddamagebyelement.png')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  - -\n**Dark**: Chiroptie, Tai\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**: Mowgli\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['traqueurd','darktraq']]):
     embed=discord.Embed(title='Taux critique supplémentaire sur les monstres de type dark (en %)', url='', color=0xffffff)
     embed.set_author(name='Traqueur (Dark)')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_selfbuffcriticalprob.png')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  - -\n**Dark**: Kiloptère, Peyote\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['defensered','breakdef']]):
     embed=discord.Embed(title='Réduit la défense de la cible de 70%', url='', color=0xffffff)
     embed.set_author(name='Défense réduite')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707574095713140816/se_debuffdefence.png')
     embed.add_field(name='(Passif)', value='**Feu**: Scarabo, Tipiaf, Lumignon, Dartagnan, Hohenheim, Citrouillon, Lumo, Cauchemar, Odin, Otari, Phibian, Tincel, Sun Wukong, Thor, Tigar, Yuki\n**Eau**: Anu, Canna, Cerise, Garuda, Gren, Hades, Latt, Monkiki, Pégase, Clamy, Soldat Slime, Victoria\n**Bois**: Tails, Arch, Bast, Chiroptie, Félinelame, Leo, Loki, Mari, Miho, Phibian, Siegfried, Slime, Ecurrix, Sun Wukong\n**Light**: Anu, Zabeille, Bon, Fée, Fenrir, Sun Wukong, Yaksha, Zarid\n**Dark**: Scarabo, Benjabuton, Cerise, Poulichon, Thor\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Arthur, Lumignon, Kiki, Lupin, Nezha, Onmyoji, Pip, Tincel, Crustarov, Succube, Thor, Lombrix, Yuki\n**Eau**: Balrona, Gren, Mera, Mona, Pincemi, Tigar, Valkyrie, Victoria, Yeti\n**Bois**: Banshee, Chiroptie, Croquignol, Somnol, Mammont, Mari, Odin, Phibian, Pottus, Stella, Sha wujing, Slime, Ecurrix, Crustarov, Sun Wukong, Verde, Zarid\n**Light**: Bon, Fennec, Médusine, Kiloptère, Latt, Loki, Peyote, Ramu, Sparkitt, Thor, Vampire\n**Dark**: Jormungandr, Monkiki, Nezha, Odin, Victoria\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['defenseaug','defup']]):
     embed=discord.Embed(title='Augmente la défense de 70%', url='', color=0xffffff)
     embed.set_author(name='Défense augmentée')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707575259926102036/se_buffdefence.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Cerise, Fée\n**Eau**: Bast, Cotonou, Mildeu\n**Bois**: Hana\n**Light**: Cerise\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('domina'):
     embed=discord.Embed(title='Diminue les PA de la cible en attaquant', url='', color=0xffffff)
     embed.set_author(name='Domination')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707575568002056212/se_decenemympbyenemydamage.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Bast\n**Eau**: Cernunnos, Fée\n**Bois**:  - -\n**Light**: Cura, Mildeu\n**Dark**: Cotonou, Sirène\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['avantage']]):
     embed=discord.Embed(title="Les dégâts comptent comme la faiblesse élémentaire de la cible", url='', color=0xffffff)
     embed.set_author(name='Avantage élémentaire')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707575571680329758/se_selfadddamagebyabsoluteelement.png')
     embed.add_field(name='(Passif)', value='**Feu**: Indra\n**Eau**: Shinobi\n**Bois**: Sparkitt\n**Light**: Artemis, Indra, Sphinx\n**Dark**: Arlequin, Garuda, Gren\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Balrona, Siegfried, Soldat Slime\n**Eau**: Garuda, Merlin, Soldat Slime\n**Bois**: Pip, Soldat Slime\n**Light**: Artemis, Balrona, Draka, Somnol, Hades, Médusa, Merlin, Mini Seira, Mini Tina, Poseidon, Soldat Slime\n**Dark**: Alpaca, Garuda, Mini Seira, Soldat Slime\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['faiblesse','expose']]):
     embed=discord.Embed(title='Double les dégâts sur la cible lors de la prochaine attaque (Premier attaquant seulement)', url='', color=0xffffff)
     embed.set_author(name='Faiblesse exposée')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707576549435637810/se_ongoingweakpoint.png')
     embed.add_field(name='(Passif)', value='**Feu**: Sha Wujing\n**Eau**: Siegfried\n**Bois**: Chapillon, Sphinx, Yuki\n**Light**: Kiki, Sherlock\n**Dark**: Bulbie\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Spectre des sables\n**Eau**:  - -\n**Bois**: Tails, Yuki\n**Light**: Mini Camilla, Tipiaf, Sherlock\n**Dark**: Bulbie, Lucy\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('fati'):
     embed=discord.Embed(title='La cible ne gagne rien des âmes bleues', url='', color=0xffffff)
     embed.set_author(name='Fatigue')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707576696802508890/se_debuffmpcrystalrecovery.png')
     embed.add_field(name='(Passif)', value='**Feu**: - -\n**Eau**: Mandragore, Tincel, Crustarov\n**Bois**: Mera, Penpen\n**Light**:  - -\n**Dark**: Mimic, Gravel\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Zarid\n**Eau**: Dartagnan, Végédalle, Tincel\n**Bois**: Félinelame, Latt\n**Light**: Ammonore, Robobot\n**Dark**: Mimic\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('intrepide'):
     embed=discord.Embed(title="Réduit les dégâts reçus + Empêche la cible d'utiliser son talent actif en le forçant à attaquer le lanceur", url='', color=0xffffff)
     embed.set_author(name='Provocation intrépide')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707577210520993813/se_provokeme.png')
     embed.add_field(name='(Passif)', value='**Feu**: Jiangshi, Victoria\n**Eau**: Champi, Leo, Zhu Bajie\n**Bois**: Poseidon\n**Light**: Mandragore, Miho, Zhu Bajie \n**Dark**: Tanya\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Arch\n**Eau**: Lermite\n**Bois**: Mona\n**Light**: Cauchemar, Arlequin \n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('acer'):
     embed=discord.Embed(title="Inflige une contre-attaque proportionnelle aux dégats subits pendant 1 tour et confère 100% de chance d'attirer l'attention des ennemis pendant 1 tours", url='', color=0xffffff)
     embed.set_author(name='Provocation acérée')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707577210520993813/se_provokeme.png')
     embed.add_field(name='(Passif)', value='**Feu**: - -\n**Eau**: Griffon\n**Bois**: - -\n**Light**: - -\n**Dark**: - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: - -\n**Eau**: - -\n**Bois**: - -\n**Light**: - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)	   

 if any([message.content.startswith (item) for item in ['chasseurfeu','feuchas']]):
     embed=discord.Embed(title='Confère un bonus de dégâts critiques sur les monstres de type feu (en %)', url='', color=0xffffff)
     embed.set_author(name='Chasseur (feu)')
     embed.set_thumbnail(url='')
     embed.add_field(name='(Passif)', value='**Feu**: Poulpo\n**Eau**: Fennec, Mowgli\n**Bois**:  - -\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**: Mino\n**Bois**:  - -\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['predateurfeu','feupreda']]):
     embed=discord.Embed(title='Augmente les dégâts sur les monstres de type feu (en %)', url='', color=0xffffff)
     embed.set_author(name='Prédateur (feu)')
     embed.set_thumbnail(url='')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**: Beth, Bron\n**Bois**:  - -\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Clamy\n**Eau**: Beth, Mowgli\n**Bois**:  - -\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['traqueurfeu','feutraq']]):

     embed=discord.Embed(title='Taux critique supplémentaire sur les monstres de type feu (en %)', url='', color=0xffffff)
     embed.set_author(name='Traqueur (feu)')
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/606439170809921549/607403889863688209/se_selfbuffcriticalprob.png')
     embed.add_field(name='(Passif)', value='**Feu**: Pincemi\n**Eau**: Croquignol, Sherlock\n**Bois**:  - -\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('foudroy'):
     embed=discord.Embed(title='Dégâts bonus en fonction du nombre de malédictions appliquées.', url='', color=0xffffff)
     embed.set_author(name='Malédiction foudroyante')
     embed.set_thumbnail(url='http://msldb.moy.su/sk/se_n_curseexplosion.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Banshee, Hades\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  - -\n**Dark**: Hades, Jiangshi\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('maledictionfou'):
     return

 if any([message.content.startswith (item) for item in ['siphondepv','siphonpv']]):
     embed=discord.Embed(title='Restaure les PVs en fonction des dégâts occasionnés', url='', color=0xffffff)
     embed.set_author(name='Siphon de PV')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707577799291961385/se_andren.png')
     embed.add_field(name='(Passif)', value='**Feu**: Balrona, Enkidu, Gemini, Médusine, Lucy, Pégase, Succube, Fenrir\n**Eau**: Chasseur, Sun Wukong\n**Bois**: Artemis, Arthur, Tipiaf, Nezha, Odin\n**Light**: Incubus, Givri, Vampire\n**Dark**: Canna, Incubus, Nezha, Onmyoji, Sanzang, Sura\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Gemini, Gilgamesh, Mera, Miho, Wendigo, Fenrir\n**Eau**: Chasseur, Sphinx, Sun Wukong\n**Bois**: Artemis, Tipiaf\n**Light**: Scarabo, Chasseur, Jiangshi, Givri\n**Dark**: Canna, Onmyoji\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('chasseur'):
     embed=discord.Embed(title='Confère un bonus de dégâts critiques (en %)', url='', color=0xffffff)
     embed.set_author(name='Chasseur')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707577956138221644/chasseur.png')
     embed.add_field(name='(Passif)', value='**Feu**: Croquignol, Fennec, Leo, Mowgli, Poulpo, Yeti\n**Eau**: Fennec, Loki, Mammont, Mowgli, Onmyoji, Poulpo\n**Bois**: Alpaca, Anu, Lumignon, Fennec, Mowgli, Pip, Poulpo\n**Light**: Fennec, Djinn, Monkiki, Mowgli, Nifa\n**Dark**: Enkidu, Griffon, Lucy, Mandragore, Mowgli, Pinolo Lie\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Leo, Mandragore, Merlin, Mino, Pégase, Vampire\n**Eau**: Enkidu, Mammont, Mino, Onmyoji\n**Bois**: Anu, Incubus, Kiki, Mino, Champi, Yaksha\n**Light**: Imperio, Indra, Citrouillon, Djinn, Mino, Nifa, Tigar\n**Dark**: Scarabo, Somnol, Félinelame, Griffon, Hohenheim, Latt, Lupin, Mandragore, Mini Tina, Mino, Mona, Pégase, Pinolo Lie, Rudolph, Sanzang, Shinobi, Sura\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['chasseurlight','lightchas']]):
     embed=discord.Embed(title='Confère un bonus de dégâts critiques sur les monstres de type light (en %)', url='', color=0xffffff)
     embed.set_author(name='Chasseur (light)')
     embed.set_thumbnail(url='')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  - -\n**Dark**: Mowgli\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  - -\n**Dark**: Mino\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['lightpredateur','predalight']]):
     embed=discord.Embed(title='Augmente les dégâts sur les monstres de type light (en %)', url='', color=0xffffff)
     embed.set_author(name='Prédateur (light)')
     embed.set_thumbnail(url='')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**: Chiroptie, Tai\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  - -\n**Dark**: Poulichon, Mowgli\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('frappeimpi'):
     embed=discord.Embed(title='Dégâts bonus en fonction du nombre de debuffs appliqués sur la cible', url='', color=0xffffff)
     embed.set_author(name='Frappe impitoyable')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707578372271767562/se_selfaddattackbytargetdebuffcount.png')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**: Tanya\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**: Misha\n**Bois**:  - -\n**Light**: Tanya\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['boostmoral','boostdemoral']]):
     embed=discord.Embed(title='Restaure les PA en fonction des degats occasionnés', url='', color=0xffffff)
     embed.set_author(name='Boost de moral')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707578556837789706/se_amfetamin.png')
     embed.add_field(name='(Passif)', value='**Feu**: Cura, Draka, Sacstère, Chasseur, Croquignol, Djinn, Jormungandr, Merlin, Mino, Penpen, Radic, Siegfried, Sura, Valkyrie\n**Eau**: Alpaca, Arthur, Cura, Lermite, Djinn, Merlin, Chapillon, Mino, Mona, Poseidon, Succube, Thor\n**Bois**: Balrona, Banshee, Gargor, Chasseur, Incubus, Jormungandr, Mino, Champi, Cauchemar, Peyote, Rudolph, Vampire, Wendigo\n**Light**: Piou, Chloe, Dartagnan, Citrouillon, Griffon, Jiangshi, Leo, Mini Tina, Mino, Otari, Persephone, Poseidon, Ramu, Gravel, Sirène, Soldat Slime, Succube, Crapora, Yeti\n**Dark**: Balrona, Bast, Cura, Félinelame, Jeanne, Mildeu, Mini Tina, Mino, Mona, Cauchemar, Pégase, Penpen, Persephone, Sparkitt, Tipiaf\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Hana\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  Succube\n**Dark**: Cura\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)
 
 if message.content.startswith('perseverance'):
     embed=discord.Embed(title="Augmente l'attaque à chaque tour (jusqu'à 10 tours)", url='', color=0xffffff)
     embed.set_author(name='Persévérance')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707578755098476594/se_selfaddattackbyturnaccumulate.png')
     embed.add_field(name='(Passif)', value='**Feu**: Knuckles\n**Eau**:  - -\n**Bois**:  - -\n**Light**: Benjabuton\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Knuckles\n**Eau**:  - -\n**Bois**: Gilgamesh\n**Light**: Benjabuton\n**Dark**: Benjabuton, Enkidu, Spectre des sables, Zephyros\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)
       
 if message.content.startswith('petri'):
     embed=discord.Embed(title='Immobilise la cible mais augmente tres fortement sa défense (Défense x10)', url='', color=0xffffff)
     embed.set_author(name='Pétrification')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707578999739777154/se_stunstone.png')
     embed.add_field(name='(Passif)', value='**Feu**: Canna, Gargor, Médusa, Peyote\n**Eau**: Tipiaf, Chloe, Verde, Zarid\n**Bois**: Kiki, Végédalle, Fenrir\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Félinelame, Médusine, Médusa, Truffel, Victoria\n**Eau**: Tipiaf, Cocomaru, Djinn, Persephone, Crustarov, Fenrir, Lombrix\n**Bois**: Arlequin, Benjabuton, Gargor, Lucy, Onmyoji, Persephone Peyote, Pincemi, Poulpo\n**Light**:  - -\n**Dark**: Kiloptère, Peyote\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)
       
 if message.content.startswith('predateur'):
     embed=discord.Embed(title='Augmente les dégâts (en %)', url='', color=0xffffff)
     embed.set_author(name='Prédateur')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707579179465572433/se_selfadddamagebyelement.png')
     embed.add_field(name='(Passif)', value='**Feu**: Beth, Bron, Lupin, Stella, Tanya, Wendigo, Zhu Bajie \n**Eau**: Beth, Bron, Valkyrie, Vampire\n**Bois**: Beth, Bron, Citrouillon, Gilgamesh, Griffon, Shiva, Tigar\n**Light**: Chiroptie, Hades, Shinobi, Tai\n**Dark**: Chiroptie, Hohenheim, Tai\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Beth, Djinn, Misha, Mowgli, Radic, Clamy, Tanya, Zhu Bajie \n**Eau**: Anu, Beth, Loki, Mowgli, Champi, Pip, Poseidon, Clamy, Sura, Thor\n**Bois**: Beth, Griffon, Mowgli, Rudolph, Clamy\n**Light**: Piou, Dartagnan, Mowgli, Otari, Pinolo, Pip, Shinobi, Yaksha\n**Dark**: Arlequin, Poulichon, Kiki, Mari, Mowgli, Persephone\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('perfo'):
     embed=discord.Embed(title='Ignore la défense de base de la cible', url='', color=0xffffff)
     embed.set_author(name='Perforation')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707579303960772679/se_n_penetrate_up.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Draka\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  - -\n**Dark**: Gilgamesh\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)


 if message.content.startswith('puri'):
     embed=discord.Embed(title='Supprime tous les effets négatifs', url='', color=0xffffff)
     embed.set_author(name='Purification')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707579545355681911/se_clearbuff.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Chapillon\n**Eau**: Cupidon\n**Bois**: Cotonou, Mildeu\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['recuperationred']]):
     embed=discord.Embed(title='Diminue la récupération de la cible de 90%', url='', color=0xffffff)
     embed.set_author(name='Récupération réduite')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707579880237170688/se_debufffinalvalueheal.png')
     embed.add_field(name='(Passif)', value='**Feu**: Félinelame\n**Eau**: Chiroptie, Cocomaru, Lumo, Pottus, Ecurrix\n**Bois**: Dartagnan, Monkiki\n**Light**: Bulbie, Mimic\n**Dark**: Mera\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Latt, Végédalle, Pincemi\n**Eau**: Mandragore\n**Bois**: Médusine, Penpen, Lombrix\n**Light**: Bulbie, Mimic\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['recuperationaug']]):
     embed=discord.Embed(title='Augmente la récupération du lanceur de 90%', url='', color=0xffffff)
     embed.set_author(name='Récupération augmentée')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707580043836260433/se_buffheal.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Lumo\n**Eau**: Rubani\n**Bois**: Sirène\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('volon'):
     embed=discord.Embed(title='Restaure les PA en fonction des dégâts reçus', url='', color=0xffffff)
     embed.set_author(name='Volonté')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707580962900541480/se_recoverymympbymydamage.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Sirène\n**Eau**: Hana\n**Bois**: Cura\n**Light**:  - -\n**Dark**: Fée\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['resistancered']]):
     embed=discord.Embed(title="Reduit la resistance de l'ennemi de 50%", url='', color=0xffffff)
     embed.set_author(name='Résistance réduite')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707581853111943289/se_n_resistdown.png')
     embed.add_field(name='(Passif)', value='**Feu**: Pip\n**Eau**: Sha wujing, Slime\n**Bois**: Hohenheim\n**Light**: Zephyros\n**Dark**: Cotonou, Djinn\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  Griffon\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('necrosex2'):
     embed=discord.Embed(title='Dégâts égaux à 7% des PVs max de la cible. Applique 2 necroses', url='', color=0xffffff)
     embed.set_author(name='Nécrosex2')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707582056946991154/se_ongoingdechppoison.png')
     embed.add_field(name='(Passif)', value='**Feu**: Chapillon, Champi, Persephone\n**Eau**: Artemis, Misha, Fée, Stella, Yuki\n**Bois**: Ammonore, Bulbie, Taupinou, Soldat Slime\n**Light**: Cerise, Cotonou\n**Dark**: Anu, Dartagnan, Torpin\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Piou, Bron, Croquignol, Jiangshi, Loki, Mari, Persephone\n**Eau**: Artemis, Banshee, Chloe, Félinelame, Givri, Yuki\n**Bois**: Jormungandr, Vampire, Yeti\n**Light**: Cosmo\n**Dark**: Chasseur, Citrouillon, Torpin, Crapora, Yuki\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('necrosex3'):
     embed=discord.Embed(title='Dégâts égaux à 7% des PVs max de la cible. Applique 3 necroses', url='', color=0xffffff)
     embed.set_author(name='Nécrosex3')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707582056946991154/se_ongoingdechppoison.png')
     embed.add_field(name='(Passif)', value='**Feu**:  Cernunnos\n**Eau**:  - -\n**Bois**: Persephone\n**Light**:  - -\n**Dark**: Banshee, Flora, Vampire, Verde\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**: Hohenheim, Chasseur, Djinn\n**Light**: Jormungandr, Mandragore, Crapora\n**Dark**: Arthur, Pip, Tipiaf\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('necrosex2'):
        return
    
 if message.content.startswith('necrosex3'):
        return
    
 if message.content.startswith('necrose'):
     embed=discord.Embed(title='Dégâts égaux à 7% des PVs max de la cible. (voir les commandes necrosex2 et necrosex3) (necrose)', url='', color=0xffffff)
     embed.set_author(name='Nécrose')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707582056946991154/se_ongoingdechppoison.png')
     embed.add_field(name='(Passif)', value='**Feu**: Cerise, Cernunnos, Cotonou, Gren, Loki, Mildeu, Chapillon, Champi, Persephone, Pottus, Sirène\n**Eau**: Artemis, Gupp, Hana, Miho, Mimic, Misha, Otari, Fée, Stella, Lombrix, Yuki\n**Bois**: Ammonore, Piou, Bulbie, Gren, Sacstère, Latt, Lucy, Mandragore, Médusa, Taupinou, Persephone, Clamy, Soldat Slime, Tincel\n**Light**: Cerise, Cotonou, Félinelame, Radic\n**Dark**: Anu, Banshee, Zabeille, Dartagnan, Flora, Torpin, Vampire, Verde, Zarid\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Ammonore, Piou, Bron, Croquignol, Gren, Jiangshi, Loki, Mari, Taupinou, Persephone, Tigar, Poulpo\n**Eau**: Arch, Artemis, Banshee, Bon, Chiroptie, Chloe, Félinelame, Miho, Mimic, Pottus, Stella, Givri, Ecurrix, Yuki, Zarid\n**Bois**: Ammonore, Cocomaru, Gren, Hohenheim, Chasseur, Citrouillon, Djinn, Jormungandr, Végédalle, Taupinou, Tincel, Sura, Vampire, Yeti\n**Light**: Cosmo, Jormungandr, Mandragore, Radic, Crapora\n**Dark**: Arthur, Zabeille, Flora, Spectros, Chasseur, Citrouillon, Pip, Tipiaf, Torpin, Crapora, Yuki, Zarid\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('sceau'):
     embed=discord.Embed(title='Désactive les talents actifs et passifs de la cible', url='', color=0xffffff)
     embed.set_author(name='Sceau')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707582461168582757/se_sealstatuseffect.png')
     embed.add_field(name='(Passif)', value='**Feu**: Garuda\n**Eau**: Scarabo, Citrouillon, Mera, Cauchemar\n**Bois**: Benjabuton, Onmyoji, Spectre des sables, Sura\n**Light**: Canna, Médusine, Phibian, Sha wujing\n**Dark**: Loki, Shiva, Sun Wukong\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Alpaca, Indra, Lucy, Sanzang\n**Eau**: Sha wujing, Verde\n**Bois**: Balrona, Nezha, Spectre des sables, Shiva\n**Light**: Mera, Sphinx\n**Dark**: Draka, Incubus, Loki, Cauchemar, Yeti\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)


 if message.content=='bouclier':
     embed=discord.Embed(title='Génère un bouclier qui absorbe les dégâts et protège des debuffs.', url='', color=0xffffff)
     embed.set_author(name='Bouclier')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707582566525435935/se_shielddamagebyabsolute.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Cura\n**Eau**: Cerise, Chapillon\n**Bois**: Cerise, Cupidon\n**Light**: Cotonou, Hana, Sirène, Venus\n**Dark**: Bast, Cupidon, Sacstère, Hana, Mildeu\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('brisebou'):
     embed=discord.Embed(title='Annule le bouclier de la cible', url='', color=0xffffff)
     embed.set_author(name='Brise bouclier')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707582874659979425/se_clearshield.png')
     embed.add_field(name='(Passif)', value='**Feu**: Kiki\n**Eau**: Bulbie, Cotonou, Médusine, Mildeu\n**Bois**:  - -\n**Light**:  - -\n**Dark**: Cosmo\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**: Succube\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('choc'):
     embed=discord.Embed(title='Immobilise la cible et réduit sa defense et son attaque de 50%', url='', color=0xffffff)
     embed.set_author(name='Choc')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707583003081048104/choc.png')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**: Alpaca, Arthur, Balrona, Banshee, Cura, Garuda, Chasseur, Latt, Lucy, Merlin, Mini Camilla, Pégase, Pinolo, Slime Stella, Sparkitt, Sun Wukong, Thor, Valkyrie, Yuki\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**: Banshee, Canna, Chiroptie, Chloe, Poulichon, Garuda, Imperio, Incubus, Kiki, Lucy, Misha, Onmyoji, Persephone, Gravel, Slime, Sun Wukong, Tai, Fenrir, Lupio, Yeti, Yuki, Zephyros\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('silence'):
     embed=discord.Embed(title="Empêche la cible d'utiliser son talent actif", url='', color=0xffffff)
     embed.set_author(name='Silence')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707583258954563614/silence.png')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  - -\n**Dark**: Ramu, Tincel\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**: Pégase\n**Bois**:  - -\n**Light**: Slime\n**Dark**: Artemis, Chiroptie, Cosmo, Fennec, Jeanne, Leo, Gravel, Tincel, Tai, Tanya, Valkyrie, Verde, Yaksha\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('sommeil'):
     embed=discord.Embed(title="Immobilise l'ennemi. La cible se reveille si elle subit un coup critique", url='', color=0xffffff)
     embed.set_author(name='Sommeil')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707583353443975188/se_stunsleep.png')
     embed.add_field(name='(Passif)', value='**Feu**: Hana, Mandragore, Monkiki\n**Eau**: Arch, Somnol, Jeanne, Pip, Végédalle, Médusa\n**Bois**: Somnol, Flora, Jiangshi, Fée, Buis, Crustarov, Succube, Yaksha\n**Light**: Somnol, Slime, Tigar\n**Dark**: Somnol, Succube\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Scarabo, Cocomaru, Enkidu, Somnol, Monkiki\n**Eau**: Somnol, Gupp, Lupin, Vampire\n**Bois**: Bron, Flora, Loki, Mandragore, Fenrir\n**Light**: Zabeille, Spectros, Zarid\n**Dark**: Gemini, Mera, Succube\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('amesrou'):
     embed=discord.Embed(title='Useless skill tbh', url='', color=0xffffff)
     embed.set_author(name="Abondance d'âmes rouge")
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/606439170809921549/607403873719549952/se_selfinvertsoulmptoPV.png')
     embed.add_field(name='(Passif)', value='**Feu**: Rubani\n**Eau**: Banshee\n**Bois**: Cupidon, Sirène\n**Light**:  - -\n**Dark**: Hana\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Jeanne\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['siphondepa','siphonpa']]):
     embed=discord.Embed(title="Vole une partie des PA de l'ennemi pour les ajouter au lanceur (en %). Sans effet si la jauge bleue de l'ennemie est vide", url='', color=0xffffff)
     embed.set_author(name='Siphon de PA')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707583617936785478/se_selfstealenemymp.png')
     embed.add_field(name='(Passif)', value='**Feu**: Mona, Onmyoji, Ramu\n**Eau**: Cernunnos, Shiva\n**Bois**: Arlequin, Shinobi\n**Light**: Silver, Bast, Hohenheim, Onmyoji, Pip, Rudolph, Verde\n**Dark**: Gemini, Lupin, Merlin, Mini Camilla, Spectre des sables, Shinobi, Yuki\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**: Alpaca, Shinobi\n**Bois**:  - -\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('traqueur'):
     embed=discord.Embed(title='Taux critique supplémentaire', url='', color=0xffffff)
     embed.set_author(name='Traqueur')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707584074616799242/se_selfbuffcriticalprob.png')
     embed.add_field(name='(Passif)', value='**Feu**: Benjabuton, Mera, Pincemi, Sherlock\n**Eau**: Lumignon, Croquignol, Pincemi, Sherlock, Yaksha\n**Bois**: Chloe, Croquignol, Jeanne, Pincemi, Sherlock\n**Light**:  - -\n**Dark**: Cernunnos, Kiloptère, Peyote, Fenrir\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Benjabuton\n**Eau**: Lumignon, Yaksha\n**Bois**: Chloe, Jeanne\n**Light**:  - -\n**Dark**: Fenrir\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('etourdi'):
     embed=discord.Embed(title='Immobilise la cible', url='', color=0xffffff)
     embed.set_author(name='Étourdissement')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707584410806911026/se_stun.png')
     embed.add_field(name='(Passif)', value='**Feu**: Anu, Artemis, Arthur, Bulbie, Gilgamesh, Latt, Cayou, Shiva, Sparkitt, Lombrix\n**Eau**: Ammonore, Piou, Bon, Taupinou, Odin, Radic, Sura, Fenrir\n**Bois**: Rubani, Cocomaru, Indra, Otari, Ramu, Victoria, Zarid\n**Light**: Scarabo, Spectros, Médusa, Tincel\n**Dark**: Alpaca, Chasseur, Radic, Valkyrie, Victoria, Yeti\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Garuda, Hohenheim, Chasseur, Pottus, Stella, Valkyrie\n**Eau**: Bron, Croquignol, Jeanne, Leo, Odin, Phibian, Radic, Zhu Bajie, Arch, Slime \n**Bois**: Arthur, Scarabo, Piou, Dartagnan, Miho, Monkiki, Otari, Poseidon, Ramu, Shinobi, Siegfried, Tigar, Victoria, Wendigo\n**Light**: Alpaca, Leo, Phibian, Rudolph, Sanzang, Tincel\n**Dark**: Merlin, Shiva, Givri, Sparkitt, Sun Wukong\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('provoc'):
     embed=discord.Embed(title="Empêche la cible d'utiliser son talent actif et force à attaquer le lanceur", url='', color=0xffffff)
     embed.set_author(name='Provocation')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707577210520993813/se_provokeme.png')
     embed.add_field(name='(Passif)', value='**Feu**: Piou, Mammont, Mimic, Clamy\n**Eau**: Ramu, Givri, Tigar\n**Bois**: Cotonou, Mildeu, Misha, Yeti\n**Light**: Penpen\n**Dark**: Ammonore, Robobot\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Artemis, Mimic, Champi, Cayou\n**Eau**: Ammonore, Incubus, Citrouillon, Taupinou, Wendigo\n**Bois**: - -\n**Light**:  - -\n**Dark**: Ramu\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('soif'):
     embed=discord.Embed(title="Empêche la cible d'utiliser son talent actif en réduisant ses PA", url='', color=0xffffff)
     embed.set_author(name='Soif')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707584555389026325/soif.png')
     embed.add_field(name='(Passif)', value='**Feu**: Arlequin\n**Eau**:  - -\n**Bois**: Hades, Stella\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Bulbie, Canna, Dartagnan, Cauchemar\n**Eau**: Piou, Médusa, Monkiki, Ramu, Shiva, Poulpo\n**Bois**: Indra, Mera, Pégase\n**Light**: Anu\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['frappeind']]):
     embed=discord.Embed(title="Augmente légèrement l'attaque en fonction des PVs max de la cible", url='', color=0xffffff)
     embed.set_author(name='Frappe indéfectible')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707584850764496926/se_selfadddamagebyenemymaxhpminimum.png')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**: Spectre des sables, Sphinx\n**Bois**:  - -\n**Light**:  - -\n**Dark**: Pinolo\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Sphinx\n**Eau**: Bulbie\n**Bois**: Alpaca, Jiangshi, Pinolo, Sphinx\n**Light**: Spectre des sables\n**Dark**: Sphinx\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('veng'):
     embed=discord.Embed(title="Augmente l'attaque en fonction du pourcentage de PVs perdus", url='', color=0xffffff)
     embed.set_author(name='Vengeance')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707585139403915324/se_selfaddattackbyhplossrate.png')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**:  - -\n**Light**: Torpin\n**Dark**: Misha, Wendigo\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**: Spectre des sables\n**Bois**:  - -\n**Light**: Torpin\n**Dark**: Mammont, Misha, Penpen\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('vigueur'):
     embed=discord.Embed(title='Restaure une partie des PVs au début de chaque tour', url='', color=0xffffff)
     embed.set_author(name='Vigueur')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707581770794532925/se_ongoinginchp.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Sacstère\n**Eau**: Sirène\n**Bois**: Rubani, Fée\n**Light**: Bast, Fée\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['eauchasseur','chasseureau']]):
     embed=discord.Embed(title='Confère un bonus de dégâts critiques sur les monstres de type eau (en %)', url='', color=0xffffff)
     embed.set_author(name='Chasseur (eau)')
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/606439170809921549/607403171827941377/se_selfbuffcriticaldamage.png')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**: Poulpo\n**Bois**: Alpaca, Lumignon, Fennec, Mowgli\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**: Mino\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['predateureau','eaupreda']]):
     embed=discord.Embed(title='Augmente les dégâts sur les monstres de type eau (en %)', url='', color=0xffffff)
     embed.set_author(name='Prédateur (eau)')
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/606439170809921549/607403180699156491/se_selfadddamagebyelement.png')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**:  - -\n**Bois**: Beth, Bron\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**:  - -\n**Eau**: Clamy\n**Bois**: Beth, Mowgli\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['traqueureau','eautraq']]):
     embed=discord.Embed(title='Taux critique supplémentaire sur les monstres de type eau (en %)', url='', color=0xffffff)
     embed.set_author(name='Traqueur (eau)')
     embed.set_thumbnail(url='')
     embed.add_field(name='(Passif)', value='**Feu**:  - -\n**Eau**: - -\n**Bois**: Sherlock\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('affaibl'):
     embed=discord.Embed(title="Réduit l'attaque et la défense de la cible de 40%", url='', color=0xffffff)
     embed.set_author(name='Affaiblissement')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707585580292112970/se_debuffattackanddefence.png')
     embed.add_field(name='(Passif)', value='**Feu**:  Cernunnos\n**Eau**: Bast, Draka, Gilgamessh\n**Bois**: Garuda\n**Light**: Draka, Enkidu\n**Dark**: Draka, Onmyoji\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Poseidon\n**Eau**: Draka\n**Bois**:  - -\n**Light**: Nezha\n**Dark**: Djinn, Sha wujing\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['boischasseur','chasseurbois']]):
     embed=discord.Embed(title='Confère un bonus de dégâts critiques sur les monstres de type bois (en %)', url='', color=0xffffff)
     embed.set_author(name='Chasseur (bois)')
     embed.set_thumbnail(url='')
     embed.add_field(name='(Passif)', value='**Feu**: Fennec, Mowgli\n**Eau**:  - -\n**Bois**: Poulpo\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Mino\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['predateurbois','boispreda']]):
     embed=discord.Embed(title='Augmente les dégâts sur les monstres de type bois (en %)', url='', color=0xffffff)
     embed.set_author(name='Prédateur (bois)')
     embed.set_thumbnail(url='')
     embed.add_field(name='(Passif)', value='**Feu**: Beth, Bron, Tanya\n**Eau**:  - -\n**Bois**:  - -\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Beth, Mowgli, Tanya\n**Eau**:  - -\n**Bois**: Clamy\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['traqueurbois','boistraq']]):
     embed=discord.Embed(title='Taux critique supplémentaire sur les monstres de type bois (en %)', url='', color=0xffffff)
     embed.set_author(name='Traqueur (bois)')
     embed.set_thumbnail(url='')
     embed.add_field(name='(Passif)', value='**Feu**: Sherlock\n**Eau**:  - -\n**Bois**: - -\n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if any([message.content.startswith (item) for item in ['volonteeternelle','eternelle']]):
     embed=discord.Embed(title="Confère aux alliés un bonus leur permettant de survivre 1 fois à une attaque mortelle. L'effet ne peut être obtenu qu'une fois par manche.", url='', color=0xffffff)
     embed.set_author(name='Volonté éternelle')
     embed.set_thumbnail(url='')
     embed.add_field(name='(Passif)', value='**Feu**: \n**Eau**:  - -\n**Bois**: \n**Light**:  - -\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: \n**Eau**:  - -\n**Bois**: Cernunnos\n**Light**:  - -\n**Dark**:  Cernunnos\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

 if message.content.startswith('zele'):
     embed=discord.Embed(title='Restaure une partie des PA au début de chaque tour', url='', color=0xffffff)
     embed.set_author(name='Zèle')
     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/707146231008460800/707586023441301554/se_ongoingincmp.png')
     embed.add_field(name='(Passif)', value='No creature found\n\n\n\n\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     embed.add_field(name='(Actif)', value='**Feu**: Rubani\n**Eau**: Sacstère\n**Bois**: Buis\n**Light**: Cupidon\n**Dark**:  - -\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)
     
     await message.channel.send(embed=embed)

##############################################################
########           Liste par type                   ##########
##############################################################


############################################################## 
###########                Leadcommands             ##########
##############################################################

 if message.content.startswith('LDrecuperation'):
     embed=discord.Embed(title='', url='https://media.discordapp.net/attachments/684370413958332436/765593408323977226/recuperation.png', color=0xffffff)
     embed.set_author(name='Vague de Vitalité (augmentation Recup')
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/684370413958332436/765593408323977226/recuperation.png')
     embed.add_field(name='Astromons', value='1★  - -\n2★ Buis, Ecurrix, Lumo, Mildeu, Mino, Rubani\n3★ Sacstère, Chapillon\n4★ Hana, Mammont\n5★  - - \n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdDefDown'):
     embed=discord.Embed(title='', url='', color=0xffffff)
     embed.set_author(name='Posture de Charge (Reduction Def Ennemie)')
     embed.set_thumbnail(url='')
     embed.add_field(name='Astromons', value='1★  - - \n2★ Gargor\n3★  - - \n4★  - - \n5★ Gilgamesh, Cernunnos \n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdAtkDown'):
     embed=discord.Embed(title='', url='', color=0xffffff)
     embed.set_author(name='Posture Défensive (Reduction Atk Ennemie')
     embed.set_thumbnail(url='')
     embed.add_field(name='Astromons', value='1★  - -\n2★  - -\n3★  - -\n4★  - - \n5★ Imperato \n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdPvUp'):
     embed=discord.Embed(title='', url='https://media.discordapp.net/attachments/684370413958332436/772868019382517771/Pv.png', color=0xffffff)
     embed.set_author(name='Grâce Vitale (augmentation PV)')
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/684370413958332436/772868019382517771/Pv.png')
     embed.add_field(name='Astromons', value='1★ Slime\n2★ Poulpo, Bron, Pottus, Zarid\n3★ Bon, Médusine, Mandragore, Piou, Misha, Soldat Slime, Pip, Shark\n4★ Cupidon, Cayou, Succube, Tails, Mini Camilla, Léo, Sparkitt, Mera\n5★ Arthur, Shiva, Odin, Shinobi, Poséidon, Zhu Bajie, Draka \n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdRouge'):
     embed=discord.Embed(title='', url='https://media.discordapp.net/attachments/684370413958332436/772867360355778590/amesrouges.png', color=0xffffff)
     embed.set_author(name="Faveur de l'Esprit Ecarlate (âmes rouges PV)")
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/684370413958332436/772867360355778590/amesrouges.png')
     embed.add_field(name='Astromons', value='1★  - - \n2★ Taupinou\n3★ Clamy, Citrouillon\n4★ Cura\n5★  - -  \n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdBleu'):
     embed=discord.Embed(title='', url='https://media.discordapp.net/attachments/684370413958332436/772867315762462741/amesbleues.png', color=0xffffff)
     embed.set_author(name="Faveur de l'Esprit Azuré (âmes bleues PA)")
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/684370413958332436/772867315762462741/amesbleues.png')
     embed.add_field(name='Astromons', value='1★  - - \n2★ Cotonou\n3★ Médusa, Radic, Givri\n4★ Canna, Pégase\n5★  - - \n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdAtkUp'):
     embed=discord.Embed(title='', url='https://media.discordapp.net/attachments/684370413958332436/772867807401607178/attaque.png', color=0xffffff)
     embed.set_author(name='Esprit combatif (augmentation atk)')
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/684370413958332436/772867807401607178/attaque.png')
     embed.add_field(name='Astromons', value='1★ Tincel, Mimic\n2★ Champi, Ammonore, Peyote, Spectros\n3★ Monkiki, Mona, Latt, Cocomaru, Phibian, Kiki, Tanya, Mowgli, Cerise, Lupio\n4★ Victoria, Tigar, Dartagnan, Knuckles, Lermite, Crapora, Verde, Sphinx\n5★ Valkyrie, Indra, Balrona, Hohenheim, Griffon \n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdResDown'):
     embed=discord.Embed(title='', url='', color=0xffffff)
     embed.set_author(name='Discernement (réduction resist)')
     embed.set_thumbnail(url='')
     embed.add_field(name='Astromons', value='1★  - - \n2★  - - \n3★  - -\n4★  - - \n5★ Jormungandr, Shadow, Hadès, Merlin\n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdResUp'):
     embed=discord.Embed(title='', url='https://media.discordapp.net/attachments/684370413958332436/772868189209624576/resistance.png', color=0xffffff)
     embed.set_author(name='Détermination D acier (augmentation resist)')
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/684370413958332436/772868189209624576/resistance.png')
     embed.add_field(name='Astromons', value='1★  - - \n2★ Zabeille, Arch, Gupp, Lombrix\n3★ Miho, Gemini, Gren, Ramu, Bulbie\n4★ Mari, Jeanne, Vampire, Flora, Venus\n5★ Silver, Cauchemar, Onmyoji, Artémis\n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdDcUp'):
     embed=discord.Embed(title='', url='https://media.discordapp.net/attachments/684370413958332436/772867991754637312/degatscritiques.png', color=0xffffff)
     embed.set_author(name='Coup Mortel (augmentation Dc)')
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/684370413958332436/772867991754637312/degatscritiques.png')
     embed.add_field(name='Astromons', value='1★  - - \n2★ Tai, Otari\n3★ Croquignol, Yeti, Wendigo, Fennec, Spectre des sables, Jiangshi, Poulichon\n4★ Yuki, Yaksha, Chloé, Gravel, Arlequin, Tipiaf\n5★ Sun Wukong\n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdDefUp'):
     embed=discord.Embed(title='', url='https://media.discordapp.net/attachments/684370413958332436/772867825441570916/defense.png', color=0xffffff)
     embed.set_author(name='Bouclier Protecteur (augmentation Def)')
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/684370413958332436/772867825441570916/defense.png')
     embed.add_field(name='Astromons', value='1★  - - \n2★ Robobot, Pincemi, Végédalle, Penpen, Chiroptie\n3★ Beth, Sirène, Félinelame, Truffel\n4★ Banshee, Loki, Nezha, Sonic, Mini Seira, Mini Tina, Torpin, Thor, Incubus, Benjabuton, Scarabo\n5★ Siegfried, Enkidu, Sanzang\n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdTcUp'):
     embed=discord.Embed(title='', url='https://media.discordapp.net/attachments/684370413958332436/772868191809699840/TC.png', color=0xffffff)
     embed.set_author(name='Boost de Critique (augmentation Tc)')
     embed.set_thumbnail(url='https://media.discordapp.net/attachments/684370413958332436/772868191809699840/TC.png')
     embed.add_field(name='Astromons', value='1★ - - \n2★ Kiloptère, Crustarov\n3★ Chasseur, Stella, Lumignon, Sherlock, Alpaca, Pinolo, Cosmo\n4★ Sura, Lupin, Mini Zephyros, Rudolph, Nifa, Fée, Somnol, Anu, Djinn\n5★ Persephone, Garuda, Sha Wujin, Bast\n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

 if message.content.startswith('LdTcDown'):
     embed=discord.Embed(title='', url='', color=0xffffff)
     embed.set_author(name='Aversion de Crise (réduction Tc)')
     embed.set_thumbnail(url='')
     embed.add_field(name='Astromons', value='1★  - -\n2★  - -\n3★  - - \n4★ Fenrir, Lucy\n5★  - -\n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ', inline=True)     
     await message.channel.send(embed=embed)

    #######################################
    ########   Liste de Leads   ###########
    #######################################

 if any([message.content.startswith (item) for item in ['Lead', 'Leads', 'lead', 'leads']]):
     embed = discord.Embed(title="", url="", color=0xfff99e)
     embed.set_author(name="Competences de Leads")
     embed.set_thumbnail(url="")
     embed.add_field(name="Liste des leads", value="Aversion de Crise : Diminue le taux de critiques des alliés \n**(commande : LdTcDown)** \n\nBoost de Critique : Augmente le taux de critiques de l'ennemi **\n(commande : LdTcUp)**\n\nBouclier Protecteur : Augmente la défense des alliés **\n(commande : LdDefUp)**\n\nCoup Mortel : Augmente les dégâts critiques des alliés **\n(commande : LdDcUp)**", inline=True)
     embed.add_field(name="-", value="Détermination D'acier : Augmente la résistance des alliés **\n(commande : LdResUp)** \n\nDiscernement : Réduit la résistance de l'ennemi **\n(commande : LdResDown)**\n\nEsprit combatif : Augmente l'attaque des alliés **\n(commande : LdAtkUp)**\n\nFaveur de l'Esprit Azuré : Augmente la récupération d'âmes bleues (PA) des alliés **\n(commande : LdBleu)**", inline=True)
     embed.add_field(name="-", value="Faveur de l'Esprit Ecarlate : Augmente la récupération d'âmes rouges (PV) des alliés **\n(commande : LdRouge)**\n\nGrâce Vitale  : Augmente les PV des alliés **\n(commande : LdPvUp)**\n\nPosture de Charge : Réduit la défense de l'ennemi **\n(commande : LdDefDown)**\n\nPosture Défensive : Réduit l'attaque de l'ennemi **\n(commande : LdAtkDown)**\n\nVague de Vitalité : Augmente la récupération des alliés **\n(commande : LdRecUp)**", inline=True)
     await message.channel.send(embed=embed)

##############################################################
########           Fusions                          ##########
##############################################################

 if message.content.startswith('FusionS'):
    embed=discord.Embed(title="Fusion : Shiva Light", url="https://i.redd.it/f34u7yfaz4yx.png", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="https://i.redd.it/f34u7yfaz4yx.png")
    embed.add_field(name="Anubis Light (evo3) + Tipiaf Feu (evo3)", value="\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", inline=False)
    embed.add_field(name="__Victoria Eau (evo3)__:", value="16 Sirène evo2\n`16 Beth Bois\n+ 16 Cotonou Eau\n+ 48 Sirène`\n\n16 Cocomaru Eau evo2\n`16 Gren Bois\n+ 16 Arch Feu\n+ 48 Cocomaru`\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", inline=True)
    embed.add_field(name="__Gravel Light (evo3)__:", value="16 Lupio Light evo2\n`16 Miho Bois\n+ 16 Miho Eau\n+ 48 Lupio`\n\n16 Cosmo Dark evo2\n`16 Cosmo Light\n+ 16 Kiloptère Light\n+ 48 Cosmo`\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", inline=True)
    await message.channel.send(embed=embed)

 if message.content.startswith('FusionM'):
    embed=discord.Embed(title="Fusion : Merlin Dark", url="https://i.imgur.com/G2gG30l.png", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="https://i.imgur.com/G2gG30l.png")
    embed.add_field(name="Mammont Dark (evo3) + Mera Eau (evo3)", value="\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", inline=False)
    embed.add_field(name="__Tigar Feu (evo3)__:", value="16 Médusa Feu evo2\n`16 Monkiki Feu\n+ 16 Gargor Bois\n+ 48 Médusa`\n\n16 Croquignol Bois evo2\n`16 Phibian Eau\n+ 16 Lombrix Feu\n+ 48 Croquignol`\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", inline=True)
    embed.add_field(name="__Nifa Dark (evo3)__:", value="16 Poulichon Light evo2\n`16 Yeti Eau\n+ 64 Wendigo Bois\n+ 48 Poulichon`\n\n16 Penpen Dark evo2\n`64 Tai Dark\n+ 256 Slime Light\n+ 48 Penpen`\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", inline=True)
    await message.channel.send(embed=embed)

 if message.content.startswith('FusionH'):
    embed=discord.Embed(title="Fusion : Hohenheim Light", url="http://bit.ly/2lJpK8d", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="http://bit.ly/2lJpK8d")
    embed.add_field(name="Mammont Light (evo3)+ Scarabo Bois (evo3)", value="\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", inline=False)
    embed.add_field(name="__Loki Bois (evo3)__:", value="16 Cayou Feu evo2\n`16 Misha Feu\n+ 16 Spectre Feu\n+ 48 Cayou`\n\n16 Lermite Eau evo2\n`16 Eau Fennec\n+ 16 Ammonore Eau\n+ 48 Lermite`\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", inline=True)
    embed.add_field(name="__Anu Dark (evo3)__:", value="15 Anubis\n\n1 Nifa Light evo2\n`4 Nifa Dark\n+ 1 Chiroptie Light`\n\n1 Gravel Dark evo2\n`16 Gravel Light\n+ 16 Mino Dark`\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", inline=True)
    await message.channel.send(embed=embed)
       
	   
#####################################################################     	 
############    où trouver les Spierres                  ############
#####################################################################

 if message.content.startswith('Super'):
    embed=discord.Embed(title="Superstones", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="Continent", value="__Area__:\n`Normal (low)`\nExtreme (mid)\n**Boss (high)**\n\n\n\n\n\n. . . . . . . .", inline=True)
    embed.add_field(name="1st contininent", value="__Phantom forest__:\n`Leaf of Yggrasil`\nShinning Branch\n**Verdant Volition**\n\n__Lunar Valley__:\n`Small rune stone`\nMoonflower\n**Verdant Volition**\n. . . . . . . .", inline=True)
    embed.add_field(name="1st contininent", value="__Aria lake__:\n`Jade pearl`\nIllusory bubble\n**Ethereal gemstone**\n\n__Mirage ruins__:\n`White sand`\nStatue of time\n**Ethereal gemstone**\n. . . . . . . .", inline=True)
    embed.add_field(name="2nd contininent", value="__Pagos coast__:\n`Everhot sand`\nCoral shard\n**Abyssal tear**\n\n__Seabed caves__:\n`Luminescia`\nGelatin\n**Abyssal tear**\n. . . . . . . .", inline=True)
    embed.add_field(name="2nd contininent", value="__Magma crags__:\n`Flamegrass`\nBlood crystal\n**Phoenix feather**\n\n__Star sanctuary__:\n`Curious metal shard`\nStrange contraption\n**Phoenix feather**\n. . . . . . . .", inline=True)
    embed.add_field(name="3rd contininent", value="__Sky falls__:\n`Heaven's dew`\nCrimson scale\n**Chaos shard**\n\n__Slumbering city__:\n`Floatstone powder`\nFloatstone shard\n**Chaos shard**\n. . . . . . . .", inline=True)
    embed.add_field(name="4th contininent", value="__Glacial plains__:\n`Ice crystal`\nCrystal shard\n**Chaos shard**\n\n__Aurora plateau__:\n`Mystic flower`\nGelid bead\n**Chaos shard**\n. . . . . . . .", inline=True)
    embed.add_field(name="5th contininent", value="__Desert battlefield__:\n`Small rune stone`\nMoonflower\n**Ethereal gemstone**\n\n__Terrestrial rift__:\n`Luminescia`\nCrystal shard\n**Ethereal gemstone**\n. . . . . . . .", inline=True)
    await message.channel.send(embed=embed)

############################################
##########    Trinkets          ############
############################################

 if any([message.content == (item) for item in ['trink','trinket','Trink','Trinket','Attirail','attirail']]):
     embed = discord.Embed(title="Attirail", url="",color=0xfff99e)
     embed.set_author(name="")
     embed.set_thumbnail(url="")
     embed.add_field(name="RC", value="Voir les attirails resistance critiques \n\nCommande :\n\n**trinketRC, TrinketRC, AttirailRC, attirailRC**", inline=True)
     embed.add_field(name="HP", value="Voir les attirails PV \n\nCommande :\n\n**trinketHP, TrinketHP, AttirailHP, attirailHP**", inline=True)
     embed.add_field(name="ATK", value="Voir les attirails attaque \n\nCommande :\n\n**trinketATK, TrinketATK, AttirailATK, attirailATK**", inline=True)

     await message.channel.send(embed=embed)

 if any([message.content == (item) for item in ['trinketRC','TrinketRC','AttirailRC','attirailRC']]):
     embed = discord.Embed(title="Attirail résistance critique",url="https://media.discordapp.net/attachments/684370413958332436/762726805777154069/trinket.png",color=0xfff99e)
     embed.set_image(url="https://media.discordapp.net/attachments/684370413958332436/762726805777154069/trinket.png")

     await message.channel.send(embed=embed)

 if any([message.content ==(item) for item in ['trinketHP','TrinketHP','AttirailHP','attirailHP']]):
     embed=discord.Embed(title="Attirail PV", url="https://media.discordapp.net/attachments/561112186466861056/664081429491220480/Stats_HP_rare_v2.PNG", color=0xfff99e)
     embed.set_image(url="https://media.discordapp.net/attachments/561112186466861056/664081429491220480/Stats_HP_rare_v2.PNG")
     
     await message.channel.send(embed=embed)

 if any([message.content == (item) for item in ['trinketATK', 'TrinketATK', 'AttirailATK', 'attirailATK']]):
     embed = discord.Embed(title="Attirail attaque",url="https://media.discordapp.net/attachments/561112186466861056/664081465725812749/Stats_atk_rare_v2.PNG",color=0xfff99e)
     embed.set_image(url="https://media.discordapp.net/attachments/561112186466861056/664081465725812749/Stats_atk_rare_v2.PNG")

     await message.channel.send(embed=embed)

#####################################################################
     	 
	 #######################################
	 ############    Top Pv     ############
	 #######################################

 if message.content =='Rang':
    embed=discord.Embed(title="", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="'Rang' isn't a valid command", value="After 'Rang' add a number à specify the element (optional):\n1 = Feu\n2=Eau\n3 = Bois\n4 = Light\n5 = Dark\n\nThen add the stat or at least the 1st letter of it\n\nHere are some examples:\nRangPV Ranga RangDef Rangrec\nRang3H Rang2", inline=False)
    await message.channel.send(embed=embed) 
    
 if any([message.content.startswith(item) for item in ['Rangh','RangH']]):
    embed=discord.Embed(title="Rang: PV", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Draka (Bois) - 50098\n#2 Arthur (Dark) - 49696\n#3 Shiva (Light) - 49376\n#4 Shiva (Eau) - 49104\n#5 Valkyrie (Dark) - 48498\n#6 Balrona (Dark) - 48212\n#7 Nifa (Dark) - 47027\n#8 Phibian (Eau) - 46993\n#9 Victoria (Bois) - 46890\n#10 Fennec (Dark) - 45951\n#11 Cosmo (Dark) - 45522\n#12 Zhu Bajie  (Dark) - 45147\n#13 Piou (Dark) - 44643\n#14 Verde (Bois) - 44160\n#15 Yuki (Dark) - 44023\n#16 Beth (Bois) - 43901\n#17 Fenrir (Eau) - 43737\n#18 Anu (Light) - 43730\n#19 Bast (Eau) - 43662\n#20 Jeanne (Light) - 43560\n#21 Givri (Eau) - 43240\n#22 Arch (Bois) - 43220\n#23 Hohenheim (Feu) - 43213\n#24 Odin (Feu) - 43077\n#25 Anu (Feu) - 42722\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Mona (Feu) - 42627\n#27 Bast (Dark) - 42546\n#28 Banshee (Dark) - 42478\n#29 Odin (Light) - 42001\n#30 Somnol (Feu) - 41919\n#31 Shinobi (Bois) - 41688\n#32 Lupin (Eau) - 41436\n#33 Benjabuton (Bois) - 41402\n#34 Scarabo (Eau)\nThor (Light) - 41388\n#35 Miho (Feu) - 41374\n#36 Miho (Dark) - 41374\n#37 Ammonore (Feu)\nCauchemar (Dark) - 41265\n#38 Hades (Bois) - 41156\n#39 Succube (Eau) - 41143\n#40 Yuki (Eau) - 41143\n#41 Leo (Eau) - 41109\n#42 Succube (Light) - 40931\n#43 Misha (Light)\nPoseidon (Feu) - 40849\n#44 Merlin (Dark) - 40801\n#45 Banshee (Eau) - 40658\n#46 Penpen (Bois) - 40312\n#47 Chloe (Feu) - 40312\n#48 Siegfried (Bois) - 40298\n#49 Mera (Dark) - 40040\n#50 Lucy (Light) - 39951\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang1h','Rang1H']]):
    embed=discord.Embed(title="Rang: PV (Feu)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Hohenheim (Feu) - 50098\n#2 Odin (Feu) - 49696\n#3 Anu (Feu) - 49376\n#4 Mona (Feu) - 49104\n#5 Somnol (Feu) - 48498\n#6 Miho (Feu) - 48212\n#7 Ammonore (Feu) - 47027\n#8 Poseidon (Feu) - 46993\n#9 Chloe (Feu) - 46890\n#10 Pincemi (Feu) - 45951\n#11 Nezha (Feu) - 45522\n#12 Jeanne (Feu) - 45147\n#13 Onmyoji (Feu) - 44643\n#14 Artemis (Feu) - 44160\n#15 Citrouillon(Feu) - 44023\n#16 Sparkitt (Feu) - 43901\n#17 Peyote (Feu)\nPottus (Feu) - 43737\n#18 Sphinx (Feu) - 43730\n#19 Tincel (Feu) - 43662\n#20 Valkyrie (Feu) - 43560\n#21 Misha (Feu) - 43240\n#22 Mammont (Feu) - 43220\n#23 Chapillon (Feu) - 43213\n#24 Zhu Bajie  (Feu) - 43077\n#25 Otari (Feu) - 42722\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Truffel (Feu)\nLombrix (Feu) - 42627\n#27 Médusa (Feu) - 42546\n#28 Canna (Feu) - 42478\n#29 Loki (Feu) - 42001\n#30 Victoria (Feu) - 41919\n#31 Fée (Feu) - 41688\n#32 Bulbie (Feu) - 41436\n#33 Gargor (Feu) - 41402\n#34 Cupidon (Feu) - 41388\n#35 Shinobi (Feu) - 41374\n#36 Cauchemar (Feu) - 41374\n#37 Incubus (Feu) - 41265\n#38 Indra (Feu) - 41156\n#39 Penpen (Feu) - 41143\n#40 Garuda (Feu) - 41143\n#41 Alpaca (Feu) - 41109\n#42 Sirène (Feu) - 40931\n#43 Cura (Feu) - 40849\n#44 Bast (Feu) - 40801\n#45 Benjabuton (Feu) - 40658\n#46 Hana (Feu) - 40312\n#47 Persephone (Feu) - 40312\n#48 Yaksha (Feu) - 40298\n#49 Sha wujing (Feu) - 40040\n#50 Ecurrix (Feu) - 39951\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang2h','Rang2H']]):
    embed=discord.Embed(title="Rang: PV (Eau)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Shiva (Eau) - 50098\n#2 Phibian (Eau) - 49696\n#3 Fenrir (Eau) - 49376\n#4 Bast (Eau) - 49104\n#5 Givri (Eau) - 48498\n#6 Lupin (Eau) - 48212\n#7 Scarabo (Eau) - 47027\n#8 Succube (Eau) - 46993\n#9 Yuki (Eau) - 46890\n#10 Leo (Eau) - 45951\n#11 Banshee (Eau) - 45522\n#12 Jiangshi (Eau) - 45147\n#13 Mimic (Eau) - 44643\n#14 Sura (Eau) - 44160\n#15 Cura (Eau) - 44023\n#16 Latt (Eau) - 43901\n#17 Lombrix (Eau) - 43737\n#18 Chiroptie (Eau)\nVégédalle (Eau) - 43730\n#19 Incubus (Eau) - 43662\n#20 Taupinou (Eau) - 43560\n#21 Médusine (Eau) - 43240\n#22 D'artagnan (Eau) - 43220\n#23 Miho (Eau) - 43213\n#24 Radic (Eau) - 43077\n#25 Sacstère (Eau) - 42722\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Gargor (Eau) - 42627\n#27 Persephone (Eau) - 42546\n#28 Hana (Eau) - 42478\n#29 Arthur (Eau) - 42001\n#30 Hohenheim (Eau) - 41919\n#31 Verde (Eau) - 41688\n#32 Hades (Eau) - 41436\n#33 Onmyoji (Eau) - 41402\n#34 Merlin (Eau) - 41388\n#35 Sha wujing (Eau) - 41374\n#36 Artemis (Eau) - 41374\n#37 Cupidon (Eau) - 41265\n#38 Sparkitt (Eau) - 41156\n#39 Loki (Eau) - 41143\n#40 Benjabuton (Eau) - 41143\n#41 Piou (Eau) - 41109\n#42 Médusa (Eau) - 40931\n#43 Cotonou (Eau) - 40849\n#44 Nezha (Eau) - 40801\n#45 Zhu Bajie  (Eau) - 40658\n#46 Djinn (Eau) - 40312\n#47 Crustarov (Eau) - 40312\n#48 Victoria (Eau) - 40298\n#49 Sun Wukong (Eau) - 40040\n#50 Lermite (Eau) - 39951\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang3h','Rang3H']]):
    embed=discord.Embed(title="Rang: PV (Bois)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1  - 50098\n#2 Victoria (Bois) - 49696\n#3 Verde (Bois) - 49376\n#4 Beth (Bois) - 49104\n#5 Arch (Bois) - 48498\n#6 Shinobi (Bois) - 48212\n#7 Benjabuton (Bois) - 47027\n#8 Hades (Bois) - 46993\n#9 Penpen (Bois) - 46890\n#10 Siegfried (Bois) - 45951\n#11 Buis (Bois) - 45522\n#12 Cura (Bois) - 45147\n#13 Piou (Bois) - 44643\n#14 Mera (Bois) - 44160\n#15 Phibian (Bois) - 44023\n#16 Poulpo (Bois) - 43901\n#17 Sanzang (Bois) - 43737\n#18 Fenrir (Bois) - 43730\n#19 Succube (Bois) - 43662\n#20 Yeti (Bois) - 43560\n#21 Sun Wukong (Bois) - 43240\n#22 Leo (Bois) - 43220\n#23 Indra (Bois) - 43213\n#24 Persephone (Bois) - 43077\n#25 Sha wujing (Bois) - 42722\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Hana (Bois) - 42627\n#27 Garuda (Bois) - 42546\n#28 Bast (Bois) - 42478\n#29 Yuki (Bois) - 42001\n#30 Cocomaru (Bois) - 41919\n#31 Vampire (Bois) - 41688\n#32 Spectre des sables (Bois) - 41436\n#33 Balrona (Bois) - 41402\n#34 Cotonou (Bois) - 41388\n#35 Merlin (Bois) - 41374\n#36 Miho (Bois) - 41374\n#37 Rubani (Bois) - 41265\n#38 Flora (Bois) - 41156\n#39 Thor (Bois) - 41143\n#40 Lucy (Bois) - 41143\n#41 Tigar (Bois) - 41109\n#42 Pégase (Bois) - 40931\n#43 Chasseur (Bois) - 40849\n#44 Valkyrie (Bois) - 40801\n#45 Médusine (Bois) - 40658\n#46 Lupin (Bois) - 40312\n#47 Mammont (Bois) - 40312\n#48 Latt (Bois) - 40298\n#49 Scarabo (Bois) - 40040\n#50 D'artagnan (Bois) - 39951\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang4h','Rang4H']]):
    embed=discord.Embed(title="Rang: PV (light)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Shiva (Light) - 50098\n#2 Anu (Light) - 49696\n#3 Jeanne (Light) - 49376\n#4 Odin (Light) - 49104\n#5 Thor (Light) - 48498\n#6 Succube (Light) - 48212\n#7 Misha (Light) - 47027\n#8 Lucy (Light) - 46993\n#9 Verde (Light) - 46890\n#10 Nezha (Light) - 45951\n#11 Sun Wukong (Light) - 45522\n#12 Stella (Light) - 45147\n#13 Flora (Light) - 44643\n#14 Cocomaru (Light) - 44160\n#15 Spectre des sables (Light) - 44023\n#16 Sacstère (Light) - 43901\n#17 Venus (Light) - 43737\n#18 Hana (Light) - 43730\n#19 Gemini (Light) - 43662\n#20 Canna (Light) - 43560\n#21 Spectros (Light) - 43240\n#22 Miho (Light) - 43220\n#23 Sanzang (Light) - 43213\n#24 Félinelame (Light) - 43077\n#25 Mammont (Light) - 42722\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Fenrir (Light) - 42627\n#27 Hades (Light) - 42546\n#28 Cosmo (Light) - 42478\n#29 Victoria (Light) - 42001\n#30 Balrona (Light) - 41919\n#31 Bulbie (Light) - 41688\n#32 Merlin (Light) - 41436\n#33 Silver (Light) - 41402\n#34 Alpaca (Light) - 41388\n#35 Sura (Light) - 41374\n#36 Banshee (Light) - 41374\n#37 Loki (Light) - 41265\n#38 Siegfried (Light) - 41156\n#39 Persephone (Light) - 41143\n#40 Valkyrie (Light) - 41143\n#41 Sphinx (Light) - 41109\n#42 Sha wujing (Light) - 40931\n#43 Pégase (Light) - 40849\n#44 Mera (Light) - 40801\n#45 Sparkitt (Light) - 40658\n#46 Chasseur (Light) - 40312\n#47 Mona (Light) - 40312\n#48 Mandragore (Light) - 40298\n#49 Draka (Light) - 40040\n#50 Poulichon (Light) - 39951\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang5h','Rang5H']]):
    embed=discord.Embed(title="Rang: PV (dark)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Arthur (Dark) - 50098\n#2 Valkyrie (Dark) - 49696\n#3 Balrona (Dark) - 49376\n#4 Nifa (Dark) - 49104\n#5 Fennec (Dark) - 48498\n#6 Cosmo (Dark) - 48212\n#7 Zhu Bajie  (Dark) - 47027\n#8 Piou (Dark) - 46993\n#9 Yuki (Dark) - 46890\n#10 Bast (Dark) - 45951\n#11 Banshee (Dark) - 45522\n#12 Miho (Dark) - 45147\n#13 Cauchemar (Dark) - 44643\n#14 Merlin (Dark) - 44160\n#15 Mera (Dark) - 44023\n#16 Djinn (Dark) - 43901\n#17 Citrouillon(Dark) - 43737\n#18 Slime (Dark) - 43730\n#19 Cupidon (Dark) - 43662\n#20 Soldat Slime (Dark) - 43560\n#21 Ramu (Dark) - 43240\n#22 Sparkitt (Dark) - 43220\n#23 Tigar (Dark) - 43213\n#24 Loki (Dark) - 43077\n#25 Médusa (Dark) - 42722\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Torpin (Dark) - 42627\n#27 Lupio (Dark) - 42546\n#28 Peyote (Dark)\nZarid (Dark) - 42478\n#29 Yeti (Dark) - 42001\n#30 Zabeille (Dark) - 41919\n#31 Sacstère (Dark) - 41688\n#32 Victoria (Dark) - 41436\n#33 Cocomaru (Dark) - 41402\n#34 Succube (Dark) - 41388\n#35 Hades (Dark) - 41374\n#36 Médusine (Dark) - 41374\n#37 Anu (Dark) - 41265\n#38 Givri (Dark) - 41156\n#39 Shiva (Dark) - 41143\n#40 Sun Wukong (Dark) - 41143\n#41 Odin (Dark) - 41109\n#42 Phibian (Dark) - 40931\n#43 Artemis (Dark) - 40849\n#44 Siegfried (Dark) - 40801\n#45 Jeanne (Dark) - 40658\n#46 Stella (Dark) - 40312\n#47 Verde (Dark) - 40312\n#48 Leo (Dark) - 40298\n#49 Gemini (Dark) - 40040\n#50 Tanya (Dark) - 39951\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)

	 #######################################
	 ###########   Top Attaque   ###########
	 #######################################

 if any([message.content.startswith(item) for item in ['Ranga','RangA']]):
    embed=discord.Embed(title="Rang: Attaque", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Draka (Light) - 4038\n#2 Siegfried (Feu) - 4018\n#3 Indra (Light) - 3977\n#4 Arthur (Light) - 3936\n#5 Shadow (Dark) - 3916\n#6 Odin (Bois) - 3909\n#7 Draka (Feu)\nShiva (Bois) - 3902\n#8 Shinobi (Light) - 3902\n#9 Poseidon (Light) - 3889\n#10 Sanzang (Dark) - 3854\n#11 Hohenheim (Light) - 3848\n#12 Persephone (Dark) - 3841\n#13 Arthur (Bois) - 3834\n#14 Sha wujing (Dark) - 3766\n#15 Hohenheim (Dark) - 3732\n#16 Onmyoji (Dark) - 3718\n#17 Hades (Dark)\nIndra (Dark)\nOnmyoji (Eau) - 3698\n#18 Valkyrie (Eau) - 3677\n#19 Zhu Bajie  (Feu) - 3677\n#20 Anu (Eau) - 3677\n#21 Indra (Feu) - 3671\n#22 Garuda (Eau) - 3664\n#23 Leo (Dark) - 3657\n#24 Garuda (Light)\nCauchemar (Feu) - 3650\n#25 Sha wujing (Feu) - 3643\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Hohenheim (Bois) - 3637\n#27 Artemis (Bois)\nArtemis (Light) - 3616\n#28 Draka (Eau) - 3616\n#29 Balrona (Eau) - 3596\n#30 Hades (Light) - 3582\n#31 Leo (Feu) - 3575\n#32 Succube (Feu) - 3575\n#33 Yuki (Light) - 3568\n#34 Merlin (Eau) - 3562\n#35 Leo (Light) - 3548\n#36 Hades (Feu) - 3521\n#37 Sun Wukong (Feu)\nVictoria (Eau) - 3514\n#38 Arthur (Feu) - 3500\n#39 Yuki (Feu) - 3494\n#40 Lucy (Dark) - 3487\n#41 Anu (Bois) - 3480\n#42 Mini Camilla (Light)\nMini Camilla (Dark)\nMini Seira (Light)\nMini Seira (Dark) - 3473\n#43 Médusine (Light)\nSun Wukong (Bois) - 3473\n#44 Merlin (Feu)\nFenrir (Feu) - 3466\n#45 Poseidon (Eau)\nSpectre des sables (Dark)\nSphinx (Light) - 3446\n#46 Bulbie (Dark)\nLucy (Feu)\nMini Tina (Dark) - 3439\n#47 Benjabuton (Light) - 3432\n#48 Bulbie (Eau)\nKiki (Dark)\nMini Tina (Light) - 3425\n#49 Knuckles (Feu)\nSonic (Eau) - 3425\n#50 Djinn (Feu) - 3425\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang1a','Rang1A']]):
    embed=discord.Embed(title="Rang: Attaque (Feu)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Siegfried (Feu) - 4038\n#2 Draka (Feu) - 4018\n#3 Zhu Bajie  (Feu) - 3977\n#4 Indra (Feu) - 3936\n#5 Cauchemar (Feu) - 3916\n#6 Sha wujing (Feu) - 3909\n#7 Leo (Feu) - 3902\n#8 Succube (Feu) - 3902\n#9 Hades (Feu) - 3889\n#10 Sun Wukong (Feu) - 3854\n#11 Arthur (Feu) - 3848\n#12 Yuki (Feu) - 3841\n#13 Merlin (Feu)\nFenrir (Feu) - 3834\n#14 Lucy (Feu) - 3766\n#15 Knuckles (Feu) - 3732\n#16 Djinn (Feu) - 3718\n#17 Lupin (Feu)\nSura (Feu) - 3698\n#18 Pégase (Feu) - 3677\n#19 Mera (Feu) - 3677\n#20 Balrona (Feu) - 3677\n#21 D'artagnan (Feu) - 3671\n#22 Benjabuton (Feu) - 3664\n#23 Persephone (Feu) - 3657\n#24 Tipiaf (Feu)\nFenrir (Feu) - 3650\n#25 Shinobi (Feu) - 3643\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Soldat Slime (Feu) - 3637\n#27 Mari (Feu) - 3616\n#28 Vampire (Feu) - 3616\n#29 Monkiki (Feu) - 3596\n#30 Phibian (Feu) - 3582\n#31 Tigar (Feu) - 3575\n#32 Ramu (Feu) - 3575\n#33 Yeti (Feu) - 3568\n#34 Artemis (Feu) - 3562\n#35 Sherlock (Feu) - 3548\n#36 Mowgli (Feu) - 3521\n#37 Valkyrie (Feu) - 3514\n#38 Incubus (Feu) - 3500\n#39 Latt (Feu)\nStella (Feu)\nTanya (Feu) - 3494\n#40 Gemini (Feu)\nMédusine (Feu) - 3487\n#41 Mandragore (Feu) - 3480\n#42 Lumignon (Feu)\nChasseur (Feu) - 3473\n#43 Scarabo (Feu) - 3473\n#44 Verde (Feu) - 3466\n#45 Wendigo (Feu) - 3446\n#46 Chiroptie (Feu)\nFennec (Feu)\nVégédalle (Feu)\nRadic (Feu) - 3439\n#47 Onmyoji (Feu) - 3432\n#48 Sanzang (Feu) - 3425\n#49 Sphinx (Feu) - 3425\n#50 Crustarov (Feu) - 3425\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang2a','Rang2A']]):
    embed=discord.Embed(title="Rang: Attaque (Eau)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Onmyoji (Eau) - 4038\n#2 Valkyrie (Eau) - 4018\n#3 Anu (Eau) - 3977\n#4 Garuda (Eau) - 3936\n#5 Draka (Eau) - 3916\n#6 Balrona (Eau) - 3909\n#7 Merlin (Eau) - 3902\n#8 Victoria (Eau) - 3902\n#9 Poseidon (Eau) - 3889\n#10 Bulbie (Eau) - 3854\n#11 Sonic (Eau) - 3848\n#12 Sun Wukong (Eau) - 3841\n#13 Shinobi (Eau) - 3834\n#14 Lucy (Eau) - 3766\n#15 Siegfried (Eau) - 3732\n#16 Vampire (Eau) - 3718\n#17 Artemis (Eau)\nSparkitt (Eau) - 3698\n#18 Odin (Eau) - 3677\n#19 Yaksha (Eau) - 3677\n#20 Loki (Eau) - 3677\n#21 Mammont (Eau)\nVictoria (Eau) - 3671\n#22 Alpaca (Eau) - 3664\n#23 Indra (Eau) - 3657\n#24 Hohenheim (Eau) - 3650\n#25 Thor (Eau) - 3643\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Clamy (Eau) - 3637\n#27 Sha wujing (Eau) - 3616\n#28 Zhu Bajie  (Eau) - 3616\n#29 Mona (Eau) - 3596\n#30 Mera (Eau) - 3582\n#31 Arthur (Eau)\nPersephone (Eau) - 3575\n#32 Bast (Eau) - 3575\n#33 Hades (Eau) - 3568\n#34 Somnol (Eau) - 3562\n#35 Fennec (Eau) - 3548\n#36 Mandragore (Eau)\nSherlock (Eau) - 3521\n#37 Mowgli (Eau) - 3514\n#38 Leo (Eau) - 3500\n#39 Lumignon (Eau)\nCauchemar (Eau) - 3494\n#40 Beth (Eau) - 3487\n#41 Croquignol (Eau) - 3480\n#42 Mari (Eau) - 3473\n#43 Sanzang (Eau) - 3473\n#44 Verde (Eau) - 3466\n#45 Stella (Eau) - 3446\n#46 Fenrir (Eau) - 3439\n#47 Nezha (Eau) - 3432\n#48 Tipiaf (Eau) - 3425\n#49 Lupin (Eau) - 3425\n#50 Sphinx (Eau) - 3425\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang3a','Rang3A']]):
    embed=discord.Embed(title="Rang: Attaque (Bois)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Odin (Bois) - 4038\n#2 Shiva (Bois) - 4018\n#3 Arthur (Bois) - 3977\n#4 Hohenheim (Bois) - 3936\n#5 Artemis (Bois) - 3916\n#6 Anu (Bois) - 3909\n#7 Sun Wukong (Bois) - 3902\n#8 Chloe (Bois) - 3902\n#9 Jeanne (Bois) - 3889\n#10 Somnol (Bois) - 3854\n#11 Sphinx (Bois) - 3848\n#12 Incubus (Bois) - 3841\n#13 Tigar (Bois) - 3834\n#14 Yaksha (Bois) - 3766\n#15 Anu (Bois)\nBanshee (Bois)\nNezha (Bois) - 3732\n#16 Tipiaf (Bois) - 3718\n#17 Garuda (Bois) - 3698\n#18 Djinn (Bois) - 3677\n#19 Merlin (Bois) - 3677\n#20 Miho (Bois) - 3677\n#21 Zhu Bajie  (Bois) - 3671\n#22 Sha wujing (Bois) - 3664\n#23 Valkyrie (Bois) - 3657\n#24 Alpaca (Bois)\nMowgli (Bois) - 3650\n#25 Indra (Bois) - 3643\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Sherlock (Bois) - 3637\n#27 Tails (Bois) - 3616\n#28 Yuki (Bois) - 3616\n#29 Sparkitt (Bois) - 3596\n#30 Poseidon (Bois) - 3582\n#31 Kiki (Bois) - 3575\n#32 Sanzang (Bois) - 3575\n#33 Soldat Slime (Bois) - 3568\n#34 Persephone (Bois) - 3562\n#35 Balrona (Bois) - 3548\n#36 Siegfried (Bois) - 3521\n#37 Thor (Bois) - 3514\n#38 Cocomaru (Bois)\nRudolph (Bois) - 3500\n#39 Lupin (Bois) - 3494\n#40 Leo (Bois) - 3487\n#41 Cauchemar (Bois) - 3480\n#42 Félinelame (Bois) - 3473\n#43 Mari (Bois) - 3473\n#44 Fennec (Bois)\nEcurrix (Bois)\nZarid (Bois) - 3466\n#45 Succube (Bois) - 3446\n#46 Croquignol (Bois)\nFenrir (Bois) - 3439\n#47 Champi (Bois) - 3432\n#48 Fée (Bois) - 3425\n#49 Citrouillon(Bois)\nLoki (Bois) - 3425\n#50 Canna (Bois)\nWendigo (Bois) - 3425\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang4a','Rang4A']]):
    embed=discord.Embed(title="Rang: Attaque (light)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1  - 4038\n#2 Indra (Light) - 4018\n#3 Arthur (Light) - 3977\n#4 Shinobi (Light) - 3936\n#5 Poseidon (Light) - 3916\n#6 Hohenheim (Light) - 3909\n#7 Garuda (Light) - 3902\n#8 Artemis (Light) - 3902\n#9 Hades (Light) - 3889\n#10 Yuki (Light) - 3854\n#11 Leo (Light) - 3848\n#12 Mini Camilla (Light)\nMini Seira (Light) - 3841\n#13 Médusine (Light) - 3834\n#14 Sphinx (Light) - 3766\n#15 Benjabuton (Light) - 3732\n#16 Mini Tina (Light) - 3718\n#17 Vampire (Light) - 3698\n#18 Sparkitt (Light) - 3677\n#19 Givri (Light) - 3677\n#20 D'artagnan (Light)\nFennec (Light)\nYaksha (Light) - 3677\n#21 Sherlock (Light) - 3671\n#22 Jiangshi (Light) - 3664\n#23 Somnol (Light) - 3657\n#24 Citrouillon(Light) - 3650\n#25 Incubus (Light) - 3643\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Leo (Light)\nTorpin (Light) - 3637\n#27 Piou (Light)\nMowgli (Light) - 3616\n#28 Radic (Light)\nTigar (Light) - 3616\n#29 Wendigo (Light) - 3596\n#30 Valkyrie (Light) - 3582\n#31 Chasseur (Light) - 3575\n#32 Soldat Slime (Light)\nTanya (Light) - 3575\n#33 Nifa (Light) - 3568\n#34 Siegfried (Light) - 3562\n#35 Merlin (Light) - 3548\n#36 Médusa (Light) - 3521\n#37 Fenrir (Light) - 3514\n#38 Balrona (Light) - 3500\n#39 Bast (Light) - 3494\n#40 Zhu Bajie  (Light) - 3487\n#41 Onmyoji (Light) - 3480\n#42 Ramu (Light) - 3473\n#43 Sanzang (Light) - 3473\n#44 Sun Wukong (Light) - 3466\n#45 Silver (Light) - 3446\n#46 Bon (Light) - 3439\n#47 Monkiki (Light) - 3432\n#48 Persephone (Light) - 3425\n#49 Mino (Light) - 3425\n#50 Sha wujing (Light) - 3425\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang5a','Rang5A']]):
    embed=discord.Embed(title="Rang: Attaque (dark)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Shadow (Dark) - 4038\n#2 Sanzang (Dark) - 4018\n#3 Persephone (Dark) - 3977\n#4 Sha wujing (Dark) - 3936\n#5 Hohenheim (Dark) - 3916\n#6 Onmyoji (Dark) - 3909\n#7 Hades (Dark)\nIndra (Dark) - 3902\n#8 Leo (Dark) - 3902\n#9 Lucy (Dark) - 3889\n#10 Mini Camilla (Dark)\nMini Seira (Dark) - 3854\n#11 Spectre des sables (Dark) - 3848\n#12 Bulbie (Dark)\nMini Tina (Dark) - 3841\n#13 Kiki (Dark) - 3834\n#14 Fenrir (Dark) - 3766\n#15 Somnol (Dark) - 3732\n#16 Lupin (Dark) - 3718\n#17 Shinobi (Dark) - 3698\n#18 Canna (Dark) - 3677\n#19 Félinelame (Dark)\nJiangshi (Dark) - 3677\n#20 Pégase (Dark) - 3677\n#21 Mona (Dark) - 3671\n#22 Incubus (Dark) - 3664\n#23 Rudolph (Dark) - 3657\n#24 Garuda (Dark) - 3650\n#25 Scarabo (Dark) - 3643\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Mandragore (Dark) - 3637\n#27 Alpaca (Dark) - 3616\n#28 Nezha (Dark) - 3616\n#29 Sura (Dark) - 3596\n#30 Draka (Dark) - 3582\n#31 Mari (Dark) - 3575\n#32 Mowgli (Dark) - 3575\n#33 Gravel (Dark) - 3568\n#34 Mammont (Dark) - 3562\n#35 Sphinx (Dark) - 3548\n#36 Latt (Dark)\nFenrir (Dark) - 3521\n#37 Odin (Dark) - 3514\n#38 Thor (Dark) - 3500\n#39 Benjabuton (Dark) - 3494\n#40 Verde (Dark) - 3487\n#41 Cocomaru (Dark) - 3480\n#42 Sun Wukong (Dark) - 3473\n#43 Chloe (Dark) - 3473\n#44 Misha (Dark) - 3466\n#45 Yaksha (Dark) - 3446\n#46 Ammonore (Dark) - 3439\n#47 Givri (Dark) - 3432\n#48 Yuki (Dark) - 3425\n#49 Penpen (Dark) - 3425\n#50 Succube (Dark) - 3425\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)

     	 
	 #######################################
	 ############    Top Def    ############
	 #######################################

 if any([message.content.startswith(item) for item in ['Rangd','RangD']]):
    embed=discord.Embed(title="Rang: Défense", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Zhu Bajie  (Light) - 3957\n#2 Zhu Bajie  (Bois) - 3943\n#3 Cauchemar (Light) - 3875\n#4 Zhu Bajie  (Eau) - 3848\n#5 Siegfried (Dark) - 3807\n#6 Poseidon (Bois) - 3773\n#7 Sanzang (Eau) - 3698\n#8 Victoria (Feu) - 3671\n#9 Anu (Dark)\nVictoria (Light) - 3657\n#10 Artemis (Dark) - 3657\n#11 Garuda (Feu)\nOnmyoji (Light) - 3650\n#12 Cauchemar (Bois)\nPoseidon (Dark) - 3609\n#13 Sha wujing (Light) - 3609\n#14 Kiki (Light)\nMari (Light) - 3602\n#15 Bast (Light)\nOnmyoji (Bois)\nSanzang (Feu)\nShiva (Dark) - 3602\n#16 Persephone (Light) - 3596\n#17 Succube (Dark) - 3568\n#18 Cauchemar (Eau) - 3568\n#19 Shiva (Feu) - 3562\n#20 Leo (Bois) - 3562\n#21 Balrona (Bois) - 3562\n#22 Mandragore (Light) - 3562\n#23 Miho (Light) - 3548\n#24 Loki (Bois) - 3521\n#25 Sirène (Light) - 3514\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Chloe (Light) - 3494\n#27 Phibian (Light)\nRudolph (Light) - 3487\n#28 Fenrir (Bois) - 3466\n#29 Canna (Eau)\nSphinx (Eau) - 3439\n#30 Scarabo (Bois)\nPégase (Light) - 3425\n#31 Balrona (Feu) - 3391\n#32 Jeanne (Eau) - 3337\n#33 Bast (Feu) - 3323\n#34 Cura (Light)\nD'artagnan (Dark) - 3310\n#35 Benjabuton (Eau)\nRadic (Dark)\nGravel (Light)\nCrapora (Dark) - 3296\n#36 Tipiaf (Eau)\nChloe (Eau)\nMammont (Bois)\nSuccube (Dark) - 3296\n#37 Monkiki (Dark)\nVampire (Dark) - 3269\n#38 Draka (Dark) - 3269\n#39 Odin (Eau) - 3248\n#40 Jeanne (Dark)\nVenus (Dark) - 3235\n#41 Bulbie (Light)\nLermite (Eau)\nChasseur (Dark)\nLeo (Bois) - 3235\n#42 Scarabo (Light)\nYeti (Light) - 3221\n#43 Silver (Light) - 3221\n#44 Misha (Dark)\nSura (Bois) - 3216\n#45 Scarabo (Feu)\nPégase (Bois)\nTanya (Dark) - 3208\n#46 Shinobi (Eau) - 3201\n#47 Odin (Feu) - 3194\n#48 Soldat Slime (Eau) - 3194\n#49 Cayou (Feu) - 3187\n#50 Mona (Light)\nTigar (Eau) - 3187", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang1d','Rang1D']]):
    embed=discord.Embed(title="Rang: Défense (Feu)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Victoria (Feu) - 3957\n#2 Garuda (Feu) - 3943\n#3 Sanzang (Feu) - 3875\n#4 Shiva (Feu) - 3848\n#5 Balrona (Feu) - 3807\n#6 Bast (Feu) - 3773\n#7 Scarabo (Feu) - 3698\n#8 Odin (Feu) - 3671\n#9 Cayou (Feu) - 3657\n#10 Thor (Feu)\nYaksha (Feu) - 3657\n#11 Spectre des sables (Feu) - 3650\n#12 Shinobi (Feu) - 3609\n#13 Tigar (Feu) - 3609\n#14 Cocomaru (Feu) - 3602\n#15 Valkyrie (Feu) - 3602\n#16 Artemis (Feu) - 3596\n#17 Persephone (Feu) - 3568\n#18 Jiangshi (Feu) - 3568\n#19 Arthur (Feu) - 3562\n#20 Onmyoji (Feu) - 3562\n#21 Anu (Feu) - 3562\n#22 Poseidon (Feu) - 3562\n#23 Arch (Feu) - 3548\n#24 Hohenheim (Feu) - 3521\n#25 Siegfried (Feu) - 3514\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Poulpo (Feu) - 3494\n#27 Penpen (Feu) - 3487\n#28 Verde (Feu) - 3466\n#29 Merlin (Feu) - 3439\n#30 Champi (Feu) - 3425\n#31 Incubus (Feu) - 3391\n#32 Fenrir (Feu) - 3337\n#33 Piou (Feu)\nSuccube (Feu) - 3323\n#34 Draka (Feu)\nLeo (Feu) - 3310\n#35 Hades (Feu) - 3296\n#36 Somnol (Feu) - 3296\n#37 Taupinou (Feu) - 3269\n#38 Sun Wukong (Feu) - 3269\n#39 Yuki (Feu) - 3248\n#40 Cura (Feu) - 3235\n#41 Banshee (Feu) - 3235\n#42 Hana (Feu) - 3221\n#43 D'artagnan (Feu) - 3221\n#44 Zhu Bajie  (Feu) - 3216\n#45 Lucy (Feu) - 3208\n#46 Kiki (Feu) - 3201\n#47 Chloe (Feu) - 3194\n#48 Sparkitt (Feu) - 3194\n#49 Pégase (Feu) - 3187\n#50 Lupin (Feu)\nFenrir (Feu) - 3187\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang2d','Rang2D']]):
    embed=discord.Embed(title="Rang: Défense (Eau)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Zhu Bajie  (Eau) - 3957\n#2 Sanzang (Eau) - 3943\n#3 Cauchemar (Eau) - 3875\n#4 Canna (Eau)\nSphinx (Eau) - 3848\n#5 Jeanne (Eau) - 3807\n#6 Benjabuton (Eau) - 3773\n#7 Tipiaf (Eau)\nChloe (Eau) - 3698\n#8 Odin (Eau) - 3671\n#9 Lermite (Eau) - 3657\n#10 Shinobi (Eau) - 3657\n#11 Soldat Slime (Eau) - 3650\n#12 Tigar (Eau) - 3609\n#13 Indra (Eau) - 3609\n#14 Hohenheim (Eau) - 3602\n#15 Ramu (Eau) - 3602\n#16 Sha wujing (Eau) - 3596\n#17 Arthur (Eau) - 3568\n#18 Garuda (Eau) - 3568\n#19 Citrouillon(Eau) - 3562\n#20 Persephone (Eau) - 3562\n#21 Artemis (Eau) - 3562\n#22 Mera (Eau) - 3562\n#23 Sun Wukong (Eau) - 3548\n#24 Hades (Eau) - 3521\n#25 Succube (Eau) - 3514\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Félinelame (Eau) - 3494\n#27 Somnol (Eau) - 3487\n#28 Siegfried (Eau) - 3466\n#29 Draka (Eau) - 3439\n#30 Wendigo (Eau) - 3425\n#31 Pégase (Eau) - 3391\n#32 Djinn (Eau) - 3337\n#33 Monkiki (Eau)\nPoseidon (Eau) - 3323\n#34 Valkyrie (Eau)\nYeti (Eau) - 3310\n#35 Nezha (Eau) - 3296\n#36 Bon (Eau)\nPenpen (Eau) - 3296\n#37 Verde (Eau) - 3269\n#38 Arch (Eau) - 3269\n#39 Mari (Eau)\nSuccube (Eau) - 3248\n#40 Balrona (Eau)\nCupidon (Eau) - 3235\n#41 Victoria (Eau) - 3235\n#42 Incubus (Eau) - 3221\n#43 Poulpo (Eau) - 3221\n#44 Shiva (Eau) - 3216\n#45 Sonic (Eau)\nLumo (Eau) - 3208\n#46 Bulbie (Eau) - 3201\n#47 Mildeu (Eau)\nSlime (Eau) - 3194\n#48 Spectre des sables (Eau) - 3194\n#49 Anu (Eau) - 3187\n#50 Ecurrix (Eau) - 3187\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang3d','Rang3D']]):
    embed=discord.Embed(title="Rang: Défense (Bois)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Zhu Bajie  (Bois) - 3957\n#2 Poseidon (Bois) - 3943\n#3 Cauchemar (Bois) - 3875\n#4 Onmyoji (Bois) - 3848\n#5 Leo (Bois) - 3807\n#6 Balrona (Bois) - 3773\n#7 Loki (Bois) - 3698\n#8 Fenrir (Bois) - 3671\n#9 Scarabo (Bois) - 3657\n#10 Mammont (Bois) - 3657\n#11 Sura (Bois) - 3650\n#12 Pégase (Bois) - 3609\n#13 Misha (Bois) - 3609\n#14 Valkyrie (Bois) - 3602\n#15 Indra (Bois) - 3602\n#16 Persephone (Bois) - 3596\n#17 Hohenheim (Bois) - 3568\n#18 Tails (Bois)\nSha wujing (Bois) - 3568\n#19 Mandragore (Bois) - 3562\n#20 Draka (Bois) - 3562\n#21 Shiva (Bois) - 3562\n#22 Ammonore (Bois) - 3562\n#23 Shinobi (Bois) - 3548\n#24 Garuda (Bois)\nMerlin (Bois) - 3521\n#25 Torpin (Bois) - 3514\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Clamy (Bois) - 3494\n#27 Hades (Bois) - 3487\n#28 Succube (Bois) - 3466\n#29 Odin (Bois) - 3439\n#30 Yuki (Bois) - 3425\n#31 Bast (Bois)\nGargor (Bois) - 3391\n#32 Sparkitt (Bois) - 3337\n#33 Sanzang (Bois) - 3323\n#34 Anu (Bois) - 3310\n#35 Bron (Bois)\nChasseur (Bois)\nMona (Bois) - 3296\n#36 Incubus (Bois) - 3296\n#37 Thor (Bois) - 3269\n#38 Artemis (Bois) - 3269\n#39 Lucy (Bois) - 3248\n#40 Arthur (Bois) - 3235\n#41 Médusa (Bois) - 3235\n#42 Sphinx (Bois) - 3221\n#43 Canna (Bois) - 3221\n#44 Peyote (Bois)\nPottus (Bois) - 3216\n#45 Lupin (Bois) - 3208\n#46 Benjabuton (Bois) - 3201\n#47 Radic (Bois) - 3194\n#48 Mimic (Bois) - 3194\n#49 D'artagnan (Bois) - 3187\n#50 Bulbie (Bois) - 3187\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang4d','Rang4D']]):
    embed=discord.Embed(title="Rang: Défense (light)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1  - 3957\n#2 Cauchemar (Light) - 3943\n#3 Victoria (Light) - 3875\n#4 Onmyoji (Light) - 3848\n#5 Sha wujing (Light) - 3807\n#6 Kiki (Light)\nMari (Light) - 3773\n#7 Bast (Light) - 3698\n#8 Persephone (Light) - 3671\n#9 Mandragore (Light) - 3657\n#10 Miho (Light) - 3657\n#11 Sirène (Light) - 3650\n#12 Chloe (Light) - 3609\n#13 Phibian (Light)\nRudolph (Light) - 3609\n#14 Pégase (Light) - 3602\n#15 Cura (Light) - 3602\n#16 Gravel (Light) - 3596\n#17 Bulbie (Light) - 3568\n#18 Scarabo (Light)\nYeti (Light) - 3568\n#19 Silver (Light) - 3562\n#20 Mona (Light) - 3562\n#21 Djinn (Light) - 3562\n#22 Mera (Light) - 3562\n#23 Shinobi (Light) - 3548\n#24 Merlin (Light) - 3521\n#25 Odin (Light) - 3514\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Balrona (Light) - 3494\n#27 Valkyrie (Light) - 3487\n#28 Lupio (Light) - 3466\n#29 Fenrir (Light) - 3439\n#30 Siegfried (Light) - 3425\n#31 Alpaca (Light) - 3391\n#32 Garuda (Light) - 3337\n#33 Monkiki (Light) - 3323\n#34 Poseidon (Light) - 3310\n#35 Banshee (Light) - 3296\n#36 Sanzang (Light) - 3296\n#37 Radic (Light) - 3269\n#38 Succube (Light) - 3269\n#39 Yuki (Light) - 3248\n#40 Sura (Light) - 3235\n#41 Zarid (Light) - 3235\n#42 Chiroptie (Light)\nKiloptère (Light) - 3221\n#43 Venus (Light) - 3221\n#44 Cupidon (Light) - 3216\n#45 Latt (Light) - 3208\n#46 Hohenheim (Light)\nMildeu (Light) - 3201\n#47 Thor (Light) - 3194\n#48 Leo (Light) - 3194\n#49 Indra (Light) - 3187\n#50 Loki (Light) - 3187\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang5d','Rang5D']]):
    embed=discord.Embed(title="Rang: Défense (dark)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Siegfried (Dark) - 3957\n#2 Anu (Dark) - 3943\n#3 Artemis (Dark) - 3875\n#4 Poseidon (Dark) - 3848\n#5 Shiva (Dark) - 3807\n#6 Succube (Dark) - 3773\n#7 D'artagnan (Dark) - 3698\n#8 Radic (Dark)\nCrapora (Dark) - 3671\n#9 Monkiki (Dark)\nVampire (Dark) - 3657\n#10 Draka (Dark) - 3657\n#11 Jeanne (Dark)\nVenus (Dark) - 3650\n#12 Chasseur (Dark) - 3609\n#13 Misha (Dark) - 3609\n#14 Tanya (Dark) - 3602\n#15 Stella (Dark) - 3602\n#16 Merlin (Dark) - 3596\n#17 Odin (Dark) - 3568\n#18 Zhu Bajie  (Dark) - 3568\n#19 Benjabuton (Dark) - 3562\n#20 Sphinx (Dark) - 3562\n#21 Sun Wukong (Dark) - 3562\n#22 Truffel (Dark) - 3562\n#23 Victoria (Dark) - 3548\n#24 Otari (Dark) - 3521\n#25 Persephone (Dark)\nShinobi (Dark) - 3514\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="Def\n#1 Siegfried (Dark) - 3957\n#2 Anu (Dark) - 3943\n#3 Artemis (Dark) - 3875\n#4 Poseidon (Dark) - 3848\n#5 Shiva (Dark) - 3807\n#6 Succube (Dark) - 3773\n#7 D'artagnan (Dark) - 3698\n#8 Radic (Dark)\nCrapora (Dark) - 3671\n#9 Monkiki (Dark)\nVampire (Dark) - 3657\n#10 Draka (Dark) - 3657\n#11 Jeanne (Dark)\nVenus (Dark) - 3650\n#12 Chasseur (Dark) - 3609\n#13 Misha (Dark) - 3609\n#14 Tanya (Dark) - 3602\n#15 Stella (Dark) - 3602\n#16 Merlin (Dark) - 3596\n#17 Odin (Dark) - 3568\n#18 Zhu Bajie  (Dark) - 3568\n#19 Benjabuton (Dark) - 3562\n#20 Sphinx (Dark) - 3562\n#21 Sun Wukong (Dark) - 3562\n#22 Truffel (Dark) - 3562\n#23 Victoria (Dark) - 3548\n#24 Otari (Dark) - 3521\n#25 Persephone (Dark)\nShinobi (Dark) - 3514\n#26 Givri (Dark) - 3494\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)

     	 
	 #######################################
	 ############   Top Recup   ############
	 #######################################

 if any([message.content.startswith(item) for item in ['Rangr','RangR']]):
    embed=discord.Embed(title="Rang: Récupération", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Hana (Bois) - 3364\n#2 Sirène (Dark) - 3344\n#3 Cupidon (Feu) - 3323\n#4 Hana (Eau) - 3310\n#5 Bast (Bois) - 3303\n#6 Bast (Feu) - 3255\n#7 Zhu Bajie  (Dark) - 3209\n#8 Cupidon (Light) - 3194\n#9 Fée (Dark) - 3173\n#10 Fée (Light) - 3139\n#11 Fée (Eau) - 3133\n#12 Cupidon (Bois) - 3099\n#13 Hana (Dark) - 3058\n#14 Odin (Eau) - 3012\n#15 Cupidon (Eau) - 3003\n#16 Balrona (Feu) - 2999\n#17 Cura (Feu) - 2996\n#18 Cauchemar (Dark) - 2916\n#19 Hana (Feu)\nFée (Bois) - 2881\n#20 Indra (Eau) - 2881\n#21 Sirène (Eau) - 2876\n#22 Mini Tina (Light) - 2867\n#23 Sanzang (Light) - 2853\n#24 Nezha (Eau) - 2787\n#25 Sirène (Feu) - 2774\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Mildeu (Bois) - 2751\n#27 Tails (Bois) - 2697\n#28 Sanzang (Eau) - 2692\n#29 Tigar (Feu) - 2690\n#30 Odin (Light) - 2685\n#31 Siegfried (Light) - 2677\n#32 Chapillon (Bois)\nZhu Bajie  (Feu) - 2672\n#33 Mera (Eau) - 2663\n#34 Arthur (Eau)\nHades (Eau) - 2663\n#35 Persephone (Eau)\nValkyrie (Bois) - 2658\n#36 Hades (Feu)\nSanzang (Feu)\nZhu Bajie  (Light) - 2644\n#37 Persephone (Feu) - 2644\n#38 Persephone (Bois) - 2624\n#39 Chapillon (Eau) - 2624\n#40 Onmyoji (Bois)\nShiva (Dark) - 2622\n#41 Zhu Bajie  (Bois) - 2622\n#42 Merlin (Bois)\nSun Wukong (Dark) - 2622\n#43 Cotonou (Feu)\nCotonou (Bois)\nMildeu (Dark)\nZhu Bajie  (Eau) - 2617\n#44 Miho (Light) - 2610\n#45 Hohenheim (Bois)\nPoseidon (Dark) - 2595\n#46 Hohenheim (Eau) - 2588\n#47 Victoria (Dark)\nYuki (Eau) - 2588\n#48 Shinobi (Eau) - 2581\n#49 Poseidon (Feu) - 2576\n#50 Fée (Feu) - 2576\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang1r','Rang1R']]):
    embed=discord.Embed(title="Rang: Récupération (Feu)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Cupidon (Feu) - 3364\n#2 Bast (Feu) - 3344\n#3 Balrona (Feu) - 3323\n#4 Cura (Feu) - 3310\n#5 Hana (Feu) - 3303\n#6 Sirène (Feu) - 3255\n#7 Tigar (Feu) - 3209\n#8 Zhu Bajie  (Feu) - 3194\n#9 Hades (Feu)\nSanzang (Feu) - 3173\n#10 Persephone (Feu) - 3139\n#11 Cotonou (Feu) - 3133\n#12 Poseidon (Feu) - 3099\n#13 Fée (Feu) - 3058\n#14 Onmyoji (Feu) - 3012\n#15 Mildeu (Feu) - 3003\n#16 Rubani (Feu) - 2999\n#17 Odin (Feu) - 2996\n#18 Cauchemar (Feu) - 2916\n#19 Sun Wukong (Feu) - 2881\n#20 Hohenheim (Feu) - 2881\n#21 Slime (Feu)\nThor (Feu) - 2876\n#22 Victoria (Feu) - 2867\n#23 Merlin (Feu) - 2853\n#24 Valkyrie (Feu) - 2787\n#25 Fenrir (Feu) - 2774\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Arthur (Feu) - 2751\n#27 Yuki (Feu) - 2697\n#28 Indra (Feu) - 2692\n#29 Artemis (Feu) - 2690\n#30 Lumo (Feu) - 2685\n#31 Verde (Feu) - 2677\n#32 Shiva (Feu) - 2672\n#33 Tipiaf (Feu) - 2663\n#34 Canna (Feu) - 2663\n#35 Sha wujing (Feu) - 2658\n#36 Scarabo (Feu) - 2644\n#37 Sparkitt (Feu) - 2644\n#38 Siegfried (Feu) - 2624\n#39 Banshee (Feu) - 2624\n#40 Draka (Feu) - 2622\n#41 Lupin (Feu) - 2622\n#42 Shinobi (Feu) - 2622\n#43 Loki (Feu) - 2617\n#44 Jeanne (Feu) - 2610\n#45 Benjabuton (Feu) - 2595\n#46 Knuckles (Feu) - 2588\n#47 Kiki (Feu) - 2588\n#48 Mammont (Feu) - 2581\n#49 Djinn (Feu) - 2576\n#50 Garuda (Feu) - 2576\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang2r','Rang2R']]):
    embed=discord.Embed(title="Rang: Récupération (Eau)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Hana (Eau) - 3364\n#2 Fée (Eau) - 3344\n#3 Odin (Eau) - 3323\n#4 Cupidon (Eau) - 3310\n#5 Indra (Eau) - 3303\n#6 Sirène (Eau) - 3255\n#7 Nezha (Eau) - 3209\n#8 Sanzang (Eau) - 3194\n#9 Mera (Eau) - 3173\n#10 Arthur (Eau)\nHades (Eau) - 3139\n#11 Persephone (Eau) - 3133\n#12 Chapillon (Eau) - 3099\n#13 Zhu Bajie  (Eau) - 3058\n#14 Hohenheim (Eau) - 3012\n#15 Yuki (Eau) - 3003\n#16 Shinobi (Eau) - 2999\n#17 Somnol (Eau) - 2996\n#18 Cotonou (Eau) - 2916\n#19 Artemis (Eau) - 2881\n#20 Mari (Eau) - 2881\n#21 Tigar (Eau) - 2876\n#22 Valkyrie (Eau) - 2867\n#23 Balrona (Eau) - 2853\n#24 Chloe (Eau) - 2787\n#25 Sun Wukong (Eau) - 2774\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Merlin (Eau)\nCauchemar (Eau) - 2751\n#27 Poseidon (Eau)\nSiegfried (Eau) - 2697\n#28 Sura (Eau) - 2692\n#29 Fenrir (Eau) - 2690\n#30 Pégase (Eau) - 2685\n#31 Canna (Eau) - 2677\n#32 Bast (Eau)\nShiva (Eau) - 2672\n#33 Draka (Eau)\nGaruda (Eau) - 2663\n#34 Benjabuton (Eau)\nDjinn (Eau) - 2663\n#35 Victoria (Eau) - 2658\n#36 Sha wujing (Eau) - 2644\n#37 Thor (Eau) - 2644\n#38 Sonic (Eau)\nVampire (Eau) - 2624\n#39 Mammont (Eau) - 2624\n#40 Cura (Eau) - 2622\n#41 Leo (Eau) - 2622\n#42 Anu (Eau) - 2622\n#43 Peyote (Eau)\nPottus (Eau) - 2617\n#44 Onmyoji (Eau) - 2610\n#45 Scarabo (Eau) - 2595\n#46 Jeanne (Eau) - 2588\n#47 Lucy (Eau) - 2588\n#48 Sphinx (Eau) - 2581\n#49 Miho (Eau) - 2576\n#50 Wendigo (Eau) - 2576\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang3r','Rang3R']]):
    embed=discord.Embed(title="Rang: Récupération (Bois)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1  - 3364\n#2 Bast (Bois) - 3344\n#3 Cupidon (Bois) - 3323\n#4 Fée (Bois) - 3310\n#5 Mildeu (Bois) - 3303\n#6 Tails (Bois) - 3255\n#7 Chapillon (Bois) - 3209\n#8 Valkyrie (Bois) - 3194\n#9 Persephone (Bois) - 3173\n#10 Onmyoji (Bois) - 3139\n#11 Zhu Bajie  (Bois) - 3133\n#12 Merlin (Bois) - 3099\n#13 Cotonou (Bois) - 3058\n#14 Hohenheim (Bois) - 3012\n#15 Hades (Bois) - 3003\n#16 Sacstère (Bois) - 2999\n#17 Sparkitt (Bois) - 2996\n#18 Rubani (Bois) - 2916\n#19 Sirène (Bois) - 2881\n#20 Tincel (Bois) - 2881\n#21 Yuki (Bois) - 2876\n#22 Canna (Bois) - 2867\n#23 Cauchemar (Bois) - 2853\n#24 Fenrir (Bois) - 2787\n#25 Lucy (Bois) - 2774\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Sun Wukong (Bois) - 2751\n#27 Sanzang (Bois) - 2697\n#28 D'artagnan (Bois)\nLupin (Bois) - 2692\n#29 Arthur (Bois)\nLumo (Bois) - 2690\n#30 Artemis (Bois) - 2685\n#31 Succube (Bois) - 2677\n#32 Vampire (Bois) - 2672\n#33 Shinobi (Bois) - 2663\n#34 Mammont (Bois) - 2663\n#35 Poseidon (Bois) - 2658\n#36 Cura (Bois)\nSiegfried (Bois) - 2644\n#37 Garuda (Bois) - 2644\n#38 Anu (Bois)\nOdin (Bois) - 2624\n#39 Shiva (Bois) - 2624\n#40 Somnol (Bois)\nFenrir (Bois) - 2622\n#41 Miho (Bois) - 2622\n#42 Balrona (Bois) - 2622\n#43 Leo (Bois) - 2617\n#44 Mera (Bois) - 2610\n#45 Victoria (Bois) - 2595\n#46 Nezha (Bois)\nTigar (Bois) - 2588\n#47 Pégase (Bois) - 2588\n#48 Sha wujing (Bois) - 2581\n#49 Yaksha (Bois) - 2576\n#50 Djinn (Bois) - 2576\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang4r','Rang4R']]):
    embed=discord.Embed(title="Rang: Récupération (light)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Cupidon (Light) - 3364\n#2 Fée (Light) - 3344\n#3 Mini Tina (Light) - 3323\n#4 Sanzang (Light) - 3310\n#5 Odin (Light) - 3303\n#6 Siegfried (Light) - 3255\n#7 Zhu Bajie  (Light) - 3209\n#8 Miho (Light) - 3194\n#9 Sun Wukong (Light) - 3173\n#10 Valkyrie (Light) - 3139\n#11 Monkiki (Light) - 3133\n#12 Mini Camilla (Light)\nMini Seira (Light)\nSha wujing (Light) - 3099\n#13 Latt (Light) - 3058\n#14 Succube (Light) - 3012\n#15 Hohenheim (Light) - 3003\n#16 Cocomaru (Light) - 2999\n#17 Loki (Light) - 2996\n#18 Stella (Light) - 2916\n#19 Somnol (Light) - 2881\n#20 Hana (Light) - 2881\n#21 Yuki (Light) - 2876\n#22 Bulbie (Light) - 2867\n#23 Mimic (Light) - 2853\n#24 Leo (Light) - 2787\n#25 Mera (Light) - 2774\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Banshee (Light) - 2751\n#27 Fenrir (Light) - 2697\n#28 Artemis (Light) - 2692\n#29 Hades (Light) - 2690\n#30 Cauchemar (Light)\nOnmyoji (Light) - 2685\n#31 Shinobi (Light) - 2677\n#32 Indra (Light)\nPoseidon (Light) - 2672\n#33 Verde (Light) - 2663\n#34 Torpin (Light)\nYaksha (Light) - 2663\n#35 Canna (Light) - 2658\n#36 Mandragore (Light) - 2644\n#37 Pégase (Light) - 2644\n#38 Crapora (Light) - 2624\n#39 Nezha (Light) - 2624\n#40 Wendigo (Light) - 2622\n#41 Leo (Light)\nSoldat Slime (Light) - 2622\n#42 Anu (Light) - 2622\n#43 Ramu (Light) - 2617\n#44 Bast (Light)\nD'artagnan (Light)\nGaruda (Light)\nIncubus (Light)\nRadic (Light) - 2610\n#45 Citrouillon(Light)\nNifa (Light) - 2595\n#46 Djinn (Light) - 2588\n#47 Chasseur (Light)\nRudolph (Light) - 2588\n#48 Flora (Light) - 2581\n#49 Mammont (Light) - 2576\n#50 Cura (Light)\nTanya (Light) - 2576\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang5r','Rang5R']]):
    embed=discord.Embed(title="Rang: Récupération (dark)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Sirène (Dark) - 3364\n#2 Zhu Bajie  (Dark) - 3344\n#3 Fée (Dark) - 3323\n#4 Hana (Dark) - 3310\n#5 Cauchemar (Dark) - 3303\n#6 Shiva (Dark) - 3255\n#7 Sun Wukong (Dark) - 3209\n#8 Mildeu (Dark) - 3194\n#9 Poseidon (Dark) - 3173\n#10 Victoria (Dark) - 3139\n#11 Chloe (Dark) - 3133\n#12 Bast (Dark) - 3099\n#13 Mini Camilla (Dark)\nMini Seira (Dark)\nVenus (Dark) - 3058\n#14 Flora (Dark) - 3012\n#15 Siegfried (Dark) - 3003\n#16 Draka (Dark) - 2999\n#17 Onmyoji (Dark) - 2996\n#18 Benjabuton (Dark) - 2916\n#19 Miho (Dark) - 2881\n#20 Mini Tina (Dark)\nSanzang (Dark) - 2881\n#21 Hohenheim (Dark) - 2876\n#22 Garuda (Dark) - 2867\n#23 Gemini (Dark) - 2853\n#24 Sha wujing (Dark)\nThor (Dark) - 2787\n#25 Stella (Dark) - 2774\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Wendigo (Dark)\nYaksha (Dark) - 2751\n#27 Tigar (Dark) - 2697\n#28 Monkiki (Dark)\nShinobi (Dark)\nFenrir (Dark) - 2692\n#29 Indra (Dark) - 2690\n#30 Leo (Dark) - 2685\n#31 Somnol (Dark) - 2677\n#32 Gravel (Dark) - 2672\n#33 Artemis (Dark) - 2663\n#34 Valkyrie (Dark) - 2663\n#35 Mera (Dark) - 2658\n#36 Vampire (Dark) - 2644\n#37 Tanya (Dark)\nCrapora (Dark) - 2644\n#38 Cupidon (Dark) - 2624\n#39 Djinn (Dark) - 2624\n#40 Jeanne (Dark) - 2622\n#41 Médusine (Dark) - 2622\n#42 Citrouillon(Dark) - 2622\n#43 Incubus (Dark)\nNezha (Dark) - 2617\n#44 Cura (Dark) - 2610\n#45 Torpin (Dark) - 2595\n#46 Fenrir (Dark) - 2588\n#47 Lucy (Dark)\nLupin (Dark)\nPégase (Dark) - 2588\n#48 Mona (Dark) - 2581\n#49 Yuki (Dark) - 2576\n#50 Succube (Dark) - 2576\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
     	 
	 #######################################
	 ############    Top Epv    ############
	 #######################################

 if any([message.content.startswith(item) for item in ['Range','RangE']]):
    embed=discord.Embed(title="Rang: ePV", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Draka (Bois) - 168121\n#2 Odin (Feu) - 153139\n#3 Arthur (Dark) - 152691\n#4 Zhu Bajie  (Dark) - 149963\n#5 Balrona (Dark) - 148935\n#6 Shiva (Eau) - 147230\n#7 Odin (Light) - 143782\n#8 Valkyrie (Dark) - 143756\n#9 Shinobi (Bois) - 138362\n#10 Anu (Feu) - 138277\n#11 Hohenheim (Feu) - 137921\n#12 Shiva (Light) - 136854\n#13 Victoria (Feu) - 136278\n#14 Merlin (Dark) - 135468\n#15 Miho (Light) - 134437\n#16 Succube (Eau) - 133878\n#17 Victoria (Light) - 133102\n#18 Anu (Dark) - 131892\n#19 Siegfried (Dark) - 131759\n#20 Bast (Dark) - 130723\n#21 Hades (Bois) - 130487\n#22 Poseidon (Feu) - 130241\n#23 Succube (Dark) - 129914\n#24 Leo (Bois) - 129162\n#25 Artemis (Dark) - 129115\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Fenrir (Bois) - 128421\n#27 Jeanne (Light) - 128393\n#28 Miho (Dark) - 128098\n#29 Somnol (Feu) - 128086\n#30 Shiva (Dark) - 128070\n#31 Cauchemar (Dark) - 128023\n#32 Succube (Light) - 127463\n#33 Thor (Light) - 127363\n#34 Victoria (Bois) - 127033\n#35 Zhu Bajie  (Light) - 126866\n#36 Zhu Bajie  (Bois) - 126844\n#37 Zhu Bajie  (Eau) - 126078\n#38 Benjabuton (Bois) - 125509\n#39 Artemis (Feu) - 124374\n#40 Garuda (Feu) - 124092\n#41 Sha wujing (Light) - 123429\n#42 Persephone (Light) - 123029\n#43 Onmyoji (Feu) - 122916\n#44 Nifa (Dark) - 122074\n#45 Balrona (Bois) - 120985\n#46 Bast (Eau) - 120507\n#47 Misha (Light) - 119727\n#48 Valkyrie (Feu) - 119384\n#49 Cauchemar (Light) - 119351\n#50 Poseidon (Dark) - 118978\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang1e','Rang1E']]):
    embed=discord.Embed(title="Rang: ePV (Feu)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Odin (Feu) - 168121\n#2 Anu (Feu) - 153139\n#3 Hohenheim (Feu) - 152691\n#4 Victoria (Feu) - 149963\n#5 Poseidon (Feu) - 148935\n#6 Somnol (Feu) - 147230\n#7 Artemis (Feu) - 143782\n#8 Garuda (Feu) - 143756\n#9 Onmyoji (Feu) - 138362\n#10 Valkyrie (Feu) - 138277\n#11 Sanzang (Feu) - 137921\n#12 Chloe (Feu) - 136854\n#13 Bast (Feu) - 136278\n#14 Miho (Feu) - 135468\n#15 Shinobi (Feu) - 134437\n#16 Shiva (Feu) - 133878\n#17 Sparkitt (Feu) - 133102\n#18 Yaksha (Feu) - 131892\n#19 Cayou (Feu) - 131759\n#20 Zhu Bajie  (Feu) - 130723\n#21 Citrouillon(Feu) - 130487\n#22 Persephone (Feu) - 130241\n#23 Cocomaru (Feu) - 129914\n#24 Incubus (Feu) - 129162\n#25 Canna (Feu) - 129115\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Penpen (Feu) - 128421\n#27 Scarabo (Feu) - 128393\n#28 Mammont (Feu) - 128098\n#29 Nezha (Feu) - 128086\n#30 Loki (Feu) - 128070\n#31 Jeanne (Feu) - 128023\n#32 Sphinx (Feu) - 127463\n#33 Thor (Feu) - 127363\n#34 Balrona (Feu) - 127033\n#35 Arch (Feu) - 126866\n#36 Fée (Feu) - 126844\n#37 Cura (Feu) - 126078\n#38 Mona (Feu) - 125509\n#39 Pincemi (Feu) - 124374\n#40 Fenrir (Feu) - 124092\n#41 Hana (Feu) - 123429\n#42 Indra (Feu) - 123029\n#43 Arthur (Feu) - 122916\n#44 Yuki (Feu) - 122074\n#45 Champi (Feu) - 120985\n#46 Médusa (Feu) - 120507\n#47 Poulpo (Feu) - 119727\n#48 Succube (Feu) - 119384\n#49 Cauchemar (Feu) - 119351\n#50 Leo (Feu) - 118978\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang2e','Rang2E']]):
    embed=discord.Embed(title="Rang: ePV (Eau)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Shiva (Eau) - 168121\n#2 Succube (Eau) - 153139\n#3 Zhu Bajie  (Eau) - 152691\n#4 Bast (Eau) - 149963\n#5 Fenrir (Eau) - 148935\n#6 Yuki (Eau) - 147230\n#7 Hohenheim (Eau) - 143782\n#8 Arthur (Eau) - 143756\n#9 Scarabo (Eau) - 138362\n#10 Benjabuton (Eau) - 138277\n#11 Persephone (Eau) - 137921\n#12 Incubus (Eau) - 136854\n#13 Leo (Eau) - 136278\n#14 Sha wujing (Eau) - 135468\n#15 Lermite (Eau) - 134437\n#16 Cauchemar (Eau) - 133878\n#17 Canna (Eau) - 133102\n#18 Banshee (Eau) - 131892\n#19 Hades (Eau) - 131759\n#20 Phibian (Eau) - 130723\n#21 Artemis (Eau) - 130487\n#22 Cura (Eau) - 130241\n#23 Lupin (Eau) - 129914\n#24 Sura (Eau) - 129162\n#25 Sanzang (Eau) - 129115\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Miho (Eau) - 128421\n#27 Jeanne (Eau) - 128393\n#28 Sun Wukong (Eau) - 128098\n#29 Verde (Eau) - 128086\n#30 Indra (Eau) - 128070\n#31 Jiangshi (Eau) - 128023\n#32 Chloe (Eau) - 127463\n#33 D'artagnan (Eau) - 127363\n#34 Lombrix (Eau) - 127033\n#35 Mimic (Eau) - 126866\n#36 Djinn (Eau) - 126844\n#37 Tigar (Eau) - 126078\n#38 Nezha (Eau) - 125509\n#39 Sphinx (Eau) - 124374\n#40 Cupidon (Eau) - 124092\n#41 Médusine (Eau) - 123429\n#42 Odin (Eau) - 123029\n#43 Bon (Eau) - 122916\n#44 Draka (Eau) - 122074\n#45 Yeti (Eau) - 120985\n#46 Shinobi (Eau) - 120507\n#47 Monkiki (Eau) - 119727\n#48 Victoria (Eau) - 119384\n#49 Siegfried (Eau) - 119351\n#50 Poseidon (Eau) - 118978\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang3e','Rang3E']]):
    embed=discord.Embed(title="Rang: ePV (Bois)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1  - 168121\n#2 Shinobi (Bois) - 153139\n#3 Hades (Bois) - 152691\n#4 Leo (Bois) - 149963\n#5 Fenrir (Bois) - 148935\n#6 Victoria (Bois) - 147230\n#7 Zhu Bajie  (Bois) - 143782\n#8 Benjabuton (Bois) - 143756\n#9 Balrona (Bois) - 138362\n#10 Onmyoji (Bois) - 138277\n#11 Siegfried (Bois) - 137921\n#12 Verde (Bois) - 136854\n#13 Poseidon (Bois) - 136278\n#14 Indra (Bois) - 135468\n#15 Sanzang (Bois) - 134437\n#16 Persephone (Bois) - 133878\n#17 Sha wujing (Bois) - 133102\n#18 Scarabo (Bois) - 131892\n#19 Cura (Bois) - 131759\n#20 Mammont (Bois) - 130723\n#21 Pégase (Bois) - 130487\n#22 Succube (Bois) - 130241\n#23 Cauchemar (Bois) - 129914\n#24 Sura (Bois) - 129162\n#25 Garuda (Bois) - 129115\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Valkyrie (Bois) - 128421\n#27 Merlin (Bois) - 128393\n#28 Bast (Bois) - 128098\n#29 Yuki (Bois) - 128086\n#30 Mandragore (Bois) - 128070\n#31 Thor (Bois) - 128023\n#32 Shiva (Bois) - 127463\n#33 Buis (Bois) - 127363\n#34 Chasseur (Bois) - 127033\n#35 Sun Wukong (Bois) - 126866\n#36 Mera (Bois) - 126844\n#37 Lucy (Bois)\nTorpin (Bois) - 126078\n#38 Loki (Bois) - 125509\n#39 Vampire (Bois) - 124374\n#40 Hohenheim (Bois) - 124092\n#41 Phibian (Bois) - 123429\n#42 Bron (Bois) - 123029\n#43 Lupin (Bois) - 122916\n#44 Beth (Bois) - 122074\n#45 Médusa (Bois) - 120985\n#46 Odin (Bois) - 120507\n#47 Canna (Bois) - 119727\n#48 Peyote (Bois)\nPottus (Bois) - 119384\n#49 D'artagnan (Bois) - 119351\n#50 Tails (Bois) - 118978\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang4e','Rang4E']]):
    embed=discord.Embed(title="Rang: ePV (light)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Odin (Light) - 168121\n#2 Shiva (Light) - 153139\n#3 Miho (Light) - 152691\n#4 Victoria (Light) - 149963\n#5 Jeanne (Light) - 148935\n#6 Succube (Light) - 147230\n#7 Thor (Light) - 143782\n#8 Zhu Bajie  (Light) - 143756\n#9 Sha wujing (Light) - 138362\n#10 Persephone (Light) - 138277\n#11 Misha (Light) - 137921\n#12 Cauchemar (Light) - 136854\n#13 Mandragore (Light) - 136278\n#14 Lucy (Light) - 135468\n#15 Bulbie (Light) - 134437\n#16 Venus (Light) - 133878\n#17 Silver (Light) - 133102\n#18 Anu (Light) - 131892\n#19 Verde (Light) - 131759\n#20 Sun Wukong (Light) - 130723\n#21 Bast (Light) - 130487\n#22 Nezha (Light) - 130241\n#23 Chloe (Light) - 129914\n#24 Pégase (Light) - 129162\n#25 Fenrir (Light) - 129115\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Torpin (Dark) - 42627\n#27 Lupio (Dark) - 42546\n#28 Peyote (Dark)\nZarid (Dark) - 42478\n#29 Yeti (Dark) - 42001\n#30 Zabeille (Dark) - 41919\n#31 Sacstère (Dark) - 41688\n#32 Victoria (Dark) - 41436\n#33 Cocomaru (Dark) - 41402\n#34 Succube (Dark) - 41388\n#35 Hades (Dark) - 41374\n#36 Médusine (Dark) - 41374\n#37 Anu (Dark) - 41265\n#38 Givri (Dark) - 41156\n#39 Shiva (Dark) - 41143\n#40 Sun Wukong (Dark) - 41143\n#41 Odin (Dark) - 41109\n#42 Phibian (Dark) - 40931\n#43 Artemis (Dark) - 40849\n#44 Siegfried (Dark) - 40801\n#45 Jeanne (Dark) - 40658\n#46 Stella (Dark) - 40312\n#47 Verde (Dark) - 40312\n#48 Leo (Dark) - 40298\n#49 Gemini (Dark) - 40040\n#50 Tanya (Dark) - 39951\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)
 if any([message.content.startswith(item) for item in ['Rang5e','Rang5E']]):
    embed=discord.Embed(title="Rang: ePV (dark)", url="", color=0xffffff)
    embed.set_author(name="")
    embed.set_thumbnail(url="")
    embed.add_field(name="#1 à #25", value="#1 Arthur (Dark) - 168121\n#2 Zhu Bajie  (Dark) - 153139\n#3 Balrona (Dark) - 152691\n#4 Valkyrie (Dark) - 149963\n#5 Merlin (Dark) - 148935\n#6 Anu (Dark) - 147230\n#7 Siegfried (Dark) - 143782\n#8 Bast (Dark) - 143756\n#9 Succube (Dark) - 138362\n#10 Artemis (Dark) - 138277\n#11 Miho (Dark) - 137921\n#12 Shiva (Dark) - 136854\n#13 Cauchemar (Dark) - 136278\n#14 Nifa (Dark) - 135468\n#15 Poseidon (Dark) - 134437\n#16 Fennec (Dark) - 133878\n#17 Piou (Dark) - 133102\n#18 Yuki (Dark) - 131892\n#19 Ramu (Dark) - 131759\n#20 Jeanne (Dark) - 130723\n#21 Mera (Dark) - 130487\n#22 Citrouillon(Dark) - 130241\n#23 Crapora (Dark) - 129914\n#24 Sparkitt (Dark) - 129162\n#25 Vampire (Dark) - 129115\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    embed.add_field(name="#26 à #50", value="#26 Cupidon (Dark) - 128421\n#27 Victoria (Dark) - 128393\n#28 Loki (Dark) - 128098\n#29 Tanya (Dark) - 128086\n#30 Radic (Dark) - 128070\n#31 Médusa (Dark) - 128023\n#32 Stella (Dark) - 127463\n#33 Chasseur (Dark) - 127363\n#34 Odin (Dark) - 127033\n#35 Sun Wukong (Dark) - 126866\n#36 Draka (Dark) - 126844\n#37 Soldat Slime (Dark) - 126078\n#38 Monkiki (Dark) - 125509\n#39 Givri (Dark) - 124374\n#40 Hades (Dark) - 124092\n#41 Banshee (Dark) - 123429\n#42 Phibian (Dark) - 123029\n#43 Cosmo (Dark) - 122916\n#44 Torpin (Dark) - 122074\n#45 Djinn (Dark) - 120985\n#46 Tigar (Dark) - 120507\n#47 Cocomaru (Dark) - 119727\n#48 Yeti (Dark) - 119384\n#49 D'artagnan (Dark) - 119351\n#50 Venus (Dark) - 118978\n .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .", inline=True)
    await message.channel.send(embed=embed)

@client.event
async def on_ready():
 print(client.user.name)
 print( "[ON]")
 print('- - - - - - - -')




client.run("NzA2MTI1OTEzMTMzMjg1NDM3.Xq1tAA.33ws5I4plwjFKXegzXbH5-D0dXE")

