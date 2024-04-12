Imports System.Net.Http
Imports Newtonsoft.Json.Linq

Public Class Form1
    Private Const API_KEY As String = "59d33cbd3c9fa3afcd384bfd41a05eed"
    Private Const API_URL As String = "http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric"

    Private Async Sub btnGetWeather_Clic(sender As Object, e As EventArgs) Handles btnGetWeather.Click
        Dim city As String = txtCity.Text.Trim()

        If city <> String.Empty Then
            lblCity.Text = $"City: {city}".ToUpper() ' Display the entered city name

            Dim apiUrl As String = String.Format(API_URL, city, API_KEY)

            Try
                Using httpClient As New HttpClient()
                    Dim response As HttpResponseMessage = Await httpClient.GetAsync(apiUrl)

                    If response.IsSuccessStatusCode Then
                        Dim responseContent As String = Await response.Content.ReadAsStringAsync()

                        Dim jsonResponse As JObject = JObject.Parse(responseContent)

                        Dim weatherDescription As String = jsonResponse.SelectToken("weather[0].description").ToString().ToUpper()
                        Dim temperature As String = jsonResponse.SelectToken("main.temp").ToString().ToUpper
                        Dim humidity As String = jsonResponse.SelectToken("main.humidity").ToString().ToUpper

                        lblWeather.Text = $"Weather: {weatherDescription}".ToUpper
                        lblTemperature.Text = $"Temperature: {temperature}°C".ToUpper
                        lblHumidity.Text = $"Humidity: {humidity}%".ToUpper

                        Select Case weatherDescription
                            Case "CLEAR SKY"
                                lblTips.Text = $"TIP: It's a clear sky! Enjoy the sunshine."
                            Case "FEW CLOUDS", "SCATTERED CLOUDS", "BROKEN CLOUDS"
                                lblTips.Text = $"TIP: There are some clouds in the sky. Consider bringing an umbrella, just in case."
                            Case "OVERCAST CLOUDS", "MIST"
                                lblTips.Text = $"TIP: It's cloudy or misty. Don't forget your jacket."
                            Case "SHOWER RAIN", "RAIN"
                                lblTips.Text = $"TIP: It's raining! Remember to carry an umbrella or raincoat."
                            Case "THUNDERSTORM", "HEAVY INTENSITY RAIN", "MODERATE RAIN", "LIGHT INTENSITY SHOWER RAIN"
                                lblTips.Text = $"TIP: Thunderstorm alert! Stay indoors and avoid going outside."
                            Case "SNOW", "SLEET", "LIGHT SNOW", "HEAVY SNOW"
                                lblTips.Text = $"TIP: It's snowing! Be cautious while driving and wear warm clothing."
                            Case "FOG"
                                lblTips.Text = $"TIP: It's foggy outside. Drive safely and use fog lights if necessary."
                            Case Else
                                lblTips.Text = $"TIP: Weather conditions are unpredictable. Stay safe!"
                        End Select
                    Else
                        MessageBox.Show("Failed to retrieve weather data. Please try again later.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
                    End If
                End Using
            Catch ex As Exception
                MessageBox.Show("Error: " & ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            End Try
        Else
            MessageBox.Show("Please enter a city name.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
        End If
    End Sub

    Private Sub Label2_Click(sender As Object, e As EventArgs) Handles Label2.Click

    End Sub

    Private Sub lblTemperature_Click(sender As Object, e As EventArgs) Handles lblTemperature.Click

    End Sub

    Private Sub lblWeather_Click(sender As Object, e As EventArgs) Handles lblWeather.Click

    End Sub

    Private Sub Label4_Click(sender As Object, e As EventArgs)

    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub BtnSignup_Click(sender As Object, e As EventArgs) Handles BtnSignup.Click

        Form2.Show()
    End Sub
End Class