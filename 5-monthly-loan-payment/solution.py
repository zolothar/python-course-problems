from decimal import Decimal, getcontext


getcontext().prec = 3


def get_monthly_payment(total_sum, months_count, percents):
    monthly_raw = Decimal(str(total_sum)) / Decimal(str(months_count))
    monthly_addition = monthly_raw * Decimal(str(percents)) / Decimal('100')
    total_per_month = monthly_raw + monthly_addition
    return total_per_month


payment_value = get_monthly_payment(54, 24, 9)
print('Ежемесячный платёж:', payment_value, 'ВтК.')
