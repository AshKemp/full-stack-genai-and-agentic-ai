def serve_chai(flavor):
    try:
        print(f"Preparing your {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We do not have that flavor.")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Thank you for visiting our chai shop!")

serve_chai("masala")
serve_chai("unknown")