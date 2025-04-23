questions = ("is it true that you can mix print drivers?",#0
             "what language do printers use to communicate with drivers?",#1
             "how does printer share work in windows?",#2
             "a printer that prints on both sides of the paper without flipping the paper is called?",#3
             "an example of print server is?",#4
             "which of these is an example of printer security?",#5 
             "what is badging?",#6
             "which printer combines paper,high voltage,charged ions,powdered ink and heat for its printing process?",#7
             "what is the job of the image drum?",#8
             "in the laser printer process what is in charge of bonding toner to paper permanently?",#9
             "the pick up rollers in a laser printer is in charge of what?",#10
             "whats the laser printer process?",#11
             "adding negatively charged toner to the drum is what step of the laser printer process?",#12
             "what is the last step of the laser printer?",#13
             "which of these would you find in the laser maintanence kit?",#14
             "whats the first thing you should do before replacing laser printer cartridge?",#15
             "what cleaning solution is best to clean laser printer rollers?",#16
             "whats the step for writing image with a laser?",#17
             "what does pcl stand for?"#18
             )




options = (
        ("a.true","b.false"),#0
        ("a.post script","b.PCL","c.adobe","d.either PCL or postcript"),#1
        ("a.use printer software to connect everyone","b.connects directly to a printer","c.connects printer to a pc on network, everyone connects  and print from that pc.","d.connects to cloud."),#2
        ("a.duplex","b.multiplexing","c.multimode","d.dual booting"),#3
        ("a.no 3rd computer print directly to printer","b.prints to an SDN device","c.print jobs are sent to one pc to print","d.None of the above"),#4
        ("a.passcode","b.badging","c.setting rights & permissions","d.all of the above"),#5
        ("a.allows you to check audit logs","b.a type of biometric passcode","c.print job doesnt print until you use your employee badge","d.None of the above"),#6
        ("a.laster printer","b.dot matrix printer(impact printer)","c.inkjet printer","d.thermal printer"),#7
        ("a.recieving image drawn by the laser","b.bonding toner to the paper","c.to pick up# paper placed into the printer","d.holding the ink for the printer"),#8
        ("a.duplexing assembly","b.transfer belt & rollers","c.the fuser assembly","d.the drum"),#9
        ("a.transer all the ink from cartridges to the single belt","b.helps the printer print on both sides","c.it cleans the printer when print job is done","d.picks the up the paper"),#10
        ("a.processing,charging,exposing,developing,transferring,fusing,cleaning","b.processing,charging,developing,fusing,cleaning","c.exposing,developing,processing,charging","d.None of the above"),#11
        ("a.processing","b.developing","c.fusing","d.transferring"),#12
        ("a.cleaning","b.exposing","c.processing","d.fusing"),#13
        ("a.printer paper","b.replacement feed rollers","c.both a and b","d.ink"),#14
        ("a.disconnect it from the network","b.find the lever to take out cartridge","c.power off the printer","d.pull the plug"),#15
        ("a.luke warm water","b.hot water","c.peroxide","d.IPA(isopropyl alcohol)"),#16
        ("a.processing","b.charging","c.developing","d.exposing"),#17
        ("a.printer connection language","b.printer common language","c.postscript language","d.postgres common language")#18
        )



answers = ("b",#0
           "d",#1
           "c",#2
           "a",#3
           "a",#4
           "d",#5
           "c",#6
           "a",#7
           "a",#8
           "c",#9
           "d",#10
           "a",#11
           "b",#12
           "a",#13
           "c",#14
           "c",#15
           "d",#16
           "d",#17
           "b"#18
           )
