def cm_to_ft_inches(cm):
  # Define conversion factors
  cm_per_inch = 2.5
  inches_per_foot = 12

  # Convert cm to inches
  inches = cm / cm_per_inch

  # Subtract 1 inch from the total inches
  inches -= 1

  # Convert inches to feet and remaining inches
  feet = int(inches // inches_per_foot)
  remaining_inches = int(inches % inches_per_foot)

  return feet, remaining_inches

# Get input from the user
cm_value = float(input("Enter height in centimeters: "))
feet, inches = cm_to_ft_inches(cm_value)
print(f"{cm_value} cm is approximately {feet}'{inches}\".")

if cm_value < 165:
  print("Damn you're short as hell")
elif cm_value > 200:
  print("Damn you're tall as hell")
