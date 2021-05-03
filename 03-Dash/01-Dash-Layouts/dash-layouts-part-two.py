import dash
import dash_core_components as dcc
import dash_html_components as html

# stil oluşturmak için renkler eklendi
COLORS = {'background': "#111111",
          "text":"#7FDBFF"}


data = [{'x': [1, 2, 3],
         'y': [4, 1, 2],
         'type': "bar",
         "name": "SF"},
        {'x': [1, 2, 3],
         'y': [2, 4, 5],
         'type': "bar",
         "name": "NYC"}]

layout = {"title": "BAR PLOTS!",
          "plot_bgcolor": COLORS["background"], # grafiğin arkaplan rengi
          "paper_bgcolor": COLORS["background"], # graph nesnesinin arkaplan rengi
          "font": {'color': COLORS["text"]}} # yazı tipinin rengi

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children="Hello Dash", style={'textAlign': 'center', # css'teki stil özniteliğine ait metin hizalama
                                          'color': COLORS['text']}), # css'teki stil özniteliğine ait yazı rengi
    dcc.Graph(id="example",
              figure={"data":data,
                      "layout": layout})],
    style={"backgroundColor": COLORS["background"]}) # Div elementinin stil özniteliğine ait arkaplan rengi

if __name__ == "__main__":
    app.run_server()