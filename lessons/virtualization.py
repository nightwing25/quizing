#this is a template for quiz taking



questions = (
        "what is it called when you can run many operating systems on one pc all at the same time virtually with independent cpu,memory,network,etc?",#0
        "whats host-based virtualization?",#1
        "a server that host virtual machines on an enterprise level is an example of what what type of virtual server?",#2
        "what is the hypervisor in charge of?",#3
        "in order for your pc to run a vm what is the MOST needed requirement?",#4
        "VT is for what companies cpu?",#5
        "for hypervisor what cpu proccessor support is AMD?",#6
        "when malware recognizes its on a vm and jumps to one host to another to gather info is an example of what?",#7
        "in virtual machine a network where the vm has the same ip as the pyhsical host when converted from nat, is what type of network?",#8
        "when the vm is a device on the physical network what type of network is this?",#9
        "what is the network called when the vm doesnt communicate with the outside network?",#10
        "an isolated test enviroment with no connection to the real world or production system is called?"#11
        )


options = (
        ("a.web server","b.standalone server","c.hypervisor","d.virtualization"),#0
        ("a.virtually use your normal desktop + others os's","b.use your desktop remotely through RDP","c.hypervisor","d.DaaS"),#1
        ("a.host based virtualization","b.standalone server","c.cross platform virtualization","d.legacy software"),#2
        ("a.sandboxing","b.manages the virtual platform & guest os / hardware managment","c.virtually use your normal desktop + other os's","d.standalone server"),#3
        ("a.storage space","b.cpu has to support virtualization","c.alot of RAM","d.network"),#4
        ("a.mediatek","b.nvidia","c.intel","d.AMD"),#5
        ("a.AMD-V","b.AMD-VT","c.AMD-NT","d.AMD hyper-v"),#6
        ("a.vm hopping","b.vdi","c.vm escaping","d.virtualization"),#7
        ("a.private address","b.Nat","c.bridged network","d.shared network"),#8
        ("a.bridge network address","b.shared network","c.private address","d.client-side"),#9
        ("a.hyper-v","b.private address network","c.shared network","d.bridge network"),#10
        ("a.guest","b.host","c.sandboxing","d.a virtual server")#11
        )

answers = (
        "d",#0    
        "a",#1   
        "b",#2   
        "b",#3   
        "b",#4   
        "c",#5   
        "a",#6   
        "c",#7   
        "d",#8   
        "a",#9   
        "b",#10   
        "c",#11  
           )

