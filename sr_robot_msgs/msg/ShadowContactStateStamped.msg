# All 3D vectors are referenced in the fingertip core center

std_msgs/Header header					# stamp
geometry_msgs/Vector3 tangential_force  	# tangential force (local shear force)
geometry_msgs/Point  contact_position		# contact position
geometry_msgs/Vector3 contact_normal      	# contact normal
float64 fnormal					# amplitude of normal force (along normal)
float64 ltorque					# amplitude of local torque (around normal)

