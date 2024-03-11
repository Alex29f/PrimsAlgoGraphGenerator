# English
# PrimsAlgoGraphGenerator
Python project for creating graphs with specific weights that will serve the purpose of teaching Prims algorithm or creating tests.
# graphFunctions.py 
This file generates graph with specific weights where there are:
a) 7-15 vertices (ammount entered by user);
b) degree of vertices is 2-5 (max ammount of edges that one vertice can have);
c) edge weights: [1-10].

Specific situations that created graph has when performing Prims algorithm on it:
1. New vertex label value is the same as old vertex label value;
2. In one of the steps, there is a case where, one must choose between several vertices with same label values;
3. Vertex with the smallest value was already obtained 2 steps earlier but should be used only in the next step;
4. Searching for adjacent vertices, all are already included in the frame and the label values of vertices are not renewed.

graphFunctions.py also contains functions that handle edge, vertex addition or removal, displaying MST and also drawGraph function to display generated graph.
# main.py
Contains code for the GUI.
# RequiredPackages
[Matplotlib](https://matplotlib.org/)
[NetworkX](https://networkx.org/)
Already with Python3 - [Tkinter],[random]

# Latvian
# PrimsAlgoGraphGenerator
Python projekts, kas ģenerē loku svarus grafam, kas nepieciešams Prima algoritma mācīšanai, uzdevumu veidošanai.
# graphFunctions.py 
Šis fails satur algoritmu kas ģenerē grafu ar šādiem nosacījumiem:
a) Virsotņu skaitu ievada lietotājs: 7-15;
b) Loku skaits katrai virsotnei jeb virsotņu lokālās pakāpes ir no 2-5;
c) Svari: [1-10].

Pielietojot Prima algoritmu izveidotajam grafam veidosies šādas situācijas:
1. Virsotnei jaunajai iezīmei ir tāda pati skaitliskā vērtība kā tās vecajai pazīmei;
2. Solī ir jāizvēlas starp vairākām virsotnēm ar vienādām iezīmju skaitliskajām vērtībām;
3. Virsotne ar mazāko iezīmi, to ieguva 2 soļu iepriekš, bet ir jāizmanto tikai nākošajā;
4. Meklējot blakusvirsotnes, visas jau ir iekļautas karkasā un iezīmes neatjauno.

graphFunctions.py satur arī funkcijas loku un virsotņu pievienošanai, noņemšanai, minimālā karasa attēlošanai, kā arī satur funkciju, kas atbildīga par grafa zīmēšanu.
# main.py
Satur kodu ar grafisko lietotāja saskarni.
# RequiredPackages
[Matplotlib](https://matplotlib.org/)
[NetworkX](https://networkx.org/)
Already with Python3 - [Tkinter],[random]