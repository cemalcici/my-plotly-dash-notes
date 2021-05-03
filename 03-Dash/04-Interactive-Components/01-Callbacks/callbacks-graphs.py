import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("../../00-data/gapminderDataFiveYear.csv")

# Dropdown menü için sözlük listesinin oluşturulması.
# Burada eşsiz yıl değerlerince label ve value değerleri belirleniyor.
year_options = [{"label": str(year), "value": year} for year in df["year"].unique()]

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id="graph"),
    dcc.Dropdown(id="year-picker",
                 options=year_options,
                 value=df["year"].min())
])

# Dropdown elementine ait value değeri girildiğinde
# Graph elementine ait figure çıktısı verilecek şekilde ayarlanıyor.
@app.callback(
    Output(component_id="graph", component_property="figure"),
    [Input(component_id="year-picker", component_property="value")]
)
def update_figure(selected_year):
    # Seçilen yıla göre veri seti filtrelenecek
    filtered_df = df[df["year"] == selected_year]

    # Görselleştirilecek grafiğin data kısmı burada otomatize edilerek oluşturuluyor.
    traces = []
    for continent_name in filtered_df["continent"].unique(): # eşsiz continent değelerince gez
        df_by_continent = filtered_df[filtered_df["continent"] == continent_name] # continent_name'e göre filtrele
        # Filtrelenmiş veri setinden grafik oluştur ve listeye at
        traces.append(go.Scatter(x=df_by_continent["gdpPercap"], # x değişkeni
                                 y=df_by_continent["lifeExp"], # y değişkeni
                                 mode="markers", # noktanın cinsi
                                 opacity=0.7, # saydamlık
                                 marker = {"size": 15}, # noktaya ait öznitelikler
                                 name = continent_name)) # kategorik kırılımların ismleri

    # app.callback fonksiyonunda output olarak tanımlanan figure parametresine karşılık oluşturulan sözlük yapısı. Bu yapıyı hatırlamıyorsan dash notlarını tekrar kontrol et.
    return {"data": traces,
            "layout": go.Layout(title="My Plot",
                                xaxis={"title": "GDP Per Cap", "type": "log"},
                                yaxis={"title": "Life Expectancy"})}

if __name__ == "__main__":
    app.run_server()