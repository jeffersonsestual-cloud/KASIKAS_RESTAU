from config import BULK_QTY, BULK_RATE, STUDENT_RATE


def compute_totals(orders, is_student):
    subtotal = 0.0
    total_qty = 0
    for item, qty, price in orders:
        subtotal += qty * price
        total_qty += qty

    # Priority: Student > Bulk (only one discount applies)
    if is_student:
        discount, label = subtotal * STUDENT_RATE, "Student Discount (10%)"
    elif total_qty >= BULK_QTY:
        discount, label = subtotal * BULK_RATE, "Discount (5%)"
    else:
        discount, label = 0.0, None

    return subtotal, discount, label, subtotal - discount