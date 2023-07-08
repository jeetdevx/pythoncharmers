class Company:
  # variables var, name
  # functions def()
  x = 5

  # def __init__(self): constructor

  def __init__(self):
    ## I am passing my work
    print(" Connecting to the BBMats..............")
    print("#####################################")

  # def function_name(parameters):
  def company_type(self):
    # I know, I have to return this string
    return "This is a dropshipping company!"

  def company_store(self):
    print(" Connecting to the BBMats Store..............")
    print("Welcome to the store!")
    qstore = input("How can I help you? Bags or Cameras?  ")
    return "Thank you for choosing " + qstore + "!"
