import streamlit as st
import os

# Step 1: Define Equipment Categories and Items
melee_weapons = {
        "DAGGER": {"DAMAGE": "1d4", "TYPE": "Piercing", "FINESSE": True}, 
        "SHORT SWORD": {"DAMAGE": "1d6", "TYPE": "Piercing", "FINESSE": True},
        "RAPIER": {"DAMAGE": "1d8", "TYPE": "Piercing", "FINESSE": True},
        "SICKLE": {"DAMAGE": "1d4", "TYPE": "Slashing", "FINESSE": False},
        "SCIMITAR": {"DAMAGE": "1d6", "TYPE": "Slashing", "FINESSE": True},
        "LONG SWORD": {"DAMAGE": "1d8", "TYPE": "Slashing", "FINESSE": False}, 
        "HANDAXE": {"DAMAGE": "1d6", "TYPE": "Slashing", "FINESSE": False},
        "BATTLE AXE": {"DAMAGE": "1d8", "TYPE": "Slashing", "FINESSE": False},
        "GREATSWORD": {"DAMAGE": "2d6", "TYPE": "Slashing", "FINESSE": False},
        "GREATAXE": {"DAMAGE": "1d12", "TYPE": "Slashing", "FINESSE": False},
        "GREATCLUB": {"DAMAGE": "1d8", "TYPE": "Bludgeoning", "FINESSE": False},
        "CLUB": {"DAMAGE": "1d4", "TYPE": "Bludgeoning", "FINESSE": False},
        "QUARTERSTAFF": {"DAMAGE": "1d6", "TYPE": "Bludgeoning", "FINESSE": False},
        "LIGHT HAMMER": {"DAMAGE": "1d4", "TYPE": "Bludgeoning", "FINESSE": False},
        "MAUL": {"DAMAGE": "2d6", "TYPE": "Bludgeoning", "FINESSE": False},
        "MORNINGSTAR": {"DAMAGE": "1d8", "TYPE": "Piercing", "FINESSE": False},
        "MACE": {"DAMAGE": "1d6", "TYPE": "Bludgeoning", "FINESSE": False},
        "FLAIL": {"DAMAGE": "1d8", "TYPE": "Bludgeoning", "FINESSE": False},
        "GLAIVE": {"DAMAGE": "1d10", "TYPE": "Slashing", "FINESSE": False},
        "HALBERD": {"DAMAGE": "1d10", "TYPE": "Slashing", "FINESSE": False},
        "PIKE": {"DAMAGE": "1d10", "TYPE": "Piercing", "FINESSE": False},
        "SPEAR": {"DAMAGE": "1d6", "TYPE": "Piercing", "FINESSE": False},
        "TRIDENT": {"DAMAGE": "1d6", "TYPE": "Piercing", "FINESSE": False},
        "WAR PICK": {"DAMAGE": "1d8", "TYPE": "Piercing", "FINESSE": False},
        "WARHAMMER": {"DAMAGE": "1d8", "TYPE": "Bludgeoning", "FINESSE": False},
        "WHIP": {"DAMAGE": "1d4", "TYPE": "Slashing", "FINESSE": True},
        "YKLWA": {"DAMAGE": "1d8", "TYPE": "Piercing", "FINESSE": False}
    }

ranged_weapons =  {
        "SHORT BOW": {"DAMAGE": "1d6", "TYPE": "Piercing", "FINESSE": False},
        "LONG BOW": {"DAMAGE": "1d8", "TYPE": "Piercing", "FINESSE": False},
        "HAND CROSSBOW": {"DAMAGE": "1d6", "TYPE": "Piercing", "FINESSE": True},
        "LIGHT CROSSBOW": {"DAMAGE": "1d8", "TYPE": "Piercing", "FINESSE": False},
        "HEAVY CROSSBOW": {"DAMAGE": "1d10", "TYPE": "Piercing", "FINESSE": False},
        "SLING": {"DAMAGE": "1d4", "TYPE": "Bludgeoning", "FINESSE": False},
        "DART": {"DAMAGE": "1d4", "TYPE": "Piercing", "FINESSE": True},
        "THROWING KNIFE": {"DAMAGE": "1d4", "TYPE": "Piercing", "FINESSE": True},
        "BLOWGUN": {"DAMAGE": "1", "TYPE": "Piercing", "FINESSE": False},
        "BOOMERANG": {"DAMAGE": "1d4", "TYPE": "Bludgeoning", "FINESSE": False},
        "JAVELIN": {"DAMAGE": "1d6", "TYPE": "Piercing", "FINESSE": False},
        "REVOLVER": {"DAMAGE": "2d8", "TYPE": "Piercing", "FINESSE": False}
    }

armor = {
        "BREASTPLATE": {"ARMOR CLASS": 14, "HEAVY": False, "STEALTH DISADVANTAGE": False},
        "CHAIN MAIL": {"ARMOR CLASS": 16, "HEAVY": True, "STEALTH DISADVANTAGE": True},
        "CHAIN SHIRT": {"ARMOR CLASS": 13, "HEAVY": False, "STEALTH DISADVANTAGE": False},
        "HIDE ARMOR": {"ARMOR CLASS": 12, "HEAVY": False, "STEALTH DISADVANTAGE": False},
        "LEATHER ARMOR": {"ARMOR CLASS": 11, "HEAVY": False, "STEALTH DISADVANTAGE": False},
        "PADDED ARMOR": {"ARMOR CLASS": 11, "HEAVY": True, "STEALTH DISADVANTAGE": True},
        "RING MAIL": {"ARMOR CLASS": 14, "HEAVY": True, "STEALTH DISADVANTAGE": True},
        "SCALE MAIL": {"ARMOR CLASS": 14, "HEAVY": True, "STEALTH DISADVANTAGE": True},
        "SPLINT MAIL": {"ARMOR CLASS": 17, "HEAVY": True, "STEALTH DISADVANTAGE": True},
        "STUDDED LEATHER ARMOR": {"ARMOR CLASS": 12, "HEAVY": False, "STEALTH DISADVANTAGE": False},
        "SCHOLARS ROBE": {"ARMOR CLASS": 10, "HEAVY": False, "STEALTH DISADVANTAGE": False},
        "MAGE ROBE": {"ARMOR CLASS": 10, "HEAVY": False, "STEALTH DISADVANTAGE": False}
    }
