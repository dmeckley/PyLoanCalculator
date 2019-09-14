from tkinter import *

class LoanCalculator:

	def __init__(self):

		# Window Object Instance Creation:
		window = Tk()
		window.title("LoanCalculator")

		# Annual Interest Rate Label and Entry Object:
		Label(window, text = "Annual Interest Rate").grid(row = 1, column = 1, sticky = W)
		self.annualInterestRateVar = StringVar()
		Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2)

		# Number of Years Label and Entry Object:
		Label(window, text = "Number of Years").grid(row = 2, column = 1, sticky = W)
		self.numberOfYearsVar = StringVar()
		Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2)

		# Loan Amount Label and Entry Object:
		Label(window, text = "Loan Amount").grid(row = 3, column = 1, sticky = W)
		self.loanAmountVar = StringVar()
		Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)

		# Monthly Payment Label Object:
		Label(window, text = "Monthly Payment").grid(row = 1, column = 3)
		self.monthlyPaymentVar = StringVar()
		lblMontlyPayment = Label(window, textvariable = self.monthlyPaymentVar).grid(row = 2, column = 3)

		# Total Payment Label Object:
		Label(window, text = "Total Payment").grid(row = 3, column = 3)
		self.totalPaymentVar = StringVar()
		lblTotalPayment = Label(window, textvariable = self.totalPaymentVar).grid(row = 4, column = 3)

		# Compute Payment Button Object:
		btComputePayment = Button(window, text = "Compute Payment", command = self.computePayment)
		btComputePayment.grid(row = 4, column = 2)

		# Main Window Continous Loop:
		window.mainloop()

	# Calculate Monthly Payment and Total Payment:
	def computePayment(self):
		monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()), 
			float(self.annualInterestRateVar.get()) / 1200,
			int(self.numberOfYearsVar.get()))
		self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f")) # Sets Monthly Payment Data Attribute for Label.
		totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
		self.totalPaymentVar.set(format(totalPayment, "10.2f")) # Sets Total Payment Data Attribute for Label.

	# Calculate and Return Monthly Payment:
	def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
		monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
		return(monthlyPayment)