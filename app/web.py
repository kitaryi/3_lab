from flask import Blueprint, render_template, request

from .calculator import (MortgageInput, monthly_payment, overpayment,
                         total_payment)

bp = Blueprint("web", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            principal = float(request.form.get("principal", "0")
                              .replace(",", "."))
            annual_rate = float(request.form.get("annual_rate", "0")
                                .replace(",", "."))
            years = int(request.form.get("years", "0"))
            m_input = MortgageInput(
                principal=principal,
                annual_rate=annual_rate,
                years=years,
            )

            mp = monthly_payment(m_input)
            tp = total_payment(m_input)
            op = overpayment(m_input)

            result = {
                "monthly_payment": mp,
                "total_payment": tp,
                "overpayment": op,
                "principal": principal,
                "annual_rate": annual_rate,
                "years": years,
            }
        except Exception as exc:  # noqa: BLE001
            error = f"Ошибка ввода: {exc}"

    return render_template("index.html", result=result, error=error)
