import customtkinter as ctk
from tkinter import messagebox

# --- Core FV function ---
def future_value(principal, annual_rate, years, monthly_deposit=0, compounds_per_year=12):
    """ Calculate the future value of an investment with compound
    interest and monthly deposits.
    """
    # Local shorthand (keeps the style of the original script)
    r = float(annual_rate)
    n = float(compounds_per_year)
    t = float(years)

    # Handle the zero-interest-rate special case to avoid division-by-zero.
    # When r == 0: principal does not grow, and deposits sum linearly: monthly * n * t
    if r == 0:
        fv_principal = float(principal)
        fv_deposits = float(monthly_deposit) * n * t
        return fv_principal + fv_deposits

    # FV of principal (compound growth)
    fv_principal = float(principal) * (1 + r / n) ** (n * t)
    # FV of monthly deposits (ordinary annuity formula)
    fv_deposits = float(monthly_deposit) * (((1 + r / n) ** (n * t) - 1) / (r / n))

    # FV total
    fv_total = fv_principal + fv_deposits
    return fv_total

    # --- Function to handle calculation ---
def calculate():
    try:
        p=float(entry_principal.get())
        r=float(entry_rate.get())/100
        t=float(entry_years.get())
        m=float(entry_deposit.get())

        fv = future_value(p, r, t, m)
        result_label.configure(text=f"Future Value after {t:.1f} years: \n ${fv:,.2f}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

# --- App UI setup ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Future Value Calculator")
app.geometry("400x450")

# --- Title ---
title_label = ctk.CTkLabel(app, text="Future Value Calculator\n(with Monthly Deposits)", font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=20)

# --- Input fields ---
entry_principal = ctk.CTkEntry(app, placeholder_text="Initial Investment Amount ($)")
entry_principal.pack(pady=10, fill="x", padx=40)

entry_rate = ctk.CTkEntry(app, placeholder_text="Annual Interest Rate (%)")
entry_rate.pack(pady=10, fill="x", padx=40)

entry_years = ctk.CTkEntry(app, placeholder_text="Number of Years")
entry_years.pack(pady=10, fill="x", padx=40)

entry_deposit = ctk.CTkEntry(app, placeholder_text="Monthly Deposit Amount ($)")
entry_deposit.pack(pady=10, fill="x", padx=40)

# --- Calculate button ---
calc_button = ctk.CTkButton(app, text="Calculate Future Value", command=calculate)
calc_button.pack(pady=20)

# --- Result display ---
result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=16))
result_label.pack(pady=20)

# --- Start the app ---
app.mainloop()
