<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Form1))
        txtCity = New TextBox()
        btnGetWeather = New Button()
        lblWeather = New Label()
        lblTemperature = New Label()
        lblHumidity = New Label()
        Label1 = New Label()
        Label2 = New Label()
        lblCity = New Label()
        lblTips = New Label()
        Label3 = New Label()
        BtnSignup = New Button()
        SuspendLayout()
        ' 
        ' txtCity
        ' 
        txtCity.Location = New Point(250, 94)
        txtCity.Multiline = True
        txtCity.Name = "txtCity"
        txtCity.Size = New Size(340, 28)
        txtCity.TabIndex = 0
        ' 
        ' btnGetWeather
        ' 
        btnGetWeather.Location = New Point(515, 128)
        btnGetWeather.Name = "btnGetWeather"
        btnGetWeather.Size = New Size(75, 23)
        btnGetWeather.TabIndex = 1
        btnGetWeather.Text = "SEARCH"
        btnGetWeather.UseVisualStyleBackColor = True
        ' 
        ' lblWeather
        ' 
        lblWeather.AutoSize = True
        lblWeather.BackColor = Color.Transparent
        lblWeather.Font = New Font("Sitka Display", 15.7499981F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        lblWeather.ForeColor = Color.Cornsilk
        lblWeather.Location = New Point(40, 197)
        lblWeather.Name = "lblWeather"
        lblWeather.Size = New Size(118, 30)
        lblWeather.TabIndex = 2
        lblWeather.Text = "WEATHER :"
        ' 
        ' lblTemperature
        ' 
        lblTemperature.AutoSize = True
        lblTemperature.BackColor = Color.Transparent
        lblTemperature.Font = New Font("Sitka Display", 15.7499981F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        lblTemperature.ForeColor = Color.Cornsilk
        lblTemperature.Location = New Point(12, 297)
        lblTemperature.Name = "lblTemperature"
        lblTemperature.Size = New Size(163, 30)
        lblTemperature.TabIndex = 3
        lblTemperature.Text = "TEMPERATURE :"
        ' 
        ' lblHumidity
        ' 
        lblHumidity.AutoSize = True
        lblHumidity.BackColor = Color.Transparent
        lblHumidity.Font = New Font("Sitka Display", 15.7499981F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        lblHumidity.ForeColor = Color.Cornsilk
        lblHumidity.Location = New Point(37, 250)
        lblHumidity.Name = "lblHumidity"
        lblHumidity.Size = New Size(122, 30)
        lblHumidity.TabIndex = 4
        lblHumidity.Text = "HUMIDITY :"
        ' 
        ' Label1
        ' 
        Label1.AutoSize = True
        Label1.BackColor = Color.Transparent
        Label1.Font = New Font("Perpetua Titling MT", 15.75F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        Label1.Location = New Point(252, 9)
        Label1.Name = "Label1"
        Label1.Size = New Size(251, 26)
        Label1.TabIndex = 5
        Label1.Text = "WORLD FORECASTER"
        ' 
        ' Label2
        ' 
        Label2.AutoSize = True
        Label2.BackColor = Color.Transparent
        Label2.Font = New Font("Sitka Display", 15.7499981F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        Label2.ForeColor = Color.Cornsilk
        Label2.Location = New Point(12, 92)
        Label2.Name = "Label2"
        Label2.Size = New Size(242, 30)
        Label2.TabIndex = 6
        Label2.Text = "ENTER CITY OF CHOICE :"
        ' 
        ' lblCity
        ' 
        lblCity.AutoSize = True
        lblCity.BackColor = Color.Transparent
        lblCity.Font = New Font("Sitka Display", 15.7499981F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        lblCity.ForeColor = Color.Cornsilk
        lblCity.Location = New Point(67, 145)
        lblCity.Name = "lblCity"
        lblCity.Size = New Size(67, 30)
        lblCity.TabIndex = 7
        lblCity.Text = "CITY :"
        ' 
        ' lblTips
        ' 
        lblTips.AutoSize = True
        lblTips.BackColor = Color.Transparent
        lblTips.Font = New Font("Sitka Display", 15.7499981F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        lblTips.ForeColor = Color.Cornsilk
        lblTips.Location = New Point(67, 342)
        lblTips.Name = "lblTips"
        lblTips.Size = New Size(54, 30)
        lblTips.TabIndex = 8
        lblTips.Text = "TIP :"
        ' 
        ' Label3
        ' 
        Label3.AutoSize = True
        Label3.BackColor = Color.Transparent
        Label3.Font = New Font("Sitka Display", 9.749999F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        Label3.Location = New Point(343, 433)
        Label3.Name = "Label3"
        Label3.Size = New Size(243, 19)
        Label3.TabIndex = 9
        Label3.Text = "TO SUBSCRIBE TO WORLD FORECASTER:"
        ' 
        ' BtnSignup
        ' 
        BtnSignup.BackColor = Color.Transparent
        BtnSignup.Location = New Point(592, 428)
        BtnSignup.Name = "BtnSignup"
        BtnSignup.Size = New Size(75, 23)
        BtnSignup.TabIndex = 10
        BtnSignup.Text = "SUBSCRIBE"
        BtnSignup.UseVisualStyleBackColor = False
        ' 
        ' Form1
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        BackColor = SystemColors.Control
        BackgroundImage = CType(resources.GetObject("$this.BackgroundImage"), Image)
        ClientSize = New Size(682, 463)
        Controls.Add(BtnSignup)
        Controls.Add(Label3)
        Controls.Add(lblTips)
        Controls.Add(lblCity)
        Controls.Add(Label2)
        Controls.Add(Label1)
        Controls.Add(lblHumidity)
        Controls.Add(lblTemperature)
        Controls.Add(lblWeather)
        Controls.Add(btnGetWeather)
        Controls.Add(txtCity)
        Name = "Form1"
        Text = "Form1"
        ResumeLayout(False)
        PerformLayout()
    End Sub

    Friend WithEvents txtCity As TextBox
    Friend WithEvents btnGetWeather As Button
    Friend WithEvents btnGetWeather_Click As Button
    Friend WithEvents lblWeather As Label
    Friend WithEvents lblTemperature As Label
    Friend WithEvents lblHumidity As Label
    Friend WithEvents Label1 As Label
    Friend WithEvents Label2 As Label
    Friend WithEvents lblCity As Label
    Friend WithEvents lblTips As Label
    Friend WithEvents Label3 As Label
    Friend WithEvents BtnSignup As Button

End Class
