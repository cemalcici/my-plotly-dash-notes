import plotly.offline as pyo
import plotly.graph_objs as go

# Veri Setinin Belirlenmesi
snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

# Kutu Grafiklerinin Oluşturulması
data = [
    go.Box(
        y=snodgrass,
        name='QCS'
    ),
    go.Box(
        y=twain,
        name='MT'
    )
]

layout = go.Layout(title = 'Comparison of three-letter-word frequencies<br>\
    between Quintus Curtius Snodgrass and Mark Twain')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='boxplot3.html')
