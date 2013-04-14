Scoregraph
==========

My first ever D3 project! Implemented a modified version of the D3 example project [Focus+Context via Brushing](http://bl.ocks.org/mbostock/1667367) to create an area chart that you can pan and zoom on. 

Live demo [here](http://scoregraph.herokuapp.com). You can view the hacky JSON HttpResponse view I made to get the data import to work in D3 [here](http://scoregraph.herokuapp.com/data/). 

Views.py averages data from each day before returning it to the template so that the data is less spikey and more readable.