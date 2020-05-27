from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#create two D8 dice
die_1 = Die(8)
die_2 = Die(8)

#roll and store results in a list
results = []
for roll_num in range(100_000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#analysis
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#vizualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 dice 100,000 times', 
	xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')