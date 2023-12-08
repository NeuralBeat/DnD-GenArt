from utils.styleCSS import *
from CharacterGenerator import *

inject_css()

main_img = "images/generic/DnDGargoyle.webp"
center_img = "images/generic/DnDMask.webp"
left_img = "images/generic/DnDCompass.webp"
right_img = "images/generic/DnDRoster.webp"

st.header("DUNGEONS & DRAGONS COMPANION")

left_col, center_col, right_col = st.columns([1,1,1])

with left_col:
    st.image(left_img, width=250)
    if st.button("CONTINUE JOURNEY"):
        pass
with center_col:
    st.image(center_img, width=250)
    if st.button("CREATE NEW CHARACTER"):
        CharacterGenerator()

with right_col:
    st.image(right_img, width=250)
    if st.button("ROSTER"):
        pass

