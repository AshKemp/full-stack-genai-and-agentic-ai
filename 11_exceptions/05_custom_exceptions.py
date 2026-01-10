def brew_chai(flavor):
    if flavor not in ['masala', 'ginger', 'cardamom']:
        raise ValueError(f"Unsupported chai flavor: {flavor}")
    print(f"Brewed a cup of {flavor} chai!")

brew_chai('vanilla')  # This will raise a ValueError
# brew_chai('masala')  # This will work fine