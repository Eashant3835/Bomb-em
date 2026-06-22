#List of dictionaries
bomb = {
    "count" : 9,
    "id" : "Bomb",
    "description" : "-1 HP",
    "category" : "Bomb"
}

nuke = {
    "count" : 1,
    "id" : "NUKE",
    "description" : "-2 HP & discard all cards",
    "category" : "Bomb"
}

time = {
    "count" : 1,
    "id" : "Time",
    "description" : "-1 HP at the end of your next turn, diffusible with any defensive card",
    "category" : "Bomb"
}

d20 = {
    "count" : 1,
    "id" : "D20",
    "description" : "-1 HP",
    "category" : "Everyone rolls a D20, lowest roll takes -1 HP"
}

the_world = {
    "count" : 3,
    "id" : "The World",
    "description" : "Skips everyone's turn, turns bombs into timed bombs, adds 1 cycle to any existing time bomb before detonation",
    "category" : "Neutral"
}

fishing = {
    "count" : 3,
    "id" : "Fishing",
    "description" : "Draw 2 cards, pick 1 and discard the other",
    "category" : "Neutral"
}

skip = {
    "count" : 2,
    "id" : "Skip",
    "description" : "Skip anyone, even yourself",
    "category" : "Neutral"
}

mango = {
    "count" : 2,
    "id" : "Mango",
    "description" : "+1 HP",
    "category" : "Neutral"
}

dumpster = {
    "count" : 3,
    "id" : "Dumpster",
    "description" : "Roll a D20, take card from discard pile that matchs roll, if roll exceeds number of discarded cards take bottom, rolling a 20 lets you choose any",
    "category" : "Neutral"
}

gremlin = {
    "count" : 8,
    "id" : "Gremlin",
    "description" : "Combine gremlins to create artificial cards, 1 - useless, 2 - fishing, 3 - thief, 4 - shield, 5 - any card",
    "category" : "Neutral"
}

buttery = {
    "count" : 2,
    "id" : "Buttery",
    "description" : "Force anyone to draw a card",
    "category" : "Neutral"
}

thief = {
    "count" : 3,
    "id" : "Thief",
    "description" : "Blindly steal a card from another player",
    "category" : "Neutral"
}

sneak_a_peak = {
    "count" : 2,
    "id" : "Sneak-A-Peak",
    "description" : "Reveal a players entire hand to yourself, cost no action",
    "category" : "Neutral"
}

advantage = {
    "count" : 2,
    "id" : "Advantage",
    "description" : "Reroll any D20 encounters, cost no action",
    "category" : "Neutral"
}

shield = {
    "count" : 3,
    "id" : "Shield",
    "description" : "Protects user from all damage execept cannibal",
    "category" : "Defense"
}

reflect = {
    "count" : 3,
    "id" : "Reflect",
    "description" : "Reflect only bombs, NUKE & Fat bypass this",
    "category" : "Defense"
}

nuh_uh = {
    "count" : 4,
    "id" : "Nuh-Uh",
    "description" : "Deny any non-lethal card, cost no action",
    "category" : "Defense"
}

cannibal = {
    "count" : 2,
    "id" : "Cannibal",
    "description" : "Steal +1 HP and deal -1 HP to any player",
    "category" : "Offense"
}

radioactive_leech = {
    "count" : 2,
    "id" : "Radioactive Leech",
    "description" : "Attach a leech to a player, -1 HP each cycle it stays on, roll a D20 when first attached that cost no action, if higher than 10 remove, use action to remove if not",
    "category" : "Offense"
}

fat = {
    "count" : 3,
    "id" : "Fat",
    "description" : "Convert any bomb into a grenade, one bomb per fat, if player doesn't use grenade before pulling another bomb, both explode",
    "category" : "Offense"
}

oiled = {
    "count" : 3,
    "id" : "Oiled",
    "description" : "Blindly force a player to discard a card then apply oil which causes any bombs to set fire dealing -1 HP if not extinguished through a denfense card, oil is removed after 1 cycle",
    "category" : "Offense"
}

equalizer = {
    "count" : 1,
    "id" : "Equalizer",
    "description" : "Equal eveyone's HP, left over HP goes to user",
    "category" : "Ultimate"
}

paladin = {
    "count" : 1,
    "id" : "Paladin",
    "description" : "Gain +1 HP upon use, roll a D20 for saturation HP, 1-9 +1 SHP, 10-15 +2 SHP, 16-19 +3 SHP, 20 +4 SHP, lose 1 SHP at the end of each cycle",
    "category" : "Ultimate"
}

theifs_gambit = {
    "count" : 1,
    "id" : "Theif's Gambit",
    "description" : "User steals a single card from everyone, user rolls a D20 once, then opponents, higher than user : take 1 card blindy, if lower gain Sneak-A-Peak passive",
    "category" : "Ultimate"
}

#List of cards
deck = [bomb, nuke, time, d20, the_world, fishing, skip, mango, dumpster, gremlin, buttery, thief, sneak_a_peak, advantage, shield, reflect, nuh_uh, cannibal, radioactive_leech, fat, oiled, equalizer, paladin, theifs_gambit]