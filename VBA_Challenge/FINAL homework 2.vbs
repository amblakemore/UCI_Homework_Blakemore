Sub VBAChallenge():

	dim current as worksheet
	dim i as long
		
	'Set WS_Count = to the number of worksheets in the workbook
	WS_Count = ActiveWorkbook.Worksheets.count
	
	'begin loop
	For i = 1 to WS_Count

	Next i

		'Setting the ticker name
		dim tickername as string

		'Setting the ticker volume
		dim tickervolume as double
		tickervolume = 0

		'Tracking the ticker location
		dim summary_ticker_row as double
		summary_ticker_row = 2

		'Name final variables for the objectives
		dim Close_Price as double
		Close_Price = 0
		dim Open_Price as double
		Open_Price = 0	
		dim Yearly_Change as double
		Yearly_Change = 0
		dim Percent_Change as double
		Percent_Change = 0

		Lastrow = Cells(rows.count, 1).End(XLup).row

		'set rows for the summary information
		cells(1, 9).value = "Ticker"
		cells(1, 10).value = "Yearly Change"
		cells(1, 11).value = "Percent Change"
		cells(1, 12).value = "Total Stock Volume"

		For i = 2 to Lastrow

			'Begin loop
			If cells(i + 1, 1).value <> cells(i, 1).value then

				'Find Ticker Name'
				Tickername = cells(i, 1).value

				'Find the closing price'
				Close_price = cells(i, 6).value

				'find the price change for the year
				Yearly_Change = (Close_Price - Open_Price)
					if open_price <> 0 then
						Percent_Change = (Yearly_Change / Open_Price)
					end If

				'find the volume
				Tickervolume = tickervolume + cells(i, 7).value

				'Assign Ticker name to the correct column
				Range("I" & summary_ticker_row).value = tickername

				'Assigned the yearly change to the correct column
				Range("J" & summary_ticker_row).value = Yearly_Change

				'Assign the volume to the correct column
				Range("L" & summary_ticker_row).value = tickervolume

				'Assign the Percentage Change to the correct column
				Range("K" & summary_ticker_row).value = Percent_Change
					if Percent_Change > 0 then
						Range("J" & summary_ticker_row).interior.colorIndex = 4
					Else	
						Range("J" & summary_ticker_row).interior.colorIndex = 3
					end if

				summary_ticker_row = summary_ticker_row +1

				Tickervolume = 0

				open_price = cells(i + 1, 3)

				Else
					tickervolume = tickervolume + cells(i, 7).value

			End If

		Next i

	lastrow_summary_table = Cells(Rows.count , 9).End(XLup).row

End Sub