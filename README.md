# Codename-FUD-C2
Bypass SIEM C2 detect
Using HTTP Protocol
RAT and Listener have the same key in order to encryp & decryp

              RAT    <    ----------SIEM --- many things --------------------------------------------   >   Listener
                                                                                                            
                                                                                                            1.	>>> cmd
                                                                                                            2.	RSA “cmd” <=> Value A
                                                                                                            3.	GET … Value A …
1.	Recv Value A
2.	Decryp Value A 
3.	Run cmd and store the output
4.	RSA “output” <=> Value B
5.	POST … Value B …
                                                                                                            4.	Recv Value B
                                                                                                            5.	Decryp Value B

SIEM:
POST …. Value B … => doesn’t have sign (“chmod”, “ifconfig” … or something like that)
GET …. Value A … => doesn’t have sign
