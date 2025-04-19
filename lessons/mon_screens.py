#quiz file for monitors

#questions is a tuple of one sentence seprated by commas
questions = ("one of TN's advantages are?",#0
            "a disadvantage of TN is?",#1
            "another disadvantage of TN is?",#2
            "what type of screen technology is IPS?",#3
             "what are the 3 technologies of LCD screens?",#4
             "is it true that LCD doesnt need a backlight and is lit by organic light?",#5
             "an advantage of IPS?",#6
             "another advantage of IPS?",#7
             "a disadvantages of IPS are?"#8
             )

#options is a tuple of many tuples within inner tuples are 4 seperated possible answers to be chosen from
options = (
        ("a.dies fast","b.very good viewing angles","c.fast respone times","d.very good color angles"),#0
        ("a.has only one color","b.poor viewing angles","c.too common","d.slow response times"),#1
        ("a.newer technology","b.low color quality","c.its very expensive","d.its very cheap"),#2
        ("a.OLED","b.LED","c.VA","d.LCD"),#3
        ("a.TN,IPS,VA","b.OLED,LED,laser","c.VGA","d.TN,OLED,VA"),#4
        ("a.true","b.false"),#5
        ("a.fast response times","b.is oled technology","c.high color quality","d.very small screen"),#6
        ("a.has only one color","b.high contrast ratio","c.wide viewing angles","d.fast response times"),#7
        ("a.slow response times","b.breaks easily","c.doesnt need backlights","d.wide view angles")#8
        )#tuple of tuples multiple choice

#answers is just a the letter a b c or d to match the index its suppose to answer
answers = ("c",#0
           "b",#1
           "b",#2
           "d",#3
           "a",#4
           "b",#5
           "c",#6
           "c",#7
           "a",#8
           )

