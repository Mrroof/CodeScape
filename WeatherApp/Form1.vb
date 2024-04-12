Imports System.Net.Http
Imports System.Windows.Forms.VisualStyles.VisualStyleElement

Public Class Form1

    Private Const OpenWeatherMapUrl As String = "https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}"

    ' Replace with your OpenWeatherMap API key
    Private Const ApiKey As String = "59d33cbd3c9fa3afcd384bfd41a05eed"

    Private Sub Button1_Click(sender As Object, e As EventArgs) Implements EventHandler
        Dim City As String = TextBox1.Text
        If String.IsNullOrEmpty(City) Then
            MsgBox("Please enter a city name.", MsgBoxStyle.Information)
            Exit Sub
        End If

        ' Build the API request URL with zip code and API key
        Dim url = String.Format(OpenWeatherMapUrl, City, ApiKey)

        Dim response As String = GetWeatherData(url)

        If String.IsNullOrEmpty(response) Then
            MsgBox("Error fetching weather data.", MsgBoxStyle.Error)
            Exit Sub
        End If

        ' Parse the JSON response (replace with your parsing logic)
        Dim data As JObject = JObject.Parse(response)
        Dim temp As Double = CType(data("main")("temp"), Double) - 273.15 ' Convert Kelvin to Celsius

        ' Update UI with weather information
        Label1.Text = String.Format("Temperature: {0:F1}°C", temp)
        ' ... update other labels with feels_like, description, etc. (refer to API documentation)
    End Sub

    Private Function GetWeatherData(ByVal url As String) As String
        Dim client As New HttpClient()
        Dim response As HttpResponseMessage = client.GetAsync(url).Result

        If response.IsSuccessStatusCode Then
            Dim responseString As String = response.Content.ReadAsStringAsync().Result
            Return responseString
        Else
            Return Nothing
        End If
    End Function
End Class