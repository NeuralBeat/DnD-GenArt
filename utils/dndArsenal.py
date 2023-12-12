import streamlit as st
import os

# Step 1: Define Equipment Categories and Items
equipment = {
    "MELEE WEAPONS": ["DAGGER", "SHORT SWORD", "RAPIER", "SICKLE", "SCIMITAR", "LONG SWORD", "HANDAXE", "BATTLE AXE", "GREATSWORD", "GREATAXE", "GREATCLUB", "CLUB", "QUARTERSTAFF", "LIGHT HAMMER", "MAUL", "MORNINGSTAR", "MACE", "FLAIL", "GLAIVE", "HALBERD", "PIKE", "SPEAR", "TRIDENT", "WAR PICK", "WARHAMMER", "WHIP", "YKLWA"],
    "RANGED WEAPONS": ["SHORT BOW", "LONG BOW", "HAND CROSSBOW", "LIGHT CROSSBOW", "HEAVY CROSSBOW", "SLING", "DART", "THROWING KNIFE", "BLOWGUN", "BOOMERANG", "JAVELIN", "REVOLVER"],
    "ARMOR": ["BREASTPLATE", "CHAIN MAIL", "CHAIN SHIRT", "HIDE ARMOR", "LEATHER ARMOR", "PADDED ARMOR", "RING MAIL", "SCALE MAIL", "SPLINT MAIL", "STUDDED LEATHER ARMOR", "SCHOLARS ROBE", "MAGE ROBE"],
    "MUNITION" : ["ARROWS", "BLOWGUN NEEDLES", "CROSSBOW BOLTS", "SLING BULLETS", "BULLETS"],
    "POTIONS": ["ANTITOXIN","POTION OF HEALING", "POISON FLASK", "ALCHEMIST'S FIRE", "VIAL OF ACID", "HOLY WATER FLASK"],
    "UTILITY": ["BACKPACK", "BEDROLL", "BLASTING POWDER", "BOOK", "BOOTS", "BUCKET", "CALTROPS","CANDLE", "CHAIN (10 FEET)", "CHALK", "CHEST", "COMPONENT POUCH", "CROWBAR", "DYNAMITE", "RATIONS (1 DAY)", "GRAPPLING HOOK", "HUNTING TRAP", "LAMP", "LOCK", "MIRROR", "OIL FLASK", "PARCHMENT", "MINER'S PICK", "POUCH", "QUIVER", "ROPE (50 FEET)", "SACK", "SEALING WAX", "SHOVEL", "SOAP", "SPELLBOOK", "TINDERBOX", "TORCH", "WATERSKIN", "WHETSTONE"],
    "FOCUS": ["AMULET", "ARCANE FOCUS", "CRYSTAL", "HOLY SYMBOL", "ORB", "RELIQUARY", "ROD", "STAFF", "WAND"],
    "INSTRUMENT": ["BAGPIPES", "FLUTE", "HAND DRUM", "HORN", "LONGHORN", "LUTE", "LYRE", "PAN FLUTE", "TANTAN", "THELAR", "VIOL", "WARGONG", "YARTLING", "ZULKOON"],
    "TOOLS": ["ALCHEMIST'S SUPPLIES", "BURGLAR'S PACK", "CALLIGRAPHER'S SUPPLIES", "CARPENTER'S TOOLS", "CARTOGRAPHER'S TOOLS", "CLIMBER'S KIT", "COBBLER'S TOOLS", "COOK'S UTENSILS", "DIPLOMAT'S PACK", "DISGUISE KIT", "DUNGEONEER'S PACK", "ENTERTAINER'S PACK", "EXPLORER'S PACK", "FORGERY KIT", "GLASSBLOWER'S TOOLS", "HERBALISM KIT", "JEWERLER'S TOOLS", "LEATHERWORKER'S TOOLS", "MASON'S TOOLS", "MONSTERHUNTER'S PACK", "NAVIGATOR'S TOOLS", "PAINTER'S SUPPLIES", "POISONER'S KIT", "POTTER'S TOOLS", "PRIEST'S PACK", "SCHOLAR'S PACK", "TINKER'S TOOLS", "WOODCARVER'S TOOL"]
    }

# Function to handle equipment selection
def handle_selection(category, items):
    selected_item = st.selectbox(f"SELECT {category}", [None] + items, key=f'select_{category}')
    if selected_item:
        st.session_state[f'selected_{category}'] = selected_item


# User Interface for Selections
def select_arsenal():
    st.title("SELECT YOUR ARSENAL")

    # Initialize or display current selections
    for category, items in equipment.items():
        if f'selected_{category}' not in st.session_state:
            st.session_state[f'selected_{category}'] = None
        handle_selection(category, items)

    if st.button("CONFIRM SELECTION"):
        show_selected_arsenal()
 

# Display Selected Equipment
def show_selected_arsenal():
    st.subheader("Your Selected Arsenal")
    for category in equipment.keys():
        if st.session_state[f'selected_{category}']:
            st.write(f"{category}: {st.session_state[f'selected_{category}']}")
