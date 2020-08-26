from django.contrib import admin
from .models import Account, Character, Inventoryitem
from .models import Account
# Register your models here.
#admin.site.register(Character)
#admin.site.register(Inventoryitem)
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fieldsets=(
            ('Required Information',{
                'description':'These fields are required for each event.',
                'fields':('name','password','birthday','email')
                }
            ),
            ('Optional Information',{
                'classes':('collapse',),
                'fields':('pin','pic','loggedin','lastlogin','createdat','banned','banreason','macs','nxcredit',
'maplepoint','nxprepaid','characterslots','gender','tempban','greason','tos','sitelogged','webadmin','nick',
'mute','ip','rewardpoints','votepoints','hwid','language',)
                }
            )
    )
    list_display=('id','name','lastlogin','nxcredit','createdat',)
    ordering=('-lastlogin','-createdat')
    list_filter=()
    search_fields=('name',)

#admin.site.register(Account, AccountAdmin)
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    fieldsets=(
        (None,{
            'fields':(
                'name',
                'gm',
                'rank',
                'jobrank',
                'reborns',
                'datastring',
                'createdate',
                'lastlogouttime',
                ),
            }
        ),
        ('stat',{
            'fields':(
                'job',
                'level',
                'str',
                'dex',
                'int',
                'luk',
                'maxhp',
                'maxmp',
                'ap',
                'fame',
                )
            }
        ),
        ('inventory',{
            'fields':(
                'equipslots',
                'useslots',
                'etcslots',
                )
            }
        ),
    )
    list_display=('accountid','name','level','rank','job','jobrank',)
    ordering=('accountid','rank')
    list_filter=('accountid','gm','job',)
    search_fields=('name',)

@admin.register(Inventoryitem)
class IventoryitemAdmin(admin.ModelAdmin):
    fieldsets=()
    list_display=('inventoryitemid','itemid','quantity','type','characterid','accountid',)
    ordering=('inventoryitemid',)
    list_filter=('characterid','accountid',)
    search_fields=('itemid',)

