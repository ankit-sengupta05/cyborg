---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:32:15.966843'
id: cfe38ca3
links: []
modified: '2026-05-07T20:32:15.966843'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: Computer Arithmetic Addition and Subtraction Addition and Su (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: f44ddbd7a292
source: Addition-and-Subtraction-using-Signed-Magnitude-form_1.pdf
page: 0
title: Computer Arithmetic Addition and Subtraction Addition and Su (Chunk 0)
keywords: ['Signed Magnitude', "One's Complement", "Two's Complement", 'Integers', 'Addition/Subtraction', 'Algorithm', 'Hardware']
created: 2026-05-08 02:02:15
tree_path: COA > Page 0 > Computer Arithmetic Addition and Subtraction Addit
---

Computer Arithmetic Addition and Subtraction Addition and Subtraction with Signed magnitude data •There are3ways ofrepresenting negative fixed point binary numbers .They are 1.Signed Magnitude representation . 2.Signed one’s Complement representation 3.Signed two’s Complement representation •Most computers use the Signed two’s Complement representation when performing operation on integers . •Consider themagnitude ofany two numbers Aand B and the eight different operation are listed below depending onthesign ofthenumber . Eight Conditions for Signed - Magnitude Addition/Subtraction OperationADD MagnitudesSUBTRACT Magnitudes A > B A < B A = B (+A) + (+B) + (A + B) (+A) + ( -B) + (A –B ) -(B –A ) + (A –B ) (-A) + (+B) -(A –B ) + (B –A ) + (A –B ) (-A) + ( -B) -( A + B) (+A) -(+B) + (A –B ) -(B –A ) + (A –B ) (+A) -(-B) + (A + B) (-A) -(+B) -( A + B) (-A) -(-B) -(A –B ) + (B –A ) + (A –B )1 2 3 4 5 6 7 8 Addition and Subtraction with Signed magnitude data ALGORITHM : •When the sign ofAand Bareidentical, add the two magnitudes and attach the sign ofAtothe result . •When thesign ofAand Baredifferent, compare the magnitudes, subtract smaller number from thelarger . •Choose the sign ofthe result tobesame asAif A>B orcomplement thesign ofAifA<B. •Ifthetwo magnitudes areequal, subtract Bfrom Aand Make thesign oftheresult positive . Hardware for signed -magnitude addition and subtraction A registerA VF EBs ASB register Complementer Parallel Adder S Load SumMMode Control Input CarryOutput Carry Hardware for signed -magnitude addition and subtraction •Let Aand Bbethe two registers that holds the magnitudes ofthe numbers and Asand Bsbetwo flipflops that holds thecorresponding sign •The result oftheoperation may betransferred tothe third register ortheresult istransferred toAand As. •First parallel adder is needed to perform microoperation A+B. •Second comparator circuit needed toestablish ifA<B, A>B orA==B . •Third subtractor circuit isneeded toperform the microoperation A-Band B-A. Hardware for signed -magnitude addition and subtraction •The block diagram consist ofregister Aand Band thesign flipflops Asand Bs.Subtraction isdone byadding Atothe 2’scomplement ofB. •The o/p carry istransferred toE.The add overflow flipflop (AVF) holds the overflow bitwhen Aand Bare added . •The addition A+B isdone through the parallel adder and thesum istransferred toAregister . •When theMode bitM=0theo/p ofBistransferred tothe adder, thei/pcarry is0and theo/poftheadder isequal to sum A+B •When M=1,the 1’scomplement ofBisapplied toadder, thei/pcarry is1and theo/pisequal toA+B’+1. Hardware Algorithm Hardware Algorithm •The two sign bits Asand Bsarecompared by XOR gate .Iftheo/p is0,thesign areidentical and iftheo/pis1,thesign aredifferent . •For an add operation the identical sign indicates that magnitudes aretobeadded . •For the subtraction operation different sign indicate that magnitude aretoadded . •The magnitudes are added with microoperation EA=A+B . Hardware Algorithm •The two magnitudes are subtracted ifthe sign are different for an add operation or identical for subtraction operation . •IfE=1,then thecondition isA>=B and thenumber inA isthecorrect result . •IfE=0then thecondition isA<B and thenumber inAis taken 2’scomplement which isthecorrect result . •Ifthesign oftheresult issame asthesign ofA,Sono change inAsisrequired . •When A<B thesign oftheresult isthecomplement of theoriginal sign ofA. •The Final result isfound inregister Aand itssign inAs. Add operation ≠ 0=0A>=BAs =BS=0 =1Augend in A Added in B ENDAs BS+ EA A + B A VF EEA A + B +1 A VF 0 E A As0A A A A+1 As AsAs ≠ BS =0 =1 A<B •For Example of Addition •(+1) + (+2) (+A) + (+B) Add operation ≠ 0=0A>=BAs =BS=0 =1Augend in A Added in B ENDAs BS+ EA A + B A VF EEA A + B +1 A VF 0 E A As0A A A A+1 As AsAs ≠BS =0 =1 A<B •(-1) + (+2) (-A) + (+B) Take A= -1, B=+2 and perform the calculation Add operation ≠ 0=0A>=BAs =BS=0 =1Augend in A Added in B ENDAs BS+ EA A + B A VF EEA A + B +1 A VF 0 E A As0A A A A+1 As AsAs ≠BS =0 =1 A<B •For Example of Subtraction •(+1) -(-2) (+A) -(-B) As ≠BSSubtract operation ≠ 0=0A>=BAs =BS=0 =1Miuend in A Subtrahend in B ENDAs BS+ EA A + B A VF EEA A + B +1 A VF 0 E A As0A A A A+1 As As=0 =1 A<B •(+5) –(+2) (+A) –(+B) As ≠BSSubtract operation ≠ 0=0A>=BAs =BS=0 =1Miuend in A Subtrahend in B ENDAs BS+ EA A + B A VF EEA A + B +1 A VF 0 E A As0A A A A+1 As As=0 =1 A<B

### Related Concepts
- [[Signed Magnitude]]
- [[Hardware]]
- [[Integers]]
- [[Algorithm]]
- [[One's Complement]]
- [[Two's Complement]]
- [[Addition/Subtraction]]
