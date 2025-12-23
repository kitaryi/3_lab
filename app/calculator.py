from dataclasses import dataclass


@dataclass
class MortgageInput:
    """Данные для расчёта ипотеки. Ипотека."""

    principal: float  # сумма кредита
    annual_rate: float  # годовая ставка, % (например 10.5)
    years: int  # срок в годах


def monthly_payment(m: MortgageInput) -> float:
    """
    Рассчитать аннуитетный ежемесячный платёж.

    Формула:
    P * r * (1 + r) ** n / ((1 + r) ** n - 1),
    где P – сумма кредита, r – месячная ставка (в долях), n – кол-во месяцев.
    """
    if m.principal <= 0 or m.years <= 0:
        raise ValueError("Сумма и срок должны быть положительными")

    months = m.years * 12
    if m.annual_rate <= 0:
        # без процентов — просто равные доли
        return round(m.principal / months, 2)

    rate_m = m.annual_rate / 100 / 12
    factor = (1 + rate_m) ** months
    payment = m.principal * rate_m * factor / (factor - 1)
    return round(payment, 2)


def total_payment(m: MortgageInput) -> float:
    """Общая сумма выплат за весь срок кредита."""
    pay = monthly_payment(m)
    return round(pay * m.years * 12, 2)


def overpayment(m: MortgageInput) -> float:
    """Переплата по кредиту (общая сумма минус тело кредита)."""
    return round(total_payment(m) - m.principal, 2)
