from django.db import models

class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=13)
    password = models.CharField(max_length=128)
    pin = models.CharField(max_length=10,blank=True, null=True)
    pic = models.CharField(max_length=26,blank=True, null=True)
    loggedin = models.IntegerField()
    lastlogin = models.DateTimeField(blank=True, null=True)
    createdat = models.DateTimeField()
    birthday = models.DateField()
    banned = models.IntegerField()
    banreason = models.TextField(blank=True, null=True)
    macs = models.TextField(blank=True, null=True)
    nxcredit = models.IntegerField(db_column='nxCredit', blank=True, null=True)  # Field name made lowercase.
    maplepoint = models.IntegerField(db_column='maplePoint', blank=True, null=True)  # Field name made lowercase.
    nxprepaid = models.IntegerField(db_column='nxPrepaid', blank=True, null=True)  # Field name made lowercase.
    characterslots = models.IntegerField()
    gender = models.IntegerField()
    tempban = models.DateTimeField()
    greason = models.IntegerField()
    tos = models.IntegerField()
    sitelogged = models.TextField(blank=True, null=True)
    webadmin = models.IntegerField(blank=True, null=True)
    nick = models.CharField(max_length=20, blank=True, null=True)
    mute = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=45, blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    rewardpoints = models.IntegerField()
    votepoints = models.IntegerField()
    hwid = models.CharField(max_length=12)
    language = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts'
        #app_label = 'ssusers'

    def __str__(self):
        return self.name

class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    accountid = models.IntegerField()
    world = models.IntegerField()
    name = models.CharField(max_length=13)
    level = models.IntegerField()
    exp = models.IntegerField()
    gachaexp = models.IntegerField()
    str = models.IntegerField()
    dex = models.IntegerField()
    luk = models.IntegerField()
    int = models.IntegerField()
    hp = models.IntegerField()
    mp = models.IntegerField()
    maxhp = models.IntegerField()
    maxmp = models.IntegerField()
    meso = models.IntegerField()
    hpmpused = models.PositiveIntegerField(db_column='hpMpUsed')  # Field name made lowercase.
    job = models.IntegerField()
    skincolor = models.IntegerField()
    gender = models.IntegerField()
    fame = models.IntegerField()
    fquest = models.IntegerField()
    hair = models.IntegerField()
    face = models.IntegerField()
    ap = models.IntegerField()
    sp = models.CharField(max_length=128)
    map = models.IntegerField()
    spawnpoint = models.IntegerField()
    gm = models.IntegerField()
    party = models.IntegerField()
    buddycapacity = models.IntegerField(db_column='buddyCapacity')  # Field name made lowercase.
    createdate = models.DateTimeField()
    rank = models.PositiveIntegerField()
    rankmove = models.IntegerField(db_column='rankMove')  # Field name made lowercase.
    jobrank = models.PositiveIntegerField(db_column='jobRank')  # Field name made lowercase.
    jobrankmove = models.IntegerField(db_column='jobRankMove')  # Field name made lowercase.
    guildid = models.PositiveIntegerField()
    guildrank = models.PositiveIntegerField()
    messengerid = models.PositiveIntegerField()
    messengerposition = models.PositiveIntegerField()
    mountlevel = models.IntegerField()
    mountexp = models.IntegerField()
    mounttiredness = models.IntegerField()
    omokwins = models.IntegerField()
    omoklosses = models.IntegerField()
    omokties = models.IntegerField()
    matchcardwins = models.IntegerField()
    matchcardlosses = models.IntegerField()
    matchcardties = models.IntegerField()
    merchantmesos = models.IntegerField(db_column='MerchantMesos', blank=True, null=True)  # Field name made lowercase.
    hasmerchant = models.IntegerField(db_column='HasMerchant', blank=True, null=True)  # Field name made lowercase.
    equipslots = models.IntegerField()
    useslots = models.IntegerField()
    setupslots = models.IntegerField()
    etcslots = models.IntegerField()
    familyid = models.IntegerField(db_column='familyId')  # Field name made lowercase.
    monsterbookcover = models.IntegerField()
    alliancerank = models.IntegerField(db_column='allianceRank')  # Field name made lowercase.
    vanquisherstage = models.PositiveIntegerField(db_column='vanquisherStage')  # Field name made lowercase.
    ariantpoints = models.PositiveIntegerField(db_column='ariantPoints')  # Field name made lowercase.
    dojopoints = models.PositiveIntegerField(db_column='dojoPoints')  # Field name made lowercase.
    lastdojostage = models.PositiveIntegerField(db_column='lastDojoStage')  # Field name made lowercase.
    finisheddojotutorial = models.PositiveIntegerField(db_column='finishedDojoTutorial')  # Field name made lowercase.
    vanquisherkills = models.PositiveIntegerField(db_column='vanquisherKills')  # Field name made lowercase.
    summonvalue = models.PositiveIntegerField(db_column='summonValue')  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='partnerId')  # Field name made lowercase.
    marriageitemid = models.IntegerField(db_column='marriageItemId')  # Field name made lowercase.
    reborns = models.IntegerField()
    pqpoints = models.IntegerField(db_column='PQPoints')  # Field name made lowercase.
    datastring = models.CharField(db_column='dataString', max_length=64)  # Field name made lowercase.
    lastlogouttime = models.DateTimeField(db_column='lastLogoutTime')  # Field name made lowercase.
    lastexpgaintime = models.DateTimeField(db_column='lastExpGainTime')  # Field name made lowercase.
    partysearch = models.IntegerField(db_column='partySearch')  # Field name made lowercase.
    jailexpire = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'characters'

    def __str__(self):
        return self.name

class Inventoryitem(models.Model):
    inventoryitemid = models.IntegerField(primary_key=True)
    type = models.PositiveIntegerField()
    characterid = models.IntegerField(blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField()
    inventorytype = models.IntegerField()
    position = models.IntegerField()
    quantity = models.IntegerField()
    owner = models.TextField()
    petid = models.IntegerField()
    flag = models.IntegerField()
    expiration = models.BigIntegerField()
    giftfrom = models.CharField(db_column='giftFrom', max_length=26)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventoryitems'

    def __str__(self):
        return str(self.inventoryitemid)
