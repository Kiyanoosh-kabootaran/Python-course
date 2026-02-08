def shipping_label(*args, **kwargs):
  for arg in args:
    print(arg, end=" ")
  print()

  if "apt" in kwargs:
    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
  elif "pobox" in kwargs:
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('pobox')}")
  else: 
    print(f"{kwargs.get('street')}")
  print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Mr.","Kiyanoosh","Kabootaran",
               street="azadi",
               #apt="100"
               pobox= "PO box #1001",
               city="Tehran",
               state="tehran",
               zip="125487")