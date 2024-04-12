<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form2
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
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
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Label1 = New Label()
        Label2 = New Label()
        Label3 = New Label()
        txtUsername = New TextBox()
        txtEmail = New TextBox()
        txtPassword = New TextBox()
        btnSignup = New Button()
        Button1 = New Button()
        Label4 = New Label()
        SuspendLayout()
        ' 
        ' Label1
        ' 
        Label1.AutoSize = True
        Label1.Font = New Font("Sitka Display", 12F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        Label1.Location = New Point(12, 53)
        Label1.Name = "Label1"
        Label1.Size = New Size(95, 23)
        Label1.TabIndex = 0
        Label1.Text = "USERNAME:"
        ' 
        ' Label2
        ' 
        Label2.AutoSize = True
        Label2.Font = New Font("Sitka Display", 12F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        Label2.Location = New Point(12, 102)
        Label2.Name = "Label2"
        Label2.Size = New Size(60, 23)
        Label2.TabIndex = 1
        Label2.Text = "EMAIL:"
        ' 
        ' Label3
        ' 
        Label3.AutoSize = True
        Label3.Font = New Font("Sitka Display", 12F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        Label3.Location = New Point(12, 142)
        Label3.Name = "Label3"
        Label3.Size = New Size(92, 23)
        Label3.TabIndex = 2
        Label3.Text = "PASSWORD:"
        ' 
        ' txtUsername
        ' 
        txtUsername.Location = New Point(110, 53)
        txtUsername.Name = "txtUsername"
        txtUsername.Size = New Size(184, 23)
        txtUsername.TabIndex = 3
        ' 
        ' txtEmail
        ' 
        txtEmail.Location = New Point(110, 102)
        txtEmail.Name = "txtEmail"
        txtEmail.Size = New Size(184, 23)
        txtEmail.TabIndex = 4
        ' 
        ' txtPassword
        ' 
        txtPassword.Location = New Point(110, 142)
        txtPassword.Name = "txtPassword"
        txtPassword.PasswordChar = "*"c
        txtPassword.Size = New Size(184, 23)
        txtPassword.TabIndex = 5
        ' 
        ' btnSignup
        ' 
        btnSignup.Font = New Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        btnSignup.Location = New Point(230, 253)
        btnSignup.Name = "btnSignup"
        btnSignup.Size = New Size(64, 25)
        btnSignup.TabIndex = 6
        btnSignup.Text = "SIGN UP"
        btnSignup.UseVisualStyleBackColor = True
        ' 
        ' Button1
        ' 
        Button1.Font = New Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        Button1.Location = New Point(12, 253)
        Button1.Name = "Button1"
        Button1.Size = New Size(75, 23)
        Button1.TabIndex = 7
        Button1.Text = "CLOSE"
        Button1.UseVisualStyleBackColor = True
        ' 
        ' Label4
        ' 
        Label4.AutoSize = True
        Label4.Font = New Font("Sitka Display", 12F, FontStyle.Bold, GraphicsUnit.Point, CByte(0))
        Label4.Location = New Point(38, 9)
        Label4.Name = "Label4"
        Label4.Size = New Size(266, 23)
        Label4.TabIndex = 8
        Label4.Text = "SUBSCRIBE TO WORLD FORECASTER"
        ' 
        ' Form2
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        BackColor = Color.DarkGray
        ClientSize = New Size(342, 288)
        Controls.Add(Label4)
        Controls.Add(Button1)
        Controls.Add(btnSignup)
        Controls.Add(txtPassword)
        Controls.Add(txtEmail)
        Controls.Add(txtUsername)
        Controls.Add(Label3)
        Controls.Add(Label2)
        Controls.Add(Label1)
        Name = "Form2"
        Text = "Form2"
        ResumeLayout(False)
        PerformLayout()
    End Sub

    Friend WithEvents Label1 As Label
    Friend WithEvents Label2 As Label
    Friend WithEvents Label3 As Label
    Friend WithEvents txtUsername As TextBox
    Friend WithEvents txtEmail As TextBox
    Friend WithEvents txtPassword As TextBox
    Friend WithEvents btnSignup As Button
    Friend WithEvents Button1 As Button
    Friend WithEvents Label4 As Label
End Class
