def calibrate(state, r, i, t, w):
    if r in state.equipped_for_imaging and (i,t) in state.calibration_target and (r,w) in state.at and (t,w) in state.visible_from and (i,r) in state.on_board:
        state.calibrated.add((i,r))
        return state


def communicate_image_data(state, r, l, o, m, x, y):
    if (r,x) in state.at and (l,y) in state.at_lander and (r,o,m) in state.have_image and (x,y) in state.visible and r in state.available and l in state.channel_free:
        state.available.discard(r)
        state.channel_free.discard(l)
        state.channel_free.add(l)
        state.communicated_image_data.add((o,m))
        state.available.add(r)
        return state


def communicate_rock_data(state, r, l, p, x, y):
    if (r,x) in state.at and (l,y) in state.at_lander and (r,p) in state.have_rock_analysis and (x,y) in state.visible and r in state.available and l in state.channel_free:
        state.available.discard(r)
        state.channel_free.discard(l)
        state.channel_free.add(l)
        state.communicated_rock_data.add(p)
        state.available.add(r)
        return state


def communicate_soil_data(state, r, l, p, x, y):
    if (r,x) in state.at and (l,y) in state.at_lander and (r,p) in state.have_soil_analysis and (x,y) in state.visible and r in state.available and l in state.channel_free:
        state.available.discard(r)
        state.channel_free.discard(l)
        state.channel_free.add(l)
        state.communicated_soil_data.add(p)
        state.available.add(r)
        return state


def drop(state, x, y):
    if (y,x) in state.store_of and y in state.full:
        state.full.discard(y)
        state.empty.add(y)
        return state


def navigate(state, x, y, z):
    if (x,y,z) in state.can_traverse and x in state.available and (x,y) in state.at and (y,z) in state.visible:
        state.at.discard((x,y))
        state.at.add((x,z))
        return state


def sample_rock(state, x, s, p):
    if (x,p) in state.at and p in state.at_rock_sample and x in state.equipped_for_rock_analysis and (s,x) in state.store_of and s in state.empty:
        state.empty.discard(s)
        state.full.add(s)
        state.have_rock_analysis.add((x,p))
        state.at_rock_sample.discard(p)
        return state


def sample_soil(state, x, s, p):
    if (x,p) in state.at and p in state.at_soil_sample and x in state.equipped_for_soil_analysis and (s,x) in state.store_of and s in state.empty:
        state.empty.discard(s)
        state.full.add(s)
        state.have_soil_analysis.add((x,p))
        state.at_soil_sample.discard(p)
        return state


def take_image(state, r, p, o, i, m):
    if (i,r) in state.calibrated and (i,r) in state.on_board and r in state.equipped_for_imaging and (i,m) in state.supports and (o,p) in state.visible_from and (r,p) in state.at:
        state.have_image.add((r,o,m))
        state.calibrated.discard((i,r))
        return state


