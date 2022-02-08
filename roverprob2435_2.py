from pyhop_anytime import *
global state, goals
state = State('state')
state.at = Oset([('rover0','waypoint0'),('rover1','waypoint0')])
state.at_lander = Oset([('general','waypoint3')])
state.at_rock_sample = Oset(['waypoint0','waypoint1'])
state.at_soil_sample = Oset(['waypoint1','waypoint2','waypoint3'])
state.available = Oset(['rover0','rover1'])
state.calibration_target = Oset([('camera0','objective1'),('camera1','objective1'),('camera2','objective1')])
state.can_traverse = Oset([('rover0','waypoint0','waypoint1'),('rover0','waypoint0','waypoint3'),('rover0','waypoint1','waypoint0'),('rover0','waypoint3','waypoint0'),('rover1','waypoint0','waypoint1'),('rover1','waypoint1','waypoint0'),('rover1','waypoint1','waypoint2'),('rover1','waypoint1','waypoint3'),('rover1','waypoint2','waypoint1'),('rover1','waypoint3','waypoint1')])
state.channel_free = Oset(['general'])
state.empty = Oset(['rover0store','rover1store'])
state.equipped_for_imaging = Oset(['rover0','rover1'])
state.equipped_for_rock_analysis = Oset(['rover0'])
state.equipped_for_soil_analysis = Oset(['rover1'])
state.on_board = Oset([('camera0','rover1'),('camera1','rover1'),('camera2','rover0')])
state.store_of = Oset([('rover0store','rover0'),('rover1store','rover1')])
state.supports = Oset([('camera0','high_res'),('camera0','low_res'),('camera1','colour'),('camera1','high_res'),('camera2','colour'),('camera2','high_res'),('camera2','low_res')])
state.visible = Oset([('waypoint0','waypoint1'),('waypoint0','waypoint2'),('waypoint0','waypoint3'),('waypoint1','waypoint0'),('waypoint1','waypoint2'),('waypoint1','waypoint3'),('waypoint2','waypoint0'),('waypoint2','waypoint1'),('waypoint2','waypoint3'),('waypoint3','waypoint0'),('waypoint3','waypoint1'),('waypoint3','waypoint2')])
state.visible_from = Oset([('objective0','waypoint0'),('objective0','waypoint1'),('objective0','waypoint2'),('objective0','waypoint3'),('objective1','waypoint0'),('objective1','waypoint1'),('objective1','waypoint2'),('objective2','waypoint0'),('objective2','waypoint1'),('objective2','waypoint2')])
state.calibrated = Oset()
state.communicated_image_data = Oset()
state.communicated_rock_data = Oset()
state.communicated_soil_data = Oset()
state.full = Oset()
state.have_image = Oset()
state.have_rock_analysis = Oset()
state.have_soil_analysis = Oset()

goals = State('goals')
goals.communicated_image_data = Oset([('objective0','colour'),('objective0','high_res'),('objective2','high_res')])
goals.communicated_rock_data = Oset(['waypoint0','waypoint1'])
goals.communicated_soil_data = Oset(['waypoint1','waypoint2'])

