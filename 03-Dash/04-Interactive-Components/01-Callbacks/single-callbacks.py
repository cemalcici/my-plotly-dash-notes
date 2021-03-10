import dash
import dash_core_components as dcc
import dash_html_components as html

# İnteraktif işlemler için gerekli sınıf yapıları
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id="my-id",
              value="Initial Text", # kullanıcıdan alınan verinin tutulduğu alan
              type="text"),
    html.Div(id="my-div") # yazdırma işlemi yapılacak alanın oluşturulması
])

# app.callback dekoratörünün amacı girilen veriye karşılık istenen çıktıyı oluşturmayı sağlar.
# argüman olarak iki liste alır. Birinci liste çıktı listesi, ikinci listesi ise girdi listesi.
# Çıktı listesinde yazılacak alanın "children" özelliğine işaret ederken
# Girdi listesinde "value" özelliğini işaret eder.
# id değerlerinin tanımlı olması bileşen özelinde işlem yapmayı kolaylaştırır.
# Bu yüzden her bir bileşenin id'si tanımlanması gerekir.
@app.callback(
    Output(component_id="my-div", component_property="children"),
    [Input(component_id="my-id", component_property="value")]
)
def update_output_div (input_value):
    # app.callback içerisinde tanımlanan gereksinimler kullanılarak buradaki fonksiyon çalıştırılıyor
    return f"You entered: {input_value}"

if __name__ == "__main__":
    app.run_server()