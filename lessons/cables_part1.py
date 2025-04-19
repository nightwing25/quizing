questions = (
        "DVI was design to replace what cable?",#0
        "what signals does DVI carry?",#1
        "what cable is HDMI backwards capatible with?",#2
        "HDMI carries what signals?",#3
        "im trying to find a cable amongst a bunch of other cables what device can i use to locate this specific cable?",#4
        "whats the purpose of the tone generator?",#5
        "to terminate cables on my patch panel in my closet what tool do i use?",#6
        "the final step of making a cable such as RJ-45 what tool is used?",#7
        "for removing the sheath from the wire what tool should i use?",#8
        "for testing cross talk or signal loss in a wire that i just made, what tool can i use?",#9
        "i want to use a network tool to test my physical port but i dont know which one to use?",#10
        "what tool do i use to intercept my newtwork traffic and send a copy to a packet capture device?",#11
        "which device were DB-9 connectors used for?",#12
        "on DB-9 connectors rs-232 means what?",#13
        "what does 8 position, 8 conductor(8p8c) refer to?",#14
        "what does 6 position, 6 conductor(6p6c) refer to",#15
        "this is similar to a docking station does not commonly have an expansion card, usually connects with USB...",#16
        "white-green,green,white-orange,blue,white-blue,orange,white-brown,brown is from what T568 termination standard?",#17
        "white-orange,orange,white-green,blue,white-blue,green,white-brown,brown is from what T658 termination standard?",#18
        "what of these cables are most likely used in digital cable,TVSatellite,TVBroadband and internetHDTV?",#19
        "what is cat 5 max supported distance?",#20
        "what is cat5e max supported distance?",#21
        "what ethernet standard is cat5 ",#22
        "whats the max supported distance for cat6A?",#23
        "what is ethernet satndard & max supported distance for cat6?"#24
        )
options = (
           ("a.VGA","b.HDMI","c.DisplayPort","d.thunderbolt"),#0
           ( "a.digital only","b.audio only","c.digital & audio","None"),#1
           ("a.mini-DVI","b.DVI-I","c.VGA","d.DVI-D"),#2
           ("a.digital video & cable","b.audio & telephone signals","c.video & audio","d.it doesnt carry signals"),#3
           ("a.loop back plug","b.punchdown tool","c.toner probe","d.cable tester"),#4
           ("a.puts a tone on a wire so the probe can follow a wire","b.makes a sound when there's no connection","c.connects rj-45 connectors to the patch panel","d.None of the above"),#5
           ("a.electrician's scissors","b.punch down tool","c.crimpers","d.wire strippers"),#6
           ("a.loop back plug","b.punchdown tool","c.cable tester","d.crimpers"),#7
           ("a.toner probe","b.punchdown tool","c.crimpers","d.wire stripper"),#8
           ("a.cable tester","b.wireless NIC","c.adapter card","d.loop back plug"),#9
           ("a.electrician's scissors","b.crimpers","c.loop back plug","d.cable tester"),#10
           ("a.taps & port mirrors","b.wifi analyzer","c.nmap","d.ping"),#11
           ("a.modems","b.networking","c.mice & pirnters","d.all of the above"),#12
           ("a.refer style 232","b.recon standard 232","c.recommended standard 232","d.recomend style 232"),#13
           ("a.molex connector","b.RJ-45 connector","c.RJ-11 connector","d.F-connector"),#14
           ("a.RJ-11","b.RJ-45","c.F-connector","d.usb-c"),#15
           ("a.port replicator","b.usb hub","c.usb converters","d.None of the above"),#16
           ("a.RJ-45","b.loop back plug","c.T568B","d.T568A"),#17
           ("a.T658B","b.loop back plug","c.RJ-45","d.T568A"),#18
           ("a.USB-C","b.RJ-11","c.RG-6","d.RJ-45"),#19
           ("a.10 meters","b.44 meters","c.100 meters","d.55 meters"),#20
           ("a.3 meters","b.50 meters","c.10 meters","d.100 meters"),#21
           ("a.1000 BASE-T","b.100 BASE-T","c.1 BASE-T","d.10 BASE-T"),#22
           ("a.20 meters","b.100 meters","c.50 meters","d.55 meters"),#23
           ("a.10BASE-T, 55 meters","b.1000BASE-T 100 meters","c.10BASE-T,un-shielded:55 meters,shielded:100 meters","d.1000BASE-T,un-shielded:100 meters,shielded:55 meters")#24
           )

answers = (
           "a",#0
           "c",#1
           "d",#2
           "c",#3
           "c",#4
           "a",#5
           "b",#6
           "d",#7
           "d",#8
           "a",#9
           "c",#10
           "a",#11
           "d",#12
           "c",#13
           "b",#14
           "a",#15
           "a",#16
           "d",#17
           "a",#18
           "c",#19
           "c",#20
           "d",#21
           "a",#22
           "b",#23
           "c"#24
           )
