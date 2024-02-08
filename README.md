# English
# PrimsAlgoGraphGenerator
Python project for creating graphs with specific weights that will serve the purpose of teaching Prims algorithm - in development stage
# generateGrahp.py
This file generates graph with specific weights where there are:
a) 7-15 vertices (ammount entered by user)
b) degree of vertices is 2-5 (max ammount of edges that one vertice can have)
c) edge weights are from 1 to 10

Specific situations that created graph must have when using Prims algorithm on it
1. New value of the Vertex has the same value of the value
2. In one of the steps, there is a case where, one must choose between several vertices with same values.
3. Vertex with the smallest value was already obtained 2 steps earlier but should be used only in the next step
4. Searching for adjacent vertices, all are already included in the frame and the values of vertices are not renewed
# drawGraph.py
Contains code for displaying the graph that is generated in generateGraph.py
# main.py
contains code for the GUI

# Latvian
# PrimsAlgoGraphGenerator
Python projekts, kas ģenerē loku svarus grafam, kas nepieciešams Prima algoritma mācīšanai.
# generateGrahp.py
Šis fails satur algoritmu kas ģenerē grafu ar šādiem nosacījumiem:
a) Virsotņu skaits maināms: 7-15
b) Loku skaits: virsotņu lokālās pakāpes ir no 2-5.
c) Svari: [1-10]

Visām virsotnēm ir jābūt savā starpā savienotām (nevar būt izolētas virsotnes), kā arī nevar būt virsotnes ar lokālo pakāpi 1.

Pielietojot Prima algoritmu, jāveidojas šādām situācijām:
1. Virsotnei jaunajai iezīmei ir tāda pati skaitliskā vērtība kā tās vecajai pazīmei.
2. Solī ir jāizvēlas starp vairākām virsotnēm ar vienādām iezīmju skaitliskajām vērtībām.
3. Virsotne ar mazāko iezīmi, to ieguva 2 soļu iepriekš, bet ir jāizmanto tikai nākošajā
4. Meklējot blakusvirsotnes, visas jau ir iekļautas karkasā un iezīmes neatjauno.
# drawGraph.py
Satur kodu lai varētu attēlot grafu kas tika izveidots ar generateGraph.py funkciju
# main.py
satur kodu kas nepieciešama grafiskajai lietotāja saskarnei un funkicju izpildei
