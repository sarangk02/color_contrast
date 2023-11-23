import re
import streamlit as st
def inv(color):
    s = list(color.strip())[:6]
    dic = {
        'a':10,
        'b':11,
        'c':12,
        'd':13,
        'e':14,
        'f':15
    }
    inv_dic = {v: k for k, v in dic.items()}
    for i in range(6):
        if s[i] in dic:
            s[i] = dic[s[i]]
        else:
            s[i] = int(s[i])
    ans = [abs(15-i) for i in s]
    for i in range(6):
        if ans[i] > 9:
            ans[i] = inv_dic[ans[i]]
        else:
            ans[i] = str(ans[i])
    ans = ''.join(ans)
    return ans

pattern = r'^[0-9A-Fa-f]{6}$'
color1 = st.text_input("Enter hex code for color")
valid = re.match(pattern, color1)

if valid:
    # color1 = color or '000000'
    color2 = inv(color1)

    styled_box1 = f'<div style="background-color:{"#"+color1}; color:{"#"+color2} ; padding:10px; border-radius:5px; height:100px; width: 100%"; display: flex; justify-content: center; align-items: center;>Background Color {"#"+color1}</div>'
    styled_box2 = f'<div style="background-color:{"#"+color2}; color:{"#"+color1} ; padding:10px; border-radius:5px; height:100px; width: 100%"; display: flex; justify-content: center; align-items: center;>Background Color {"#"+color2}</div>'
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(styled_box1, unsafe_allow_html=True)
    with col2:
        st.write(styled_box2, unsafe_allow_html=True)
else:
    st.write("""<div style='background-color:#F2DEDE; padding:10px; border-radius:5px;'>
                <h2 style='color:#B94A48;'>Enter proper hex code nigglet</h2>
            </div>""", unsafe_allow_html=True)