Imports System.Net.Http
Imports Newtonsoft.Json.Linq
Imports System.Net.Mail
Imports MySql.Data.MySqlClient
Imports System.Security.Cryptography

Public Class Form2
    Private Function HashPassword(password As String, salt As String) As String
        ' Combine salt and password
        Dim combinedBytes() As Byte = System.Text.Encoding.UTF8.GetBytes(password & salt)

        ' Hash the combined value
        Dim hashedBytes() As Byte = New SHA256Managed().ComputeHash(combinedBytes)
        Return Convert.ToBase64String(hashedBytes)
    End Function

    Private Sub ConnectToDatabase()
        ' Connection string for MySQL database
        Dim connectionString As String = "server=localhost;user id=root;password=******;database=Subscription"

        ' Create a MySqlConnection object
        Dim connection As New MySqlConnection(connectionString)

        Try
            ' Open the database connection
            connection.Open()

            ' Generate salt
            Dim rng As New RNGCryptoServiceProvider()
            Dim saltBytes(15) As Byte
            rng.GetBytes(saltBytes)
            Dim salt As String = Convert.ToBase64String(saltBytes)

            ' Hash password
            Dim hashedPassword As String = HashPassword(txtPassword.Text.Trim(), salt)

            ' Insert user information into the database
            Dim query As String = "INSERT INTO users (username, email, password_hash, password_salt) VALUES (@username, @email, @password, @salt)"
            Using cmd As New MySqlCommand(query, connection)
                cmd.Parameters.AddWithValue("@username", txtUsername.Text.Trim())
                cmd.Parameters.AddWithValue("@email", txtEmail.Text.Trim())
                cmd.Parameters.AddWithValue("@password", hashedPassword)
                cmd.Parameters.AddWithValue("@salt", salt)
                cmd.ExecuteNonQuery()
            End Using

            ' Close the connection when done
            connection.Close()

            ' Send confirmation email to the user
            SendConfirmationEmail(txtEmail.Text.Trim())

            ' Display success message
            MessageBox.Show("Subscription successful! You will receive daily weather information and tips from WORLD FORECASTER!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information)
            Me.DialogResult = DialogResult.OK
        Catch ex As Exception
            ' Handle any errors that occur during connection or database operation
            MessageBox.Show("Error: " & ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
        Finally
            ' Ensure that the connection is closed even if an exception occurs
            If connection.State = ConnectionState.Open Then
                connection.Close()
            End If
        End Try
    End Sub

    Private Sub SendConfirmationEmail(email As String)
        ' Send email with confirmation message and subscription details
        Try
            Dim smtpClient As New SmtpClient("smtp.gmass.co") 'Replace with your smtp server
            smtpClient.Port = 25
            smtpClient.Credentials = New System.Net.NetworkCredential("gmass", "f160834f-012c-40cb-83ea-ec09f05e2134") 'replace with your email credentials
            smtpClient.EnableSsl = True

            Dim mailMessage As New MailMessage()
            mailMessage.From = New MailAddress("codhops41@gmail.com") ' Replace with your email address
            mailMessage.To.Add(email)
            mailMessage.Subject = "Subscription Confirmation"
            mailMessage.Body = "Thank you for subscribing to WORLD FORECASTER! You will receive daily weather information and tips."

            smtpClient.Send(mailMessage)
        Catch ex As Exception
            MessageBox.Show("Error sending confirmation email: " & ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
        End Try
    End Sub

    Private Sub btnSignup_Click(sender As Object, e As EventArgs) Handles btnSignup.Click
        ' Check if username, password, and email are provided
        If txtUsername.Text.Trim() <> "" AndAlso txtPassword.Text.Trim() <> "" AndAlso txtEmail.Text.Trim() <> "" Then
            ' Save user information to database and send confirmation email
            ConnectToDatabase()
        Else
            ' Display error message if any field is empty
            MessageBox.Show("Please fill in all fields.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
        End If
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Me.Close()
    End Sub

    Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

    End Sub

    Private Sub Form2_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub
End Class