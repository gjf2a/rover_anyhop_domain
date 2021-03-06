from pyhop_anytime import *
global state, goals
state = State('state')
state.at = Oset([('rover0','waypoint7'),('rover1','waypoint6'),('rover2','waypoint6'),('rover3','waypoint3')])
state.at_lander = Oset([('general','waypoint2')])
state.at_rock_sample = Oset(['waypoint0','waypoint1','waypoint2','waypoint4','waypoint6','waypoint7','waypoint8'])
state.at_soil_sample = Oset(['waypoint2','waypoint4','waypoint5','waypoint7'])
state.available = Oset(['rover0','rover1','rover2','rover3'])
state.calibration_target = Oset([('camera0','objective1'),('camera1','objective1'),('camera2','objective1'),('camera3','objective2'),('camera4','objective1')])
state.can_traverse = Oset([('rover0','waypoint0','waypoint6'),('rover0','waypoint0','waypoint7'),('rover0','waypoint1','waypoint3'),('rover0','waypoint1','waypoint5'),('rover0','waypoint1','waypoint7'),('rover0','waypoint2','waypoint4'),('rover0','waypoint2','waypoint7'),('rover0','waypoint3','waypoint1'),('rover0','waypoint4','waypoint2'),('rover0','waypoint5','waypoint1'),('rover0','waypoint6','waypoint0'),('rover0','waypoint7','waypoint0'),('rover0','waypoint7','waypoint1'),('rover0','waypoint7','waypoint2'),('rover0','waypoint7','waypoint8'),('rover0','waypoint8','waypoint7'),('rover1','waypoint0','waypoint2'),('rover1','waypoint0','waypoint3'),('rover1','waypoint0','waypoint6'),('rover1','waypoint0','waypoint7'),('rover1','waypoint1','waypoint3'),('rover1','waypoint2','waypoint0'),('rover1','waypoint2','waypoint4'),('rover1','waypoint2','waypoint8'),('rover1','waypoint3','waypoint0'),('rover1','waypoint3','waypoint1'),('rover1','waypoint4','waypoint2'),('rover1','waypoint6','waypoint0'),('rover1','waypoint7','waypoint0'),('rover1','waypoint8','waypoint2'),('rover2','waypoint0','waypoint1'),('rover2','waypoint0','waypoint3'),('rover2','waypoint0','waypoint4'),('rover2','waypoint0','waypoint5'),('rover2','waypoint0','waypoint6'),('rover2','waypoint1','waypoint0'),('rover2','waypoint2','waypoint6'),('rover2','waypoint2','waypoint8'),('rover2','waypoint3','waypoint0'),('rover2','waypoint4','waypoint0'),('rover2','waypoint5','waypoint0'),('rover2','waypoint6','waypoint0'),('rover2','waypoint6','waypoint2'),('rover2','waypoint6','waypoint7'),('rover2','waypoint7','waypoint6'),('rover2','waypoint8','waypoint2'),('rover3','waypoint0','waypoint3'),('rover3','waypoint0','waypoint4'),('rover3','waypoint0','waypoint6'),('rover3','waypoint1','waypoint2'),('rover3','waypoint1','waypoint3'),('rover3','waypoint2','waypoint1'),('rover3','waypoint3','waypoint0'),('rover3','waypoint3','waypoint1'),('rover3','waypoint3','waypoint5'),('rover3','waypoint3','waypoint7'),('rover3','waypoint3','waypoint8'),('rover3','waypoint4','waypoint0'),('rover3','waypoint5','waypoint3'),('rover3','waypoint6','waypoint0'),('rover3','waypoint7','waypoint3'),('rover3','waypoint8','waypoint3')])
state.channel_free = Oset(['general'])
state.empty = Oset(['rover0store','rover1store','rover2store','rover3store'])
state.equipped_for_imaging = Oset(['rover0','rover1','rover2','rover3'])
state.equipped_for_rock_analysis = Oset(['rover2','rover3'])
state.equipped_for_soil_analysis = Oset(['rover0','rover1','rover2','rover3'])
state.on_board = Oset([('camera0','rover2'),('camera1','rover2'),('camera2','rover3'),('camera3','rover1'),('camera4','rover0')])
state.store_of = Oset([('rover0store','rover0'),('rover1store','rover1'),('rover2store','rover2'),('rover3store','rover3')])
state.supports = Oset([('camera0','colour'),('camera0','high_res'),('camera1','colour'),('camera1','low_res'),('camera2','high_res'),('camera3','colour'),('camera3','low_res'),('camera4','high_res'),('camera4','low_res')])
state.visible = Oset([('waypoint0','waypoint1'),('waypoint0','waypoint2'),('waypoint0','waypoint3'),('waypoint0','waypoint4'),('waypoint0','waypoint5'),('waypoint0','waypoint6'),('waypoint0','waypoint7'),('waypoint1','waypoint0'),('waypoint1','waypoint2'),('waypoint1','waypoint3'),('waypoint1','waypoint4'),('waypoint1','waypoint5'),('waypoint1','waypoint7'),('waypoint1','waypoint8'),('waypoint2','waypoint0'),('waypoint2','waypoint1'),('waypoint2','waypoint4'),('waypoint2','waypoint5'),('waypoint2','waypoint6'),('waypoint2','waypoint7'),('waypoint2','waypoint8'),('waypoint3','waypoint0'),('waypoint3','waypoint1'),('waypoint3','waypoint4'),('waypoint3','waypoint5'),('waypoint3','waypoint7'),('waypoint3','waypoint8'),('waypoint4','waypoint0'),('waypoint4','waypoint1'),('waypoint4','waypoint2'),('waypoint4','waypoint3'),('waypoint4','waypoint8'),('waypoint5','waypoint0'),('waypoint5','waypoint1'),('waypoint5','waypoint2'),('waypoint5','waypoint3'),('waypoint6','waypoint0'),('waypoint6','waypoint2'),('waypoint6','waypoint7'),('waypoint7','waypoint0'),('waypoint7','waypoint1'),('waypoint7','waypoint2'),('waypoint7','waypoint3'),('waypoint7','waypoint6'),('waypoint7','waypoint8'),('waypoint8','waypoint1'),('waypoint8','waypoint2'),('waypoint8','waypoint3'),('waypoint8','waypoint4'),('waypoint8','waypoint7')])
state.visible_from = Oset([('objective0','waypoint0'),('objective1','waypoint0'),('objective1','waypoint1'),('objective1','waypoint2'),('objective1','waypoint3'),('objective1','waypoint4'),('objective1','waypoint5'),('objective1','waypoint6'),('objective1','waypoint7'),('objective2','waypoint0'),('objective2','waypoint1'),('objective2','waypoint2'),('objective2','waypoint3'),('objective2','waypoint4'),('objective2','waypoint5'),('objective3','waypoint0'),('objective3','waypoint1'),('objective3','waypoint2'),('objective3','waypoint3'),('objective3','waypoint4'),('objective3','waypoint5'),('objective3','waypoint6'),('objective3','waypoint7')])
state.calibrated = Oset()
state.communicated_image_data = Oset()
state.communicated_rock_data = Oset()
state.communicated_soil_data = Oset()
state.full = Oset()
state.have_image = Oset()
state.have_rock_analysis = Oset()
state.have_soil_analysis = Oset()

goals = State('goals')
goals.communicated_image_data = Oset([('objective1','high_res'),('objective2','high_res'),('objective3','high_res')])
goals.communicated_rock_data = Oset(['waypoint1','waypoint4','waypoint6','waypoint7','waypoint8'])
goals.communicated_soil_data = Oset(['waypoint2','waypoint4','waypoint5','waypoint7'])

