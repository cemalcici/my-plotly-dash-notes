import dash
import dash_core_components as dcc
import dash_html_components as html

# Veri Setimizi oluşturduk
# Aynı grafik üzerinde birden fazla veri görebilmek için liste içerisinde tutuyoruz.
# Bununla beraber grafik için parametrelerimizi de sözlük yapısı içerisinde tutuyoruz.
data = [{'x': [1, 2, 3],
         'y': [4, 1, 2],
         'type': "bar",
         "name": "SF"},
        {'x': [1, 2, 3],
         'y': [2, 4, 5],
         'type': "bar",
         "name": "NYC"}]

# Grafiğin arayüz özelliklerini sözlük içerisinde tutumamız gerek.
layout = {"title": "BAR PLOTS!"}

app = dash.Dash()

app.layout = html.Div(children=[ # html'deki div elementi
    html.H1("Hello Dash"), # html'deki h1 elementi
    html.Div("Dash: Web Dashboards with Python"), # html'deki div elementi
    # Grafik bileşeni
    dcc.Graph(id="example", # id attribute
              figure={"data":data,
                      "layout": layout}) # figür yapısı. Yukarıdaki değerler verildi
])

if __name__ == "__main__":
    app.run_server()