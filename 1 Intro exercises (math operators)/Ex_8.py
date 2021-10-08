# weight of widgets and gizmos

w_gizmo = 112
w_widget = 75

widget_no = float(input("How many widgets would you like to order?: "))
gizmo_no = float(input("How many gizmos would you like to order?: "))

weight = (w_gizmo * gizmo_no) + (w_widget*widget_no)

print("Total weight of order: %.2f g" %weight)
