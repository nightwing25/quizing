questions = ("file transfer protocol is on what ports?",#1
             "what port is for http servers?",#2
             "voip is on which port?",#3
             "what are the non-ephemeral ports(permenant ports)that are usually on a server or service?",#4
             "what are the ephemeral ports determined by the client?",#5
             "in port numbers tcp and udp can be any number between___",#6
             "what port do you use when you need to connect to a remote device terminals(encrypted)?",#7
             "what port do you use to send emails?",#8
             "to convert ip's to name addresses what port is in use?",#9
             "the automatic assignment of ip adresses are on what port(s)?",#10
             "to login to a devices terminal remotely what port is in use(unencrypted)?",#11
             "this port/protocol downloads & manages email inboxes from multiple clients ____",#12
             "this protocol/port has basic email transfer functionality wasnt built for multiple email clients____",#13
             "this protocol/port is for communictaion in browsers(securely)",#14
             )


options = (
        ("a.tcp/21(active mode data),udp/22(control)","b.tcp/22,tcp/23","c.udp/21(control),udp/22(data)","d.tcp/20(active data mode),tcp/21(control)"),#1
        ("a.udp/80","b.tcp/8080","c.tcp/389","d.udp/443"),#2
            ("a.udp/5004","b.tcp/5004","c.tcp/123","d.udp/5003"),#3
        ("a.ports 1024-65,535","b.ports 0-65,535","c.ports 0-1023","d.ports 1-1024"),#4
        ("a.ports 1024-65,535","b.ports 0-65,535","c.ports 1-1024","d.ports 1000"),#5 
        ("a.ports 1024-65,535","b.ports 1-5555","c.ports 2000-5555","d.ports 0-65,535"),#6
        ("a.netbios udp/137,udp/139","b.smb","c.smtp tcp/25","d.ssh tcp/22 "),#7
        ("a.POP3 tcp/110","b.IMAP tcp/143","c.ssh tcp/22","d.smtp tcp/25"),#8
        ("a.DHCP udp/67 udp/68","b.SNMP (queries:udp/161,traps:udp/162)","c.DNS udp/53","d.LDAP tcp/389"),#9
        ("a.smtp tcp/25","b.DHCP udp/67 udp/68","c.netbios udp/137,udp/139","d.smtp tcp/25"),#10
        ("a.DNS udp/53","b.POP3 110","c.telnet tcp/23","d.ssh tcp/22"),#11
        ("a.smtp tcp/25","b.POP3 110","c.http 8080","d.IMAP tcp/143"),#12
        ("a.POP3 tcp/110","b.IMAP tcp/143","c.netbios udp/137,udp/139","d.smtp tcp/25"),#13
        ("a.HTTPS tcp/443","b.http tcp/8080","c.netbios udp/137,udp/139","d.DHCP udp/67")#14
        )

answers = ("d",#1
        "b",#2
        "a",#3
        "c",#4
        "a",#5
        "d",#6
        "d",#7
        "d",#8
        "c",#9
        "b",#10
        "c",#11
        "d",#12
        "a",#13
        "a"#14
           )


