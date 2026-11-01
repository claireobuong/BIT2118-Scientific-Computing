from scipy.optimize import root_scalar

# A microfinance borrower receives 50,000 and repays 12 monthly
# instalments of 4,800. What monthly interest rate is being charged?
# Assumptions: payments at the end of each month, no extra fees.
cash_flows = [50000] + [-4800] * 12

def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))

def d_npv(rate):
    return sum(-t * cf / (1 + rate)**(t + 1)
               for t, cf in enumerate(cash_flows) if t > 0)

newton = root_scalar(npv, fprime=d_npv, x0=0.02, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.01, x1=0.05, method="secant", xtol=1e-12)

monthly = newton.root
annual = (1 + monthly)**12 - 1

print(f"Monthly rate (Newton): {monthly:.6%}")
print(f"Monthly rate (Secant): {secant.root:.6%}")
print(f"Equivalent annual rate: {annual:.4%}")
print(f"Total repaid: {4800*12}  Interest paid: {4800*12 - 50000}")
print(f"NPV at solution: {npv(monthly):.6f}")
print("Newton iterations:", newton.iterations, " Secant iterations:", secant.iterations)
