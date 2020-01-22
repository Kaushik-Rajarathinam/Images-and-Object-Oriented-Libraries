import time, random
hats = ["panda", "panda king", "red mask", "bandit", "afro", "lord panda",'soldier','hard hat','purple cap','santa hat','Tron']
bodies = ["basket", 'bloodharvest', 'demonic wings', 'robo wings', 'diablo wings', 'baby panda','angelic wings']
skins = ['black', 'white', 'pale', 'red', 'yellow', 'brown', 'god']
prime = ['famas', 'assualt rifle', 'revolver', 'semi-auto', 'lmg', 'smg', 'sniper', 'rocket launcher', 'shotgun','akimbo uzi']
second = ['pistol', 'deagle', 'sawed-off', 'alienblaster']

class Avatar(object): # Krunker.io based avatar chooser.
  def __init__(self, hat="panda", body="bloodharvest", skinTone="brown", primary="sniper", secondary="pistol"):
    self.hat = hat
    self.body = body
    self.skin = skinTone
    self.primary = primary
    self.secondary = secondary
  def typehat(self):
    print "Change Hat? What is your hat?"
    prompt = raw_input("Hat> ")
    prompt = prompt.lower()
    sen=0
    check = False
    for char in hats:
      if prompt == hats[sen]:
        check = True
        print "Set: "+prompt
        self.hat = prompt
        break
      else:
        check = False
      sen+=1
    if check == False:
      print "The Hat is not in the list! Your hat has been tagged custom."
      self.hat = prompt+" [CUSTOM]"
      time.sleep(2)
    user.run()
  def typebody(self):
    print "Change Body? What is your Body?"
    prompt = raw_input("Body> ")
    prompt = prompt.lower()
    sen=0
    check = False
    for char in bodies:
      if prompt == bodies[sen]:
        check = True
        print "Set: "+prompt
        self.body = prompt
        break
      
      else:
        check = False
      sen+=1
    if check == False:
      print "The body is not in the list! Your hat has been tagged custom."
      self.body = prompt+" [CUSTOM]"
      print "Set: "+prompt+" [CUSTOM]"
      time.sleep(2)
    user.run()
  def typeskin(self):
    print "Change Skin Color? What is your skin?"
    prompt = raw_input("Skin> ")
    prompt = prompt.lower()
    sen=0
    check = False
    for char in hats:
      if prompt == hats[sen]:
        check = True
        print "Set: "+prompt
        self.skin = prompt
        break
      else:
        check = False
      sen+=1
    if check == False:
      print "The skin color is not in the list! However, it's set."
      print "Set: "+prompt
      self.skin = prompt
      time.sleep(2)
    user.run()
  def typeprime(self):
    print "Change Primary? What is your primary?"
    prompt = raw_input("Primary> ")
    prompt = prompt.lower()
    sen=0
    check = False
    for char in prime:
      if prompt == prime[sen]:
        check = True
        print "Set: "+prompt
        self.primary = prompt
        break

      else:
        check = False
      sen+=1
    if check == False:
      print "The primary weapon you chose is not in the list! Your primary has been tagged custom."
      self.primary = prompt+" [CUSTOM]"
      print "Set: "+prompt+" [CUSTOM]"
      time.sleep(2)
    user.run()
    
  def typesecond(self):
    print "Change Secondary? What is your Secondary?"
    prompt = raw_input("Secondary> ")
    prompt = prompt.lower()
    sen=0
    check = False
    for char in second:
      if prompt == second[sen]:
        check = True
        print "Set: "+prompt
        self.secondary = prompt
        break
      
      else:
        check = False
      sen+=1
    if check == False:
      print "The secondary weapon you chose is not in the list! Your secondary has been tagged custom."
      self.secondary = prompt+" [CUSTOM]"
      print "Set: "+prompt+" [CUSTOM]"
      time.sleep(2)
    user.run()
  def randomize(self):
    print "Choosing Random Attributes..."
    time.sleep(2)
    print "Set! "
    self.hat = random.choice(hats)
    self.body = random.choice(bodies)
    self.skin = random.choice(skins)
    self.primary = random.choice(prime)
    self.secondary = random.choice(second)
    print
    time.sleep(1)
    user.run()
  def lists(self):
    print "---------HATS---------"
    s = 0
    for each in hats:
      s+=1
      s = str(s)
      print s+". "+each
      s = int(s)
    time.sleep(1)
    print "-------BODIES:--------"
    s = 0
    for each in bodies:
      s+=1
      s = str(s)
      print s+". "+each
      s = int(s)
    time.sleep(1)
    print "----PRIMARY WEAPONS:--"
    s = 0
    for each in prime:
      s+=1
      s = str(s)
      print s+". "+each
      s = int(s)
    time.sleep(1)
    print "--SECONDARY WEAPONS:--"
    s = 0
    for each in second:
      s+=1
      s = str(s)
      print s+". "+each
      s = int(s)
    time.sleep(1)
    print "---------------------------------------------------------------------------------------------------------->"
    print "There is a list for skin tones, but it need not be shown as skin colors are allowed to be custom without"
    print " being tagged. Missing Items will be added in the next update."
    print "<----------------------------------------------------------------------------------------------------------"
    raw_input("Press [enter] to continue to menu:")
    user.run()
    
# RUN FUNCTION
  def run(self):
    number = ["1","2","3","4","5","6","7","8"]
    s = ""
    while s not in number:
      print ""
      print "[1] Change Hat               | Your Hat               : "+self.hat
      print "[2] Change Body              | Your Body              : "+self.body
      print "[3] Change Skin Tone         | Your Skin Tone         : "+self.skin
      print "[4] Change Primary Weapon    | Your Primary           : "+self.primary
      print "[5] Change Secondary Weapon  | Your Secondary         : "+self.secondary
      print "[6] Randomize Inventory ------------------------------------------------->"
      print "[7] View lists of all attributes ---------------------------------------->"
      print "[8] Exit Loop and Complete ---------------------------------------------->"
      s = raw_input(">>> ")
    if s == "1":
      user.typehat()
    elif s == "2":
      user.typebody()
    elif s == '3':
      user.typeskin()
    elif s == '4':
      user.typeprime()
    elif s == '5':
      user.typesecond()
    elif s == '6':
      user.randomize()
    elif s == '7':
      user.lists()
    elif s == '8':
      print "EXITED LOOP! ---- OVER."
    else:
      print ' Error --> InvalidPrompt'
      print ''
    


# BETA EDITION - NO USER CREATED
user = Avatar('panda', 'bloodharvest', 'brown', 'sniper', 'pistol')
print "CONSOLE LOADING"
time.sleep(1)
print ""
print ""
print "Choose Following Options: "
time.sleep(1)
user.run()


    
              
  
    
    