shields = {
        "WOODEN SHIELD":{"ARMOR CLASS": +2},
        "METAL SHIELD": {"ARMOR CLASS": +2}
    }

other_equipment = {
    "MUNITION" : ["ARROWS", "BLOWGUN NEEDLES", "CROSSBOW BOLTS", "SLING BULLETS", "BULLETS"],
    "POTIONS": ["ANTITOXIN","POTION OF HEALING", "POISON FLASK", "ALCHEMIST'S FIRE", "VIAL OF ACID", "HOLY WATER FLASK"],
    "UTILITY": ["BACKPACK", "BEDROLL", "BLASTING POWDER", "BOOK", "BOOTS", "BUCKET", "CALTROPS","CANDLE", "CHAIN (10 FEET)", "CHALK", "CHEST", "COMPONENT POUCH", "CROWBAR", "DYNAMITE", "RATIONS (1 DAY)", "GRAPPLING HOOK", "HUNTING TRAP", "LAMP", "LOCK", "MIRROR", "OIL FLASK", "PARCHMENT", "MINER'S PICK", "POUCH", "QUIVER", "ROPE (50 FEET)", "SACK", "SEALING WAX", "SHOVEL", "SOAP", "SPELLBOOK", "TINDERBOX", "TORCH", "WATERSKIN", "WHETSTONE"],
    "FOCUS": ["AMULET", "ARCANE FOCUS", "CRYSTAL", "HOLY SYMBOL", "ORB", "RELIQUARY", "ROD", "STAFF", "WAND"],
    "INSTRUMENT": ["BAGPIPES", "FLUTE", "HAND DRUM", "HORN", "LONGHORN", "LUTE", "LYRE", "PAN FLUTE", "TANTAN", "THELAR", "VIOL", "WARGONG", "YARTLING", "ZULKOON"],
    "TOOLS": ["ALCHEMIST'S SUPPLIES", "BURGLAR'S PACK", "CALLIGRAPHER'S SUPPLIES", "CARPENTER'S TOOLS", "CARTOGRAPHER'S TOOLS", "CLIMBER'S KIT", "COBBLER'S TOOLS", "COOK'S UTENSILS", "DIPLOMAT'S PACK", "DISGUISE KIT", "DUNGEONEER'S PACK", "ENTERTAINER'S PACK", "EXPLORER'S PACK", "FORGERY KIT", "GLASSBLOWER'S TOOLS", "HERBALISM KIT", "JEWERLER'S TOOLS", "LEATHERWORKER'S TOOLS", "MASON'S TOOLS", "MONSTERHUNTER'S PACK", "NAVIGATOR'S TOOLS", "PAINTER'S SUPPLIES", "POISONER'S KIT", "POTTER'S TOOLS", "PRIEST'S PACK", "SCHOLAR'S PACK", "TINKER'S TOOLS", "WOODCARVER'S TOOL"]
    }

# Combine all equipment into a single dictionary
equipment = {"MELEE WEAPONS": melee_weapons, "RANGED WEAPONS": ranged_weapons, "ARMOR": armor, "SHIELDS": shields}
equipment.update(other_equipment)

# Function to handle equipment selection
def handle_selection(category, items):
    selected_item = st.selectbox(f"SELECT {category}", [None] + items, key=f'select_{category}')
    if selected_item:
        st.session_state[f'selected_{category}'] = selected_item


# User Interface for Selections
def select_arsenal():
    # Render a selectbox for each equipment category
    for category, items in equipment.items():
        selected_item_key = f'selected_{category}'
        item_options = list(items.keys()) if isinstance(items, dict) else items

        selected_item = st.selectbox(f"SELECT {category}", [None] + item_options, key=selected_item_key)

        # Update the session state
        if selected_item and selected_item in item_options:
            st.session_state[selected_item_key] = selected_item

            # Display additional attributes if applicable
            if category == "MELEE WEAPONS" and selected_item in melee_weapons:
                for attribute, value in melee_weapons[selected_item].items():
                    st.write(f"{attribute}: {value}")
            elif category == "RANGED WEAPONS" and selected_item in ranged_weapons:
                for attribute, value in ranged_weapons[selected_item].items():
                    st.write(f"{attribute}: {value}")
            elif category == "ARMOR" and selected_item in armor:
                for attribute, value in armor[selected_item].items():
                    st.write(f"{attribute}: {value}")
            elif category == "SHIELDS" and selected_item in shields:
                for attribute, value in shields[selected_item].items():
                    st.write(f"{attribute}: {value}")
            else:
                for attribute, value in items[selected_item].items():
                    st.write(f"{attribute}: {value}")
            

    # Button to confirm selections
    if st.button("CONFIRM SELECTIONS"):
        show_selected_arsenal()
 

# Display Selected Equipment
def show_selected_arsenal():
    
    st.subheader("YOUR SELECTED ARSENAL")
    for category in equipment.keys():
        selected_item_key = f'selected_{category}'
        if selected_item_key in st.session_state and st.session_state[selected_item_key]:
            st.write(f"{category}: {st.session_state[selected_item_key]}")


