# Konstanta untuk menghindari Magic Numbers (Prinsip Clean Code)
ADDITIONAL_MEMBER_DISCOUNT = 5000

def calculate_final_price(price, discount_percentage, is_member):
    """
    Fungsi untuk menghitung harga akhir.
    Menerapkan prinsip SRP (Single Responsibility Principle).
    """
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    
    if is_member:
        final_price -= ADDITIONAL_MEMBER_DISCOUNT
        
    return final_price

def main():
    # Data transaksi dalam list untuk menghindari duplikasi kode (DRY Principle)
    transactions = [
        {"price": 100000, "discount": 10, "is_member": True},
        {"price": 200000, "discount": 15, "is_member": False}
    ]
    
    for item in transactions:
        total = calculate_final_price(item["price"], item["discount"], item["is_member"])
        # Format output
        print(f"Total yang harus dibayar: Rp{total:,.0f}")

if __name__ == "__main__":
    main()