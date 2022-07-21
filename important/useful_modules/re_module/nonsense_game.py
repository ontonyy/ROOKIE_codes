import re

text = """Жирафы любят таскать различные __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__
целый день напролет. Жирафы
также славябся тем, что поедают
прекрасные __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__, но
после этого у них часто
болит __ЧАСТЬ_ТЕЛА__. Если же
жирафы находят __ЧИСЛО__
__СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__, у
них моментально отваливается __ЧАСТЬ ТЕЛА__.
"""

def mad_libs(mls):
    hints = re.findall("__.*?__", mls)
    if hints is None:
        for word in hints:
            new = input("Write {}".format(word))
            mls = mls.replace(word, new, 1)
        print("\n")
        mls = mls.replace("\n", "")
        print(mls)
    else: 
        print("Typing error!")
        
if __name__ == '__main__':
    mad_libs(text)


