Module Module1
    Sub main()
        Dim radius As Double
        Dim area As Double
        Dim pi As Double = 3.142
        Try
            radius = Double.Parse(InputBox("enter"))
        Catch ex As Exception
            MsgBox("no number")
            Exit Sub

        End Try
        Try
            area = pi * radius * radius
        Catch ex As Exception
            MsgBox("error")
            Exit Sub

        End Try
        MsgBox("Ayekoo")
    End Sub
End Module
