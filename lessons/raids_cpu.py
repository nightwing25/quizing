
#when i add a new question to questions and tuple of 4 options in options
#then and a letter from a to d for the index you want correct


questions = (
        "what light source does multifiber use",#0
        "whats the max distance for multifiber?",#1
        "what is the max distance for single mode fiber?",#2
        "what light source does single mode fiber use?",#3
        "what type of memory is RAM?",#4
        "minimum hdd requirements for raid 1?",#5
        "minimum hdd requirements for raid 5?",#6
        "minmum hdd requirements for raid 0?",#7
        "what company's form factor is PGA for?",#8
        "what company's form factor is LGA for?"#9
        )
#("a.","b.","c.","d.")
options = (("a.led","b.laser","c.oled","d.flourescent"),#0
           ("a.1km","b.2km","c.100m","d.100km"),#1
           ("a.100m","b.20km","c.3meters","d.100km"),#2
           ("a.oled","b.led","c.laser","d.crystals"),#3
           ("a.volatile","b.non-volatile","c.ssd","d.hdd"),#4 
           ("a.1 hard drive","b.4 hard drives","c.2 hard drives","d.3 hard drives"),#5
           ("a.2 hard drives","b.3 hard drives","c.0 hard drives","d.4 hard drives"),#6
           ("a.2 hard drives","b.1 hard drives","c.3 hard drives","d.1 m.2 ssd"),#7
           ("a.intel","b.AMD","c.nvidia","d.apple"),#8
           ("a.microsoft","b.nvidia","c.AMD","d.intel")#9
           )

##for correct answers
answers = ("a",#0
           "b",#1
           "d",#2
           "c",#3
           "a",#4
           "c",#5
           "b",#6
           "a",#7
           "b",#8
           "d"#9
           )
#for correct answers
