#Random module command
import random

#Card registry
CARD_LIST = {
'Bomb' : {
    "count" : 9,
    "description" : "-1 HP",
    "category" : "Bomb"
},

'NUKE' : {
    "count" : 1,
    "description" : "-2 HP & discard all cards",
    "category" : "Bomb"
},

'Time' : {
    "count" : 1,
    "description" : "-1 HP at the end of your next turn, diffusible with any defensive card",
    "category" : "Bomb"
},

'D20' : {
    "count" : 1,
    "description" : "-1 HP",
    "category" : "Everyone rolls a D20, lowest roll takes -1 HP"
},

'The World' : {
    "count" : 3,
    "description" : "Skips everyone's turn, turns bombs into timed bombs, adds 1 cycle to any existing time bomb before detonation",
    "category" : "Neutral"
},

'Fishing' : {
    "count" : 3,
    "description" : "Draw 2 cards, pick 1 and discard the other",
    "category" : "Neutral"
},

'Skip' : {
    "count" : 2,
    "description" : "Skip anyone, even yourself",
    "category" : "Neutral"
},

'Mango' : {
    "count" : 2,
    "description" : "+1 HP",
    "category" : "Neutral"
},

'Dumpster' : {
    "count" : 3,
    "description" : "Roll a D20, take card from discard pile that matchs roll, if roll exceeds number of discarded cards take bottom, rolling a 20 lets you choose any",
    "category" : "Neutral"
},

'Gremlin' : {
    "count" : 8,
    "description" : "Combine gremlins to create artificial cards, 1 - useless, 2 - fishing, 3 - thief, 4 - shield, 5 - any card",
    "category" : "Neutral"
},

'Buttery' : {
    "count" : 2,
    "description" : "Force anyone to draw a card",
    "category" : "Neutral"
},

'Thief' : {
    "count" : 3,
    "description" : "Blindly steal a card from another player",
    "category" : "Neutral"
},

'Sneak-A-Peak' : {
    "count" : 2,
    "description" : "Reveal a players entire hand to yourself, cost no action",
    "category" : "Neutral"
},

'Advantage' : {
    "count" : 2,
    "description" : "Reroll any D20 encounters, cost no action",
    "category" : "Neutral"
},

'Shield' : {
    "count" : 3,
    "description" : "Protects user from all damage execept cannibal",
    "category" : "Defense"
},

'Reflect' : {
    "count" : 3,
    "description" : "Reflect only bombs, NUKE & Fat bypass this",
    "category" : "Defense"
},

'Nuh-Uh' : {
    "count" : 4,
    "description" : "Deny any non-lethal card, cost no action",
    "category" : "Defense"
},

'Cannibal' : {
    "count" : 2,
    "description" : "Steal +1 HP and deal -1 HP to any player",
    "category" : "Offense"
},

'Radioactive Leech':{
    "count" : 2,
    "description" : "Attach a leech to a player, -1 HP each cycle it stays on, roll a D20 when first attached that cost no action, if higher than 10 remove, use action to remove if not",
    "category" : "Offense"
},

'Fat' : {
    "count" : 3,
    "description" : "Convert any bomb into a grenade, one bomb per fat, if player doesn't use grenade before pulling another bomb, both explode",
    "category" : "Offense"
},

'Oiled' : {
    "count" : 3,
    "description" : "Blindly force a player to discard a card then apply oil which causes any bombs to set fire dealing -1 HP if not extinguished through a denfense card, oil is removed after 1 cycle",
    "category" : "Offense"
},

'Equalizer' : {
    "count" : 1,
    "description" : "Equal eveyone's HP, left over HP goes to user",
    "category" : "Ultimate"
},

'Paladin' : {
    "count" : 1,
    "description" : "Gain +1 HP upon use, roll a D20 for saturation HP, 1-9 +1 SHP, 10-15 +2 SHP, 16-19 +3 SHP, 20 +4 SHP, lose 1 SHP at the end of each cycle",
    "category" : "Ultimate"
},

'Theifs Gambit' : {
    "count" : 1,
    "description" : "User steals a single card from everyone, user rolls a D20 once, then opponents, higher than user : take 1 card blindy, if lower gain Sneak-A-Peak passive",
    "category" : "Ultimate"
}
    }


#Shuffle function 
def shuffle_deck(registry):
    deck = []

    for card_id, data in registry.items():
        deck.extend([card_id] * data["count"])

    random.shuffle(deck)
    
    return deck

randomized = shuffle_deck(CARD_LIST)
print(randomized)

randomized = shuffle_deck(CARD_LIST)
print(randomized)

def deal_damage(damage,hp):
    pass